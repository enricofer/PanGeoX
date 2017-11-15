# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\dev\PanGeoX\PanGeoX_dialog_base.ui'
#
# Created: Thu Jul 09 17:21:52 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PanGeoXDialogBase(object):
    def setupUi(self, PanGeoXDialogBase):
        PanGeoXDialogBase.setObjectName(_fromUtf8("PanGeoXDialogBase"))
        PanGeoXDialogBase.resize(1300, 317)
        self.verticalLayout_10 = QtGui.QVBoxLayout(PanGeoXDialogBase)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setMargin(3)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.webView = QtWebKit.QWebView(PanGeoXDialogBase)
        self.webView.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(0, 0))
        self.webView.setMaximumSize(QtCore.QSize(10000, 10000))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///Z:/dev/PanGeoX/lib/index.html")))
        self.webView.setRenderHints(QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_10.addWidget(self.webView)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)

        self.retranslateUi(PanGeoXDialogBase)
        QtCore.QMetaObject.connectSlotsByName(PanGeoXDialogBase)

    def retranslateUi(self, PanGeoXDialogBase):
        PanGeoXDialogBase.setWindowTitle(_translate("PanGeoXDialogBase", "PanGeox", None))

from PyQt4 import QtWebKit
import resources_rc
