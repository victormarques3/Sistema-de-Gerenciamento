# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTimeEdit,
    QToolBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(749, 463)
        MainWindow.setMinimumSize(QSize(749, 463))
        icon = QIcon()
        icon.addFile(u":/icon/Icones/Hopstarter-Puck-Norton-System-Works.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.frame_direita = QFrame(self.centralwidget)
        self.frame_direita.setObjectName(u"frame_direita")
        self.frame_direita.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"border-radius: 8px")
        self.frame_direita.setFrameShape(QFrame.StyledPanel)
        self.frame_direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_direita)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.frame_direita)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.frame_2)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"background-color:none")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Icones/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_principal = QFrame(self.frame_direita)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.stackedWidget = QStackedWidget(self.frame_principal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(u"background-color: none;\n"
"border-radius: none;")
        self.pg_menu = QWidget()
        self.pg_menu.setObjectName(u"pg_menu")
        self.pg_menu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_14 = QVBoxLayout(self.pg_menu)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_22 = QLabel(self.pg_menu)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setTabletTracking(False)
        self.label_22.setAcceptDrops(False)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet(u"background-color: none")
        self.label_22.setScaledContents(False)
        self.label_22.setWordWrap(False)
        self.label_22.setOpenExternalLinks(False)

        self.verticalLayout_14.addWidget(self.label_22)

        self.stackedWidget.addWidget(self.pg_menu)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.pg_estoque.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_6 = QVBoxLayout(self.pg_estoque)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.pg_estoque)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 8px")

        self.verticalLayout_6.addWidget(self.label_6)

        self.tabWidget = QTabWidget(self.pg_estoque)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"font: bold;\n"
