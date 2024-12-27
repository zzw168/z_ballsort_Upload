# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainCtl_Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1326, 973)
        MainWindow.setMinimumSize(QSize(100, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_Ranking = QTabWidget(self.centralwidget)
        self.tabWidget_Ranking.setObjectName(u"tabWidget_Ranking")
        self.tabWidget_Ranking.setMinimumSize(QSize(10, 10))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        self.tabWidget_Ranking.setFont(font)
        self.tabWidget_Ranking.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_39 = QGridLayout(self.tab_2)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_map_big = QWidget(self.tab_2)
        self.widget_map_big.setObjectName(u"widget_map_big")
        self.widget_map_big.setMinimumSize(QSize(860, 860))

        self.gridLayout_39.addWidget(self.widget_map_big, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.tab_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(420, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_21)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.groupBox_21 = QGroupBox(self.frame_21)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMaximumSize(QSize(16777215, 150))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox_21.setFont(font1)
        self.gridLayout_45 = QGridLayout(self.groupBox_21)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.pushButton_del_camera = QPushButton(self.groupBox_21)
        self.pushButton_del_camera.setObjectName(u"pushButton_del_camera")

        self.gridLayout_45.addWidget(self.pushButton_del_camera, 0, 2, 1, 1)

        self.pushButton_add_camera = QPushButton(self.groupBox_21)
        self.pushButton_add_camera.setObjectName(u"pushButton_add_camera")

        self.gridLayout_45.addWidget(self.pushButton_add_camera, 0, 0, 1, 1)

        self.pushButton_save_camera = QPushButton(self.groupBox_21)
        self.pushButton_save_camera.setObjectName(u"pushButton_save_camera")

        self.gridLayout_45.addWidget(self.pushButton_save_camera, 0, 3, 1, 1)


        self.gridLayout_42.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.groupBox_22 = QGroupBox(self.frame_21)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(0, 0))
        self.groupBox_22.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_22.setFont(font1)
        self.gridLayout_46 = QGridLayout(self.groupBox_22)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_add_Audio = QPushButton(self.groupBox_22)
        self.pushButton_add_Audio.setObjectName(u"pushButton_add_Audio")

        self.gridLayout_46.addWidget(self.pushButton_add_Audio, 2, 0, 1, 1)

        self.pushButton_del_Audio = QPushButton(self.groupBox_22)
        self.pushButton_del_Audio.setObjectName(u"pushButton_del_Audio")

        self.gridLayout_46.addWidget(self.pushButton_del_Audio, 2, 1, 1, 1)

        self.pushButton_save_Audio = QPushButton(self.groupBox_22)
        self.pushButton_save_Audio.setObjectName(u"pushButton_save_Audio")

        self.gridLayout_46.addWidget(self.pushButton_save_Audio, 2, 2, 1, 1)

        self.tableWidget_Audio = QTableWidget(self.groupBox_22)
        if (self.tableWidget_Audio.columnCount() < 4):
            self.tableWidget_Audio.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Audio.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Audio.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Audio.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Audio.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_Audio.setObjectName(u"tableWidget_Audio")
        self.tableWidget_Audio.setMinimumSize(QSize(0, 0))
        self.tableWidget_Audio.setMaximumSize(QSize(500, 16777215))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.tableWidget_Audio.setFont(font2)
        self.tableWidget_Audio.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_Audio.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Audio.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_46.addWidget(self.tableWidget_Audio, 3, 0, 1, 3)

        self.checkBox_main_music = QCheckBox(self.groupBox_22)
        self.checkBox_main_music.setObjectName(u"checkBox_main_music")
        self.checkBox_main_music.setFont(font1)

        self.gridLayout_46.addWidget(self.checkBox_main_music, 1, 0, 1, 1)

        self.frame_162 = QFrame(self.groupBox_22)
        self.frame_162.setObjectName(u"frame_162")
        self.gridLayout_50 = QGridLayout(self.frame_162)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(-1, 0, -1, 3)
        self.radioButton_music_1 = QRadioButton(self.frame_162)
        self.radioButton_music_1.setObjectName(u"radioButton_music_1")
        self.radioButton_music_1.setChecked(False)

        self.gridLayout_50.addWidget(self.radioButton_music_1, 0, 0, 1, 1)

        self.radioButton_music_2 = QRadioButton(self.frame_162)
        self.radioButton_music_2.setObjectName(u"radioButton_music_2")
        self.radioButton_music_2.setChecked(True)

        self.gridLayout_50.addWidget(self.radioButton_music_2, 0, 1, 1, 1)

        self.radioButton_music_3 = QRadioButton(self.frame_162)
        self.radioButton_music_3.setObjectName(u"radioButton_music_3")

        self.gridLayout_50.addWidget(self.radioButton_music_3, 0, 2, 1, 1)


        self.gridLayout_46.addWidget(self.frame_162, 1, 1, 1, 2)


        self.gridLayout_42.addWidget(self.groupBox_22, 2, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.frame_21)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setFont(font1)
        self.gridLayout_44 = QGridLayout(self.groupBox_19)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.pushButton_add_Ai = QPushButton(self.groupBox_19)
        self.pushButton_add_Ai.setObjectName(u"pushButton_add_Ai")

        self.gridLayout_44.addWidget(self.pushButton_add_Ai, 0, 0, 1, 1)

        self.pushButton_del_Ai = QPushButton(self.groupBox_19)
        self.pushButton_del_Ai.setObjectName(u"pushButton_del_Ai")

        self.gridLayout_44.addWidget(self.pushButton_del_Ai, 0, 1, 1, 1)

        self.pushButton_save_Ai = QPushButton(self.groupBox_19)
        self.pushButton_save_Ai.setObjectName(u"pushButton_save_Ai")
        self.pushButton_save_Ai.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout_44.addWidget(self.pushButton_save_Ai, 0, 2, 1, 1)

        self.tableWidget_Ai = QTableWidget(self.groupBox_19)
        if (self.tableWidget_Ai.columnCount() < 4):
            self.tableWidget_Ai.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Ai.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Ai.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Ai.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Ai.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_Ai.setObjectName(u"tableWidget_Ai")
        self.tableWidget_Ai.setMinimumSize(QSize(0, 0))
        self.tableWidget_Ai.setMaximumSize(QSize(500, 380))
        self.tableWidget_Ai.setFont(font2)
        self.tableWidget_Ai.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_Ai.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Ai.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_44.addWidget(self.tableWidget_Ai, 1, 0, 1, 3)


        self.gridLayout_42.addWidget(self.groupBox_19, 3, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.frame_21)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMaximumSize(QSize(16777215, 150))
        self.groupBox_23.setFont(font1)
        self.gridLayout_49 = QGridLayout(self.groupBox_23)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.checkBox_show_ai = QCheckBox(self.groupBox_23)
        self.checkBox_show_ai.setObjectName(u"checkBox_show_ai")
        self.checkBox_show_ai.setFont(font1)
        self.checkBox_show_ai.setChecked(True)

        self.gridLayout_49.addWidget(self.checkBox_show_ai, 1, 3, 1, 1)

        self.checkBox_show_audio = QCheckBox(self.groupBox_23)
        self.checkBox_show_audio.setObjectName(u"checkBox_show_audio")
        self.checkBox_show_audio.setFont(font1)
        self.checkBox_show_audio.setChecked(True)

        self.gridLayout_49.addWidget(self.checkBox_show_audio, 1, 2, 1, 1)

        self.checkBox_show_orbit = QCheckBox(self.groupBox_23)
        self.checkBox_show_orbit.setObjectName(u"checkBox_show_orbit")
        self.checkBox_show_orbit.setFont(font1)

        self.gridLayout_49.addWidget(self.checkBox_show_orbit, 1, 0, 1, 1)

        self.checkBox_show_camera = QCheckBox(self.groupBox_23)
        self.checkBox_show_camera.setObjectName(u"checkBox_show_camera")
        self.checkBox_show_camera.setFont(font1)
        self.checkBox_show_camera.setChecked(True)

        self.gridLayout_49.addWidget(self.checkBox_show_camera, 1, 1, 1, 1)


        self.gridLayout_42.addWidget(self.groupBox_23, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_21, 0, 1, 1, 1)

        self.tabWidget_Ranking.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_26 = QGridLayout(self.tab_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_camera = QFrame(self.tab_3)
        self.frame_camera.setObjectName(u"frame_camera")
        self.frame_camera.setMinimumSize(QSize(0, 10))
        self.frame_camera.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_camera.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_camera)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 9, 0)
        self.widget = QWidget(self.frame_camera)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(320, 0))
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_65 = QGridLayout(self.widget)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.widget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(300, 10))
        self.groupBox_8.setMaximumSize(QSize(320, 16777215))
        self.groupBox_8.setFont(font1)
        self.gridLayout_28 = QGridLayout(self.groupBox_8)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.label_16, 3, 0, 1, 1)

        self.lineEdit_result_send = QLineEdit(self.groupBox_8)
        self.lineEdit_result_send.setObjectName(u"lineEdit_result_send")
        self.lineEdit_result_send.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.lineEdit_result_send, 3, 1, 1, 1)

        self.pushButton_Send_Res = QPushButton(self.groupBox_8)
        self.pushButton_Send_Res.setObjectName(u"pushButton_Send_Res")
        self.pushButton_Send_Res.setMinimumSize(QSize(50, 10))

        self.gridLayout_28.addWidget(self.pushButton_Send_Res, 3, 2, 1, 1)

        self.checkBox_ShowUdp = QCheckBox(self.groupBox_8)
        self.checkBox_ShowUdp.setObjectName(u"checkBox_ShowUdp")
        self.checkBox_ShowUdp.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.checkBox_ShowUdp, 4, 0, 1, 2)

        self.textBrowser_background_data = QTextBrowser(self.groupBox_8)
        self.textBrowser_background_data.setObjectName(u"textBrowser_background_data")
        self.textBrowser_background_data.setMinimumSize(QSize(0, 10))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.textBrowser_background_data.setFont(font3)
        self.textBrowser_background_data.setReadOnly(False)

        self.gridLayout_28.addWidget(self.textBrowser_background_data, 5, 0, 1, 3)

        self.widget_camera_sony = QWidget(self.groupBox_8)
        self.widget_camera_sony.setObjectName(u"widget_camera_sony")
        self.widget_camera_sony.setMinimumSize(QSize(230, 38))

        self.gridLayout_28.addWidget(self.widget_camera_sony, 0, 1, 1, 2)

        self.widget_camera_monitor = QWidget(self.groupBox_8)
        self.widget_camera_monitor.setObjectName(u"widget_camera_monitor")
        self.widget_camera_monitor.setMinimumSize(QSize(230, 38))

        self.gridLayout_28.addWidget(self.widget_camera_monitor, 1, 1, 1, 2)

        self.widget_camera_fit = QWidget(self.groupBox_8)
        self.widget_camera_fit.setObjectName(u"widget_camera_fit")
        self.widget_camera_fit.setMinimumSize(QSize(230, 38))

        self.gridLayout_28.addWidget(self.widget_camera_fit, 2, 1, 1, 2)

        self.label_87 = QLabel(self.groupBox_8)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.label_87, 0, 0, 1, 1)

        self.label_88 = QLabel(self.groupBox_8)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.label_88, 1, 0, 1, 1)

        self.label_89 = QLabel(self.groupBox_8)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.label_89, 2, 0, 1, 1)


        self.gridLayout_65.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.widget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(50, 50))
        self.groupBox_12.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_12.setFont(font1)
        self.gridLayout_31 = QGridLayout(self.groupBox_12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_Draw = QPushButton(self.groupBox_12)
        self.pushButton_Draw.setObjectName(u"pushButton_Draw")
        self.pushButton_Draw.setMinimumSize(QSize(0, 25))

        self.gridLayout_31.addWidget(self.pushButton_Draw, 0, 0, 1, 1)

        self.pushButton_to_TXT = QPushButton(self.groupBox_12)
        self.pushButton_to_TXT.setObjectName(u"pushButton_to_TXT")
        self.pushButton_to_TXT.setMinimumSize(QSize(0, 25))

        self.gridLayout_31.addWidget(self.pushButton_to_TXT, 0, 1, 1, 1)


        self.gridLayout_65.addWidget(self.groupBox_12, 1, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget, 0, 2, 2, 1)

        self.widget_camera = QWidget(self.frame_camera)
        self.widget_camera.setObjectName(u"widget_camera")
        self.groupBox_monitor_cam = QGroupBox(self.widget_camera)
        self.groupBox_monitor_cam.setObjectName(u"groupBox_monitor_cam")
        self.groupBox_monitor_cam.setGeometry(QRect(480, 0, 320, 480))
        self.groupBox_monitor_cam.setMinimumSize(QSize(0, 300))
        self.groupBox_monitor_cam.setFont(font1)
        self.groupBox_monitor_cam.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_33 = QGridLayout(self.groupBox_monitor_cam)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_monitor_picture = QLabel(self.groupBox_monitor_cam)
        self.label_monitor_picture.setObjectName(u"label_monitor_picture")
        self.label_monitor_picture.setMinimumSize(QSize(300, 10))

        self.gridLayout_33.addWidget(self.label_monitor_picture, 0, 0, 1, 1)

        self.groupBox_main_camera = QGroupBox(self.widget_camera)
        self.groupBox_main_camera.setObjectName(u"groupBox_main_camera")
        self.groupBox_main_camera.setGeometry(QRect(0, 0, 320, 480))
        self.groupBox_main_camera.setMinimumSize(QSize(0, 300))
        self.groupBox_main_camera.setFont(font1)
        self.groupBox_main_camera.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_15 = QGridLayout(self.groupBox_main_camera)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_main_picture = QLabel(self.groupBox_main_camera)
        self.label_main_picture.setObjectName(u"label_main_picture")
        self.label_main_picture.setMinimumSize(QSize(300, 10))

        self.gridLayout_15.addWidget(self.label_main_picture, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_camera, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_camera, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.tab_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 10))
        self.frame_11.setMaximumSize(QSize(16777215, 420))
        self.gridLayout_27 = QGridLayout(self.frame_11)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(9, 0, -1, 0)
        self.groupBox_14 = QGroupBox(self.frame_11)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(0, 10))
        self.groupBox_14.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_14.setFont(font1)
        self.gridLayout_37 = QGridLayout(self.groupBox_14)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, -1, 0, -1)
        self.widget_map = QWidget(self.groupBox_14)
        self.widget_map.setObjectName(u"widget_map")
        self.widget_map.setMinimumSize(QSize(350, 350))

        self.gridLayout_37.addWidget(self.widget_map, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.frame_11)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 10))
        self.groupBox_7.setMaximumSize(QSize(500, 16777215))
        self.groupBox_7.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_Ranking = QTableWidget(self.groupBox_7)
        if (self.tableWidget_Ranking.columnCount() < 5):
            self.tableWidget_Ranking.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_Ranking.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_Ranking.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_Ranking.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_Ranking.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Ranking.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.tableWidget_Ranking.setObjectName(u"tableWidget_Ranking")
        self.tableWidget_Ranking.setMinimumSize(QSize(330, 10))
        self.tableWidget_Ranking.setMaximumSize(QSize(500, 16777215))
        self.tableWidget_Ranking.setFont(font2)
        self.tableWidget_Ranking.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_Ranking.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Ranking.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget_Ranking, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.widget_20 = QWidget(self.frame_11)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(320, 10))
        self.widget_20.setMaximumSize(QSize(200, 16777215))
        self.widget_20.setFont(font1)
        self.gridLayout_29 = QGridLayout(self.widget_20)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.widget_20)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 10))
        self.groupBox_11.setMaximumSize(QSize(16777215, 180))
        self.gridLayout_30 = QGridLayout(self.groupBox_11)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(-1, 0, -1, 6)
        self.label_15 = QLabel(self.groupBox_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.label_15, 2, 0, 1, 1)

        self.pushButton_save_Ranking = QPushButton(self.groupBox_11)
        self.pushButton_save_Ranking.setObjectName(u"pushButton_save_Ranking")
        self.pushButton_save_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.pushButton_save_Ranking, 4, 0, 1, 4)

        self.lineEdit_area_Ranking = QLineEdit(self.groupBox_11)
        self.lineEdit_area_Ranking.setObjectName(u"lineEdit_area_Ranking")
        self.lineEdit_area_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.lineEdit_area_Ranking, 1, 2, 1, 2)

        self.lineEdit_lap_Ranking = QLineEdit(self.groupBox_11)
        self.lineEdit_lap_Ranking.setObjectName(u"lineEdit_lap_Ranking")
        self.lineEdit_lap_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.lineEdit_lap_Ranking, 3, 2, 1, 2)

        self.lineEdit_Time_Restart_Ranking = QLineEdit(self.groupBox_11)
        self.lineEdit_Time_Restart_Ranking.setObjectName(u"lineEdit_Time_Restart_Ranking")
        self.lineEdit_Time_Restart_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.lineEdit_Time_Restart_Ranking, 2, 2, 1, 2)

        self.label_13 = QLabel(self.groupBox_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 10))

        self.gridLayout_30.addWidget(self.label_14, 3, 0, 1, 1)

        self.pushButton_udp_time = QPushButton(self.groupBox_11)
        self.pushButton_udp_time.setObjectName(u"pushButton_udp_time")
        self.pushButton_udp_time.setMinimumSize(QSize(0, 10))
        self.pushButton_udp_time.setStyleSheet(u"background:rgb(0, 255, 0)")

        self.gridLayout_30.addWidget(self.pushButton_udp_time, 0, 0, 1, 4)


        self.gridLayout_29.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.widget_20)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMinimumSize(QSize(0, 10))
        self.groupBox_18.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_18.setFont(font1)
        self.gridLayout_48 = QGridLayout(self.groupBox_18)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(-1, 0, -1, 6)
        self.groupBox_25 = QGroupBox(self.groupBox_18)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(0, 10))
        self.gridLayout_41 = QGridLayout(self.groupBox_25)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(-1, 0, -1, 0)
        self.label_42 = QLabel(self.groupBox_25)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 10))
        self.label_42.setFont(font1)

        self.gridLayout_41.addWidget(self.label_42, 0, 5, 1, 1)

        self.label_27 = QLabel(self.groupBox_25)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 10))
        self.label_27.setMaximumSize(QSize(120, 16777215))
        self.label_27.setFont(font1)

        self.gridLayout_41.addWidget(self.label_27, 0, 2, 1, 1)

        self.checkBox_restart = QCheckBox(self.groupBox_25)
        self.checkBox_restart.setObjectName(u"checkBox_restart")
        self.checkBox_restart.setMinimumSize(QSize(80, 10))
        self.checkBox_restart.setFont(font1)

        self.gridLayout_41.addWidget(self.checkBox_restart, 0, 0, 1, 1)

        self.lineEdit_time = QLineEdit(self.groupBox_25)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setMinimumSize(QSize(0, 10))
        self.lineEdit_time.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_time.setFont(font1)
        self.lineEdit_time.setStyleSheet(u"background:rgb(238, 238, 238)")
        self.lineEdit_time.setReadOnly(True)

        self.gridLayout_41.addWidget(self.lineEdit_time, 0, 3, 1, 1)

        self.frame_30 = QFrame(self.groupBox_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(20, 10))
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_41.addWidget(self.frame_30, 0, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_25, 0, 0, 1, 1)

        self.groupBox_33 = QGroupBox(self.groupBox_18)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setMinimumSize(QSize(0, 10))
        self.gridLayout_47 = QGridLayout(self.groupBox_33)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.lineEdit_time_count_ball = QLineEdit(self.groupBox_33)
        self.lineEdit_time_count_ball.setObjectName(u"lineEdit_time_count_ball")
        self.lineEdit_time_count_ball.setMinimumSize(QSize(0, 10))
        self.lineEdit_time_count_ball.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_47.addWidget(self.lineEdit_time_count_ball, 2, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_33)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 10))
        self.label_28.setFont(font1)

        self.gridLayout_47.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_33)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 10))
        self.label_41.setFont(font1)

        self.gridLayout_47.addWidget(self.label_41, 2, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox_33)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 10))
        self.label_29.setFont(font1)

        self.gridLayout_47.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_40 = QLabel(self.groupBox_33)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 10))
        self.label_40.setFont(font1)

        self.gridLayout_47.addWidget(self.label_40, 2, 2, 1, 1)

        self.lineEdit_time_send_result = QLineEdit(self.groupBox_33)
        self.lineEdit_time_send_result.setObjectName(u"lineEdit_time_send_result")
        self.lineEdit_time_send_result.setMinimumSize(QSize(0, 10))
        self.lineEdit_time_send_result.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_47.addWidget(self.lineEdit_time_send_result, 0, 1, 1, 1)

        self.pushButton_CardRun_2 = QPushButton(self.groupBox_33)
        self.pushButton_CardRun_2.setObjectName(u"pushButton_CardRun_2")
        self.pushButton_CardRun_2.setMinimumSize(QSize(0, 10))
        self.pushButton_CardRun_2.setFont(font1)
        self.pushButton_CardRun_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_47.addWidget(self.pushButton_CardRun_2, 0, 3, 1, 1)

        self.pushButton_CardStop_2 = QPushButton(self.groupBox_33)
        self.pushButton_CardStop_2.setObjectName(u"pushButton_CardStop_2")
        self.pushButton_CardStop_2.setMinimumSize(QSize(0, 10))
        self.pushButton_CardStop_2.setFont(font1)
        self.pushButton_CardStop_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_47.addWidget(self.pushButton_CardStop_2, 2, 3, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_33, 1, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.groupBox_18)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(0, 10))
        self.gridLayout_43 = QGridLayout(self.groupBox_24)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.frame_32 = QFrame(self.groupBox_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(20, 10))
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_43.addWidget(self.frame_32, 1, 3, 1, 1)

        self.frame_31 = QFrame(self.groupBox_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(20, 10))
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_43.addWidget(self.frame_31, 0, 3, 1, 1)

        self.pushButton_CardClose = QPushButton(self.groupBox_24)
        self.pushButton_CardClose.setObjectName(u"pushButton_CardClose")
        self.pushButton_CardClose.setMinimumSize(QSize(80, 0))
        self.pushButton_CardClose.setFont(font1)
        self.pushButton_CardClose.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_43.addWidget(self.pushButton_CardClose, 0, 4, 1, 1)

        self.pushButton_Cardreset = QPushButton(self.groupBox_24)
        self.pushButton_Cardreset.setObjectName(u"pushButton_Cardreset")
        self.pushButton_Cardreset.setMinimumSize(QSize(80, 0))
        self.pushButton_Cardreset.setFont(font1)
        self.pushButton_Cardreset.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_43.addWidget(self.pushButton_Cardreset, 1, 4, 1, 1)

        self.lineEdit_ball_start = QLineEdit(self.groupBox_24)
        self.lineEdit_ball_start.setObjectName(u"lineEdit_ball_start")
        self.lineEdit_ball_start.setMinimumSize(QSize(50, 10))
        self.lineEdit_ball_start.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_ball_start.setFont(font1)
        self.lineEdit_ball_start.setStyleSheet(u"background:rgb(238, 238, 238)")
        self.lineEdit_ball_start.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_ball_start, 0, 2, 1, 1)

        self.lineEdit_ball_end = QLineEdit(self.groupBox_24)
        self.lineEdit_ball_end.setObjectName(u"lineEdit_ball_end")
        self.lineEdit_ball_end.setMinimumSize(QSize(50, 10))
        self.lineEdit_ball_end.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_ball_end.setFont(font1)
        self.lineEdit_ball_end.setStyleSheet(u"background:rgb(238, 238, 238)")
        self.lineEdit_ball_end.setReadOnly(True)

        self.gridLayout_43.addWidget(self.lineEdit_ball_end, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_24)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 10))
        self.label_8.setMaximumSize(QSize(150, 16777215))
        self.label_8.setFont(font1)

        self.gridLayout_43.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_24)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 10))
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setFont(font1)

        self.gridLayout_43.addWidget(self.label_7, 1, 1, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_24, 2, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_18, 1, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_20, 0, 3, 1, 1)


        self.gridLayout_26.addWidget(self.frame_11, 0, 0, 1, 1)

        self.tabWidget_Ranking.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget_Ranking, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_Ranking.setCurrentIndex(0)
        self.pushButton_CardRun_2.setDefault(True)
        self.pushButton_CardStop_2.setDefault(True)
        self.pushButton_CardClose.setDefault(True)
        self.pushButton_Cardreset.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u63a7", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u955c\u5934\u70b9\u4f4d\u8bbe\u7f6e", None))
        self.pushButton_del_camera.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u5c11\u70b9\u4f4d", None))
        self.pushButton_add_camera.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u70b9\u4f4d", None))
        self.pushButton_save_camera.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u70b9\u4f4d", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\u97f3\u6548\u70b9\u4f4d\u8bbe\u7f6e", None))
        self.pushButton_add_Audio.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u70b9\u4f4d", None))
        self.pushButton_del_Audio.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u5c11\u70b9\u4f4d", None))
        self.pushButton_save_Audio.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u70b9\u4f4d", None))
        ___qtablewidgetitem = self.tableWidget_Audio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u6548", None));
        ___qtablewidgetitem1 = self.tableWidget_Audio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u6570", None));
        ___qtablewidgetitem2 = self.tableWidget_Audio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6", None));
        ___qtablewidgetitem3 = self.tableWidget_Audio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None));
        self.checkBox_main_music.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898\u97f3", None))
        self.radioButton_music_1.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898\u97f31", None))
        self.radioButton_music_2.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898\u97f32", None))
        self.radioButton_music_3.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898\u97f33", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"AI\u8bed\u97f3\u70b9\u4f4d\u8bbe\u7f6e", None))
        self.pushButton_add_Ai.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u70b9\u4f4d", None))
        self.pushButton_del_Ai.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u5c11\u70b9\u4f4d", None))
        self.pushButton_save_Ai.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u70b9\u4f4d", None))
        ___qtablewidgetitem4 = self.tableWidget_Ai.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u6548", None));
        ___qtablewidgetitem5 = self.tableWidget_Ai.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6b21\u6570", None));
        ___qtablewidgetitem6 = self.tableWidget_Ai.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6", None));
        ___qtablewidgetitem7 = self.tableWidget_Ai.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None));
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"\u70b9\u4f4d\u663e\u793a", None))
        self.checkBox_show_ai.setText(QCoreApplication.translate("MainWindow", u"Ai\u70b9\u4f4d", None))
        self.checkBox_show_audio.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u6548\u70b9\u4f4d", None))
        self.checkBox_show_orbit.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8f68\u8ff9", None))
        self.checkBox_show_camera.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\u70b9\u4f4d", None))
        self.tabWidget_Ranking.setTabText(self.tabWidget_Ranking.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u536b\u661f\u56fe", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6570\u636e", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_result_send.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u6700\u5927\u5708\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Send_Res.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u7ed3\u679c", None))
        self.checkBox_ShowUdp.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u670d\u52a1\u5668\u6570\u636e", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u7d22\u5c3c:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5bf9:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u5730\u56fe\u5212\u533a\u7f16\u8f91\u5236\u4f5c", None))
        self.pushButton_Draw.setText(QCoreApplication.translate("MainWindow", u"\u753b\u56fe\u5de5\u5177", None))
        self.pushButton_to_TXT.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362TXT", None))
        self.groupBox_monitor_cam.setTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u6444\u50cf\u673a\u8bc6\u522b\u7ed3\u679c", None))
        self.label_monitor_picture.setText("")
        self.groupBox_main_camera.setTitle(QCoreApplication.translate("MainWindow", u"\u7d22\u5c3c\u6444\u50cf\u673a\u8bc6\u522b\u7ed3\u679c", None))
        self.label_main_picture.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u536b\u661f\u56fe", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u6392\u540d", None))
        ___qtablewidgetitem8 = self.tableWidget_Ranking.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None));
        ___qtablewidgetitem9 = self.tableWidget_Ranking.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u533a\u57df", None));
        ___qtablewidgetitem10 = self.tableWidget_Ranking.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5708\u6570", None));
        ___qtablewidgetitem11 = self.tableWidget_Ranking.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem12 = self.tableWidget_Ranking.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"y", None));
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u6392\u540d\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u65f6\u95f4:", None))
        self.pushButton_save_Ranking.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_area_Ranking.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u6700\u5927\u533a\u57df\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_lap_Ranking.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u6700\u5927\u5708\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_Time_Restart_Ranking.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u533a\u57df:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u5708\u6570:", None))
        self.pushButton_udp_time.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b\u72b6\u6001\u6b63\u5e38", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\u7ec8\u70b9\u8bbe\u7f6e", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u5012\u8ba1\u65f6\uff1a", None))
        self.checkBox_restart.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6a21\u5f0f", None))
        self.lineEdit_time_count_ball.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u7ed3\u679c\u65f6\u95f4\uff1a", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1\u7403\u65f6\u95f4\uff1a", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.lineEdit_time_send_result.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_CardRun_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_CardStop_2.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_CardClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u673a\u5173", None))
        self.pushButton_Cardreset.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d", None))
        self.lineEdit_ball_start.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_ball_end.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u70b9\u7403\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u7ec8\u70b9\u7403\u6570\uff1a", None))
        self.tabWidget_Ranking.setTabText(self.tabWidget_Ranking.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b", None))
    # retranslateUi

