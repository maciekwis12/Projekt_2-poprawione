# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delta_h_pole_powierzchni_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeltaH_PolePowDialogBase(object):
    def setupUi(self, DeltaH_PolePowDialogBase):
        DeltaH_PolePowDialogBase.setObjectName("DeltaH_PolePowDialogBase")
        DeltaH_PolePowDialogBase.resize(604, 515)
        self.button_box = QtWidgets.QDialogButtonBox(DeltaH_PolePowDialogBase)
        self.button_box.setGeometry(QtCore.QRect(150, 430, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.pushButton_oblicz_roznice_wysokosci = QtWidgets.QPushButton(DeltaH_PolePowDialogBase)
        self.pushButton_oblicz_roznice_wysokosci.setGeometry(QtCore.QRect(97, 16, 341, 71))
        self.pushButton_oblicz_roznice_wysokosci.setObjectName("pushButton_oblicz_roznice_wysokosci")
        self.textEdit_pokaz_roznice_wysokosci = QtWidgets.QTextEdit(DeltaH_PolePowDialogBase)
        self.textEdit_pokaz_roznice_wysokosci.setGeometry(QtCore.QRect(120, 120, 301, 61))
        self.textEdit_pokaz_roznice_wysokosci.setObjectName("textEdit_pokaz_roznice_wysokosci")
        self.horizontalLayoutWidget = QtWidgets.QWidget(DeltaH_PolePowDialogBase)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 220, 321, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_oblicz_pole_powierzchni = QtWidgets.QPushButton(DeltaH_PolePowDialogBase)
        self.pushButton_oblicz_pole_powierzchni.setGeometry(QtCore.QRect(150, 260, 241, 71))
        self.pushButton_oblicz_pole_powierzchni.setObjectName("pushButton_oblicz_pole_powierzchni")
        self.textEdit_pokaz_pole_powierzchni = QtWidgets.QTextEdit(DeltaH_PolePowDialogBase)
        self.textEdit_pokaz_pole_powierzchni.setGeometry(QtCore.QRect(110, 350, 321, 61))
        self.textEdit_pokaz_pole_powierzchni.setObjectName("textEdit_pokaz_pole_powierzchni")

        self.retranslateUi(DeltaH_PolePowDialogBase)
        self.button_box.accepted.connect(DeltaH_PolePowDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(DeltaH_PolePowDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeltaH_PolePowDialogBase)

    def retranslateUi(self, DeltaH_PolePowDialogBase):
        _translate = QtCore.QCoreApplication.translate
        DeltaH_PolePowDialogBase.setWindowTitle(_translate("DeltaH_PolePowDialogBase", "delta_h_pole_powierzchni"))
        self.pushButton_oblicz_roznice_wysokosci.setText(_translate("DeltaH_PolePowDialogBase", "Oblicz różnicę wysokości"))
        self.pushButton_oblicz_pole_powierzchni.setText(_translate("DeltaH_PolePowDialogBase", "Oblicz pole powierzchni"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeltaH_PolePowDialogBase = QtWidgets.QDialog()
    ui = Ui_DeltaH_PolePowDialogBase()
    ui.setupUi(DeltaH_PolePowDialogBase)
    DeltaH_PolePowDialogBase.show()
    sys.exit(app.exec_())