"color:rgb(255, 255, 255)")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_estoque_adicionar = QTableWidget(self.tab)
        if (self.tableWidget_estoque_adicionar.columnCount() < 5):
            self.tableWidget_estoque_adicionar.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_estoque_adicionar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_estoque_adicionar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_estoque_adicionar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_estoque_adicionar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_estoque_adicionar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_estoque_adicionar.setObjectName(u"tableWidget_estoque_adicionar")
        self.tableWidget_estoque_adicionar.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.tableWidget_estoque_adicionar)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_estoque_produto = QLineEdit(self.frame_3)
        self.lineEdit_estoque_produto.setObjectName(u"lineEdit_estoque_produto")
        self.lineEdit_estoque_produto.setMinimumSize(QSize(0, 20))
        self.lineEdit_estoque_produto.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_estoque_produto, 1, 0, 1, 2)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignLeft)

        self.btn_estoque_adicionar = QPushButton(self.frame_3)
        self.btn_estoque_adicionar.setObjectName(u"btn_estoque_adicionar")
        self.btn_estoque_adicionar.setMinimumSize(QSize(200, 20))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btn_estoque_adicionar.setFont(font1)
        self.btn_estoque_adicionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque_adicionar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.btn_estoque_adicionar, 4, 1, 1, 2, Qt.AlignHCenter)

        self.lineEdit_estoque_valorVenda = QLineEdit(self.frame_3)
        self.lineEdit_estoque_valorVenda.setObjectName(u"lineEdit_estoque_valorVenda")
        self.lineEdit_estoque_valorVenda.setMinimumSize(QSize(0, 20))
        self.lineEdit_estoque_valorVenda.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_estoque_valorVenda, 3, 2, 1, 2)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1, Qt.AlignLeft)

        self.lineEdit_estoque_quantidade = QLineEdit(self.frame_3)
        self.lineEdit_estoque_quantidade.setObjectName(u"lineEdit_estoque_quantidade")
        self.lineEdit_estoque_quantidade.setMinimumSize(QSize(0, 20))
        self.lineEdit_estoque_quantidade.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_estoque_quantidade, 3, 0, 1, 2)

        self.lineEdit_estoque_valorCompra = QLineEdit(self.frame_3)
        self.lineEdit_estoque_valorCompra.setObjectName(u"lineEdit_estoque_valorCompra")
        self.lineEdit_estoque_valorCompra.setMinimumSize(QSize(0, 20))
        self.lineEdit_estoque_valorCompra.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_2.addWidget(self.lineEdit_estoque_valorCompra, 1, 2, 1, 2)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 2, 1, 1, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_21 = QVBoxLayout(self.tab_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_estoque_remover = QTableWidget(self.tab_2)
        if (self.tableWidget_estoque_remover.columnCount() < 5):
            self.tableWidget_estoque_remover.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_estoque_remover.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_estoque_remover.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_estoque_remover.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_estoque_remover.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_estoque_remover.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_estoque_remover.setObjectName(u"tableWidget_estoque_remover")
        self.tableWidget_estoque_remover.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_21.addWidget(self.tableWidget_estoque_remover)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_27 = QLabel(self.tab_2)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_9.addWidget(self.label_27)

        self.lineEdit_estoque_remover = QLineEdit(self.tab_2)
        self.lineEdit_estoque_remover.setObjectName(u"lineEdit_estoque_remover")
        self.lineEdit_estoque_remover.setMinimumSize(QSize(0, 20))
        self.lineEdit_estoque_remover.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.verticalLayout_9.addWidget(self.lineEdit_estoque_remover)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_10)

        self.btn_estoque_remover = QPushButton(self.tab_2)
        self.btn_estoque_remover.setObjectName(u"btn_estoque_remover")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_estoque_remover.sizePolicy().hasHeightForWidth())
        self.btn_estoque_remover.setSizePolicy(sizePolicy1)
        self.btn_estoque_remover.setMinimumSize(QSize(0, 20))
        self.btn_estoque_remover.setFont(font1)
        self.btn_estoque_remover.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque_remover.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.btn_estoque_remover)


        self.horizontalLayout_8.addLayout(self.verticalLayout_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_estoque_editar = QTableWidget(self.tab_3)
        if (self.tableWidget_estoque_editar.columnCount() < 5):
            self.tableWidget_estoque_editar.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_estoque_editar.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_estoque_editar.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_estoque_editar.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_estoque_editar.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_estoque_editar.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableWidget_estoque_editar.setObjectName(u"tableWidget_estoque_editar")
        self.tableWidget_estoque_editar.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.tableWidget_estoque_editar)

        self.btn_estoque_editar = QPushButton(self.tab_3)
        self.btn_estoque_editar.setObjectName(u"btn_estoque_editar")
        self.btn_estoque_editar.setMinimumSize(QSize(200, 20))
        self.btn_estoque_editar.setFont(font1)
        self.btn_estoque_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estoque_editar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btn_estoque_editar, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.pg_estoque)
        self.pg_clientes = QWidget()
        self.pg_clientes.setObjectName(u"pg_clientes")
        self.pg_clientes.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_12 = QVBoxLayout(self.pg_clientes)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_11 = QLabel(self.pg_clientes)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 8px")

        self.verticalLayout_12.addWidget(self.label_11)

        self.tabWidget_3 = QTabWidget(self.pg_clientes)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setMouseTracking(False)
        self.tabWidget_3.setTabletTracking(False)
        self.tabWidget_3.setAcceptDrops(False)
        self.tabWidget_3.setAutoFillBackground(False)
        self.tabWidget_3.setStyleSheet(u"font: bold;\n"
"color:rgb(255, 255, 255)")
        self.tabWidget_3.setTabPosition(QTabWidget.North)
        self.tabWidget_3.setTabShape(QTabWidget.Triangular)
        self.tabWidget_3.setIconSize(QSize(16, 16))
        self.tabWidget_3.setElideMode(Qt.ElideNone)
        self.tabWidget_3.setUsesScrollButtons(True)
        self.tabWidget_3.setDocumentMode(True)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setMovable(True)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setSpacing(9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.tab_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-radius: none;\n"
"background-color: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.radioButton_clientes_sim = QRadioButton(self.frame_4)
        self.radioButton_clientes_sim.setObjectName(u"radioButton_clientes_sim")
        self.radioButton_clientes_sim.setEnabled(True)
        self.radioButton_clientes_sim.setCheckable(True)
        self.radioButton_clientes_sim.setChecked(False)

        self.gridLayout_3.addWidget(self.radioButton_clientes_sim, 2, 0, 1, 1)

        self.radioButton_clientes_nao = QRadioButton(self.frame_4)
        self.radioButton_clientes_nao.setObjectName(u"radioButton_clientes_nao")
        self.radioButton_clientes_nao.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_clientes_nao, 1, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_cliente_produto = QComboBox(self.frame_4)
        self.comboBox_cliente_produto.setObjectName(u"comboBox_cliente_produto")
        self.comboBox_cliente_produto.setMinimumSize(QSize(0, 20))
        self.comboBox_cliente_produto.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_4.addWidget(self.comboBox_cliente_produto, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit_cliente_quantidade = QLineEdit(self.frame_4)
        self.lineEdit_cliente_quantidade.setObjectName(u"lineEdit_cliente_quantidade")
        self.lineEdit_cliente_quantidade.setMinimumSize(QSize(0, 20))
        self.lineEdit_cliente_quantidade.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_5.addWidget(self.lineEdit_cliente_quantidade, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_5)

        self.btn_cliente_adicionar = QPushButton(self.frame_4)
        self.btn_cliente_adicionar.setObjectName(u"btn_cliente_adicionar")
        self.btn_cliente_adicionar.setMinimumSize(QSize(100, 20))
        self.btn_cliente_adicionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente_adicionar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.btn_cliente_adicionar)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.label_cliente_valor = QLabel(self.frame_4)
        self.label_cliente_valor.setObjectName(u"label_cliente_valor")

        self.verticalLayout_11.addWidget(self.label_cliente_valor)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.btn_cliente_apagar = QPushButton(self.frame_4)
        self.btn_cliente_apagar.setObjectName(u"btn_cliente_apagar")
        self.btn_cliente_apagar.setMinimumSize(QSize(100, 25))
        self.btn_cliente_apagar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente_apagar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.btn_cliente_apagar)


        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.tab_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: none;\n"
