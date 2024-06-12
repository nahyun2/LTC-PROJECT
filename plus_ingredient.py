import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon, QImage, QBrush, QPalette
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QRect, QLineF, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor


        
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

        # 이미지 로드
        self.background_img = self.load_image(self.background_image_path, (1200, 820))
        self.ingredient_img = self.load_image(self.image_paths["재료 이름"], (630, 130))
        self.date_img = self.load_image(self.image_paths["구입 날짜"], (620, 90))
        self.expiry_img = self.load_image(self.image_paths["유통기한"], (595, 90))
        self.memo_img = self.load_image(self.image_paths["기타 메모"], (600, 300))
        self.save_img = self.load_image(self.image_paths["저장"], (100, 60))
        self.fridge_img = self.load_image(self.image_paths["냉장고 사진"], (500, 500))

        self.selected_image = None
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # 배경 이미지 설정
        self.draw_background_image()

        # 이미지 버튼과 이미지 라벨을 담을 수평 레이아웃
        image_layout = QHBoxLayout()

        # 냉장고 사진 버튼 생성
        if self.fridge_img:
            self.picture_button = QPushButton()
            size = QSize(self.fridge_img.width(), self.fridge_img.height())
            self.picture_button.setIconSize(size)
            self.picture_button.setIcon(QIcon(self.fridge_img))
            self.picture_button.clicked.connect(self.select_image)
            image_layout.addWidget(self.picture_button)

        # 이미지 라벨들을 담을 수직 레이아웃 생성
        right_layout = QVBoxLayout()

        # 이미지 라벨들 생성
        if self.ingredient_img:
            self.ingredient_entry = self.create_image_with_entry(self.ingredient_img)
            right_layout.addWidget(self.ingredient_entry)

        if self.date_img:
            self.date_entry = self.create_image_with_entry(self.date_img)
            right_layout.addWidget(self.date_entry)

        if self.expiry_img:
            self.expiry_entry = self.create_image_with_entry(self.expiry_img)
            right_layout.addWidget(self.expiry_entry)

        # 이미지 라벨과 메모를 겹쳐서 표시하기 위한 위젯 생성
        if self.memo_img:
            memo_widget = self.create_image_with_text(self.memo_img)
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
            pixmap = QPixmap(image_path).scaled(size[0], size[1], Qt.KeepAspectRatio)
            return pixmap
        except Exception as e:
            QMessageBox.critical(None, "이미지 로드 오류", f"이미지를 로드하는 동안 오류가 발생했습니다: {e}")
            return None

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path).scaled(500, 500, Qt.KeepAspectRatio)
            self.picture_button.setIcon(QIcon(pixmap))
            self.selected_image = pixmap

    def create_image_with_entry(self, pixmap):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)

        entry = QLineEdit()
        layout.addWidget(entry)
        return widget

    def create_image_with_text(self, pixmap):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # 메모 이미지 라벨 생성
        memo_label = QLabel()
        memo_label.setPixmap(pixmap)

        # 텍스트 입력란 생성
        memo_entry = QTextEdit()

        layout.addWidget(memo_label)
        layout.addWidget(memo_entry)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
