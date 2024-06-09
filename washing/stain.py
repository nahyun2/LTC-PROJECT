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
        self.stain_path = os.path.join(self.base_path, "stain")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('얼룩_세탁')

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
        self.title_label = QLabel('얼룩', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['sweat.png', 'pen.png', 'makeup.png', 'drink.png', 'blood.png', 'perfume.png']
        texts = ['땀', '볼펜', '화장품', '음료', '피', '향수']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.stain_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.stain_path, img)}")
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
            os.path.join(self.stain_path, 'sweat.png'),
            os.path.join(self.stain_path, 'pen.png'),
            os.path.join(self.stain_path, 'makeup.png'),
            os.path.join(self.stain_path, 'drink.png'),
            os.path.join(self.stain_path, 'blood.png'),
            os.path.join(self.stain_path, 'perfume.png')
        ]

        image_titles = ['땀', '볼펜', '화장품', '음료', '피', '향수']  # 추가된 부분

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('세탁 방법', 
             '\n\n\n- 얼룩진 부위에 레몬즙을 발라준 후 두 시간\n 정도 뒤에 세탁\n'
             '\n\n- 레몬즙이 없다면 백식초 125ml를 물 1L에\n 희석한 후 옷을 40분간 담갔다가 헹궈주기'),

            ('세탁 방법', 
             '\n\n\n- 얼룩진 부위에 물파스를 충분히 바른 후\n 미온수로 헹구기\n'
             '\n- 오염된 옷 뒤에 휴지, 수건 등을 대고\n 물파스를 두드려야 볼펜 잉크가 묻어나지 \n 않음\n'
             '\n- 물파스 대신 알코올을 적신 천으로 해당\n 부위를 닦아내도 됨'),

            ('세탁 방법', 
             '\n\n\n- 파운데이션 얼룩: 알코올이 함유된 스킨을\n 적셔 얼룩 부위를 문지른 후, 젖은 수건으로\n 두드려주기\n'
             '\n\n- 립스틱 얼룩: 클렌징 오일과 폼클렌징을\n 이용'),

            ('세탁 방법', 
             '\n\n\n- 커피, 녹차: 식초, 베이킹소다를 활용\n'
             '- 물과 베이킹소다를 1:2 비율로 섞어 얼룩\n 부분에 적시고 그 위에 식초를 뿌린 뒤\n 따뜻한 물로 가볍게 문질러 빨면 얼룩이\n 제거됨\n'
             '\n\n- 과일주스, 탄산음료: 소금물에 옷을 담근 뒤\n 세탁\n'
             '- 소금의 염소 성분의 표백효과로 얼룩 제거\n 에 도움을 줌'),

             ('세탁 방법', 
             '\n\n\n\n- 얼룩진 부위에 과산화수소를 두 세 방울\n 떨어뜨려 세탁'
             '\n\n\n- 따뜻한 물로 세척하면 혈액 속 단백질이\n 응고되어 얼룩이 잘 지워지지 않으니 차가운\n 물을 사용해 세탁\n'
             '\n\n- 얼룩이 심하면 산소계 표백제를 사용'),


            ('세탁 방법', 
             '\n\n\n- 헝겊에 과산화수소를 묻혀 얼룩 부분의\n 양면에 대고 눌러주면 얼룩이 사라짐')
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