"border-radius: none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_cliente_venda = QTableWidget(self.frame_5)
        if (self.tableWidget_cliente_venda.columnCount() < 3):
            self.tableWidget_cliente_venda.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_cliente_venda.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_cliente_venda.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_cliente_venda.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        self.tableWidget_cliente_venda.setObjectName(u"tableWidget_cliente_venda")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.tableWidget_cliente_venda.setFont(font2)
        self.tableWidget_cliente_venda.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 0px")
        self.tableWidget_cliente_venda.setTabKeyNavigation(True)
        self.tableWidget_cliente_venda.setProperty("showDropIndicator", True)
        self.tableWidget_cliente_venda.setDragEnabled(False)
        self.tableWidget_cliente_venda.setDragDropOverwriteMode(True)
        self.tableWidget_cliente_venda.setAlternatingRowColors(False)
        self.tableWidget_cliente_venda.horizontalHeader().setDefaultSectionSize(85)

        self.verticalLayout_13.addWidget(self.tableWidget_cliente_venda)

        self.label_38 = QLabel(self.frame_5)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_13.addWidget(self.label_38)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.radioButton_cliente_novoCliente = QRadioButton(self.frame_5)
        self.radioButton_cliente_novoCliente.setObjectName(u"radioButton_cliente_novoCliente")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radioButton_cliente_novoCliente.sizePolicy().hasHeightForWidth())
        self.radioButton_cliente_novoCliente.setSizePolicy(sizePolicy2)
        self.radioButton_cliente_novoCliente.setMinimumSize(QSize(1, 20))
        self.radioButton_cliente_novoCliente.setChecked(True)

        self.gridLayout_6.addWidget(self.radioButton_cliente_novoCliente, 0, 0, 1, 1)

        self.lineEdit_cliente_novoCliente = QLineEdit(self.frame_5)
        self.lineEdit_cliente_novoCliente.setObjectName(u"lineEdit_cliente_novoCliente")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_cliente_novoCliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_cliente_novoCliente.setSizePolicy(sizePolicy3)
        self.lineEdit_cliente_novoCliente.setMinimumSize(QSize(0, 20))
        self.lineEdit_cliente_novoCliente.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")
        self.lineEdit_cliente_novoCliente.setDragEnabled(False)
        self.lineEdit_cliente_novoCliente.setReadOnly(False)
        self.lineEdit_cliente_novoCliente.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.lineEdit_cliente_novoCliente, 0, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_6)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_13.addWidget(self.label_16)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(8)
        self.comboBox_cliente_cliente = QComboBox(self.frame_5)
        self.comboBox_cliente_cliente.setObjectName(u"comboBox_cliente_cliente")
        self.comboBox_cliente_cliente.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.comboBox_cliente_cliente.sizePolicy().hasHeightForWidth())
        self.comboBox_cliente_cliente.setSizePolicy(sizePolicy1)
        self.comboBox_cliente_cliente.setMinimumSize(QSize(0, 20))
        self.comboBox_cliente_cliente.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")
        self.comboBox_cliente_cliente.setEditable(False)
        self.comboBox_cliente_cliente.setDuplicatesEnabled(False)
        self.comboBox_cliente_cliente.setFrame(True)

        self.gridLayout_7.addWidget(self.comboBox_cliente_cliente, 1, 1, 1, 1)

        self.radioButton_cliente_cliente = QRadioButton(self.frame_5)
        self.radioButton_cliente_cliente.setObjectName(u"radioButton_cliente_cliente")
        sizePolicy2.setHeightForWidth(self.radioButton_cliente_cliente.sizePolicy().hasHeightForWidth())
        self.radioButton_cliente_cliente.setSizePolicy(sizePolicy2)
        self.radioButton_cliente_cliente.setMinimumSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.radioButton_cliente_cliente, 1, 0, 1, 1)

        self.btn_cliente_vender = QPushButton(self.frame_5)
        self.btn_cliente_vender.setObjectName(u"btn_cliente_vender")
        self.btn_cliente_vender.setMinimumSize(QSize(100, 25))
        self.btn_cliente_vender.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente_vender.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.btn_cliente_vender, 2, 0, 1, 2)


        self.verticalLayout_13.addLayout(self.gridLayout_7)


        self.gridLayout_8.addWidget(self.frame_5, 0, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_10 = QVBoxLayout(self.tab_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_cliente_tabela = QTableWidget(self.tab_7)
        if (self.tableWidget_cliente_tabela.columnCount() < 5):
            self.tableWidget_cliente_tabela.setColumnCount(5)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_cliente_tabela.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_cliente_tabela.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_cliente_tabela.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_cliente_tabela.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_cliente_tabela.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        self.tableWidget_cliente_tabela.setObjectName(u"tableWidget_cliente_tabela")
        self.tableWidget_cliente_tabela.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.tableWidget_cliente_tabela)

        self.tabWidget_3.addTab(self.tab_7, "")

        self.verticalLayout_12.addWidget(self.tabWidget_3)

        self.stackedWidget.addWidget(self.pg_clientes)
        self.pg_dividas = QWidget()
        self.pg_dividas.setObjectName(u"pg_dividas")
        self.pg_dividas.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: bold;\n"
"color:rgb(255, 255, 255)")
        self.verticalLayout_19 = QVBoxLayout(self.pg_dividas)
        self.verticalLayout_19.setSpacing(7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.pg_dividas)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.label_17)

        self.tableWidget_dividas = QTableWidget(self.pg_dividas)
        if (self.tableWidget_dividas.columnCount() < 3):
            self.tableWidget_dividas.setColumnCount(3)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_dividas.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_dividas.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_dividas.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        self.tableWidget_dividas.setObjectName(u"tableWidget_dividas")
        self.tableWidget_dividas.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_19.addWidget(self.tableWidget_dividas)

        self.splitter = QSplitter(self.pg_dividas)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setFrameShadow(QFrame.Plain)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(True)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.comboBox_dividas_cliente = QComboBox(self.layoutWidget)
        self.comboBox_dividas_cliente.setObjectName(u"comboBox_dividas_cliente")
        self.comboBox_dividas_cliente.setMinimumSize(QSize(0, 20))
        self.comboBox_dividas_cliente.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_11.addWidget(self.comboBox_dividas_cliente, 1, 0, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_11)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lineEdit_dividas_valorRecebido = QLineEdit(self.layoutWidget)
        self.lineEdit_dividas_valorRecebido.setObjectName(u"lineEdit_dividas_valorRecebido")
        self.lineEdit_dividas_valorRecebido.setMinimumSize(QSize(0, 20))
        self.lineEdit_dividas_valorRecebido.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.gridLayout_9.addWidget(self.lineEdit_dividas_valorRecebido, 1, 0, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_9)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_dividas_total = QLabel(self.layoutWidget1)
        self.label_dividas_total.setObjectName(u"label_dividas_total")
        self.label_dividas_total.setMinimumSize(QSize(120, 0))

        self.verticalLayout_23.addWidget(self.label_dividas_total)

        self.label_dividas_troco = QLabel(self.layoutWidget1)
        self.label_dividas_troco.setObjectName(u"label_dividas_troco")

        self.verticalLayout_23.addWidget(self.label_dividas_troco)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_19.addWidget(self.splitter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_dividas_resetar = QPushButton(self.pg_dividas)
        self.btn_dividas_resetar.setObjectName(u"btn_dividas_resetar")
        self.btn_dividas_resetar.setMinimumSize(QSize(200, 20))
        self.btn_dividas_resetar.setFont(font1)
        self.btn_dividas_resetar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dividas_resetar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_dividas_resetar)

        self.btn_dividas_pagar = QPushButton(self.pg_dividas)
        self.btn_dividas_pagar.setObjectName(u"btn_dividas_pagar")
        self.btn_dividas_pagar.setMinimumSize(QSize(200, 20))
        self.btn_dividas_pagar.setFont(font1)
        self.btn_dividas_pagar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dividas_pagar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_dividas_pagar)


        self.verticalLayout_19.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.pg_dividas)
        self.pg_balanco = QWidget()
        self.pg_balanco.setObjectName(u"pg_balanco")
        self.pg_balanco.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: bold;\n"
