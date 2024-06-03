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
        self.setWindowTitle('분리수거 미용')

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
        self.title_label = QLabel('미용', self)
        self.title_label.setGeometry(550, 50, 120, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['cosmetic.png', 'perfume.png', 'pump_cosmetic.png', 'stick_cosmetic.png', 'tube_cosmetic.png']
        texts = ['화장품', '향수', '펌프형', '스틱형', '튜브형']
        positions = [(200, 200), (500, 200), (800, 200), (500, 500), (200, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            button.setIcon(QIcon(f'cometic/{img}'))  # 이미지 파일 경로를 넣어주세요
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
            'cometic/cosmetic.png',
            'cometic/perfume.png',
            'cometic/pump_cosmetic.png',
            'cometic/stick_cosmetic.png',
            'cometic/tube_cosmetic.png'
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
            ['화장품', '처리 방법', '- 크림, 로션, 클렌징 오일, 파운데이\n션 등 유분이 있는 화장품은 키친타\n올 등으로 내용물을 최대한 제거하고\n, 공병을 깨끗이 세척한 후 재질별로\n분리 배출\n'
'- 알루미늄 튜브 용기의 화장품은 재\n활용이 가능하지만 의무대상이 아니\n라서 일반쓰레기로 버린다.\n\n'
'- 용기에 부착된 라벨은 떼어내서 일\n반쓰레기로 버린다.\n'],
            ['향수', '처리 방법', '- 향수가 남았다면 키친타올이나 신\n문지에 흡수시킨 뒤 일반쓰레기로 버\n린다.\n'
'- 본체(유리병)는 물로 내부를 깨끗이\n세척한 후 유리로 분리배출\n'
'- 펌프가 달린 뚜껑 부분은 해체가 가\n능하다면 헤드, 몸통, 스프링, 튜브(\n빨대)로 분리해서 스프링은 일반 쓰\n레기, 나머지는 플라스틱(또는 유리)\n으로 분리배출. 분해가 불가능하다면\n모두 일반쓰레기로 버린다.\n'],
            ['펌프형', '처리 방법', '- 용기 내에 남아있는 내용물은 키친\n타올이나 신문지로 닦거나 흡수시켜\n서 일반쓰레기로 버린다.\n'
'- 펌프가 달린 뚜껑 부분은 해체가 가\n능하다면 분리해서 스프링은 일반 쓰\n레기, 나머지는 플라스틱으로 분리\n배출. 분해가 불가능하다면 모두 일\n반쓰레기로 버린다.\n'
'- 본체(플라스틱 용기)는 물로 내부를\n깨끗이 세척한 후 플라스틱으로 분리\n배출\n'],
            ['스틱형', '처리 방법', '- 내용물(화장품)은 일반쓰레기로 버\n리고, 뚜껑과 용기(스틱)는 플라스틱\n등 재질에 맞게 분리 배출\n\n'
'- 틴트와 매니큐어는 남아있는 내용\n물을 키친타올 등에 흡수시켜서 최대\n한 제거한 후, 공병은 세척 후 플라스\n틱, 유리 등 재질별로 분리배출. 뚜껑\n은 솔 부분만 분리해서 일반쓰레기로\n버리고, 분리가 불가능하면 통째로\n일반쓰레기로 버린다.\n'],
            ['튜브형', '처리 방법', '- 용기 내에 남아있는 내용물은 물에\n 흘려보내지않고 키친타올로 흡수시\n켜서 일반쓰레기로 버린다.\n'
'- 플라스틱은 가위로 반을 잘라서 물\n로 내부를 완전히 세척한 후 플라스\n틱으로 분리배출\n'
'- 알루미늄은 재활용이 가능한 재질\n이더라도 재활용 의무대상이 아니라\n서 일반쓰레기로 버린다.\n'
'- 뚜껑과 튜브 본체는 다른 재질이므\n로 분리해서 배출\n']
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
