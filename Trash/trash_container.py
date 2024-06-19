import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt

class ImageBackgroundApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 경로 설정
        self.base_path = os.path.expanduser("~/Desktop/Recycling")
        self.container_path = os.path.join(self.base_path, "container")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('분리수거_포장지')

        # 배경 이미지 추가
        self.label = QLabel(self)
        self.pixmap = QPixmap(os.path.join(self.base_path, 'background.png'))
        if self.pixmap.isNull():
            print(f"Failed to load {os.path.join(self.base_path, 'background.png')}")
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(0, 0, 1200, 820)

        # 폰트 설정
        font = QFont()
        font.setPointSize(16)
        
        title_font = QFont()
        title_font.setPointSize(30)
        
        item_font = QFont()
        item_font.setPointSize(18)
        item_font.setBold(True)

        # 라벨 추가
        self.title_label = QLabel('포장지', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['bottle.png', 'box.png', 'can.png', 'plasticbag.png', 'styrofoam.png', 'wrapper.png']
        texts = ['기름병', '과자 박스', '캔', '과자 봉지', '스티로폼', '개별 포장지']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.container_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.container_path, img)}")
            button.setIcon(icon)
            button.setIconSize(button.size())
            button.setStyleSheet("border: none;")  # 회색 버튼 영역을 제거합니다.
            button.clicked.connect(lambda _, x=i: self.showDetails(x))
            self.buttons.append(button)

            label = QLabel(text, self)
            label.setGeometry(pos[0], pos[1] + 230, 225, 50)
            label.setAlignment(Qt.AlignCenter)
            label.setFont(item_font)
            self.labels.append(label)

        # 선택한 아이템의 이름을 왼쪽 아래에 표시할 라벨 추가
        self.item_label = QLabel('', self)
        self.item_label.setGeometry(100, 680, 400, 50)
        self.item_label.setFont(QFont('Arial', 20, QFont.Bold))
        self.item_label.setAlignment(Qt.AlignCenter)
        self.item_label.hide()

        # 숨겨질 라벨 및 버튼들
        self.image_label = QLabel(self)
        self.image_label.hide()

        self.image_title_label = QLabel(self)  # 추가된 부분
        self.image_title_label.setGeometry(100, 680, 400, 50)  # 사진 아래에 제목을 표시할 위치
        self.image_title_label.setFont(QFont('Arial', 22, QFont.Bold))
        self.image_title_label.setAlignment(Qt.AlignCenter)
        self.image_title_label.hide()

        self.additional_image_label = QLabel(self)
        self.additional_image_label.setPixmap(QPixmap(os.path.join(self.base_path, 'memo.png')))
        if self.additional_image_label.pixmap().isNull():
            print(f"Failed to load {os.path.join(self.base_path, 'memo.png')}")
        self.additional_image_label.setGeometry(540, 170, 600, 600)
        self.additional_image_label.hide()

        self.text_labels = []

        # 닫기 버튼을 PNG 파일로 변경하고 효과 추가
        self.close_button = QPushButton(self)
        close_button_pixmap = QPixmap(os.path.join(self.base_path, 'closebutton.png'))
        if close_button_pixmap.isNull():
            print(f"Failed to load {os.path.join(self.base_path, 'closebutton.png')}")
        self.close_button.setIcon(QIcon(close_button_pixmap))
        self.close_button.setIconSize(close_button_pixmap.size())
        self.close_button.setGeometry(1050, 700, close_button_pixmap.width(), close_button_pixmap.height())
        self.close_button.setStyleSheet("border: none;")
        self.close_button.pressed.connect(self.closeButtonPressed)
        self.close_button.released.connect(self.closeButtonReleased)
        self.close_button.hide()

        # 메인 화면 버튼 추가
        self.main_button = QPushButton(self)
        main_button_pixmap = QPixmap(os.path.join(self.base_path, 'mainbutton.png'))
        if main_button_pixmap.isNull():
            print(f"Failed to load {os.path.join(self.base_path, 'mainbutton.png')}")
        self.main_button.setIcon(QIcon(main_button_pixmap))
        self.main_button.setIconSize(main_button_pixmap.size())
        self.main_button.setGeometry(45, 47, main_button_pixmap.width(), main_button_pixmap.height())
        self.main_button.setStyleSheet("border: none;")
        self.main_button.pressed.connect(self.mainButtonPressed)
        self.main_button.released.connect(self.mainButtonReleased)

        # 이전 화면 버튼 추가
        self.previous_button = QPushButton(self)
        previous_button_pixmap = QPixmap(os.path.join(self.base_path, 'backbutton.png'))
        if previous_button_pixmap.isNull():
            print(f"Failed to load {os.path.join(self.base_path, 'backbutton.png')}")
        self.previous_button.setIcon(QIcon(previous_button_pixmap))
        self.previous_button.setIconSize(previous_button_pixmap.size())
        self.previous_button.setGeometry(200, 50, previous_button_pixmap.width(), previous_button_pixmap.height())
        self.previous_button.setStyleSheet("border: none;")
        self.previous_button.pressed.connect(self.previousButtonPressed)
        self.previous_button.released.connect(self.previousButtonReleased)

        self.show()

    def mainButtonPressed(self):
        self.main_button.setIcon(QIcon(os.path.join(self.base_path, 'mainbutton_pressed.png')))

    def mainButtonReleased(self):
        self.main_button.setIcon(QIcon(os.path.join(self.base_path, 'mainbutton.png')))
        print("메인 화면 버튼이 클릭되었습니다.")  # 여기서 원하는 동작을 추가할 수 있습니다.

    def previousButtonPressed(self):
        self.previous_button.setIcon(QIcon(os.path.join(self.base_path, 'backbutton_pressed.png')))

    def previousButtonReleased(self):
        self.previous_button.setIcon(QIcon(os.path.join(self.base_path, 'backbutton.png')))
        print("이전 화면 버튼이 클릭되었습니다.")  # 여기서 원하는 동작을 추가할 수 있습니다.

    def closeButtonPressed(self):
        self.close_button.setIcon(QIcon(os.path.join(self.base_path, 'closebutton_pressed.png')))

    def closeButtonReleased(self):
        self.close_button.setIcon(QIcon(os.path.join(self.base_path, 'closebutton.png')))
        self.closeDetails()

    def showDetails(self, index):
        for button in self.buttons:
            button.hide()
        for label in self.labels:
            label.hide()
        self.title_label.hide()
        self.main_button.hide()
        self.previous_button.hide()

        image_paths = [
            os.path.join(self.container_path, 'bottle.png'),
            os.path.join(self.container_path, 'box.png'),
            os.path.join(self.container_path, 'can.png'),
            os.path.join(self.container_path, 'plasticbag.png'),
            os.path.join(self.container_path, 'styrofoam.png'),
            os.path.join(self.container_path, 'wrapper.png')
        ]

        image_titles = ['기름병', '과자 박스', '캔', '과자 봉지', '스티로폼', '개별 포장지']  # 추가된 부분

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('처리 방법', 
             '\n\n\n\n- 내용물을 비운 뒤 기름기를 제거해 말린 뒤\n 유리로 분리배출\n'
             '\n- 상표와 기름병 마개(뚜껑)는 제거 후 배출\n'
             '\n- 유리병이 깨졌을 경우 주민센터에서 \n 불연성 마대를 구입해 배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 종이 재질의 과자 포장 박스는 종이로 \n 분리배출\n'
             '\n- 비닐 코팅되어 찢어지지 않는 과자 박스는\n 재활용이 불가능하니 일반쓰레기\n (종량제봉투)로 배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 내용물을 비우고 물로 깨끗이 헹군 뒤 라벨,\n 스티커 등이 붙어있을 경우 깨끗하게 떼어낸\n 후 캔류로 배출\n'
             '\n- 플라스틱 뚜껑 등 다른 재질은 분리해서 \n배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 내부의 기름기와 음식물을 깨끗이 세척한\n 후 비닐류로 분리배출\n'
             '\n- 스티커, 테이프 등을 모두 떼어내서 일반\n 쓰레기(종량제봉투)로 버린 후 과자 봉지만\n 비닐류로 분리배출\n'
             '\n- 봉지를 접지 말고 펼친 채로 분리배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 이물질이 묻어있을 경우 물로 깨끗이 세척\n 한 후 분리배출\n'
             '\n- 박스에 붙어있는 택배송장, 테이프, 스티커\n 는 완전히 떼어내서 일반쓰레기로 배출\n'
             '\n- 무늬와 색상이 있거나 비닐이 코팅된\n 스티로폼은 일반쓰레기(종량제봉투)로 배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 커피믹스, 낱개포장 과자 등을 포장한 비닐\n 포장재는 내부의 음식물을 모두 비우거나\n 씻어낸 뒤 비닐류로 분리배출\n'
             '\n- 음식물을 제거하기 어려우면 그냥 일반\n 쓰레기(종량제봉투)로 배출\n'
             '\n- 스티커, 테이프 등이 붙어있으면 모두\n 떼어내서 일반 쓰레기(종량제봉투)로 버린\n 후 포장 비닐만 비닐류로 분리배출\n')
        ]

        text_positions = [
            [(610, 210), (620, 230)],
            [(610, 210), (620, 230)],
            [(610, 210), (620, 230)],
            [(610, 210), (620, 230)],
            [(610, 210), (620, 230)],
            [(610, 210), (620, 230)]
        ]

        self.image_label.setPixmap(QPixmap(image_paths[index]).scaled(image_sizes[index][0], image_sizes[index][1], Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if self.image_label.pixmap().isNull():
            print(f"Failed to load {image_paths[index]}")
        self.image_label.setGeometry(100, 270, image_sizes[index][0], image_sizes[index][1])
        self.image_label.show()

        self.image_title_label.setText(image_titles[index])  # 추가된 부분
        self.image_title_label.show()  # 추가된 부분

        self.additional_image_label.show()

        # 텍스트 라벨 갯수를 텍스트 갯수에 맞게 설정
        for i in range(len(self.text_labels)):
            self.text_labels[i].hide()

        required_text_labels = len(texts[index])
        while len(self.text_labels) < required_text_labels:
            text_label = QLabel(self)
            self.text_labels.append(text_label)

        text_sizes = [(750, 50), (560, 400)]  # 각 텍스트 라벨의 크기 지정
        text_fonts = [QFont('Arial', 25, QFont.Bold), QFont('Arial', 18)]  # 각 텍스트 라벨의 폰트 지정

        for i, text in enumerate(texts[index]):
            self.text_labels[i].setText(text)
            self.text_labels[i].setFont(text_fonts[i])  # 폰트 지정
            self.text_labels[i].setGeometry(text_positions[index][i][0], text_positions[index][i][1], text_sizes[i][0], text_sizes[i][1])  # 크기와 위치 조정
            self.text_labels[i].show()

        self.close_button.show()

    def closeDetails(self):
        self.image_label.hide()
        self.image_title_label.hide()  # 추가된 부분
        self.additional_image_label.hide()
        for text_label in self.text_labels:
            text_label.hide()
        self.close_button.hide()
        
        for button in self.buttons:
            button.show()
        for label in self.labels:
            label.show()
        self.title_label.show()
        self.main_button.show()
        self.previous_button.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageBackgroundApp()
    sys.exit(app.exec_())