"color:rgb(255, 255, 255)")
        self.verticalLayout_27 = QVBoxLayout(self.pg_balanco)
        self.verticalLayout_27.setSpacing(7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.label_39 = QLabel(self.pg_balanco)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_27.addWidget(self.label_39)

        self.frame_7 = QFrame(self.pg_balanco)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_balanco_LI = QTableWidget(self.frame_7)
        if (self.tableWidget_balanco_LI.columnCount() < 3):
            self.tableWidget_balanco_LI.setColumnCount(3)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_balanco_LI.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_balanco_LI.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_balanco_LI.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        self.tableWidget_balanco_LI.setObjectName(u"tableWidget_balanco_LI")
        self.tableWidget_balanco_LI.setMinimumSize(QSize(300, 0))
        self.tableWidget_balanco_LI.setStyleSheet(u"font: bold;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.tableWidget_balanco_LI)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: none")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_18.addWidget(self.label_25)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_invest_3 = QLabel(self.frame_8)
        self.lbl_invest_3.setObjectName(u"lbl_invest_3")

        self.horizontalLayout_5.addWidget(self.lbl_invest_3)

        self.lbl_invest = QLabel(self.frame_8)
        self.lbl_invest.setObjectName(u"lbl_invest")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lbl_invest.sizePolicy().hasHeightForWidth())
        self.lbl_invest.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.lbl_invest)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_18.addWidget(self.label_26)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_invest_2 = QLabel(self.frame_8)
        self.lbl_invest_2.setObjectName(u"lbl_invest_2")

        self.horizontalLayout_3.addWidget(self.lbl_invest_2)

        self.lbl_lucro = QLabel(self.frame_8)
        self.lbl_lucro.setObjectName(u"lbl_lucro")
        sizePolicy5.setHeightForWidth(self.lbl_lucro.sizePolicy().hasHeightForWidth())
        self.lbl_lucro.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.lbl_lucro)


        self.verticalLayout_18.addLayout(self.horizontalLayout_3)


        self.verticalLayout_24.addWidget(self.frame_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_balanco_mes = QComboBox(self.frame_7)
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.addItem("")
        self.comboBox_balanco_mes.setObjectName(u"comboBox_balanco_mes")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_balanco_mes.sizePolicy().hasHeightForWidth())
        self.comboBox_balanco_mes.setSizePolicy(sizePolicy6)
        self.comboBox_balanco_mes.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.comboBox_balanco_mes.setFont(font3)
        self.comboBox_balanco_mes.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")
        self.comboBox_balanco_mes.setMaxVisibleItems(13)

        self.horizontalLayout_4.addWidget(self.comboBox_balanco_mes)

        self.btn_balanco_deletar = QPushButton(self.frame_7)
        self.btn_balanco_deletar.setObjectName(u"btn_balanco_deletar")
        sizePolicy6.setHeightForWidth(self.btn_balanco_deletar.sizePolicy().hasHeightForWidth())
        self.btn_balanco_deletar.setSizePolicy(sizePolicy6)
        self.btn_balanco_deletar.setMinimumSize(QSize(0, 25))
        self.btn_balanco_deletar.setFont(font1)
        self.btn_balanco_deletar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_balanco_deletar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_balanco_deletar)


        self.verticalLayout_24.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_24)


        self.verticalLayout_27.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.pg_balanco)
        self.pg_definicoes = QWidget()
        self.pg_definicoes.setObjectName(u"pg_definicoes")
        self.pg_definicoes.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: bold;\n"
