import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Living Tips for CBNU")
        self.setGeometry(400, 100, 1180, 820)
    
        self.image_label_main = QLabel(self)
        self.image_label_main.setGeometry(0, 0, 1180, 820)    
        
        pixmap_main = QPixmap('main.jpg')  
        scaled_pixmap_main = pixmap_main.scaled(self.image_label_main.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_main.setPixmap(scaled_pixmap_main)
        self.image_label_main.setAlignment(Qt.AlignCenter)
        
        self.create_image_button('laundry_btn1.png', 250, 300, "laundry_tip", 200, 150, self.dummy_function)
        self.create_image_button('trash_btn2.png', 500, 280, "trash_tip", 200, 150, self.open_trashmain)
        self.create_image_button('cooking_btn3.png', 750, 290, "cooking_tip", 200, 150, self.dummy_function)
        self.create_image_button('login_btn.png', 980, 720, "login", 150, 120, self.dummy_function)

        self.create_image_button('cat_btn.png', 50, 500, "exp", 300, 300, self.dummy_function)
        self.create_image_button('dog_btn.png', 705, 15, "exp", 300, 300, self.dummy_function)
        self.create_image_button('hippo_btn.png', 700, 500, "exp", 250, 250, self.dummy_function)
        self.create_image_button('frog_btn.png', 0, 15, "exp", 270, 270, self.dummy_function)

    def create_image_button(self, image_path, x, y, tooltip, width, height, function):
        btn = QPushButton(parent=self)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setToolTip(tooltip)
        btn.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())
        btn.setStyleSheet("border: none;")
        btn.clicked.connect(function)

    def open_trashmain(self):
        subprocess.Popen([sys.executable, "LTC_TrashMain.py"])
        self.close()

    def dummy_function(self):
        print("This button does nothing for now.")

if __name__ == '__main__':
    app_main = QApplication(sys.argv) 
    mainwindow = main_window() 
    mainwindow.show() 
    sys.exit(app_main.exec_())
