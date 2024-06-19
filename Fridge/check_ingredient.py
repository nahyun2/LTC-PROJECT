import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QPixmap

class CheckIngredientWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("냉장고 안 재료 확인하기")
        self.setGeometry(0, 0, 1200, 820)

        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 이미지 라벨 생성 및 위치 설정
        self.image_label = QLabel(self.central_widget)
        self.image_label.setGeometry(30, 30, 500, 500)
        pixmap = self.load_image(self.image_path, (500, 500))
        if pixmap:
            self.image_label.setPixmap(pixmap)

        # 메모 입력 위젯 생성
        self.memo1_input = QTextEdit(self.central_widget)
        self.memo1_input.setGeometry(570, 30, 600, 700)
        self.memo1_input.setReadOnly(True)  # 읽기 전용으로 설정

        # 저장 버튼 생성
        self.close_button = QPushButton("닫기", self.central_widget)
        self.close_button.setGeometry(1000, 730, 100, 60)
        self.close_button.clicked.connect(self.close_action)

        # 텍스트 파일에서 메모 내용 읽어오기
        memo_file_name = os.path.splitext(os.path.basename(self.image_path))[0] + ".txt"
        memo_file_path = os.path.join("saved_data", memo_file_name)
        if os.path.exists(memo_file_path):
            with open(memo_file_path, "r", encoding="utf-8") as f:
                memo_content = f.read()
                self.memo1_input.setPlainText(memo_content)

    def load_image(self, image_path, size):
        try:
            pixmap = QPixmap(image_path).scaled(size[0], size[1])
            return pixmap
        except Exception as e:
            print(f"이미지를 로드하는 동안 오류 발생: {e}")
            return None

    def close_action(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CheckIngredientWindow("example_image.png")  # 여기서 "example_image.png"는 예시로 설정한 이미지 경로입니다.
    window.show()
    sys.exit(app.exec_())
