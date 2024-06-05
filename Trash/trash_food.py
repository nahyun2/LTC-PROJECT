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
        self.food_path = os.path.join(self.base_path, "food")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('분리수거_음식')

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
        self.title_label = QLabel('음식', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['bone.png', 'eggshell.png', 'oil.png', 'peel.png', 'seed.png', 'pill.png']
        texts = ['동물 뼈', '달걀 껍질', '기름', '과일 껍질', '과일 씨', '약']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.food_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.food_path, img)}")
            button.setIcon(icon)
            button.setIconSize(button.size())
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

        self.close_button = QPushButton('닫기', self)
        self.close_button.setGeometry(1050, 700, 100, 50)
        self.close_button.hide()
        self.close_button.clicked.connect(self.closeDetails)

        # 메인 화면 버튼 및 이전 화면 버튼 추가
        self.main_button = QPushButton('메인 화면', self)
        self.main_button.setGeometry(50, 50, 120, 50)
        
        self.previous_button = QPushButton('이전 화면', self)
        self.previous_button.setGeometry(200, 50, 120, 50)
        
        self.show()

    def showDetails(self, index):
        for button in self.buttons:
            button.hide()
        for label in self.labels:
            label.hide()
        self.title_label.hide()
        self.main_button.hide()
        self.previous_button.hide()

        image_paths = [
            os.path.join(self.food_path, 'bone.png'),
            os.path.join(self.food_path, 'eggshell.png'),
            os.path.join(self.food_path, 'oil.png'),
            os.path.join(self.food_path, 'peel.png'),
            os.path.join(self.food_path, 'seed.png'),
            os.path.join(self.food_path, 'pill.png')
        ]

        image_titles = ['동물 뼈', '달걀 껍질', '기름', '과일 껍질', '과일 씨', '약']  # 추가된 부분

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('처리 방법', 
             '\n\n\n\n- 닭고기, 소고기, 돼지고기, 생선 등을 먹고\n 남은 뼈는 일반쓰레기(종량제봉투)로 배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 달걀의 단단한 껍질은 일반쓰레기\n (종량제봉투)에 배출\n'),

            ('처리 방법', 
             '\n\n\n\n- 폐식용유 수거함이 있다면 이물질이 섞이지\n 않게 잘 모아서 배출\n'
             '\n- 수거함이 없으면 식용유와 기름은 모두\n 일반쓰레기(종량제봉투)로 배출\n'
             '\n- 기름의 양이 적다면 키친타올에 기름을\n 흡수시켜서, 양이 많다면 통에 신문지를\n 구겨넣고 기름을 부은 뒤 완전히 흡수되면\n 일반쓰레기로 배출\n'),

            ('처리 방법', 
             '\n\n\n- 일반적으로 쉽게 분해되는 부드러운 과일\n 껍질은 음식물 쓰레기: 사과, 배, 포도, 키위\n'
             '\n- 단단한 과일 껍질은 일반쓰레기\n (종량제봉투): 오렌지, 바나나, 파인애플,\n 수박\n'),

            ('처리 방법', 
             '\n\n\n\n- 크고 단단한 과일 씨는 일반쓰레기\n(종량제봉투): 아보카도, 자두, 복숭아, 살구,\n 감\n'
             '\n- 크기가 작고 강도가 낮은 과일 씨는 음식물\n 쓰레기: 사과, 배\n'),

            ('처리 방법', 
             '\n\n\n\n- 약과 영양제는 종류에 상관없이 가까운\n 약국, 보건소, 보건진료소 등에 비치된\n 폐의약품 수거함에 배출\n'
             '\n - 약 봉지, 플라스틱 알약 포장재, 연고(튜브),\n 물약, 안약, 영양제통 등은 그대로 폐의약품\n 수거함으로 배출\n')
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
