from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(253, 412)
        Calculator.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 24pt \"Arial\";")
        self.label.setMidLineWidth(-1)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.acButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("AC"))
        self.acButton.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.acButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 24pt \"Arial\";\n"
                                    "background-color: rgb(179, 179, 179);")
        self.acButton.setObjectName("acButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus())
        self.plusminusButton.setGeometry(QtCore.QRect(70, 70, 51, 51))
        self.plusminusButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 24pt \"Arial\";\n"
                                           "background-color: rgb(179, 179, 179);")
        self.plusminusButton.setObjectName("plusminusButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.procent())
        self.percentButton.setGeometry(QtCore.QRect(130, 70, 51, 51))
        self.percentButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "font: 24pt \"Arial\";\n"
                                         "background-color: rgb(179, 179, 179);")
        self.percentButton.setObjectName("percentButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("/"))
        self.divideButton.setGeometry(QtCore.QRect(190, 70, 51, 51))
        self.divideButton.setStyleSheet("background-color: rgb(255, 164, 39);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 24pt \"Arial\";")
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(190, 130, 51, 51))
        self.multiplyButton.setStyleSheet("background-color: rgb(255, 164, 39);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 24pt \"Arial\";")
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("9"))
        self.nineButton.setGeometry(QtCore.QRect(130, 130, 51, 51))
        self.nineButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 24pt \"Arial\";\n"
                                      "background-color: rgb(70, 70, 70);")
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 130, 51, 51))
        self.sevenButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 24pt \"Arial\";\n"
                                       "background-color: rgb(70, 70, 70);")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("8"))
        self.eightButton.setGeometry(QtCore.QRect(70, 130, 51, 51))
        self.eightButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 24pt \"Arial\";\n"
                                       "background-color: rgb(70, 70, 70);")
        self.eightButton.setObjectName("eightButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("-"))
        self.minusButton.setGeometry(QtCore.QRect(190, 190, 51, 51))
        self.minusButton.setStyleSheet("background-color: rgb(255, 164, 39);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 24pt \"Arial\";")

        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("6"))
        self.sixButton.setGeometry(QtCore.QRect(130, 190, 51, 51))
        self.sixButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 24pt \"Arial\";\n"
                                     "background-color: rgb(70, 70, 70);")

        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 190, 51, 51))
        self.fourButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 24pt \"Arial\";\n"
                                      "background-color: rgb(70, 70, 70);")
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("5"))
        self.fiveButton.setGeometry(QtCore.QRect(70, 190, 51, 51))
        self.fiveButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 24pt \"Arial\";\n"
                                      "background-color: rgb(70, 70, 70);")
        self.fiveButton.setObjectName("fiveButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("+"))
        self.plusButton.setGeometry(QtCore.QRect(190, 250, 51, 51))
        self.plusButton.setStyleSheet("background-color: rgb(255, 164, 39);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 24pt \"Arial\";")
        self.plusButton.setObjectName("plusButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("3"))
        self.threeButton.setGeometry(QtCore.QRect(130, 250, 51, 51))
        self.threeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 24pt \"Arial\";\n"
                                       "background-color: rgb(70, 70, 70);")
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 250, 51, 51))
        self.oneButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 24pt \"Arial\";\n"
                                     "background-color: rgb(70, 70, 70);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("2"))
        self.twoButton.setGeometry(QtCore.QRect(70, 250, 51, 51))
        self.twoButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 24pt \"Arial\";\n"
                                     "background-color: rgb(70, 70, 70);")
        self.twoButton.setObjectName("twoButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.eval())
        self.equalButton.setGeometry(QtCore.QRect(190, 310, 51, 51))
        self.equalButton.setStyleSheet("background-color: rgb(255, 164, 39);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 24pt \"Arial\";")
        self.equalButton.setObjectName("equalButton")
        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addDot())
        self.dotButton.setGeometry(QtCore.QRect(130, 310, 51, 51))
        self.dotButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 24pt \"Arial\";\n"
                                     "background-color: rgb(70, 70, 70);")
        self.dotButton.setObjectName("dotButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("0"))
        self.zeroButton.setEnabled(True)
        self.zeroButton.setGeometry(QtCore.QRect(10, 310, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.zeroButton.setFont(font)
        self.zeroButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zeroButton.setAutoFillBackground(False)
        self.zeroButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 24pt \"Arial\";\n"
                                      "background-color: rgb(70, 70, 70);")
        self.zeroButton.setAutoDefault(False)
        self.zeroButton.setDefault(False)
        self.zeroButton.setFlat(False)
        self.zeroButton.setObjectName("zeroButton")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 24))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.label.setText(_translate("Calculator", "0"))
        self.acButton.setText(_translate("Calculator", "AC"))
        self.plusminusButton.setText(_translate("Calculator", "+/-"))
        self.percentButton.setText(_translate("Calculator", "%"))
        self.divideButton.setText(_translate("Calculator", "÷"))
        self.multiplyButton.setText(_translate("Calculator", "x"))
        self.nineButton.setText(_translate("Calculator", "9"))
        self.sevenButton.setText(_translate("Calculator", "7"))
        self.eightButton.setText(_translate("Calculator", "8"))
        self.minusButton.setText(_translate("Calculator", "-"))
        self.sixButton.setText(_translate("Calculator", "6"))
        self.fourButton.setText(_translate("Calculator", "4"))
        self.fiveButton.setText(_translate("Calculator", "5"))
        self.plusButton.setText(_translate("Calculator", "+"))
        self.threeButton.setText(_translate("Calculator", "3"))
        self.oneButton.setText(_translate("Calculator", "1"))
        self.twoButton.setText(_translate("Calculator", "2"))
        self.equalButton.setText(_translate("Calculator", "="))
        self.dotButton.setText(_translate("Calculator", "."))
        self.zeroButton.setText(_translate("Calculator", "0"))

    def pressed(self, pressedButton):
        if pressedButton == "AC":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f'{self.label.text()}{pressedButton}')

    def procent(self):
        if self.label.text() == "0":
            self.label.setText("0")
        else:
            ans = str(round(float(self.label.text()) / 100, 10))
            self.label.setText(ans)

    def eval(self):
        try:
            ans = eval(self.label.text())
            self.label.setText(str(ans))
        except:
            self.label.setText("ERR")

    def plus_minus(self):
        if self.label.text() == "0":
            self.label.setText("0")
        else:
            self.label.setText(str(eval(self.label.text())))
            ans = str(round(float(self.label.text()) * -1, 2))
            self.label.setText(ans)

    def addDot(self):
        chars = ["+", "-", "/", "%"]
        if "." not in self.label.text():
            self.label.setText(f'{self.label.text()}.')
        for ele in chars:
            if ele in self.label.text()[::-1] and "." not in self.label.text()[::-1][
                                                             :self.label.text()[::-1].index(ele)]:
                self.label.setText(f'{self.label.text()}.')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
