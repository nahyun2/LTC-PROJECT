import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class TrashMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Living Tips for CBNU - Trash Tips")
        self.setGeometry(400, 100, 1180, 820)
        
        layout = QVBoxLayout()
    
        self.image_label_trashmain = QLabel(self)
        self.image_label_trashmain.setGeometry(0, 0, 1180, 820)    
        pixmap_trashmain = QPixmap('background.jpg')
        scaled_pixmap_trashmain = pixmap_trashmain.scaled(self.image_label_trashmain.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_trashmain.setPixmap(scaled_pixmap_trashmain)
        self.image_label_trashmain.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.image_label_trashmain)
        
        self.setLayout(layout)
        self.show()

    def create_image_button(self, image_path, x, y, tooltip, width, height):
        btn = QPushButton(parent=self)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setToolTip(tooltip)
        btn.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())
        btn.setStyleSheet("border: none;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    trashmainwindow = TrashMainWindow()
    trashmainwindow.show()
    sys.exit(app.exec_())
