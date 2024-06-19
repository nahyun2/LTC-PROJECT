import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPainter, QPalette, QBrush
from PyQt5.QtCore import QTimer, Qt, QProcess

from check_ingredient import CheckIngredientWindow  # check_ingredient.py에서 CheckIngredientWindow를 import

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나만의 냉장고")
        self.setGeometry(0, 0, 1200, 820)

        self.background_image_path = "background.png"
        self.background_img = self.load_image(self.background_image_path, (1200, 820))

        self.image_paths = set()
        self.image_buttons = []
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_new_image)
        self.timer.start(5000)  # 5초마다 새로운 이미지 체크

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.draw_background_image()

        # 메인 화면 버튼
        self.main_screen_button = QPushButton(self.central_widget)
        self.main_screen_button.setGeometry(30, 30, 120, 60)
        pixmap_main_screen = QPixmap("main_button.png").scaled(120, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.main_screen_button.setIcon(QIcon(pixmap_main_screen))
        self.main_screen_button.setIconSize(pixmap_main_screen.size())
        self.main_screen_button.setStyleSheet("border: none;")
        self.main_screen_button.clicked.connect(self.show_main_screen)

        # 재료 추가 버튼
        self.add_ingredient_button = QPushButton(self.central_widget)
        self.add_ingredient_button.setGeometry(1015, 730, 150, 60)
        pixmap_add_ingredient = QPixmap("Fridge/add.png").scaled(150, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.add_ingredient_button.setIcon(QIcon(pixmap_add_ingredient))
        self.add_ingredient_button.setIconSize(pixmap_add_ingredient.size())
        self.add_ingredient_button.setStyleSheet("border: none;")
        self.add_ingredient_button.clicked.connect(self.add_ingredient)

        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setGeometry(200, 150, 800, 600)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        self.set_image_layout_background("Fridge/list.png")  # 이미지 레이아웃의 배경 설정

    def set_image_layout_background(self, image_path):
        try:
            image = QImage(image_path)
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(image))
            self.scroll_widget.setAutoFillBackground(True)
            self.scroll_widget.setPalette(palette)

            # scroll_widget의 사이즈를 이미지 사이즈에 맞게 조정
            self.scroll_widget.setFixedSize(image.width(), image.height())
        except Exception as e:
            print(f"배경 이미지 설정 중 오류 발생: {e}")

    def draw_background_image(self):
        if self.background_img:
            palette = self.palette()
            brush = QBrush(self.background_img)
            palette.setBrush(self.backgroundRole(), brush)
            self.setPalette(palette)

    def load_image(self, image_path, size):
        try:
            pixmap = QPixmap(image_path).scaled(size[0], size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
            return pixmap
        except Exception as e:
            print(f"이미지를 로드하는 동안 오류 발생: {e}")
            return None

    def add_image_button(self, image_path):
        if image_path in self.image_paths:
            return  # 이미 추가된 이미지 경로는 건너뜀

        button = QPushButton(self.scroll_widget)
        pixmap = QPixmap(image_path).scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 이미지 크기를 더 크게 설정
        button.setIcon(QIcon(pixmap))
        button.setIconSize(pixmap.size())
        button.setFixedSize(pixmap.size())
        button.setStyleSheet("border: none; background-color: transparent;")
        button.clicked.connect(lambda: self.run_check_ingredient(image_path))

        self.image_buttons.append(button)
        self.image_paths.add(image_path)  # 추가된 이미지 경로를 기록

        self.refresh_image_layout()

    def check_for_new_image(self):
        flag_path = "saved_data/new_image_flag.txt"
        if os.path.exists(flag_path):
            with open(flag_path, "r", encoding="utf-8") as f:
                new_image_path = f.read().strip()
                if new_image_path and os.path.isfile(new_image_path):
                    self.add_image_button(new_image_path)
            os.remove(flag_path)

        self.refresh_image_layout()

    def refresh_image_layout(self):
        # 이미지 버튼 레이아웃 초기화
        for layout_index in reversed(range(self.scroll_layout.count())):
            layout_item = self.scroll_layout.itemAt(layout_index)
            if layout_item.widget():
                layout_item.widget().deleteLater()
            self.scroll_layout.removeItem(layout_item)

        # 새로운 이미지 버튼 추가
        current_layout = None
        for index, button in enumerate(self.image_buttons):
            if index % 4 == 0:
                current_layout = QHBoxLayout()
                current_layout.setAlignment(Qt.AlignCenter)  # 이미지 버튼을 가운데 정렬
                current_layout.setContentsMargins(0, 100, 0, 0)  # 위쪽 마진 설정
                self.scroll_layout.addLayout(current_layout)
            current_layout.addWidget(button)

    def show_main_screen(self):
        print("메인 화면을 보여줍니다.")

    def add_ingredient(self):
        print("재료 추가 기능을 실행합니다.")
        self.run_plus_ingredient()

    def run_plus_ingredient(self):
        process = QProcess(self)
        process.start("python", ["plus_ingredient.py"])
        process.finished.connect(self.refresh_after_ingredient_addition)  # 프로세스가 종료된 후에 화면 업데이트

    def refresh_after_ingredient_addition(self):
        # 재료 추가 프로세스가 종료된 후에 이미지를 다시 로드하여 버튼 업데이트
        self.image_paths.clear()  # 기존 이미지 경로 초기화
        self.image_buttons.clear()  # 기존 이미지 버튼 초기화

        # 새로운 이미지 버튼 추가
        for image_path in os.listdir("saved_data"):  # 저장된 데이터 폴더에서 이미지 파일을 찾음
            if image_path.endswith(".png") or image_path.endswith(".jpg"):
                full_path = os.path.join("saved_data", image_path)
                self.add_image_button(full_path)

        self.refresh_image_layout()

    def run_check_ingredient(self, image_path):
        self.check_ingredient_window = CheckIngredientWindow(image_path)
        self.check_ingredient_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
