import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt

class ImageBackgroundApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('분리수거_가구')

        # 배경 이미지 추가
        self.label = QLabel(self)
        self.pixmap = QPixmap('배경.png')  # 이미지 파일 경로를 넣어주세요
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(0, 0, 1200, 820)  # 이미지 크기와 윈도우 크기를 동일하게 설정합니다.

        # 폰트 설정
        font = QFont()
        font.setPointSize(18)
        
        title_font = QFont()
        title_font.setPointSize(30)
         
        # 라벨 추가
        self.title_label = QLabel('가구', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['거울.png', '방석.png', '베개.png', '의자.png', '이불.png']
        texts = ['거울', '방석', '베개', '의자', '이불']
        positions = [(200, 200), (500, 200), (800, 200), (500, 500), (200, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 250, 250)
            button.setIcon(QIcon(f'C:/Users/chlsk/Desktop/opensw project/가구/{img}'))  # 이미지 파일 경로를 넣어주세요
            button.setIconSize(QPixmap(f'C:/Users/chlsk/Desktop/opensw project/가구/{img}').size())
            button.clicked.connect(lambda _, x=i: self.showDetails(x))
            self.buttons.append(button)
            
            label = QLabel(text, self)
            label.setGeometry(pos[0], pos[1] + 255, 250, 50)
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            self.labels.append(label)

        # 숨겨질 라벨 및 버튼들
        self.image_label = QLabel(self)
        self.image_label.hide()

        self.additional_image_label = QLabel(self)
        self.additional_image_label.hide()

        self.text_labels = []

        self.close_button = QPushButton('닫기', self)
        self.close_button.setGeometry(1050, 700, 100, 50)
        self.close_button.hide()
        self.close_button.clicked.connect(self.closeDetails)

        # 메인 화면 버튼 및 이전 화면 버튼 추가
        self.main_button = QPushButton('메인 화면', self)
        self.main_button.setGeometry(50, 50, 150, 50)
        
        self.previous_button = QPushButton('이전 화면', self)
        self.previous_button.setGeometry(250, 50, 150, 50)
        
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
            'C:/Users/chlsk/Desktop/opensw project/가구/거울.png',
            'C:/Users/chlsk/Desktop/opensw project/가구/방석.png',
            'C:/Users/chlsk/Desktop/opensw project/가구/베개.png',
            'C:/Users/chlsk/Desktop/opensw project/가구/의자.png',
            'C:/Users/chlsk/Desktop/opensw project/가구/이불.png'
        ]

        image_sizes = [(500, 500), (500, 500), (500, 500), (500, 500), (500, 500)]
        text_positions = [
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)]

        ]
        text_fonts = [18]

        texts = [
            ['거울', '처리 방법', '- 거울은 불에 타지 않아 크기에 따라 불연성 쓰레기\n와 대형 생활 폐기물로 구분해 신고\n배출\n'
'- 불연성 쓰레기 봉투(마대): 손거울\n등 불연성 쓰레기 봉투에 담을 수 있\n는 크기의 거울/ 지역 내 마트, 주민\n센터, 철물점 등에서 구매 가능\n'
'- 대형 생활 폐기물: 전신 거울, 벽면\n거울 등 대형 거울/ 주민센터, 구청\n등 지자체에 신고 후 폐기물 스티거\n를 부착해 집 밖에 두면 1~2일 내에\n수거됨\n\n'],
            ['방석', '처리 방법', '- 방석은 재활용이 불가능해 종류와\n상관없이 모두 일반쓰레기(종량제봉\n투)로 버림\n\n'
'- 부피가 크거나 양이 많은 경우에는\n주민센터, 구청 등의 지자체를 통해\n대형생활폐기물로 신고/배출\n\n'
'- 방석은 의류수거함 해당 품목이 아\n니므로 의류수거함으로 배출 X\n'],
            ['베개', '처리 방법', '- 베개류는 재활용이 불가능해 종류\n와 상관없이 모두 일반쓰레기(종량제\n봉투)로 버림\n\n'
'- 양이 많아서 일반쓰레기로 버리기\n어렵다면 대형 생활 폐기물로 신고\n배출\n'],
            ['의자', '처리 방법', '- 의자는 다양한 재질이 혼합돼서 제\n작되어 재질별로 분리배출하기는 매\n우 어려우므로 대형 생활 폐기물로\n신고 배출\n'],
            ['이불', '처리 방법', '- 홑이불, 담요, 누빔이불 등 부피가\n작은 침구류는 의류수거함에 넣거나\n일반쓰레기(종량제봉투)로 버림\n\n'
'- 솜이불, 오리털이불, 베개 등 부피\n가 큰 침구류는 잘라서 일반쓰레기\n(종량제봉투)로 버리거나 대형 생활\n폐기물로 신고 배출\n']
        ]

        self.image_label.setPixmap(QPixmap(image_paths[index]).scaled(image_sizes[index][0], image_sizes[index][1], Qt.KeepAspectRatio))
        self.image_label.setGeometry(50, 200, image_sizes[index][0], image_sizes[index][1])
        self.image_label.show()

        self.additional_image_label.setPixmap(QPixmap('C:/Users/chlsk/Desktop/opensw project/memo.png'))
        self.additional_image_label.setGeometry(540, 170, 600, 600)
        self.additional_image_label.show()

        # 텍스트 라벨 갯수를 텍스트 갯수에 맞게 설정
        for i in range(len(self.text_labels)):
            self.text_labels[i].hide()

        required_text_labels = len(texts[index])
        while len(self.text_labels) < required_text_labels:
            text_label = QLabel(self)
            self.text_labels.append(text_label)

        text_sizes = [(750, 50), (750, 50), (450, 450), (750, 50), (750, 100)]  # 각 텍스트 라벨의 크기 지정
        text_fonts = [QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 14), QFont('Arial', 18), QFont('Arial', 18)]  # 각 텍스트 라벨의 폰트 지정

        for i, text in enumerate(texts[index]):
            self.text_labels[i].setText(text)
            self.text_labels[i].setFont(text_fonts[i])  # 폰트 지정
            self.text_labels[i].setGeometry(text_positions[index][i][0], text_positions[index][i][1], text_sizes[i][0], text_sizes[i][1])  # 크기와 위치 조정
            self.text_labels[i].show()


        self.close_button.show()

    def closeDetails(self):
        self.image_label.hide()
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
