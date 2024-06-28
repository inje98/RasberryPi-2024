import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test01.ui', self)

        # ���� ��ư ��������
        # self.radioButton1 = self.findChild(QRadioButton, 'radioButton1')
        # self.radioButton2 = self.findChild(QRadioButton, 'radioButton2')
        # self.radioButton3 = self.findChild(QRadioButton, 'radioButton3')
        
        # ���� ��ư Ŭ�� �� ������ �Լ�
        self.radioButton1.toggled.connect(self.on_radio_button_toggled)
        self.radioButton2.toggled.connect(self.on_radio_button_toggled)
        self.radioButton3.toggled.connect(self.on_radio_button_toggled)
    
    def on_radio_button_toggled(self):
        # ���õ� ���� ��ư Ȯ��
        if self.radioButton1.isChecked():
            print("Radio Button 1 selected")
        elif self.radioButton2.isChecked():
            print("Radio Button 2 selected")
        elif self.radioButton3.isChecked():
            print("Radio Button 3 selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
