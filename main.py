import copy
import json
import os
import socket
import sys
import webbrowser

import cv2
import numpy as np
import yaml
from PySide6.QtCore import Slot, QThread, Signal, QTimer, Qt
from PySide6.QtGui import QIcon, QPixmap, QColor, QPainter, QBrush, QFont, QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout

from MainCtl_Ui import Ui_MainWindow
from unit.tool_unit import fail, divide_path, succeed
from unit.z_json2txt import json_to_txt


class z_App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.aboutToQuit.connect(self.onAboutToQuit)

    @Slot()
    def onAboutToQuit(self):
        print("Exiting the application.")
        try:
            # 停止所有服务线程
            self.stop_all_threads()

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping application.")

        finally:
            print("Waiting for all threads to exit...")
            self.join_all_threads()
            print("All servers are closed. Exiting.")

    def stop_all_threads(self):
        """停止所有线程的函数。"""
        try:
            udp_thread.stop()
        except Exception as e:
            print(f"Error stopping threads: {e}")

    def join_all_threads(self):
        """等待所有线程退出。"""
        try:
            udp_thread.wait()
        except Exception as e:
            print(f"Error waiting threads: {e}")


class z_Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口图标
        self.setWindowIcon(QIcon("./icon.ico"))

    def closeEvent(self, event):
        # 创建确认对话框
        reply = QMessageBox.question(
            self,
            "退出",
            "您确定要退出程序吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        # 检查用户的响应
        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件，程序退出
        else:
            event.ignore()  # 忽略关闭事件，程序继续运行


class z_Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, z_window):
        super(z_Ui, self).setupUi(z_window)


"************************************图像跟踪_开始****************************************"


