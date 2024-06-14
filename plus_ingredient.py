import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QFileDialog, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QPalette
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나만의 냉장고")
        self.setGeometry(0, 0, 1200, 820)

        # 이미지 파일 경로
        self.image_paths = {
            "구입 날짜": "Fridge/date.png",
            "기타 메모": "Fridge/memo.png",
            "유통기한": "Fridge/Expiration.png",
            "저장": "Fridge/save.png",
            "재료 이름": "Fridge/name.png",
            "냉장고 사진": "Fridge/picture.png",
        }

        # 배경 이미지 파일 경로
        self.background_image_path = "background.png"
        self.circular_image_path = "Fridge/picture.png"

        # 이미지 로드
        self.background_img = self.load_image(self.background_image_path, (1200, 820))
        self.ingredient_img = self.load_image(self.image_paths["재료 이름"], (630, 130))
        self.date_img = self.load_image(self.image_paths["구입 날짜"], (620, 90))
        self.expiry_img = self.load_image(self.image_paths["유통기한"], (595, 90))
        self.memo_img = self.load_image(self.image_paths["기타 메모"], (600, 300))
        self.save_img = self.load_image(self.image_paths["저장"], (100, 60))
        self.fridge_img = self.load_image(self.image_paths["냉장고 사진"], (500, 500))
        self.circular_img = self.load_image(self.circular_image_path, (200, 200))  # 크기를 키움

        self.selected_image = None
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # 배경 이미지 설정
        self.draw_background_image()

        # 이미지 라벨들을 담을 수평 레이아웃
        image_layout = QHBoxLayout()

        # 원형 이미지 버튼 생성
        if self.circular_img:
            self.circular_button = QPushButton()
            self.circular_button.setIcon(QIcon(self.circular_img))
            self.circular_button.setIconSize(self.circular_img.size())
            self.circular_button.setFixedSize(self.circular_img.size())
            self.circular_button.setStyleSheet("border: none; background-color: transparent;")
            self.circular_button.clicked.connect(self.open_image_dialog)
            image_layout.addWidget(self.circular_button)

        # 이미지 라벨들을 담을 수직 레이아웃 생성
        right_layout = QVBoxLayout()

        # 이미지 라벨들 생성
        if self.ingredient_img:
            self.ingredient_entry = self.create_image_with_entry(self.ingredient_img, QSize(600, 30))
            right_layout.addWidget(self.ingredient_entry)

        if self.date_img:
            self.date_entry = self.create_image_with_entry(self.date_img, QSize(600, 30))
            right_layout.addWidget(self.date_entry)

        if self.expiry_img:
            self.expiry_entry = self.create_image_with_entry(self.expiry_img, QSize(600, 30))
            right_layout.addWidget(self.expiry_entry)

        # 이미지 라벨과 메모를 겹쳐서 표시하기 위한 위젯 생성
        if self.memo_img:
            memo_widget = self.create_image_with_text(self.memo_img, QSize(600, 150))
            right_layout.addWidget(memo_widget)

        # 수평 레이아웃에 수직 레이아웃 추가
        image_layout.addLayout(right_layout)

        # 센트럴 위젯의 레이아웃 설정
        layout.addLayout(image_layout)

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

    def create_image_with_entry(self, pixmap, entry_size):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)

        entry = QLineEdit()
        entry.setFixedSize(entry_size)
        layout.addWidget(entry)
        return widget

    def create_image_with_text(self, pixmap, text_size):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # 메모 이미지 라벨 생성
        memo_label = QLabel()
        memo_label.setPixmap(pixmap)

        # 텍스트 입력란 생성
        memo_entry = QTextEdit()
        memo_entry.setFixedSize(text_size)

        layout.addWidget(memo_label)
        layout.addWidget(memo_entry)
        return widget

    def open_image_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 선택", "", "이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.update_button_image(file_path)

    def update_button_image(self, image_path):
        pixmap = QPixmap(image_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.circular_button.setIcon(QIcon(pixmap))
        self.circular_button.setIconSize(QSize(200, 200))
        self.circular_button.setFixedSize(QSize(200, 200))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
