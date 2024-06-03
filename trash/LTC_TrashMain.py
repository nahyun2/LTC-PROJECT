import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class TrashMain_window(QWidget):
    def __init__(self):
        super(TrashMain_window, self).__init__()
        self.setWindowTitle("Living Tips for CBNU")
        self.setGeometry(400, 100, 1180, 820)
        
        self.image_label_Trashmain = QLabel(self)
        self.image_label_Trashmain.setGeometry(0, 0, 1180, 820)    
        pixmap_Trashmain = QPixmap('background.jpg')
        scaled_pixmap_Trashmain = pixmap_Trashmain.scaled(self.image_label_Trashmain.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.image_label_Trashmain.setPixmap(scaled_pixmap_Trashmain)
        self.image_label_Trashmain.setAlignment(Qt.AlignCenter)


    def create_image_button(self, image_path, x, y, tooltip, width, height):
        btn = QPushButton(parent=self)
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        btn.setIcon(QIcon(scaled_pixmap))
        btn.setIconSize(scaled_pixmap.size())
        btn.setToolTip(tooltip)
        btn.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())
        btn.setStyleSheet("border: none;")
        

app_Trashmain = QApplication(sys.argv)
Trashmainwindow = TrashMain_window()
Trashmainwindow.show()
app_Trashmain.exec_()
