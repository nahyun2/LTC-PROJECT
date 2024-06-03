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
        self.setWindowTitle('분리수거 욕실용품')

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
        self.title_label = QLabel('욕실용품', self)
        self.title_label.setGeometry(500, 50, 250, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['cleaning_brush.png', 'pump.png', 'tissue.png', 'tooth_brush.png', 'tooth_paste.png', 'towel.png']  # 새 이미지 파일명 추가
        texts = ['청소 솔', '펌프 용기', '휴지', '칫솔', '치약', '수건']  # 새 품목 텍스트 추가
        positions = [(150, 200), (450, 200), (750, 200), (150, 500), (450, 500), (750, 500)]  # 버튼 위치 조정

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 215, 215)
            button.setIcon(QIcon(f'bathroom_ware/{img}'))  # 이미지 파일 경로를 넣어주세요
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
            'bathroom_ware/cleaning_brush.png',
            'bathroom_ware/pump.png',
            'bathroom_ware/tissue.png',
            'bathroom_ware/tooth_brush.png',
            'bathroom_ware/tooth_paste.png',
            'bathroom_ware/towel.png'
        ]

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]
        text_positions = [
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)],
            [(250, 700), (620, 210), (620, 290)]  # 새 품목 텍스트 위치 추가
        ]
        text_fonts = [18]

        texts = [
            ['청소 솔', '처리 방법', '- 청소 솔은 솔과 플라스틱 손잡이를\n분리할 수 있고, 손잡이에 고무 등 다\n른 재질이 붙어있지 않은 경우만 플\n라스틱으로 분리배출\n\n'
'- 솔과 손잡이를 분리할 수 없고, 다\n른 재질이 혼합되어 있으면 모두 일\n반쓰레기로 버린다.\n'],
            ['펌프 용기', '처리 방법', '- 내부를 물로 깨끗이 헹군 뒤 배출\n'
'- 뚜껑 부분은 해체가 가능하다면 헤\n드, 몸통, 스프링, 튜브(빨대)로 분리\n해서 스프링은 일반 쓰레기, 나머지\n는 플라스틱으로 분리배출. 분해\n불가능하다면 뚜껑 부분 통째로 일반\n쓰레기로 버린다.\n'
'- 본체(플라스틱 용기)는 플라스틱으\n로 분리배출\n'
'- 라벨 스티커는 떼어내서 일반쓰레\n기로 버린다.\n'],
            ['휴지', '처리 방법', '- 화장실에서 주로 사용하는 두루마\n리 휴지는 화장실 변기에 버린다. 변\n기에 버리지 않을 경우엔 일반쓰레기\n로 버린다.\n\n'
'- 휴지심은 종이로 분리 배출\n'],
            ['칫솔', '처리 방법', '- 칫솔은 부피가 작고, 칫솔모, 고무\n손잡이 등 다른 재질이 혼합되어 있\n어서 모두 일반쓰레기로 버린다.\n'],
            ['치약', '처리 방법', '- 플라스틱 튜브 형태의 용기는 가위\n로 반을 잘라서 물로 내부를 완전히\n세척한 후 플라스틱으로 분리 배출\n\n'
'- 알루미늄 튜브 용기는 재활용 의무\n대상이 아니라서 일반쓰레기로 버린\n다.\n\n'
'- 뚜껑과 튜브 본체는 다른 재질이므\n로 분리 배출\n'],
            ['수건', '처리 방법', '- 낡은 수건은 일반쓰레기로 버린다.\n\n'
'- 새 수건도 재활용이 불가능하니 일\n반쓰레기로 버린다.\n\n'
'- 수건은 의류수거함 배출 품목이 아\n니므로 의류수거함으로 배출 불가능\n']
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

        text_sizes = [(750, 50), (750, 50), (450, 450), (750, 50), (750, 100), (750, 100)]  # 각 텍스트 라벨의 크기 지정
        text_fonts = [QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 14), QFont('Arial', 18), QFont('Arial', 18), QFont('Arial', 18)]  # 각 텍스트 라벨의 폰트 지정

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
