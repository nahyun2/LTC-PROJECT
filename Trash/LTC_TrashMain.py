import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class TrashMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Living Tips for CBNU / Trash Tips")
        self.setWindowIcon(QIcon('Logo.png'))
        self.setGeometry(400, 100, 1180, 820)
    
        self.image_label_trashmain = QLabel(self)
        self.image_label_trashmain.setGeometry(0, 0, 1180, 820)    
        pixmap_trashmain = QPixmap(r'C:\Users\user\Desktop\LTC_project\IMG_background\background.jpg')
        scaled_pixmap_trashmain = pixmap_trashmain.scaled(self.image_label_trashmain.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_trashmain.setPixmap(scaled_pixmap_trashmain)
        self.image_label_trashmain.setAlignment(Qt.AlignCenter)

        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\daily_b.png', 30, 250, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\bathroom_b.png', 230, 250, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\container_b.png', 430, 250, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\cosmetic_b.png', 630, 250, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\fashion_b.png', 30, 460, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\food_b.png', 230, 457, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\furniture_b.png', 430, 460, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\home_b.png', 630, 460, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\kitchen_b.png', 30, 660, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\stationery_b.png', 230, 660, 150, 150, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\etc_b.png', 430, 663, 150, 150, self.dummy_function)
        
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\daily_k.png', 40, 165, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\bathroom_k.png', 240, 165, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\container_k.png', 440, 165, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\cosmetic_k.png', 640, 165, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\fashion_k.png', 40, 375, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\food_k.png', 240, 374, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\furniture_k.png', 440, 375, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\home_k.png', 640, 375, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\kitchen_k.png', 40, 580, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\stationery_k.png', 240, 580, 130, 130, self.dummy_function)
        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_button\etc_k.png', 440, 580, 127, 127, self.dummy_function)

        self.create_image_button(r'C:\Users\user\Desktop\LTC_project\IMG_map\map.png', 850, 150, 300, 550, self.dummy_function)

        self.create_main_button()
        
        self.show()
        
    def create_image_button(self, image_path, x, y, width, height, function):
        container = QWidget(self)
        container.setGeometry(x, y, width, height + 60)  # 60 is the extra height for the label and button spacing

        btn = QPushButton(container)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setGeometry(0, 0, width, height)
        btn.setStyleSheet("border: none;")

    def dummy_function(self):
        print("This button does nothing for now.")
    
    def create_main_button(self):
        main_button = QPushButton("Main", self)
        main_button.setGeometry(20, 20, 100, 50)  
        main_button.clicked.connect(self.go_to_main)
        
    def go_to_main(self):
        print("Go to main screen")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    trashmainwindow = TrashMainWindow()
    trashmainwindow.show()
    sys.exit(app.exec_())
