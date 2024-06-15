import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QMessageBox, QFileDialog, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QPalette
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나만의 냉장고")
        self.setGeometry(0, 0, 1180, 820)

        # 배경 이미지 파일 경로
        self.background_image_path = "background.png"
        self.circular_image_path = "Fridge/picture.png"
        self.image_paths = [
            "Fridge/image.png",
            "Fridge/save.png",
        ]

        # 이미지 로드
        self.background_img = self.load_image(self.background_image_path, (1200, 820))
        self.circular_img = self.load_image(self.circular_image_path, (500, 500))  # 크기를 키움
        self.image_labels = []  # 이미지 라벨들을 담을 리스트

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 배경 이미지 설정
        self.draw_background_image()

        # 원형 이미지 버튼 생성
        if self.circular_img:
            self.circular_button = QPushButton(self.central_widget)
            self.circular_button.setIcon(QIcon(self.circular_img))
            self.circular_button.setIconSize(self.circular_img.size())
            self.circular_button.setGeometry(30, 150, self.circular_img.width(), self.circular_img.height())
            self.circular_button.setStyleSheet("border: none; background-color: transparent;")
            self.circular_button.clicked.connect(self.open_image_dialog)

        # 이미지 라벨들 생성 및 위치 설정
        label1 = QLabel(self.central_widget)
        label1.setGeometry(570, 30, 700, 700)
        pixmap1 = self.load_image(self.image_paths[0], (700, 700))
        if pixmap1:
            label1.setPixmap(pixmap1)
        self.image_labels.append(label1)

        label2 = QLabel(self.central_widget)
        label2.setGeometry(980, 730, 100, 60)
        pixmap2 = self.load_image(self.image_paths[1], (100, 60))
        if pixmap2:
            label2.setPixmap(pixmap2)
        self.image_labels.append(label2)

    def draw_background_image(self):
        if self.background_img:
            palette = self.palette()
            brush = QBrush(self.background_img)
            palette.setBrush(QPalette.Background, brush)
            self.setPalette(palette)

    def load_image(self, image_path, size):
        try:
            pixmap = QPixmap(image_path).scaled(size[0], size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
            return pixmap
        except Exception as e:
            QMessageBox.critical(None, "이미지 로드 오류", f"이미지를 로드하는 동안 오류가 발생했습니다: {e}")
            return None

    def open_image_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 선택", "", "이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.update_button_image(file_path)

    def update_button_image(self, image_path):
        pixmap = QPixmap(image_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.circular_button.setIcon(QIcon(pixmap))
        self.circular_button.setIconSize(QSize(500, 500))
        self.circular_button.setFixedSize(QSize(500, 500))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
