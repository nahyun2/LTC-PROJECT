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
        self.setWindowTitle('분리수거 생활용품')

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
        self.title_label = QLabel('생활용품', self)
        self.title_label.setGeometry(500, 50, 250, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['battery.png', 'hot_pack.png', 'lighter.png', 'mask.png', 'moisture.png', 'umbrella.png', 'wet_tissue.png']
        texts = ['배터리', '핫팩', '라이터', '마스크', '습기제거제', '우산', '물티슈']
        positions = [(50, 200), (350, 200), (650, 200), (950, 200), (50, 500), (350, 500), (650, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 210, 210)
            button.setIcon(QIcon(f'daily_necessities/{img}'))  # 이미지 파일 경로를 넣어주세요
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
            'daily_necessities/battery.png',
            'daily_necessities/hot_pack.png',
            'daily_necessities/lighter.png',
            'daily_necessities/mask.png',
            'daily_necessities/moisture.png',
            'daily_necessities/umbrella.png',
            'daily_necessities/wet_tissue.png'
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
            ['배터리', '처리 방법', '- 다 쓴 건전지는 반드시 가까운 주민\n센터, 구청 또는 아파트 단지 내에 설\n치된 폐건전지 전용 수거함에 버린다.\n\n'
'- 만약 가까운 곳에 폐건전지 수거함\n이 없다면 박스 등 한곳에 모아두었\n다가 양이 많아지면 한번에 버린다.\n'],
            ['핫팩', '처리 방법', '- 핫팩 내부의 철가루와 포장재(부직\n포)는 모두 재활 용이 불가능하기 때\n문에 통째로 일반쓰레기(종량제봉투\n)로 버린다.\n'],
            ['라이터', '처리 방법', '- 일회용 라이터, 가스 라이터, 기름\n라이터는 모두 플라스틱, 알루미늄\n등이 뒤섞인 복합재질 제품이고, 재\n질별로 분리하더라도 조각이 작아 재\n활용이 어려워 일반쓰레기(종량제봉\n투)로 버린다.\n\n'
'- 라이터 내부에 가스가 많이 남아있\n다면 최대한 소진한 후 버린다.\n'],
            ['마스크', '처리 방법', '- 마스크는 종류와 상관없이 모두 일\n반쓰레기(종량제 봉투)로 버린다.\n\n'
'- 버릴 때는 마스크의 오염된 겉면이\n손에 닿지 않도록 마스크 안쪽에서부\n터 반으로 접은 후 종량제 봉투에 넣\n는다.\n\n'
'- 사용한 면 마스크도 반드시 일반쓰\n레기로 버린다.\n'],
            ['습기제거제', '처리 방법', '- 습기제거제의 용기 내부 표시선의\n높이까지 찬 물은 뚜껑을 열고 봉해\n져있는 흡습지를 뜯어낸 다음, 물은\n하수구에 버리고 뚜껑과 용기는 플라\n스틱으로 배출\n\n'
'- 염화칼슘 성분의 하얀색 내부충진\n재는 분리해서 일반쓰레기(종량제봉\n투)로 버린다.\n'],
            ['우산', '처리 방법', '- 우산은 플라스틱, 알루미늄, 합성섬\n유 등 여러 재질이 섞여있어 재활용\n이 불가능하니 통째로 일반쓰레기\n(종량제봉투)로 버린다.\n\n'
'- 크기가 커서 종량제봉투에 담을 수\n없는 우산은 주민 센터, 시/군/구청을\n통해 대형생활폐기물로 신고/배출\n'],
            ['물티슈', '처리 방법', '- 사용한 물티슈는 반드시 일반쓰레\n기(종량제봉투)로 버린다.\n\n'
'- 물티슈를 다 뽑아쓴 물티슈 포장재\n는 플라스틱 캡 등 다른 재질을 비닐\n포장재에서 떼어낸 후 재질별로 분리\n배출\n']
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
