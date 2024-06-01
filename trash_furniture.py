import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont

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
        title_label = QLabel('가구', self)
        title_label.setGeometry(575, 50, 100, 50)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)


        # 이미지가 들어간 버튼 및 라벨 추가
        button1 = QPushButton(self)
        button1.setGeometry(200, 200, 250, 250)
        button1.setIcon(QIcon('C:/Users/chlsk/Desktop/opensw project/가구/거울.png'))  # 이미지 파일 경로를 넣어주세요
        button1.setIconSize(QPixmap('C:/Users/chlsk/Desktop/opensw project/가구/거울.png').size())
        
        label1 = QLabel('거울', self)
        label1.setGeometry(200, 455, 250, 50)
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(font)

        button2 = QPushButton(self)
        button2.setGeometry(500, 200, 250, 250)
        button2.setIcon(QIcon('C:/Users/chlsk/Desktop/opensw project/가구/방석.png'))  # 이미지 파일 경로를 넣어주세요
        button2.setIconSize(QPixmap('C:/Users/chlsk/Desktop/opensw project/가구/방석.png').size())

        label2 = QLabel('방석', self)
        label2.setGeometry(500, 455, 250, 50)
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(font)

        button3 = QPushButton(self)
        button3.setGeometry(800, 200, 250, 250)
        button3.setIcon(QIcon('C:/Users/chlsk/Desktop/opensw project/가구/베개.png'))  # 이미지 파일 경로를 넣어주세요
        button3.setIconSize(QPixmap('C:/Users/chlsk/Desktop/opensw project/가구/베개.png').size())

        label3 = QLabel('베개', self)
        label3.setGeometry(800, 455, 250, 50)
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(font)

        button4 = QPushButton(self)
        button4.setGeometry(500, 500, 250, 250)
        button4.setIcon(QIcon('C:/Users/chlsk/Desktop/opensw project/가구/의자.png'))  # 이미지 파일 경로를 넣어주세요
        button4.setIconSize(QPixmap('C:/Users/chlsk/Desktop/opensw project/가구/의자.png').size())

        label4 = QLabel('의자', self)
        label4.setGeometry(500, 755, 250, 50)
        label4.setAlignment(Qt.AlignCenter)
        label4.setFont(font)

        button5 = QPushButton(self)
        button5.setGeometry(200, 500, 250, 250)
        button5.setIcon(QIcon('C:/Users/chlsk/Desktop/opensw project/가구/이불.png'))  # 이미지 파일 경로를 넣어주세요
        button5.setIconSize(QPixmap('C:/Users/chlsk/Desktop/opensw project/가구/이불.png').size())

        label5 = QLabel('이불', self)
        label5.setGeometry(200, 755, 250, 50)
        label5.setAlignment(Qt.AlignCenter)
        label5.setFont(font)

        self.show()

if __name__ == '__main__':
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    ex = ImageBackgroundApp()
    sys.exit(app.exec_())
