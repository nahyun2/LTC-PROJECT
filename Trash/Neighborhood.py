import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon

class GarbageCollectionSchedule(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 메인 레이아웃 생성
        main_layout = QVBoxLayout()
        
        self.setWindowTitle('수거 요일 안내')
        self.setFixedSize(1200, 820)

        # 배경 이미지 설정
        self.setAutoFillBackground(True)
        palette = self.palette()
        background_image = QPixmap("C:\\Users\\hcm\\Desktop\\LTC\\back2.png")
        # 배경 이미지를 창의 크기에 맞게 조정
        scaled_background = background_image.scaled(self.size(), Qt.IgnoreAspectRatio)
        palette.setBrush(QPalette.Window, QBrush(scaled_background))
        self.setPalette(palette)

        # 뒤로가기 버튼 이미지 설정
        back_button = QLabel(self)
        back_image = QPixmap("C:\\Users\\hcm\\Desktop\\LTC\\back_button.png")
        back_button.setPixmap(back_image.scaled(100, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        back_button.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        back_button.mousePressEvent = self.goBack  # 마우스 클릭 이벤트를 이용해 뒤로가기 기능 호출

        # 뒤로가기 버튼을 왼쪽 상단에 추가
        main_layout.addWidget(back_button)

        # 청주시 생활쓰레기 수거 요일 제목 레이블 생성 및 설정
        city_label_title = QLabel("청주시 생활쓰레기 수거 요일", self)
        city_label_title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        city_label_title.setStyleSheet("""
            padding: 20px;
            font-family: Arial;
            font-size: 20px;
            font-weight: bold;
        """)

        # 청주시 생활쓰레기 수거 요일 관련 정보 레이블 생성 및 설정
        city_label_info = QLabel("- 일요일 ~ 목요일 저녁(일몰 후 ~ 자정 전)\n\n- 배출 장소 : 배출자 집 앞이나 지정된 장소(골목길은 청소차가 다닐 수 있는 지정 장소)\n\n- 배출 방법\n  1. 타는 쓰레기 : 종량제 봉투나 노란색 종량제마대에 넣어 배출\n  2. 안 타는 쓰레기 : 보라색 종량제마대에 넣어 배출", self)
        city_label_info.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        city_label_info.setStyleSheet("""
            padding: 0px 20px 20px 20px;
            font-family: Arial;
            font-size: 17px;
        """)

        # 메인 레이아웃에 제목과 정보를 추가
        main_layout.addWidget(city_label_title)
        main_layout.addWidget(city_label_info)

        # 음식물 쓰레기 수거 요일 제목 레이블 생성 및 설정
        food_waste_title = QLabel("동네별 음식물 쓰레기 수거 요일", self)
        food_waste_title.setAlignment(Qt.AlignLeft)
        food_waste_title.setStyleSheet("""
            padding-left: 20px;
            font-family: Arial;
            font-size: 20px;
            font-weight: bold;
        """)

        # 제목과 동네 레이아웃 사이에 간격 추가
        main_layout.addWidget(food_waste_title)

        # 동네와 이미지를 위한 레이아웃 생성
        neighborhoods_layout = QVBoxLayout()

        # 동네와 해당 이미지 경로 정의
        neighborhoods = [
            ("개신동 : 월 수 금", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\gaesindong.jpg"),
            ("복대동 : 화 목 일", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\bokdaedong.jpg"),
            ("모충동 : 화 목 일", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\mochungdong.jpg"),
            ("사직동 : 화 목 일", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\sigikdong.jpg"),
            ("봉명동 : 월 수 금", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\bongmyeongdong.jpg"),
            ("사창동 : 화 목 일", "C:\\Users\\hcm\\Desktop\\LTC\\openimg\\dong\\sachangdong.jpg"),
        ]

        # 각 동네의 행 레이아웃 생성
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()

        for i, (name, image_path) in enumerate(neighborhoods):
            # 동네 이름 레이블 생성
            name_label = QLabel(name, self)
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("""
                padding: 10px;
                font-family: Arial;
                font-size: 14px;
                font-weight: bold;
            """)

            # 동네 이미지 레이블 생성
            image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():  # 이미지가 제대로 로드되었는지 확인
                image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setAlignment(Qt.AlignCenter)

            # 각 동네를 위한 세로 레이아웃 생성
            neighborhood_layout = QVBoxLayout()
            neighborhood_layout.addWidget(name_label)
            neighborhood_layout.addWidget(image_label)

            # 각 동네 레이아웃을 해당 행 레이아웃에 추가
            if i < 3:
                row1_layout.addLayout(neighborhood_layout)
            else:
                row2_layout.addLayout(neighborhood_layout)

        # 행 레이아웃을 동네 레이아웃에 추가
        neighborhoods_layout.addLayout(row1_layout)
        neighborhoods_layout.addLayout(row2_layout)

        # 동네 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(neighborhoods_layout)

        # 창에 메인 레이아웃 설정
        self.setLayout(main_layout)

        # 창 보이기
        self.show()

    def goBack(self, event):
        print("뒤로가기 버튼 클릭됨")
        self.close()

def main():
    app = QApplication(sys.argv)
    ex = GarbageCollectionSchedule()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