class MapLabel(QLabel):
    def __init__(self, picture_size=860, ball_space=10, ball_radius=10, flash_time=30, step_length=2, parent=None):
        super().__init__(parent)
        self.map_action = 0  # 地图触发点位
        img = map_data[0]
        pixmap = QPixmap(img)
        self.picture_size = picture_size
        # 设置label的尺寸
        self.setMaximumSize(picture_size, picture_size)
        self.setPixmap(pixmap)
        self.setScaledContents(True)

        self.color_names = {'red': QColor(255, 0, 0), 'green': QColor(0, 255, 0), 'blue': QColor(0, 0, 255),
                            'pink': QColor(255, 0, 255), 'yellow': QColor(255, 255, 0), 'black': QColor(0, 0, 0),
                            'purple': QColor(128, 0, 128), 'orange': QColor(255, 165, 0),
                            'White': QColor(248, 248, 255),
                            'Brown': QColor(139, 69, 19)}

        self.path_points = []
        if os.path.exists(map_data[1]):
            with open(map_data[1], 'r', encoding='utf-8') as fcc_file:
                fcc_data = json.load(fcc_file)
            if picture_size == 860:
                map_scale = 1
            else:
                map_scale = picture_size / int(map_data[2])  # 缩放比例
            for p in fcc_data[0]["content"]:
                self.path_points.append((p['x'] * map_scale, p['y'] * map_scale))
            self.path_points = divide_path(self.path_points, step_length)

        self.ball_space = ball_space  # 球之间的距离
        self.ball_radius = ball_radius  # 小球半径
        # self.num_balls = 8  # 8个小球
        self.speed = 1  # 小球每次前进的步数（可以根据需要调整）
        self.flash_time = flash_time
        self.positions = []  # 每个球的当前位置索引
        for num in range(balls_count):
            self.positions.append([num * self.ball_space, QColor(255, 0, 0), 0])

        # 创建定时器，用于定时更新球的位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_positions)  # 定时触发更新
        self.timer.start(self.flash_time)  # 每1秒更新一次

    def update_positions(self):
        # 更新每个小球的位置
        p_num = 0
        if len(self.positions) != balls_count:
            self.positions = []  # 每个球的当前位置索引
            for num in range(balls_count):
                self.positions.append([num * self.ball_space, QColor(255, 0, 0), 0])
        for num in range(0, balls_count):
            if ranking_array[num][5] in self.color_names.keys():
                color = self.color_names[ranking_array[num][5]]
                if ranking_array[num][6] == 0:  # 起点
                    if p_num == 0:
                        index = (len(ranking_array)-1) * self.ball_space
                    else:
                        index = (len(ranking_array)-1) * self.ball_space - p_num * self.ball_space
                elif (ranking_array[num][6] >= max_area_count - balls_count
                      and ranking_array[num][8] >= max_lap_count - 1):  # 最后一圈处理
                    if p_num == 0:
                        index = len(self.path_points) - 1
                    else:
                        index = len(self.path_points) - 1 - p_num * self.ball_space
                elif ranking_array[num][8] == ranking_array[0][1]:  # 同圈才运动
                    area_num = max_area_count - balls_count  # 跟踪区域数量
                    p = int(len(self.path_points) * (ranking_array[num][6] / area_num)) - 1
                    color = self.color_names[ranking_array[num][5]]
                    if p - self.positions[p_num][0] > 50:
                        self.speed = 3
                    elif 30 >= p - self.positions[p_num][0] >= 25:
                        self.speed = 2
                    elif p < self.positions[p_num][0]:
                        self.speed = 0
                    else:
                        self.speed = 1
                    if self.positions[p_num][0] > len(self.path_points) - self.ball_radius - 1:
                        index = 0
                    elif p_num == 0:
                        index = self.positions[p_num][0] + self.speed
                    elif (0 < self.positions[p_num - 1][0] - self.positions[p_num][0] < self.ball_space
                          and int(len(self.path_points) * (5 / area_num)) < self.positions[p_num][0] < len(
                                self.path_points) - self.ball_space):
                        index = self.positions[p_num][0] - self.ball_radius
                    else:
                        index = self.positions[p_num][0] + self.speed
                else:  # 不同圈情况
                    area_num = max_area_count - balls_count  # 跟踪区域数量
                    p = int(len(self.path_points) * (ranking_array[num][6] / area_num)) - 1
                    color = self.color_names[ranking_array[num][5]]
                    if p - self.positions[p_num][0] > 50:
                        self.speed = 3
                    elif 30 >= p - self.positions[p_num][0] >= 25:
                        self.speed = 2
                    elif p < self.positions[p_num][0]:
                        self.speed = 0
                    else:
                        self.speed = 1
                    index = self.positions[p_num][0] + self.speed
                    if index > len(self.path_points) - self.ball_radius - 1:
                        index = len(self.path_points) - 1
                self.positions[p_num][0] = index
                self.positions[p_num][1] = color
                for color_index in range(len(init_array)):
                    if init_array[color_index][5] == ranking_array[num][5]:
                        self.positions[p_num][2] = color_index + 1
                        break
                # if index >= len(self.path_points):
                #     self.positions[p_num][0] = 0  # 回到起点循环运动
                p_num += 1
        if self.positions[0][0] - self.map_action < 300:
            self.map_action = self.positions[0][0]  # 赋值实时位置
        # 触发重绘
        self.update()

    # 通过重载paintEvent方法进行自定义绘制
    def paintEvent(self, event):
        # 调用父类的 paintEvent 以确保 QLabel 正常显示文本或图片
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if ui.checkBox_show_orbit.isChecked():  # 绘制路径
            for index in range(len(self.path_points)):
                part = len(self.path_points) / (max_area_count - balls_count)
                if index % int(part) == 0:
                    painter.setBrush(QBrush(QColor(255, 0, 0), Qt.SolidPattern))
                    font = QFont("Arial", 12, QFont.Bold)  # 字体：Arial，大小：16，加粗
                    painter.setFont(font)
                    painter.setPen('green')
                    painter.drawText(int(self.path_points[index][0]), int(self.path_points[index][1]),
                                     str(index // int(part)))
                    painter.drawEllipse(int(self.path_points[index][0]), int(self.path_points[index][1]),
                                        10, 10)
                else:
                    painter.setBrush(QBrush(QColor(0, 255, 0), Qt.SolidPattern))
                    painter.drawEllipse(int(self.path_points[index][0]), int(self.path_points[index][1]),
                                        2, 2)

        # 绘制每个小球
        for index_position in range(len(self.positions)):
            index = self.positions[index_position][0]  # 获取当前球的路径索引
            if index in range(len(self.path_points)):
                x, y = self.path_points[index]
                # 设置球的颜色
                painter.setBrush(QBrush(self.positions[index_position][1], Qt.SolidPattern))
                # 绘制球
                painter.drawEllipse(int(x - self.ball_radius), int(y - self.ball_radius),
                                    self.ball_radius * 2, self.ball_radius * 2)
                if self.picture_size == 860:
                    if str(self.positions[index_position][2]) in ['1', '7']:
                        font = QFont("Arial", 12, QFont.Bold)  # 字体：Arial，大小：16，加粗
                        painter.setFont(font)
                        painter.setPen('black')
                        painter.drawText(int(x - self.ball_radius / 2), int(y + self.ball_radius / 2),
                                         str(self.positions[index_position][2]))
                    elif str(self.positions[index_position][2]) == '10':
                        font = QFont("Arial", 11, QFont.Bold)  # 字体：Arial，大小：16，加粗
                        painter.setFont(font)
                        painter.setPen('black')
                        painter.drawText(int(x - self.ball_radius / 2 - 4), int(y + self.ball_radius / 2),
                                         str(self.positions[index_position][2]))
                    else:
                        font = QFont("Arial", 12, QFont.Bold)  # 字体：Arial，大小：16，加粗
                        painter.setFont(font)
                        painter.setPen('white')
                        painter.drawText(int(x - self.ball_radius / 2), int(y + self.ball_radius / 2),
                                         str(self.positions[index_position][2]))

    def mouseReleaseEvent(self, event: QMouseEvent):
        """释放鼠标时停止拖动"""
        if event.button() == Qt.LeftButton:
            print(event.position().toPoint())


"************************************图像识别_开始****************************************"


def reset_ranking_array():
    """
    重置排名数组
    # 前0~3是坐标↖↘,4=置信度，5=名称,6=赛道区域，7=方向排名,8=圈数,9=0不可见 1可见.
    """
    global ranking_array
    global ball_sort

    ranking_array = []  # 排名数组
    for row in range(0, len(init_array)):
        ranking_array.append([])
        for col in range(0, len(init_array[row])):
            ranking_array[row].append(init_array[row][col])
    ball_sort = []  # 位置寄存器
    for row in range(0, max_area_count + 1):
        ball_sort.append([])
        for col in range(0, max_lap_count):
            ball_sort[row].append([])


# 处理排名
def deal_rank(integration_qiu_array):
    global ranking_array
    for r_index in range(0, len(ranking_array)):
        replaced = False
        for q_item in integration_qiu_array:
            if ranking_array[r_index][5] == q_item[5]:  # 更新 ranking_array
                if q_item[6] < ranking_array[r_index][6]:  # 处理圈数（上一次位置，和当前位置的差值大于等于12为一圈）
                    result_count = ranking_array[r_index][6] - q_item[6]
                    if result_count >= max_area_count - balls_count - 6:
                        ranking_array[r_index][8] += 1
                        if ranking_array[r_index][8] > max_lap_count - 1:
                            ranking_array[r_index][8] = 0
                            ranking_array[r_index][6] = 0
                if (ranking_array[0][6] >= max_area_count - balls_count
                        and ranking_array[0][8] >= max_lap_count - 1):
                    area_limit = balls_count
                else:
                    area_limit = 5
                # if ((ranking_array[r_index][6] == 0)  # 等于0 刚初始化，未检测区域
                if ((ranking_array[r_index][6] == 0 and q_item[6] < 5)  # 等于0 刚初始化，未检测区域
                        or (q_item[6] >= ranking_array[r_index][6] and  # 新位置要大于旧位置
                            (q_item[6] - ranking_array[r_index][6] <= area_limit  # 新位置相差旧位置三个区域以内
                                    # or ranking_array[0][6] - ranking_array[r_index][6] > 5
                            ))  # 当新位置与旧位置超过3个区域，则旧位置与头名要超过5个区域才统计
                        or (q_item[6] < 8 and ranking_array[r_index][6] >= max_area_count - balls_count - 6)):  # 跨圈情况
                    for r_i in range(0, len(q_item)):
                        ranking_array[r_index][r_i] = copy.deepcopy(q_item[r_i])  # 更新 ranking_array
                    ranking_array[r_index][9] = 1
                replaced = True
                break
        if not replaced:
            ranking_array[r_index][9] = 0
    # print(ranking_array)
    # print('到这里~~~~')
    sort_ranking()


def sort_ranking():
    global ranking_array
    global ball_sort
    # 1.排序区域
    for i in range(0, len(ranking_array)):  # 冒泡排序
        for j in range(0, len(ranking_array) - i - 1):
            if ranking_array[j][6] < ranking_array[j + 1][6]:
                ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
    # 2.区域内排序
    for i in range(0, len(ranking_array)):  # 冒泡排序
        for j in range(0, len(ranking_array) - i - 1):
            if ranking_array[j][6] == ranking_array[j + 1][6]:
                if ranking_array[j][7] == 0:  # (左后->右前)
                    if ranking_array[j][0] < ranking_array[j + 1][0]:
                        ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
                if ranking_array[j][7] == 1:  # (左前<-右后)
                    if ranking_array[j][0] > ranking_array[j + 1][0]:
                        ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
                if ranking_array[j][7] == 10:  # (上前 ↑ 下后)
                    if ranking_array[j][1] > ranking_array[j + 1][1]:
                        ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
                if ranking_array[j][7] == 11:  # (上后 ↓ 下前)
                    if ranking_array[j][1] < ranking_array[j + 1][1]:
                        ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
    # 3.圈数排序
    for i in range(0, len(ranking_array)):  # 冒泡排序
        for j in range(0, len(ranking_array) - i - 1):
            if ranking_array[j][8] < ranking_array[j + 1][8]:
                ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]
    # 4.寄存器保存固定每个区域的最新排位（因为ranking_array 变量会因实时动态变动，需要寄存器辅助固定每个区域排位）
    for i in range(0, len(ranking_array)):
        # print(ranking_array[i], '~~~~~~~~~~~')
        if not (ranking_array[i][5] in ball_sort[ranking_array[i][6]][ranking_array[i][8]]):
            ball_sort[ranking_array[i][6]][ranking_array[i][8]].append(copy.deepcopy(ranking_array[i][5]))  # 添加寄存器球排序
            # if ranking_array[i][6] == 35 and ranking_array[i][8] == 1:
            #     print(ball_sort[ranking_array[i][6]][ranking_array[i][8]])
    # 5.按照寄存器位置，重新排序排名同圈数同区域内的球
    for i in range(0, len(ranking_array)):
        for j in range(0, len(ranking_array) - i - 1):
            if (ranking_array[j][6] == ranking_array[j + 1][6]) and (ranking_array[j][8] == ranking_array[j + 1][8]):
                m = 0
                n = 0

                for k in range(0, len(ball_sort[ranking_array[j][6]][ranking_array[j][8]])):
                    if ranking_array[j][5] == ball_sort[ranking_array[j][6]][ranking_array[j][8]][k]:
                        n = k
                    elif ranking_array[j + 1][5] == ball_sort[ranking_array[j][6]][ranking_array[j][8]][k]:
                        m = k
                if n > m:  # 把区域排位索引最小的球（即排名最前的球）放前面
                    ranking_array[j], ranking_array[j + 1] = ranking_array[j + 1], ranking_array[j]


class UdpThread(QThread):
    _signal = Signal(object)

    def __init__(self):
        super(UdpThread, self).__init__()
        self.run_flg = True
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        udp_socket.close()
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        while self.running:
            try:
                # 3. 等待接收对方发送的数据
                recv_data = udp_socket.recvfrom(10240)  # 1024表示本次接收的最大字节数
                if len(recv_data) < 1:
                    print('UDP无数据！')
                    continue
                if self.run_flg:
                    res = recv_data[0].decode('utf8')
                    if res == '':
                        print('UDP_res无数据！', recv_data[0])
                        continue
                    data_res = eval(res)  # str转换list
                    if len(recv_data) < 2:
                        print('UDP_recv_data无数据！', res)
                        continue
                    self._signal.emit(data_res)
                    array_data = []
                    for i_ in range(1, len(data_res)):  # data_res[0] 是时间戳差值 ms
                        array_data.append(copy.deepcopy(data_res[i_]))
                    # print(array_data)
                    if len(array_data) < 1:
                        continue
                    if len(array_data[0]) < 7:
                        self._signal.emit(fail('array_data:%s < 7数据错误！' % array_data[0]))
                        print('array_data < 7数据错误！', array_data[0])
                        continue
                    array_data = deal_area(array_data, array_data[0][6])  # 收集统计区域内的球
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1', array_data)
                    if array_data is None or len(array_data) < 1:
                        continue
                    if len(array_data[0]) < 8:
                        self._signal.emit(fail('array_data:%s < 8数据错误！' % array_data[0]))
                        print('array_data < 8数据错误！', array_data[0])
                        continue
                    if (ranking_array[0][6] >= max_area_count - balls_count
                            and ranking_array[0][8] >= max_lap_count - 1):  # 在最后面排名阶段，以区域先后为准
                        array_data = filter_max_area(array_data)
                    else:
                        array_data = filter_max_value(array_data)  # 在平时球位置追踪，以置信度为准
                    if array_data is None or len(array_data) < 1:
                        continue

                    deal_rank(array_data)

            except Exception as e:
                print("UDP数据接收出错:%s" % e)
                self._signal.emit("UDP数据接收出错:%s" % e)
        # 5. 关闭套接字
        udp_socket.close()


def udp_signal_accept(msg):
    print(msg)


def load_area():  # 载入位置文件初始化区域列表
    global area_Code
    for key in area_Code.keys():
        track_file = "./txts/%s.txt" % key
        if os.path.exists(track_file):  # 存在就加载数据对应赛道数据
            with open(track_file, 'r') as file:
                content = file.read().split('\n')
            for area in content:
                if area:
                    polgon_array = {'coordinates': [], 'area_code': 0, 'direction': 0}
                    paths = area.split(' ')
                    if len(paths) < 2:
                        print("分区文件错误！")
                        return
                    lines = paths[0].split(',')
                    for line in lines:
                        if line:
                            x, y = line.split('/')
                            polgon_array['coordinates'].append((int(x), int(y)))
                    polgon_array['area_code'] = int(paths[1])
                    if len(paths) > 2:
                        polgon_array['direction'] = int(paths[2])
                    area_Code[key].append(polgon_array)


def deal_area(ball_array, cap_num):  # 找出该摄像头内所有球的区域
    ball_area_array = []
    if len(ball_array) < 1 or cap_num == '':
        return
    for ball in ball_array:
        # print(ball)
        if ball[4] < 0.35:  # 置信度小于 0.45 的数据不处理
            continue
        if len(ball) == 7:
            ball.append(0)
        x = (ball[0] + ball[2]) / 2
        y = (ball[1] + ball[3]) / 2
        point = (x, y)
        if cap_num in area_Code.keys():
            for area in area_Code[cap_num]:
                pts = np.array(area['coordinates'], np.int32)
                res = cv2.pointPolygonTest(pts, point, False)  # -1=在外部,0=在线上，1=在内部
                if res > -1.0 and len(ball) <= 8:
                    ball[6] = area['area_code']
                    ball[7] = area['direction']
                    ball_area_array.append(copy.deepcopy(ball))  # ball结构：x1,y1,x2,y2,置信度,球名,区域号,方向
    return ball_area_array  # ball_area_array = [[x1,y1,x2,y2,置信度,球名,区域号,方向]]


# 33 17 25 29
def filter_max_area(lists):  # 在区域范围内如果出现两个相同的球，则取区域最大的球为准
    max_area = {}
    # print('原', lists)
    for sublist in lists:
        key, area = sublist[5], sublist[6]
        if (key not in max_area) or (area > max_area[key]):
            max_area[key] = copy.deepcopy(area)
    filtered_list = []
    for sublist in lists:
        if sublist[6] == max_area[sublist[5]]:  # 选取同一区域置信度最大的球添加到修正后的队列
            filtered_list.append(copy.deepcopy(sublist))
            # print(filtered_list)
    return filtered_list


def filter_max_value(lists):  # 在区域范围内如果出现两个相同的球，则取置信度最高的球为准
    max_values = {}
    for sublist in lists:
        value, key = sublist[4], sublist[5]
        if key not in max_values or max_values[key] < value:
            max_values[key] = copy.deepcopy(value)
    filtered_list = []
    for sublist in lists:
        if sublist[4] == max_values[sublist[5]]:  # 选取置信度最大的球添加到修正后的队列
            filtered_list.append(copy.deepcopy(sublist))
    return filtered_list


"************************************图像识别_结束****************************************"


def open_draw():
    url = 'https://zzw168.github.io/LabelImg/'
    webbrowser.open(url)


def json_txt():
    if json_to_txt():
        ui.textBrowser.append(succeed('区域文件转TXT成功！'))
    else:
        ui.textBrowser.append(fail('区域文件转TXT失败！'))


def save_ballsort_yaml():
    global max_lap_count
    global max_area_count
    global flash_t
    file = "./ballsort_config.yml"
    if os.path.exists(file):
        f = open(file, 'r', encoding='utf-8')
        ballsort_all = yaml.safe_load(f)
        f.close()
        if (ui.lineEdit_lap_Ranking.text().isdigit()
                and ui.lineEdit_area_Ranking.text().isdigit()
                and ui.lineEdit_flash_Ranking.text().isdigit()):
            ballsort_all['max_lap_count'] = int(ui.lineEdit_lap_Ranking.text())
            ballsort_all['max_area_count'] = int(ui.lineEdit_area_Ranking.text())
            ballsort_all['flash_time'] = int(ui.lineEdit_flash_Ranking.text())
            max_lap_count = int(ui.lineEdit_lap_Ranking.text())
            max_area_count = int(ui.lineEdit_area_Ranking.text())
            flash_t = int(ui.lineEdit_flash_Ranking.text())
            # print(ballsort_conf)
            with open(file, "w", encoding="utf-8") as f:
                yaml.dump(ballsort_all, f, allow_unicode=True)
            f.close()
            ui.textBrowser.setText(
                succeed("%s,%s,%s 保存服务器完成" % (ballsort_all['max_lap_count'],
                                                     ballsort_all['max_area_count'],
                                                     ballsort_all['flash_time'])))
        else:
            ui.textBrowser.setText(fail("错误，只能输入数字！"))

def load_ballsort_yaml():
    global max_lap_count
    global max_area_count
    global flash_t
    file = "./ballsort_config.yml"
    if os.path.exists(file):
        f = open(file, 'r', encoding='utf-8')
        ballsort_all = yaml.safe_load(f)
        max_area_count = int(ballsort_all['max_area_count'])
        max_lap_count = int(ballsort_all['max_lap_count'])
        flash_t = int(ballsort_all['flash_time'])

        ui.lineEdit_flash_Ranking.setText(str(flash_t))
        ui.lineEdit_lap_Ranking.setText(str(max_lap_count))
        ui.lineEdit_area_Ranking.setText(str(max_area_count))

        f.close()
    else:
        print("文件不存在")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = z_App(sys.argv)

    z_window = z_Mainwindow()
    ui = z_Ui()
    ui.setupUi(z_window)
    z_window.show()

    ui.pushButton_Draw.clicked.connect(open_draw)
    ui.pushButton_to_TXT.clicked.connect(json_txt)
    ui.pushButton_save_Ranking.clicked.connect(save_ballsort_yaml)

    "**************************图像识别算法_开始*****************************"
    # set_run_toggle 发送请求运行数据
    camera_num = 15  # 摄像头数量
    area_Code = {1: [], 2: [], 3: [], 4: [], 5: [],
                 6: [], 7: [], 8: [], 9: [], 10: [],
                 11: [], 12: [], 13: [], 14: [], 15: [], 16: []}  # 摄像头代码列表
    load_area()  # 初始化区域划分

    balls_count = 8  # 运行球数
    ranking_array = []  # 前0~3是坐标↖↘,4=置信度，5=名称,6=赛道区域，7=方向排名,8=圈数,9=0不可见 1可见.
    keys = ["x1", "y1", "x2", "y2", "con", "name", "position", "direction", "lapCount", "visible", "lastItem"]
    ball_sort = []  # 位置寄存器 ball_sort[[[]*max_lap_count]*max_area_count + 1]

    # 初始化数据
    max_lap_count = 1  # 最大圈
    max_area_count = 87  # 统计一圈的位置差
    flash_t = 30

    load_ballsort_yaml()

    init_array = [
        [0, 0, 0, 0, 0, 'yellow', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'blue', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'red', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'purple', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'pink', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'green', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'White', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'black', 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 'orange', 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 'Brown', 0, 0, 0, 0]
    ]
    color_ch = {'yellow': '黄',
                'blue': '蓝',
                'red': '红',
                'purple': '紫',
                'orange': '橙',
                'green': '绿',
                'Brown': '棕',
                'black': '黑',
                'pink': '粉',
                'White': '白'}
    udpServer_addr = ('0.0.0.0', 22222)  # 接收图像识别结果
    wakeup_addr = ["http://192.168.0.110:8080"]  # 唤醒服务器网址

    reset_ranking_array()  # 初始化

    # 1. Udp 接收数据 14
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(udpServer_addr)
        print('Udp_socket Server Started.')
        udp_thread = UdpThread()
        udp_thread._signal.connect(udp_signal_accept)
        udp_thread.start()
    except:
        # 使用infomation信息框
        QMessageBox.information(z_window, "UDP", "UDP端口被占用")

    "**************************地图_开始*****************************"
    map_data = ['./img/09_沙漠.jpg', './img/09_沙漠.json', '860']  # 卫星地图资料
    map_label_big = MapLabel(flash_time=flash_t)
    layout_big = QVBoxLayout(ui.widget_map_big)
    layout_big.setContentsMargins(0, 0, 0, 0)
    layout_big.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # 添加自定义的 QLabel 到布局中
    layout_big.addWidget(map_label_big)

    sys.exit(app.exec())