"color:rgb(255, 255, 255)")
        self.verticalLayout_15 = QVBoxLayout(self.pg_definicoes)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pg_definicoes)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame)
        self.verticalLayout_17.setSpacing(7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 8px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_17.addWidget(self.label_15)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setSpacing(7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_16.addWidget(self.label_20)

        self.lineEdit_definicoes_nomelocal = QLineEdit(self.frame_6)
        self.lineEdit_definicoes_nomelocal.setObjectName(u"lineEdit_definicoes_nomelocal")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit_definicoes_nomelocal.sizePolicy().hasHeightForWidth())
        self.lineEdit_definicoes_nomelocal.setSizePolicy(sizePolicy7)
        self.lineEdit_definicoes_nomelocal.setMinimumSize(QSize(300, 20))
        self.lineEdit_definicoes_nomelocal.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 8px;")

        self.verticalLayout_16.addWidget(self.lineEdit_definicoes_nomelocal)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_16.addWidget(self.label_21)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label_23)

        self.timeEdit_definicoes_DE = QTimeEdit(self.frame_6)
        self.timeEdit_definicoes_DE.setObjectName(u"timeEdit_definicoes_DE")
        self.timeEdit_definicoes_DE.setMinimumSize(QSize(0, 20))
        self.timeEdit_definicoes_DE.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 5px;")

        self.horizontalLayout.addWidget(self.timeEdit_definicoes_DE)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label_24)

        self.timeEdit_definicoes_AS = QTimeEdit(self.frame_6)
        self.timeEdit_definicoes_AS.setObjectName(u"timeEdit_definicoes_AS")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.timeEdit_definicoes_AS.sizePolicy().hasHeightForWidth())
        self.timeEdit_definicoes_AS.setSizePolicy(sizePolicy8)
        self.timeEdit_definicoes_AS.setMinimumSize(QSize(0, 20))
        self.timeEdit_definicoes_AS.setStyleSheet(u"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 5px;")

        self.horizontalLayout.addWidget(self.timeEdit_definicoes_AS)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_16.addLayout(self.horizontalLayout)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_9)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.btn_definicoes_salvar = QPushButton(self.frame)
        self.btn_definicoes_salvar.setObjectName(u"btn_definicoes_salvar")
        self.btn_definicoes_salvar.setMinimumSize(QSize(200, 20))
        self.btn_definicoes_salvar.setFont(font1)
        self.btn_definicoes_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_definicoes_salvar.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.btn_definicoes_salvar, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame)

        self.stackedWidget.addWidget(self.pg_definicoes)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.frame_principal)

        self.label = QLabel(self.frame_direita)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_direita, 0, 1, 1, 1)

        self.frame_esquerda = QFrame(self.centralwidget)
        self.frame_esquerda.setObjectName(u"frame_esquerda")
        self.frame_esquerda.setEnabled(True)
        self.frame_esquerda.setMinimumSize(QSize(0, 0))
        self.frame_esquerda.setMaximumSize(QSize(0, 16777215))
        font4 = QFont()
        font4.setBold(True)
        self.frame_esquerda.setFont(font4)
        self.frame_esquerda.setStyleSheet(u"QFrame{\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 8px;\n"
"}\n"
"font: bold;")
        self.frame_esquerda.setFrameShape(QFrame.StyledPanel)
        self.frame_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_esquerda)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_nomeEstabelecimento = QLabel(self.frame_esquerda)
        self.label_nomeEstabelecimento.setObjectName(u"label_nomeEstabelecimento")
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_nomeEstabelecimento.setFont(font5)
        self.label_nomeEstabelecimento.setTabletTracking(False)
        self.label_nomeEstabelecimento.setAcceptDrops(False)
        self.label_nomeEstabelecimento.setAutoFillBackground(False)
        self.label_nomeEstabelecimento.setStyleSheet(u"")
        self.label_nomeEstabelecimento.setScaledContents(False)
        self.label_nomeEstabelecimento.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_nomeEstabelecimento)

        self.toolBox = QToolBox(self.frame_esquerda)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setSizeIncrement(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.toolBox.setFont(font6)
        self.toolBox.setMouseTracking(False)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"QToolBox:tab{\n"
"	border-radius:5px;\n"
"	background-color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.toolBox.setLocale(QLocale(QLocale.Portuguese, QLocale.EastTimor))
        self.tab_menu = QWidget()
        self.tab_menu.setObjectName(u"tab_menu")
        self.tab_menu.setGeometry(QRect(0, 0, 92, 254))
        self.tab_menu.setMinimumSize(QSize(0, 0))
        self.tab_menu.setSizeIncrement(QSize(0, 0))
        self.tab_menu.setLayoutDirection(Qt.LeftToRight)
        self.tab_menu.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.tab_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.Button_menu_estoque = QPushButton(self.tab_menu)
        self.Button_menu_estoque.setObjectName(u"Button_menu_estoque")
        self.Button_menu_estoque.setMinimumSize(QSize(0, 30))
        self.Button_menu_estoque.setFont(font1)
        self.Button_menu_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_menu_estoque.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Button_menu_estoque)

        self.Button_menu_clientes = QPushButton(self.tab_menu)
        self.Button_menu_clientes.setObjectName(u"Button_menu_clientes")
        self.Button_menu_clientes.setMinimumSize(QSize(0, 30))
        self.Button_menu_clientes.setFont(font1)
        self.Button_menu_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_menu_clientes.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Button_menu_clientes)

        self.Button_menu_dividas = QPushButton(self.tab_menu)
        self.Button_menu_dividas.setObjectName(u"Button_menu_dividas")
        self.Button_menu_dividas.setMinimumSize(QSize(0, 30))
        self.Button_menu_dividas.setFont(font1)
        self.Button_menu_dividas.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_menu_dividas.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Button_menu_dividas)

        self.Button_menu_balanco = QPushButton(self.tab_menu)
        self.Button_menu_balanco.setObjectName(u"Button_menu_balanco")
        self.Button_menu_balanco.setMinimumSize(QSize(0, 30))
        self.Button_menu_balanco.setFont(font1)
        self.Button_menu_balanco.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_menu_balanco.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Button_menu_balanco)

        self.Button_menu_definicoes = QPushButton(self.tab_menu)
        self.Button_menu_definicoes.setObjectName(u"Button_menu_definicoes")
        self.Button_menu_definicoes.setMinimumSize(QSize(0, 30))
        self.Button_menu_definicoes.setFont(font1)
        self.Button_menu_definicoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_menu_definicoes.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color: rgb(255, 255, 0);\n"
