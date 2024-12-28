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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 889)
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
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.gridLayout_39 = QGridLayout(self.tab_0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_map_big = QWidget(self.tab_0)
        self.widget_map_big.setObjectName(u"widget_map_big")
        self.widget_map_big.setMinimumSize(QSize(860, 860))

        self.gridLayout_39.addWidget(self.widget_map_big, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.tab_0)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(300, 0))
        self.frame_21.setMaximumSize(QSize(300, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_21)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser = QTextBrowser(self.frame_21)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 10))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.textBrowser.setFont(font1)
        self.textBrowser.setReadOnly(False)

        self.gridLayout_3.addWidget(self.textBrowser, 3, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.frame_21)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(50, 50))
        self.groupBox_15.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.groupBox_15.setFont(font2)
        self.gridLayout_34 = QGridLayout(self.groupBox_15)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(-1, 9, -1, -1)
        self.pushButton_Draw = QPushButton(self.groupBox_15)
        self.pushButton_Draw.setObjectName(u"pushButton_Draw")
        self.pushButton_Draw.setMinimumSize(QSize(0, 25))

        self.gridLayout_34.addWidget(self.pushButton_Draw, 0, 0, 1, 1)

        self.pushButton_to_TXT = QPushButton(self.groupBox_15)
        self.pushButton_to_TXT.setObjectName(u"pushButton_to_TXT")
        self.pushButton_to_TXT.setMinimumSize(QSize(0, 25))

        self.gridLayout_34.addWidget(self.pushButton_to_TXT, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_15, 2, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.frame_21)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 10))
        self.groupBox_13.setMaximumSize(QSize(16777215, 180))
        self.groupBox_13.setFont(font2)
        self.gridLayout_32 = QGridLayout(self.groupBox_13)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(6)
        self.gridLayout_32.setContentsMargins(-1, 9, -1, 9)
        self.label_19 = QLabel(self.groupBox_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.label_17, 2, 0, 1, 1)

        self.lineEdit_lap_Ranking = QLineEdit(self.groupBox_13)
        self.lineEdit_lap_Ranking.setObjectName(u"lineEdit_lap_Ranking")
        self.lineEdit_lap_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.lineEdit_lap_Ranking, 3, 1, 1, 2)

        self.label_18 = QLabel(self.groupBox_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_area_Ranking = QLineEdit(self.groupBox_13)
        self.lineEdit_area_Ranking.setObjectName(u"lineEdit_area_Ranking")
        self.lineEdit_area_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.lineEdit_area_Ranking, 1, 1, 1, 2)

        self.lineEdit_flash_Ranking = QLineEdit(self.groupBox_13)
        self.lineEdit_flash_Ranking.setObjectName(u"lineEdit_flash_Ranking")
        self.lineEdit_flash_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.lineEdit_flash_Ranking, 2, 1, 1, 2)

        self.pushButton_save_Ranking = QPushButton(self.groupBox_13)
        self.pushButton_save_Ranking.setObjectName(u"pushButton_save_Ranking")
        self.pushButton_save_Ranking.setMinimumSize(QSize(0, 10))

        self.gridLayout_32.addWidget(self.pushButton_save_Ranking, 4, 0, 1, 3)


        self.gridLayout_3.addWidget(self.groupBox_13, 1, 0, 1, 1)

        self.checkBox_show_orbit = QCheckBox(self.frame_21)
        self.checkBox_show_orbit.setObjectName(u"checkBox_show_orbit")
        self.checkBox_show_orbit.setFont(font2)

        self.gridLayout_3.addWidget(self.checkBox_show_orbit, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_21, 0, 1, 1, 1)

        self.tabWidget_Ranking.addTab(self.tab_0, "")

        self.gridLayout.addWidget(self.tabWidget_Ranking, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_Ranking.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u63a7", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u5730\u56fe\u5212\u533a\u7f16\u8f91\u5236\u4f5c", None))
        self.pushButton_Draw.setText(QCoreApplication.translate("MainWindow", u"\u753b\u56fe\u5de5\u5177", None))
        self.pushButton_to_TXT.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362TXT", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u6392\u540d\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5708\u6570:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u8e2a\u901f\u5ea6(ms):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_lap_Ranking.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u6700\u5927\u5708\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u533a\u57df:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_area_Ranking.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u6700\u5927\u533a\u57df\u6570</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_flash_Ranking.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_Ranking.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.checkBox_show_orbit.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8f68\u8ff9", None))
        self.tabWidget_Ranking.setTabText(self.tabWidget_Ranking.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"\u536b\u661f\u56fe", None))
    # retranslateUi

