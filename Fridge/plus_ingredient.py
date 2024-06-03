from msilib.schema import Icon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QImage, QIcon
from PyQt5.QtCore import QSize
from PIL import Image, ImageOps, ImageDraw
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Living Tips for CBNU")
        self.setGeometry(0, 0, 1200, 820)

        # 이미지 파일 경로
        self.image_paths = {
            "구입 날짜": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/구입 날짜.png",
            "기타 메모": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/기타 메모.png",
            "유통기한": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/유통기한.png",
            "저장": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/저장버튼.png",
            "재료 이름": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/재료 이름.png",
            "냉장고 사진": "C:/Users/chlsk/Desktop/opensw project/재료관리사진/냉장고 사진.png",  # 냉장고 사진 경로 추가
        }

        # 배경 이미지 파일 경로
        self.background_image_path = "C:/Users/chlsk/Desktop/opensw project/배경.png"

        # 이미지 로드
        self.ingredient_img = self.load_image(self.image_paths["재료 이름"], (630, 130))
        self.date_img = self.load_image(self.image_paths["구입 날짜"], (620, 90))
        self.expiry_img = self.load_image(self.image_paths["유통기한"], (595, 90))
        self.memo_img = self.load_image(self.image_paths["기타 메모"], (600, 300))
        self.save_img = self.load_image(self.image_paths["저장"], (100, 60))
        self.pic_img = self.load_image(self.image_paths["냉장고 사진"], (500, 500))  # 냉장고 사진 크기 조정
        self.background_img = self.load_image(self.background_image_path, (1200, 820))

        self.selected_image = None  # 초기화
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Canvas 위젯 생성 및 배경 이미지 설정
        self.canvas_label = QLabel()
        layout.addWidget(self.canvas_label)
        self.draw_background_image()

        # 냉장고 사진 버튼 생성
        if self.pic_img:
            self.picture_button = QPushButton()
            self.picture_button.setIconSize(QSize(*self.pic_img.size))  # QSize로 변환
            self.picture_button.setIcon(QIcon(QPixmap.fromImage(self.pil_image_to_qimage(self.pic_img))))

            self.picture_button.clicked.connect(self.select_image)
            layout.addWidget(self.picture_button)

        # 오른쪽에 이미지와 입력란 추가
        right_layout = QVBoxLayout()

        if self.ingredient_img:
            self.ingredient_entry = self.create_image_with_entry(self.ingredient_img, 20)
            right_layout.addWidget(self.ingredient_entry)

        if self.date_img:
            self.date_entry = self.create_image_with_entry(self.date_img, 20)
            right_layout.addWidget(self.date_entry)

        if self.expiry_img:
            self.expiry_entry = self.create_image_with_entry(self.expiry_img, 20)
            right_layout.addWidget(self.expiry_entry)

        if self.memo_img:
            self.memo_entry = self.create_image_with_text(self.memo_img, 30, 15)
            right_layout.addWidget(self.memo_entry)

        # 저장 버튼 추가
        if self.save_img:
            self.save_button = QPushButton()
            self.save_button.setIconSize(QSize(*self.save_img.size))  # QSize로 변환
            self.save_button.setIcon(QIcon(QPixmap.fromImage(self.pil_image_to_qimage(self.save_img))))
            self.save_button.clicked.connect(self.save_data)
            right_layout.addWidget(self.save_button)

        layout.addLayout(right_layout)

    def draw_background_image(self):
        if self.background_img:
            q_image = self.pil_image_to_qimage(self.background_img)
            self.canvas_label.setPixmap(QPixmap.fromImage(q_image))

    def load_image(self, image_path, size):
        try:
            image = Image.open(image_path)
            image = image.resize(size, Image.LANCZOS)
            return image
        except Exception as e:
            QMessageBox.critical(None, "이미지 로드 오류", f"이미지를 로드하는 동안 오류가 발생했습니다: {e}")
            return None

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            img = self.load_image(file_path, (500, 500))
            if img:
                circular_img = ImageOps.fit(img, (500, 500), Image.LANCZOS)
                mask = Image.new('L', (500, 500), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 500, 500), fill=255)
                circular_img.putalpha(mask)
                self.selected_image = img
                q_image = self.pil_image_to_qimage(circular_img)
                self.picture_button.setIcon(QPixmap.fromImage(q_image))

    def create_image_with_entry(self, image, entry_font_size):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        q_image = self.pil_image_to_qimage(image)
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(q_image))
        layout.addWidget(label)

        entry = QTextEdit()
        entry.setFont(QFont("Arial", entry_font_size))
        layout.addWidget(entry)
        widget.entry = entry  # QMainWindow 내에서 entry 접근을 위함
        return widget

    def create_image_with_text(self, image, text_width, text_height):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        q_image = self.pil_image_to_qimage(image)
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(q_image))
        layout.addWidget(label)

        text = QTextEdit()
        text.setFixedSize(text_width * 10, text_height * 20)
        layout.addWidget(text)
        widget.text = text  # QMainWindow 내에서 text 접근을 위함
        return widget

    def pil_image_to_qimage(self, pil_image):
        if pil_image.mode == "RGB":
            r, g, b = pil_image.split()
            return QImage(Image.merge("RGB", (b, g, r)).tobytes(), pil_image.width, pil_image.height, QImage.Format_RGB888)
        elif pil_image.mode == "RGBA":
            r, g, b, a = pil_image.split()
            return QImage(Image.merge("RGBA", (b, g, r, a)).tobytes(), pil_image.width, pil_image.height, QImage.Format_RGBA8888)
        else:
            return QImage(pil_image.tobytes(), pil_image.width, pil_image.height, QImage.Format_Indexed8)

    def save_data(self):
        try:
            ingredient = self.ingredient_entry.entry.toPlainText().strip()
            date = self.date_entry.entry.toPlainText().strip()
            expiry = self.expiry_entry.entry.toPlainText().strip()
            memo = self.memo_entry.text.toPlainText().strip()

            if not (ingredient and date and expiry):
                QMessageBox.critical(self, "입력 오류", "재료 이름, 구입 날짜, 유통기한은 필수 입력 항목입니다.")
                return

            if self.selected_image is None:
                QMessageBox.critical(self, "이미지 선택 오류", "이미지를 선택해주세요.")
                return

            save_directory = "C:/Users/chlsk/Desktop/opensw project/saved_data"
            os.makedirs(save_directory, exist_ok=True)

            base_filename = os.path.join(save_directory, ingredient.replace(" ", "_"))

            # 이미지 저장
            image_save_path = base_filename + ".png"
            self.selected_image.save(image_save_path)

            # 텍스트 데이터 저장
            text_save_path = base_filename + ".txt"
            with open(text_save_path, "w") as file:
                file.write(f"재료 이름: {ingredient}\n")
                file.write(f"구입 날짜: {date}\n")
                file.write(f"유통기한: {expiry}\n")
                file.write(f"메모: {memo}\n")

            QMessageBox.information(self, "저장 완료", "데이터가 성공적으로 저장되었습니다.")
        except Exception as e:
                        QMessageBox.critical(self, "오류 발생", f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

