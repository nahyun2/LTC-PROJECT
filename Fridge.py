import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtCore import QProcess


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나만의 냉장고")
        self.setGeometry(0, 0, 1200, 820)

        # 배경 이미지 파일 경로 (임의로 설정)
        self.background_image_path = "background.png"

        # 이미지 로드 (배경 이미지)
        self.background_img = self.load_image(self.background_image_path, (1200, 820))

        # 이미지 라벨들을 담을 리스트
        self.image_labels = []

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 배경 이미지 설정
        self.draw_background_image()

        # 메인화면 버튼 생성
        self.main_screen_button = QPushButton('메인화면', self.central_widget)
        self.main_screen_button.setGeometry(30, 30, 100, 50)
        self.main_screen_button.clicked.connect(self.show_main_screen)

        # 이미지 라벨 추가
        label_img = QLabel(self.central_widget)
        label_img.setGeometry(250, 150, 800, 600)
        pixmap_img = self.load_image("Fridge/list.png", (700, 600))  # 경로 수정
        if pixmap_img:
            label_img.setPixmap(pixmap_img)
            self.image_labels.append(label_img)  # 이미지 라벨 객체를 리스트에 추가

        # 재료 추가 버튼 생성
        self.add_ingredient_button = QPushButton('재료 추가', self.central_widget)
        self.add_ingredient_button.setGeometry(1000, 730, 150, 60)
        self.add_ingredient_button.clicked.connect(self.add_ingredient)

    def draw_background_image(self):
        if self.background_img:
            palette = self.palette()
            brush = QBrush(self.background_img)
            palette.setBrush(self.backgroundRole(), brush)
            self.setPalette(palette)

    def load_image(self, image_path, size):
        try:
            pixmap = QPixmap(image_path).scaled(size[0], size[1])
            return pixmap
        except Exception as e:
            print(f"이미지를 로드하는 동안 오류 발생: {e}")
            return None

    def show_main_screen(self):
        # 메인 화면을 보여주는 동작을 여기에 구현
        print("메인 화면을 보여줍니다.")

    def add_ingredient(self):
        # 재료 추가 기능을 여기에 구현
        print("재료 추가 기능을 실행합니다.")
        self.run_plus_ingredient()

    def run_plus_ingredient(self):
        process = QProcess(self)
        process.start("python", ["plus_ingredient.py"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
