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
        self.setGeometry(400, 100, 1180, 820)
    
        self.image_label_trashmain = QLabel(self)
        self.image_label_trashmain.setGeometry(0, 0, 1180, 820)    
        pixmap_trashmain = QPixmap('background.jpg')
        scaled_pixmap_trashmain = pixmap_trashmain.scaled(self.image_label_trashmain.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_trashmain.setPixmap(scaled_pixmap_trashmain)
        self.image_label_trashmain.setAlignment(Qt.AlignCenter)

        self.create_image_button('labtop.png', 200, 170, "labtop", 150, 150, self.dummy_function)
        self.create_image_button('pump.png', 500, 170, "pump", 150, 150, self.dummy_function)
        self.create_image_button('chair.png', 800, 170, "chair", 150, 150, self.dummy_function)
        self.create_image_button('cosmetic.png', 200, 450, "cosmetic", 150, 150, self.dummy_function)
        self.create_image_button('stapler.png', 500, 450, "stapler", 150, 150, self.dummy_function)
        self.create_image_button('umbrella.png', 800, 450, "umbrella", 150, 150, self.dummy_function)
        
        self.create_main_button()
        
        self.show()
        
    def create_image_button(self, image_path, x, y, text, width, height, function):
        container = QWidget(self)
        container.setGeometry(x, y, width, height + 60)  # 60 is the extra height for the label and button spacing

        btn = QPushButton(container)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setToolTip(text)
        btn.setGeometry(0, 0, width, height)
        btn.setStyleSheet("border: none;")

        label = QLabel(text, container)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, height + 20, width, 40)  # Position the label below the button and add 20 pixels for spacing
        label.setStyleSheet("background-color: rgba(255, 255, 255, 1);")  # Set background color with transparency
        
        # Increase font size for the label
        font = label.font()
        font.setPointSize(12)
        label.setFont(font)
        
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
