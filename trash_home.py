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
        self.setWindowTitle('분리수거 가전제품')

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
        self.title_label = QLabel('가전제품', self)
        self.title_label.setGeometry(500, 50, 250, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['charger.png', 'consent.png', 'earphone.png', 'heating_pad.png', 'laptop.png', 'mouse.png', 'phone_battery.png']
        texts = ['충전기', '멀티탭', '이어폰', '전기장판', '노트북', '마우스', '보조배터리']
        positions = [(50, 200), (350, 200), (650, 200), (950, 200), (50, 500), (350, 500), (650, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 210, 210)
            button.setIcon(QIcon(f'home_appliances/{img}'))  # 이미지 파일 경로를 넣어주세요
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
            'home_appliances/charger.png',
            'home_appliances/consent.png',
            'home_appliances/earphone.png',
            'home_appliances/heating_pad.png',
            'home_appliances/laptop.png',
            'home_appliances/mouse.png',
            'home_appliances/phone_battery.png'
        ]
        
        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]
        text_positions = [
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)]
        ]

        texts = [
            ['충전기', '처리 방법', '- 한국전자제품자원 순환공제조합에\n서 운영하는 폐휴대폰 수거서비스를\n이용해서 배출 가능해 착불택배로 수\n도권 자원순환센터로 보낸다.\n'
'- 가까운 주민센터 등 지자체에 비치\n된 소형 폐가전 전용 수거함으로 배\n출도 가능\n'
'- 휴대폰 세트(휴대폰, 충전기, 케이\n블)와 함께 5개 이상의 소형 가전제\n품을 한번에 버릴 경우 폐가전 무상\n방문수거 서비스 이용 가능\n'],
            ['멀티탭', '처리 방법', '- 멀티탭은 재활용 가치가 높은 구리\n등의 유가 금속이 포함되어 있지만\n아직까지 명확한 분리배출 지침이나\n수거 시스템이 없어 일반쓰레기(종량\n제봉투)로 분류\n\n'
'- 가까운 주민센터 등 지자체에 비치\n된 소형 폐가전 전용 수거함으로 배\n출도 가능\n'],
            ['이어폰', '처리 방법', '- 이어폰에는 구리 등 재활용 가치가\n있는 유가 금속이 포함되어 있지만\n아직까지 명확한 분리배출 지침이나\n수거 시스템이 없어 일반쓰레기(종량\n제봉투)로 분류\n\n'
'- 가까운 주민센터 등 지자체에 비치\n된 소형 폐가전 전용 수거함으로 배\n출도 가능\n'],
            ['전기장판', '처리 방법', '- 전기장판은 복합재질로 구성되어\n있어서 재활용이 불가능하고 보통 종\n량제봉투에 담을 수 없는 크기이므로\n대형 생활 폐기물로 신고 배출\n'],
            ['노트북', '처리 방법', '- 노트북을 포함해 5개 이상의 소형\n가전제품을 한번에 배출시, 폐가전\n무상방문수거 서비스 이용 가능\n\n'
'- 또는 노트북 수거/매입 업체를 통해\n 버릴 수 있다.\n\n' 
'- 대형 생활 폐기물처럼 유료로 폐기\n물 스티커를 발급 받아 버릴 수도 있\n다. \n'],
            ['마우스', '처리 방법', '- 마우스는 폐가전 무상방문수거 서\n비스를 통해 컴퓨터를 배출할 때 함\n께 배출할 수 있다.\n\n'
'- 컴퓨터 외의 대형 가전제품이나 소\n형 가전제품을 5개 이상 배출할 때도\n폐가전 무상방문수거 서비스 이용 가\n능\n'
'- 당장 버려야 한다면 일반쓰레기(종\n량제봉투)로 버린다.\n'],
            ['보조배터리', '처리 방법', '- 성능이 다한 보조배터리는 반드시\n가까운 주민센터, 구청 또는 아파트\n단지 내에 설치된 폐건전지 전용 수\n거함에 버린다.\n\n'
'- 만약 가까운 곳에 폐건전지 수거함\n이 없다면 박스 등 한곳에 건전지와\n함께 모아두었다가 양이 많아지면 한\n번에 버린다.\n']
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

        text_sizes = [(750, 50), (750, 50), (450, 450), (750, 50), (750, 100), (750, 50), (750, 50)]  # 각 텍스트 라벨의 크기 지정
        text_fonts = [QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 14), QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 18)]  # 각 텍스트 라벨의 폰트 지정

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