"	border-top-left-radius: 15px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.Button_menu_definicoes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.tab_menu, u"Menu")
        self.tab_sobre = QWidget()
        self.tab_sobre.setObjectName(u"tab_sobre")
        self.tab_sobre.setGeometry(QRect(0, 0, 175, 254))
        self.tab_sobre.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_3 = QVBoxLayout(self.tab_sobre)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.tab_sobre)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(75, 75, 75);")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.tab_sobre)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(75, 75, 75);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.tab_sobre)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(75, 75, 75);")

        self.verticalLayout_3.addWidget(self.label_4)

        self.toolBox.addItem(self.tab_sobre, u"Sobre")

        self.verticalLayout.addWidget(self.toolBox)


        self.gridLayout.addWidget(self.frame_esquerda, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_estoque_produto, self.lineEdit_estoque_quantidade)
        QWidget.setTabOrder(self.lineEdit_estoque_quantidade, self.lineEdit_estoque_valorCompra)
        QWidget.setTabOrder(self.lineEdit_estoque_valorCompra, self.lineEdit_estoque_valorVenda)
        QWidget.setTabOrder(self.lineEdit_estoque_valorVenda, self.lineEdit_definicoes_nomelocal)
        QWidget.setTabOrder(self.lineEdit_definicoes_nomelocal, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableWidget_estoque_adicionar)
        QWidget.setTabOrder(self.tableWidget_estoque_adicionar, self.tableWidget_estoque_remover)
        QWidget.setTabOrder(self.tableWidget_estoque_remover, self.btn_estoque_remover)
        QWidget.setTabOrder(self.btn_estoque_remover, self.tableWidget_estoque_editar)
        QWidget.setTabOrder(self.tableWidget_estoque_editar, self.btn_estoque_editar)
        QWidget.setTabOrder(self.btn_estoque_editar, self.tabWidget_3)
        QWidget.setTabOrder(self.tabWidget_3, self.radioButton_clientes_sim)
        QWidget.setTabOrder(self.radioButton_clientes_sim, self.radioButton_clientes_nao)
        QWidget.setTabOrder(self.radioButton_clientes_nao, self.comboBox_cliente_produto)
        QWidget.setTabOrder(self.comboBox_cliente_produto, self.lineEdit_cliente_quantidade)
        QWidget.setTabOrder(self.lineEdit_cliente_quantidade, self.btn_cliente_adicionar)
        QWidget.setTabOrder(self.btn_cliente_adicionar, self.tableWidget_cliente_venda)
        QWidget.setTabOrder(self.tableWidget_cliente_venda, self.radioButton_cliente_novoCliente)
        QWidget.setTabOrder(self.radioButton_cliente_novoCliente, self.lineEdit_cliente_novoCliente)
        QWidget.setTabOrder(self.lineEdit_cliente_novoCliente, self.comboBox_cliente_cliente)
        QWidget.setTabOrder(self.comboBox_cliente_cliente, self.radioButton_cliente_cliente)
        QWidget.setTabOrder(self.radioButton_cliente_cliente, self.btn_cliente_vender)
        QWidget.setTabOrder(self.btn_cliente_vender, self.tableWidget_cliente_tabela)
        QWidget.setTabOrder(self.tableWidget_cliente_tabela, self.tableWidget_dividas)
        QWidget.setTabOrder(self.tableWidget_dividas, self.comboBox_dividas_cliente)
        QWidget.setTabOrder(self.comboBox_dividas_cliente, self.lineEdit_dividas_valorRecebido)
        QWidget.setTabOrder(self.lineEdit_dividas_valorRecebido, self.btn_dividas_pagar)
        QWidget.setTabOrder(self.btn_dividas_pagar, self.btn_estoque_adicionar)
        QWidget.setTabOrder(self.btn_estoque_adicionar, self.timeEdit_definicoes_DE)
        QWidget.setTabOrder(self.timeEdit_definicoes_DE, self.timeEdit_definicoes_AS)
        QWidget.setTabOrder(self.timeEdit_definicoes_AS, self.btn_definicoes_salvar)
        QWidget.setTabOrder(self.btn_definicoes_salvar, self.Button_menu_estoque)
        QWidget.setTabOrder(self.Button_menu_estoque, self.Button_menu_clientes)
        QWidget.setTabOrder(self.Button_menu_clientes, self.Button_menu_dividas)
        QWidget.setTabOrder(self.Button_menu_dividas, self.Button_menu_balanco)
        QWidget.setTabOrder(self.Button_menu_balanco, self.Button_menu_definicoes)

        self.retranslateUi(MainWindow)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.setHidden)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.radioButton_cliente_novoCliente.setHidden)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.label_38.setHidden)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.label_38.setVisible)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.radioButton_cliente_novoCliente.setVisible)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.setVisible)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.label_16.setHidden)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.radioButton_cliente_cliente.setHidden)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.comboBox_cliente_cliente.setHidden)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.label_16.setVisible)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.radioButton_cliente_cliente.setVisible)
        self.radioButton_clientes_nao.clicked["bool"].connect(self.comboBox_cliente_cliente.setVisible)
        self.radioButton_cliente_cliente.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.setDisabled)
        self.radioButton_cliente_cliente.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.clear)
        self.radioButton_cliente_novoCliente.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.setEnabled)
        self.radioButton_clientes_sim.clicked["bool"].connect(self.lineEdit_cliente_novoCliente.clear)
        self.radioButton_cliente_cliente.clicked["bool"].connect(self.comboBox_cliente_cliente.setEnabled)
        self.radioButton_cliente_novoCliente.clicked["bool"].connect(self.comboBox_cliente_cliente.setDisabled)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema De Gerenciamento", None))
        self.btn_menu.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;\">Sistema de Gerenciamento!</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/Icones/logo-vm3.ico\"/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">ESTOQUE</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem = self.tableWidget_estoque_adicionar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem1 = self.tableWidget_estoque_adicionar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem2 = self.tableWidget_estoque_adicionar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor Da Compra", None));
        ___qtablewidgetitem3 = self.tableWidget_estoque_adicionar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor Da Venda", None));
        ___qtablewidgetitem4 = self.tableWidget_estoque_adicionar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lucro Unidade", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.btn_estoque_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Valor de Compra:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Valor da Venda:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Adicionar", None))
        ___qtablewidgetitem5 = self.tableWidget_estoque_remover.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem6 = self.tableWidget_estoque_remover.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem7 = self.tableWidget_estoque_remover.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Valor Da Compra", None));
        ___qtablewidgetitem8 = self.tableWidget_estoque_remover.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Valor Da Venda", None));
        ___qtablewidgetitem9 = self.tableWidget_estoque_remover.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Lucro Unidade", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Quntidade:</p><p>(0 Deleta tudo)</p></body></html>", None))
        self.lineEdit_estoque_remover.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_estoque_remover.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem10 = self.tableWidget_estoque_editar.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem11 = self.tableWidget_estoque_editar.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem12 = self.tableWidget_estoque_editar.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Valor Da Compra", None));
        ___qtablewidgetitem13 = self.tableWidget_estoque_editar.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Valor Da Venda", None));
        ___qtablewidgetitem14 = self.tableWidget_estoque_editar.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Lucro Unidade", None));
        self.btn_estoque_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"   Editar   ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">CLIENTES</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tabWidget_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tabWidget_3.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tabWidget_3.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"A Vista:", None))
        self.radioButton_clientes_sim.setText(QCoreApplication.translate("MainWindow", u"SIM", None))
        self.radioButton_clientes_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00c3O", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Produto:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.btn_cliente_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_cliente_valor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">R$0,00</span></p></body></html>", None))
        self.btn_cliente_apagar.setText(QCoreApplication.translate("MainWindow", u"Apagar Dados", None))
        ___qtablewidgetitem15 = self.tableWidget_cliente_venda.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem16 = self.tableWidget_cliente_venda.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem17 = self.tableWidget_cliente_venda.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Novo Cliente:", None))
        self.radioButton_cliente_novoCliente.setText("")
