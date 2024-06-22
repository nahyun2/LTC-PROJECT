import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QFont

class CheckIngredientWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("냉장고 안 재료 확인하기")
        self.setGeometry(400, 100, 1200, 820)

        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 배경 이미지 설정
        self.background_label = QLabel(self.central_widget)
        self.background_label.setGeometry(0, 0, 1200, 820)
        pixmap_background = self.load_image("background.png", (1200, 820))
        if pixmap_background:
            self.background_label.setPixmap(pixmap_background)

        # 첫 번째 이미지 라벨 생성 및 위치 설정
        self.image_label = QLabel(self.central_widget)
        self.image_label.setGeometry(30, 150, 500, 500)
        pixmap = self.load_image(self.image_path, (500, 500))
        if pixmap:
            self.image_label.setPixmap(pixmap)

        # 두 번째 이미지 라벨 생성 및 위치 설정
        self.image_label2 = QLabel(self.central_widget)
        self.image_label2.setGeometry(570, 30, 550, 700)
        pixmap2 = self.load_image("Fridge/image.png", (550, 700))
        if pixmap2:
            self.image_label2.setPixmap(pixmap2)

        # 메모 입력 위젯 생성
        self.memo1_input = QTextEdit(self.central_widget)
        self.memo1_input.setGeometry(800, 100, 250, 50)
        self.set_text_edit_font_size(self.memo1_input, 14)  # 폰트 크기 설정

        self.memo2_input = QTextEdit(self.central_widget)
        self.memo2_input.setGeometry(800, 200, 250, 50)
        self.set_text_edit_font_size(self.memo2_input, 14)  # 폰트 크기 설정

        self.memo3_input = QTextEdit(self.central_widget)
        self.memo3_input.setGeometry(800, 310, 250, 50)
        self.set_text_edit_font_size(self.memo3_input, 14)  # 폰트 크기 설정

        self.memo4_input = QTextEdit(self.central_widget)
        self.memo4_input.setGeometry(630, 470, 420, 200)
        self.set_text_edit_font_size(self.memo4_input, 14)  # 폰트 크기 설정

        # 삭제 버튼 이미지 설정
        self.delete_button = QPushButton(self.central_widget)
        self.delete_button.setGeometry(860, 735, 110, 60)
        pixmap_delete = QPixmap("Fridge/delete.png").scaled(110, 60)
        self.delete_button.setIcon(QIcon(pixmap_delete))
        self.delete_button.setIconSize(pixmap_delete.size())
        self.delete_button.setStyleSheet("border: none;")
        self.delete_button.clicked.connect(self.delete_action)

        # 닫기 버튼 이미지 설정
        self.close_button = QPushButton(self.central_widget)
        self.close_button.setGeometry(980, 730, 110, 70)  # 수정된 부분: 닫기 버튼 위치 조정
        pixmap_close = QPixmap("close_button.png").scaled(110, 70)
        self.close_button.setIcon(QIcon(pixmap_close))
        self.close_button.setIconSize(pixmap_close.size())
        self.close_button.setStyleSheet("border: none;")
        self.close_button.clicked.connect(self.close_action)

        # 텍스트 파일에서 메모 내용 읽어오기
        for i in range(4):
            memo_file_name = f"{os.path.splitext(os.path.basename(self.image_path))[0]}{i + 1}.txt"
            memo_file_path = os.path.join("saved_data", memo_file_name)
            memo_input = getattr(self, f"memo{i + 1}_input")  # 동적으로 메모 입력 위젯에 접근

            if os.path.exists(memo_file_path):
                with open(memo_file_path, "r", encoding="utf-8") as f:
                    memo_content = f.read()
                    memo_input.setPlainText(memo_content)

    def load_image(self, image_path, size):
        try:
            pixmap = QPixmap(image_path).scaled(size[0], size[1])
            return pixmap
        except Exception as e:
            print(f"이미지를 로드하는 동안 오류 발생: {e}")
            return None

    def set_text_edit_font_size(self, text_edit, font_size):
        font = QFont()
        font.setPointSize(font_size)
        text_edit.setFont(font)

    def delete_action(self):
        # 이미지 파일 및 메모 파일 삭제 기능 구현
        image_file_path = self.image_path
        memo_file_name = os.path.splitext(os.path.basename(image_file_path))[0] + ".txt"
        image_save_path = os.path.join("saved_data", os.path.basename(image_file_path))
        memo_save_path = os.path.join("saved_data", memo_file_name)

        try:
            # 이미지 파일 삭제
            if os.path.exists(image_save_path):
                os.remove(image_save_path)
                QMessageBox.information(self, "삭제 완료", "이미지 파일이 삭제되었습니다.")
            else:
                QMessageBox.warning(self, "삭제 실패", "이미지 파일을 찾을 수 없습니다.")

            # 메모 파일 삭제
            if os.path.exists(memo_save_path):
                os.remove(memo_save_path)
                QMessageBox.information(self, "삭제 완료", "메모 파일이 삭제되었습니다.")
            else:
                QMessageBox.warning(self, "삭제 완료", "메모 파일을 삭제하였습니다.")

            self.close()

        except Exception as e:
            QMessageBox.critical(self, "오류", f"삭제 중 오류가 발생했습니다: {str(e)}")

    def close_action(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CheckIngredientWindow("example_image.png")  # 여기서 "example_image.png"는 예시로 설정한 이미지 경로입니다.
    window.show()
    sys.exit(app.exec_())
