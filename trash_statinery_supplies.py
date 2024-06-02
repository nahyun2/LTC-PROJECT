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
        self.setWindowTitle('분리수거 문구')

        # 배경 이미지 추가
        self.label = QLabel(self)
        self.pixmap = QPixmap('background.png')  # 이미지 파일 경로를 넣어주세요
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(0, 0, 1200, 820)  # 이미지 크기와 윈도우 크기를 동일하게 설정합니다.

        # 폰트 설정
        font = QFont()
        font.setPointSize(16)
        
        title_font = QFont()
        title_font.setPointSize(30)
         
        # 라벨 추가
        self.title_label = QLabel('문구', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['cutter_knife.png', 'notebook.png', 'paper.png', 'pen.png', 'stapler.png']
        texts = ['커터칼', '노트', '일반종이', '필기구', '스테이플러']
        positions = [(200, 200), (500, 200), (800, 200), (500, 500), (200, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            button.setIcon(QIcon(f'statinery_supplies/{img}'))  # 이미지 파일 경로를 넣어주세요
            button.setIconSize(button.size())           
            button.clicked.connect(lambda _, x=i: self.showDetails(x))
            self.buttons.append(button)
            
            label = QLabel(text, self)
            label.setGeometry(pos[0], pos[1] + 230, 225, 50)
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
            'statinery_supplies/cutter_knife.png',
            'statinery_supplies/notebook.png',
            'statinery_supplies/paper.png',
            'statinery_supplies/pen.png',
            'statinery_supplies/stapler.png'
        ]

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]
        text_positions = [
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)]

        ]
        text_fonts = [18]

        texts = [
            ['커터칼', '처리 방법', '- 커터칼이나 칼날 등은 고철류에 해\n당되지만 재활용 업체의 수거, 선별\n과정에서 사람이 다칠 위험이 있기\n때문에 캔류가 아닌 일반쓰레기로 분\n류\n\n'
'- 커터칼을 신문지 등으로 밀봉해서\n버린다. 칼날만 따로 버려야 한다면\n여러겹의 종이로 싸고 테이프로 단단\n히 고정해서 종량제봉투에 버린다.\n'],
            ['노트', '처리 방법', '- 물이나 이물질을 묻지 않게 하고 구\n겨지지 않게 배출\n\n'
'- 양장본 책은 겉표지(일반쓰레기)와\n속지(종이)를 분리해서 배출\n\n'
'- 노트나 제본된 종이를 묶는 스프링\n(플라스틱 또는 고철)은 분리해서 배\n출\n'
'- 잡지는 비닐 코팅된 겉표지(일반쓰\n레기)와 속지(종이)를 분리해서 배출\n'],
            ['일반종이', '처리 방법', '- 물이나 이물질을 묻지 않게 하고 구\n겨지지 않게 배출\n\n'
'- 고지서는 주소, 이름 등의 개인정보\n가 인쇄된 부분은 잘라서 일반쓰레기\n로 버리고 나머지는 종이로 배출\n\n'
'- 끈끈이가 묻어있는 포스트잇은 그\n대로 배출\n'
'-  종이와 종이팩은 다른 방식으로 재\n활용되므로 반드시 종이팩이 아닌 종\n이로 분리 배출\n'],
            ['필기구', '처리 방법', '- 볼펜 등의 플라스틱 필기구는 부피\n가 작고, 고무 손 잡이, 쇠 스프링 등\n다른 재질이 혼합되어 있어서 재활용\n이 불가능하기 때문에 모두 일반쓰레\n기로 버린다.\n'],
            ['스테이플러', '처리 방법', '- 스테이플러는 고철, 플라스틱, 고무\n등 여러 재질이 섞인 경우가 대부분\n이라 통째로 일반쓰레기로 버린다.\n\n'
'- 스테이플러 심은 모아서 투명 비닐\n봉지에 담아 캔류로 배출. 매우 소량\n이거나 낱개로 배출해야 한다면 일반\n쓰레기로 버린다.\n']
        ]

        self.image_label.setPixmap(QPixmap(image_paths[index]).scaled(image_sizes[index][0], image_sizes[index][1], Qt.KeepAspectRatio))
        self.image_label.setGeometry(100, 270, image_sizes[index][0], image_sizes[index][1])
        self.image_label.show()

        self.additional_image_label.setPixmap(QPixmap('memo.png'))
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
