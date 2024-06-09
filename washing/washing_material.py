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
        self.material_path = os.path.join(self.base_path, "material")

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 820)
        self.setWindowTitle('소재_세탁')

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
        self.title_label = QLabel('소재', self)
        self.title_label.setGeometry(550, 50, 100, 50)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # 이미지가 들어간 버튼 및 라벨 추가
        self.buttons = []
        self.labels = []

        images = ['cotton.png', 'poly.png', 'denim.png', 'linen.png', 'knit.png', 'wool.png']
        texts = ['면', '폴리', '데님', '린넨', '니트', '울']
        positions = [(200, 200), (500, 200), (800, 200), (200, 500), (500, 500), (800, 500)]

        for i, (img, text, pos) in enumerate(zip(images, texts, positions)):
            button = QPushButton(self)
            button.setGeometry(pos[0], pos[1], 225, 225)
            icon = QIcon(os.path.join(self.material_path, img))
            if icon.isNull():
                print(f"Failed to load {os.path.join(self.material_path, img)}")
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
            os.path.join(self.material_path, 'cotton.png'),
            os.path.join(self.material_path, 'poly.png'),
            os.path.join(self.material_path, 'denim.png'),
            os.path.join(self.material_path, 'linen.png'),
            os.path.join(self.material_path, 'knit.png'),
            os.path.join(self.material_path, 'wool.png')
        ]

        image_titles = ['면', '폴리', '데님', '린넨', '니트', '울']

        image_sizes = [(400, 400), (400, 400), (400, 400), (400, 400), (400, 400), (400, 400)]

        texts = [
            ('세탁 방법', 
             '\n\n\n- 단독 손세탁\n'
             '\n- 차가운 물세탁\n'
             '\n- 중성세제를 사용\n'
             '\n- 짙은 색상의 경우 장시간 세제에 담글 경우,\n 물빠짐이 있을 수 있으니 주의'),

            ('세탁 방법', 
             '\n\n\n- 단독 손세탁\n'
             '\n- 미온수 세탁\n'
             '\n- 중성세제를 사용\n'
             '\n- 물세탁은 가능하지만 높은 온도에 약한\n 소재이므로 삶거나 높은 온도에서 다리면\n 안 됨'),

            ('세탁 방법', 
             '\n\n\n- 단독 손세탁\n'
             '\n- 드라이크리닝\n'
             '\n- 그늘에 건조\n'
             '\n- 물빠짐이 쉬운 소재로 첫 세탁은 드라이\n 크리닝을 권장\n'
             '\n- 다른 옷과 함께 세탁시 이염될 수 있으니\n 주의'),

            ('세탁 방법', 
             '\n\n\n- 드라이크리닝\n'
             '\n\n- 소재 특성상 세탁 후 옷감이 손상되거나\n 변형이 있을 수 있으니 드라이크리닝을\n 권장'),

            ('세탁 방법', 
             '\n\n\n- 드라이크리닝\n'
             '\n\n- 높은 온도에 약한 소재로 옷감이 줄어들거\n 나 틀어질 가능성이 많으므로 드라이크리닝\n 을 권장'),

            ('세탁 방법', 
             '\n\n\n- 드라이크리닝\n'
             '\n\n- 약한 소재이기 때문에 물에 닿으면 변형이\n 생길 수 있으니 주의')
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