#if QT_CONFIG(statustip)
        self.lineEdit_cliente_novoCliente.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.radioButton_cliente_cliente.setText("")
        self.btn_cliente_vender.setText(QCoreApplication.translate("MainWindow", u"Vender", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Venda", None))
        ___qtablewidgetitem18 = self.tableWidget_cliente_tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem19 = self.tableWidget_cliente_tabela.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem20 = self.tableWidget_cliente_tabela.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem21 = self.tableWidget_cliente_tabela.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem22 = self.tableWidget_cliente_tabela.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Tabela", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">DIVIDAS</span></p></body></html>", None))
        ___qtablewidgetitem23 = self.tableWidget_dividas.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem24 = self.tableWidget_dividas.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem25 = self.tableWidget_dividas.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Divida", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Valor Recebido:", None))
        self.label_dividas_total.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">R$0,00</span></p></body></html>", None))
        self.label_dividas_troco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Troco</span></p></body></html>", None))
        self.btn_dividas_resetar.setText(QCoreApplication.translate("MainWindow", u"Resetar", None))
        self.btn_dividas_pagar.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">BALAN\u00c7O</span></p></body></html>", None))
        ___qtablewidgetitem26 = self.tableWidget_balanco_LI.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem27 = self.tableWidget_balanco_LI.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Lucro", None));
        ___qtablewidgetitem28 = self.tableWidget_balanco_LI.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Investimento", None));
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">INVESTIMENTO TOTAL</span></p></body></html>", None))
        self.lbl_invest_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">R$</span></p></body></html>", None))
        self.lbl_invest.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0,00</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">LUCRO TOTAL</span></p></body></html>", None))
        self.lbl_invest_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">R$</span></p></body></html>", None))
        self.lbl_lucro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0,00</span></p></body></html>", None))
        self.comboBox_balanco_mes.setItemText(0, QCoreApplication.translate("MainWindow", u"TUDO", None))
        self.comboBox_balanco_mes.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_balanco_mes.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_balanco_mes.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_balanco_mes.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_balanco_mes.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_balanco_mes.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_balanco_mes.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_balanco_mes.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_balanco_mes.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_balanco_mes.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_balanco_mes.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_balanco_mes.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))

        self.btn_balanco_deletar.setText(QCoreApplication.translate("MainWindow", u"Deletar tudo", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">DEFINI\u00c7\u00d5ES</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Nome do Local:</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Hor\u00e1rio de funcionamento:</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">DE:</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u00c1S:</span></p></body></html>", None))
        self.btn_definicoes_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">VM3Art's</span></p></body></html>", None))
        self.label_nomeEstabelecimento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">NOME DO LOCAL</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Button_menu_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.Button_menu_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.Button_menu_dividas.setText(QCoreApplication.translate("MainWindow", u"Dividas", None))
        self.Button_menu_balanco.setText(QCoreApplication.translate("MainWindow", u"Balan\u00e7o", None))
        self.Button_menu_definicoes.setText(QCoreApplication.translate("MainWindow", u"Defini\u00e7\u00f5es", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tab_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/Icones/whatsapp.png\"/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffef0c; vertical-align:super;\">(18) 99644-3281</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/Icones/instagram.png\"/></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffff00;\">@vm3code</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/Icones/email.png\"/></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffff00;\">vm3code@gmail.com</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.tab_sobre), QCoreApplication.translate("MainWindow", u"Sobre", None))
    # retranslateUi

