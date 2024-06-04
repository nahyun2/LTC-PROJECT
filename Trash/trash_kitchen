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
        self.kitchen_path = os.path.join(self.base_path, "kitchen")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('분리수거_주방')

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
        self.title_label = QLabel('주방', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['pot.png', 'scissors.png', 'gloves.png', 'bowl.png', 'tableware.png', 'knife.png']
        texts = ['냄비', '가위', '장갑', '그릇', '식기', '식칼']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.kitchen_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.kitchen_path, img)}")
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
            os.path.join(self.kitchen_path, 'pot.png'),
            os.path.join(self.kitchen_path, 'scissors.png'),
            os.path.join(self.kitchen_path, 'gloves.png'),
            os.path.join(self.kitchen_path, 'bowl.png'),
            os.path.join(self.kitchen_path, 'tableware.png'),
            os.path.join(self.kitchen_path, 'knife.png')
        ]

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('처리 방법\n- 음식물이나 이물질이 묻어있지 않게 깨끗이 세척한 후 배출\n'
             '- 유리 뚜껑/플라스틱 손잡이 등 분리할 수 있는 다른 재질이 있으면\n'
             '떼어낸 후 재질별로 분리 배출, 따로 떼어낼 수 없으면 그대로 배출\n'
             '- 캔류의 수거 장소가 종류에 따라 나뉘어져 있으면 캔류(철)로 분리배출하고,\n'
             '그렇지 않으면 다른 고철들과 함께 캔류로 분리배출'),

            ('처리 방법\n- 가위는 고철류지만 재활용 업체의 수거 과정에서 사람이 다칠 위험이\n'
             '있기 때문에 고철이 아닌 일반쓰레기(종량제봉투)로 분류\n'
             '- 가위의 날카로운 날이 종량제봉투를 찢고 나오는 등 사고가 일어나지 않도록\n'
             '가위를 신문지로 여러 겹 싸고 테이프로 단단히 고정해서 종량제봉투에 배출'),

            ('처리 방법\n- 고무장갑, 라텍스장갑, 니트릴장갑 등 고무 재질은 재활용이 어려워서\n'
             '분리수거되지 않으니 모두 일반쓰레기(종량제봉투)로 배출\n'
             '- 천연고무는 재활용이 가능하나 우리가 사용하는 대부분의 고무 제품은\n'
             '합성 고무 제품으로 재활용이 불가능'),

            ('처리 방법\n- 사기그릇이나 유리그릇은 재활용이 불가능하고 불에 타지 않는\n'
             '쓰레기이므로 불연성 쓰레기 봉투(마대)에 배출\n'
             '- 플라스틱 그릇은 깨끗이 세척 후 플라스틱으로 분리배출\n'
             '- 유기그릇(방짜 유기, 스테인리스, 놋그릇 등)도 재활용이 가능하니\n'
             '깨끗이 씻어서 캔류 (고철)로 분리배출'),

            ('처리 방법\n- 깨끗이 씻어 캔류(철)로 분리배출\n'
             '- 나무, 플라스틱 손잡이 등 다른 재질을 분리할 수 있는 경우 떼어낸 후\n'
             '각각의 재질별로 분리배출, 분리가 어려우면 그대로 배출\n'
             '- 나무젓가락 등 나무 재질의 식사 도구는 일반쓰레기(종량제봉투)\n'
             '- 일회용 플라스틱 숟가락, 포크, 나이프는 플라스틱으로 분리배출'),

            ('처리 방법\n- 고철류지만 재활용 업체의 수거 과정에서 다칠 위험이 있기 때문에\n'
             '고철이 아닌 일반쓰레기(종량제봉투)로 배출\n'
             '- 날카로운 칼날이 종량제봉투를 찢고 나오는 등의 사고가 일어나지 않도록\n'
             '칼을 신문지로 여러 겹 싸고 테이프로 단단히 고정해서 종량제봉투 배출')
        ]

        self.image_label.setPixmap(QPixmap(image_paths[index]).scaled(image_sizes[index][0], image_sizes[index][1], Qt.KeepAspectRatio))
        if self.image_label.pixmap().isNull():
            print(f"Failed to load {image_paths[index]}")
        self.image_label.setGeometry(100, 270, image_sizes[index][0], image_sizes[index][1])
        self.image_label.show()

        self.additional_image_label.show()

        # 텍스트 라벨 갯수를 텍스트 갯수에 맞게 설정
        for label in self.text_labels:
            label.hide()
        
        self.text_labels = []

        text = texts[index]
        text_label = QLabel(text, self)
        text_label.setFont(QFont('Arial', 14, QFont.Bold))
        text_label.setGeometry(560, 200, 560, 400)  # 크기와 위치 조정
        text_label.setWordWrap(True)
        text_label.show()
        self.text_labels.append(text_label)

        # 선택한 아이템의 이름을 왼쪽 아래에 표시
        self.item_label.setText(self.labels[index].text())
        self.item_label.show()

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
        self.item_label.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageBackgroundApp()
    sys.exit(app.exec_())
