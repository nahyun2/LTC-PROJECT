import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QBrush, QIcon
from PyQt5.QtCore import QTimer, Qt, QProcess

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

        self.main_screen_button = QPushButton('메인화면', self.central_widget)
        self.main_screen_button.setGeometry(30, 30, 100, 50)
        self.main_screen_button.clicked.connect(self.show_main_screen)

        self.add_ingredient_button = QPushButton('재료 추가', self.central_widget)
        self.add_ingredient_button.setGeometry(1000, 730, 150, 60)
        self.add_ingredient_button.clicked.connect(self.add_ingredient)

        self.image_layout = QVBoxLayout()
        self.image_container = QWidget(self.central_widget)
        self.image_container.setGeometry(250, 150, 800, 600)
        self.image_container.setLayout(self.image_layout)

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

        button = QPushButton(self.central_widget)
        pixmap = QPixmap(image_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        button.setIcon(QIcon(pixmap))
        button.setIconSize(pixmap.size())
        button.setFixedSize(pixmap.size())
        button.setStyleSheet("border: none; background-color: transparent;")

        self.image_layout.addWidget(button)
        self.image_buttons.append(button)
        self.image_paths.add(image_path)  # 추가된 이미지 경로를 기록

    def check_for_new_image(self):
        flag_path = "saved_data/new_image_flag.txt"
        if os.path.exists(flag_path):
            with open(flag_path, "r", encoding="utf-8") as f:
                new_image_path = f.read().strip()
                if new_image_path and os.path.isfile(new_image_path):
                    self.add_image_button(new_image_path)
            os.remove(flag_path)

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

        # 기존 이미지 버튼 모두 제거
        while self.image_layout.count():
            item = self.image_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # 새로운 이미지 버튼 추가
        for image_path in os.listdir("saved_data"):  # 저장된 데이터 폴더에서 이미지 파일을 찾음
            if image_path.endswith(".png") or image_path.endswith(".jpg"):
                full_path = os.path.join("saved_data", image_path)
                self.add_image_button(full_path)

        # 화면 업데이트
        self.image_container.update()
        self.central_widget.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
