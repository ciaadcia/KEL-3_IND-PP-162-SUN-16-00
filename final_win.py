from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
class Testwin(QWidget):
    def __init__(self):
       super().__init__()
       self.initUI()
       self.set_appear()
       self.show()
    def initUI(self):
      self.btn_next = QPushButton(txt_sendresults, self)
      self.btn_next.clicked.connect(self.next_click)
      layout = QVBoxLayout()
      layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
      self.setLayout(layout)
    def next_click(self):
      self.hide()
      self.fw = FinalWin()
    def set_appear(self):
      self.setWindowTitle(txt_title)
      self.resize(win_width, win_height)
      self.move(win_x, win_y)

#scond_win part1

from PyQt5.QtCore import Qt,QTimer,QTime,QLocale
from PyQt5.QtGui import QDoubleValidator,QIntValidator,QFont
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(Qwidget):
   def __init__(self):
      super().__init__()
      self.init()
      self.set_appear()
      self.show()

      def initUI(self):
         self.workh_text = QLabel(txt_workheart)
         self.index_text = QLabel(txt_index)
         self.layout_line = QVBoxLayout()
         self.layout_line = addWidget(self.index_text, alignment=Qt.AlignCenter)
         self.layout_line.addWidget(self.workh_text,alignment=Qt.AlignCenter)
         self.setLayout(self.layout_line)

         def set_appear(self):
            self.setWindowTitle(txt_finalwin)
            self>resize(win_width, win_height)
            self>move(win_x, win_y)

#second_win part 2
