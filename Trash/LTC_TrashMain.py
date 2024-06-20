import sys
import os
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        main_folder = os.path.join(os.path.expanduser("~"), "Desktop", "living-main")
        
        logo_path = os.path.join(main_folder, "img", "Logo.png")
        
        self.setWindowTitle("Living Tips for CBNU")
        self.setWindowIcon(QIcon(logo_path))
        self.setGeometry(400, 100, 1180, 820)
    
        self.image_label_main = QLabel(self)
        self.image_label_main.setGeometry(0, 0, 1180, 820)    
        
        main_background_path = os.path.join(main_folder, "img", "Main", "mainback.jpg")
        pixmap_main = QPixmap(main_background_path)  
        scaled_pixmap_main = pixmap_main.scaled(self.image_label_main.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_main.setPixmap(scaled_pixmap_main)
        self.image_label_main.setAlignment(Qt.AlignCenter)
        
        self.image_label_Logo = QLabel(self)
        self.image_label_Logo.setGeometry(360, 255, 450, 450)    
        
        pixmap_Logo = QPixmap(logo_path)  
        scaled_pixmap_Logo = pixmap_Logo.scaled(self.image_label_Logo.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_Logo.setPixmap(scaled_pixmap_Logo)
        self.image_label_Logo.setAlignment(Qt.AlignCenter)
        
        self.create_image_button(os.path.join(main_folder, "img", "Main", "laundry.png"), 250, 300, "laundry_tip", 200, 150, self.dummy_function)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "trash.png"), 500, 280, "trash_tip", 200, 150, self.open_trashmain)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "fridge.png"), 750, 290, "cooking_tip", 200, 150, self.open_fridgemain)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "login.png"), 980, 720, "login", 150, 120, self.dummy_function)

        self.create_image_button(os.path.join(main_folder, "img", "Main", "cat.png"), 50, 500, "exp", 300, 300, self.dummy_function)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "dog.png"), 705, 15, "exp", 300, 300, self.dummy_function)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "hippo.png"), 750, 500, "exp", 250, 250, self.dummy_function)
        self.create_image_button(os.path.join(main_folder, "img", "Main", "frog.png"), 0, 15, "exp", 270, 270, self.dummy_function)

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
        trashmain_script_path = os.path.join(os.path.expanduser("~"), "Desktop", "living-main", "LTC_TrashMain.py")
        subprocess.Popen([sys.executable, trashmain_script_path])
        self.close()

    def open_fridgemain(self):
        fridgemain_script_path = os.path.join(os.path.expanduser("~"), "Desktop", "living-main", "Fridge.py")
        subprocess.Popen([sys.executable, fridgemain_script_path])
        self.close()

    def dummy_function(self):
        print("This button does nothing for now.")

if __name__ == '__main__':
    app_main = QApplication(sys.argv) 
    mainwindow = MainWindow() 
    mainwindow.show() 
    sys.exit(app_main.exec_())
