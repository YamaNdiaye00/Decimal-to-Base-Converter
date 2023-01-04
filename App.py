from math import floor
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(728, 177)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.numberInput = QtWidgets.QTextEdit(Dialog)
        self.numberInput.setGeometry(QtCore.QRect(20, 70, 113, 31))
        self.numberInput.setText("")
        self.numberInput.setObjectName("numberInput")
        self.baseInput = QtWidgets.QTextEdit(Dialog)
        self.baseInput.setGeometry(QtCore.QRect(250, 70, 113, 31))
        self.baseInput.setText("")
        self.baseInput.setObjectName("baseInput")
        self.outputDisplay = QtWidgets.QTextBrowser(Dialog)
        self.outputDisplay.setGeometry(QtCore.QRect(460, 70, 256, 31))
        self.outputDisplay.setObjectName("outputDisplay")
        self.numberLabel = QtWidgets.QLabel(Dialog)
        self.numberLabel.setGeometry(QtCore.QRect(30, 30, 81, 31))
        self.numberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numberLabel.setObjectName("numberLabel")
        self.baseLabel = QtWidgets.QLabel(Dialog)
        self.baseLabel.setGeometry(QtCore.QRect(270, 30, 81, 31))
        self.baseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.baseLabel.setObjectName("baseLabel")
        self.outputLabel = QtWidgets.QLabel(Dialog)
        self.outputLabel.setGeometry(QtCore.QRect(550, 30, 81, 31))
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.computeButton = QtWidgets.QPushButton(Dialog)
        self.computeButton.setGeometry(QtCore.QRect(270, 130, 121, 28))
        self.computeButton.setObjectName("computeButton")
        self.computeButton.clicked.connect(self.check)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Converter"))
        self.numberLabel.setText(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:12pt;\">NUMBER</span></p></body></html>"))
        self.baseLabel.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:12pt;\">BASE</span></p></body></html>"))
        self.outputLabel.setText(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:12pt;\">OUTPUT</span></p></body></html>"))
        self.computeButton.setText(_translate("Dialog", "COMPUTE"))

    def check(self):
        number = self.numberInput.toPlainText()
        base = self.baseInput.toPlainText()
        try:
            if number == "" or base == "": raise Exception
            number = int(number)
            base = int(base)
            if number < 0 or base < 0: raise Exception
            self.outputDisplay.setText(self.convert(number, base))
        except:
            self.outputDisplay.setText("Incorrect input values! Try again")

    def convert(self, number, n):
        binary = ""
        while number > 0:
            modulo = number % n
            number = floor(number / n)
            if modulo <= 9:
                binary = str(modulo) + binary
            else:
                binary = chr(modulo + 55) + binary

        return binary


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
