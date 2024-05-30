import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Living Tips for CBNU")
        self.setGeometry(400, 100, 1180, 820)
    
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 1180, 820)    
        
        pixmap = QPixmap('main.jpg')  
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        self.create_image_button('laundry_btn1.png', 250, 300, "btn1", 200, 150)
        self.create_image_button('trash_btn2.png', 500, 280, "btn2", 200, 150)
        self.create_image_button('cooking_btn3.png', 750, 290, "btn3", 200, 150)
        self.create_image_button('login_btn.png', 980, 720, "login_btn", 150, 120)

        self.create_image_button('cat_btn.png', 50, 500, "cat_btn", 300, 300)
        self.create_image_button('dog_btn.png', 705, 15, "dog_btn", 300, 300)
        self.create_image_button('hippo_btn.png', 700, 500, "hippo_btn", 250, 250)
        self.create_image_button('frog_btn.png', 0, 15, "frog_btn", 270, 270)

    def create_image_button(self, image_path, x, y, tooltip, width, height):
        btn = QPushButton(parent=self)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setToolTip(tooltip)
        btn.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())
        btn.setStyleSheet("border: none;")
    
app = QApplication(sys.argv) 
window = main_window() 
window.show() 
app.exec_() 