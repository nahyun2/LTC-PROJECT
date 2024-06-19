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
        self.base_path = os.path.expanduser("~/Desktop/Washing")
        self.smell_path = os.path.join(self.base_path, "smell")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('냄새_세탁')

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
        self.title_label = QLabel('냄새', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['sweat.png', 'mold.png', 'sour.png', 'rainy.png', 'oil.png', 'smoke.png']
        texts = ['땀', '곰팡이', '쉰내', '장마철', '기름', '담배']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.smell_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.smell_path, img)}")
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

        self.image_title_label = QLabel(self)
        self.image_title_label.setGeometry(100, 680, 400, 50)
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
            os.path.join(self.smell_path, 'sweat.png'),
            os.path.join(self.smell_path, 'mold.png'),
            os.path.join(self.smell_path, 'sour.png'),
            os.path.join(self.smell_path, 'rainy.png'),
            os.path.join(self.smell_path, 'oil.png'),
            os.path.join(self.smell_path, 'smoke.png')
        ]

        image_titles = ['땀', '곰팡이', '쉰내', '장마철', '기름', '담배']

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('세탁 방법', 
             '\n\n\n\n- 뜨거운 물에 과탄산소다를 풀어준 상태로\n 30분 정도 담가둔 뒤 세탁\n'
             '\n\n- 옷감이 상할 수도 있으니 오랜 시간 담가\n 두지 않는 게 좋고 물빠짐 방지를 위해\n 색깔이 있는 옷과 흰 옷을 분류해서 진행'),

            ('세탁 방법', 
             '\n\n\n- 식초 활용: 물과 식초를 섞어 식초 용액을\n 만들고 곰팡이 냄새가 나는 옷을 식초 용액\n 에 1~2시간 담가둔 뒤 세탁\n'
             '\n\n- 베이킹 소다 활용: 베이킹 소다와 물을 섞어\n 만든 반죽을 천에 부드럽게 문지른 뒤 30분~\n1시간 방치 후 세탁'),

            ('세탁 방법', 
             '\n\n\n\n- 뜨거운 물에 과탄산소다를 풀어준 상태로\n 30분 정도 담가둔 뒤 세탁\n'
             '\n\n- 옷감이 상할 수도 있으니 오랜 시간 담가\n 두지 않는 게 좋고 물빠짐 방지를 위해\n 색깔이 있는 옷과 흰 옷을 분류해서 진행'),

            ('세탁 방법', 
             '\n\n\n- 젖은 빨래는 말려서 세탁\n'
             '\n- 식초 또는 과탄산소다를 넣고 세탁\n'
             '\n- 세탁이 끝나자마자 바로 건조대에 널기\n'
             '\n- 빨래 사이에 여유를 두어 널기'),

            ('세탁 방법', 
             '\n\n\n- 식초 활용: 물과 식초를 섞어 식초 용액을\n 만들고 곰팡이 냄새가 나는 옷을 식초 용액\n 에 1~2시간 담가둔 뒤 세탁\n'
             '\n\n- 베이킹 소다 활용: 베이킹 소다와 물을 섞어\n 만든 반죽을 천에 부드럽게 문지른 뒤 30분~\n 1시간 방치 후 세탁'),

            ('세탁 방법', 
             '\n\n\n- 녹차 활용: 먹고 남은 녹차 티백을 말려\n 두었다가 망사 주머니에 넣어 옷이나 옷장\n 안에 넣어두기\n'
             '\n\n- 숯 활용: 숯에 물을 뿌린 후 옷장에 넣어두기')
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

        self.image_title_label.setText(image_titles[index])
        self.image_title_label.show()

        self.additional_image_label.show()

        # 텍스트 라벨 갯수를 텍스트 갯수에 맞게 설정
        for i in range(len(self.text_labels)):
            self.text_labels[i].hide()

        required_text_labels = len(texts[index])
        while len(self.text_labels) < required_text_labels:
            text_label = QLabel(self)
            self.text_labels.append(text_label)

        text_sizes = [(750, 50), (560, 400)]
        text_fonts = [QFont('Arial', 25, QFont.Bold), QFont('Arial', 18)]

        for i, text in enumerate(texts[index]):
            self.text_labels[i].setText(text)
            self.text_labels[i].setFont(text_fonts[i])
            self.text_labels[i].setGeometry(text_positions[index][i][0], text_positions[index][i][1], text_sizes[i][0], text_sizes[i][1])
            self.text_labels[i].show()

        self.close_button.show()

    def closeDetails(self):
        self.image_label.hide()
        self.image_title_label.hide()
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
