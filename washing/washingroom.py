import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QStackedWidget, QMainWindow, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class LaundryRoom(QWidget):
    def __init__(self, room_name, photo_path, map_path, stacked_widget, desc_text):
        super().__init__()
        self.room_name = room_name
        self.photo_path = photo_path
        self.map_path = map_path
        self.stacked_widget = stacked_widget
        self.desc_text = desc_text
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setGeometry(100, 100, 1200, 820)

        # 상단 여백 추가
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 세탁방 사진 표시
        self.photo_label = QLabel(self)
        pixmap_photo = QPixmap(self.photo_path)
        if not pixmap_photo.isNull():
            self.photo_label.setPixmap(pixmap_photo)
        else:
            self.photo_label.setText(f"이미지 로드 실패: {self.photo_path}")
        self.photo_label.setFixedSize(400, 400)
        self.photo_label.setScaledContents(True)

        # 세탁방 지도 표시
        self.map_label = QLabel(self)
        pixmap_map = QPixmap(self.map_path)
        if not pixmap_map.isNull():
            self.map_label.setPixmap(pixmap_map)
        else:
            self.map_label.setText(f"이미지 로드 실패: {self.map_path}")
        self.map_label.setFixedSize(400, 400)
        self.map_label.setScaledContents(True)

        # 세탁방 사진과 지도 사진 사이에 간격 추가
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.photo_label)
        h_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        h_layout.addWidget(self.map_label)

        layout.addLayout(h_layout)

        # 세탁방 사진과 지도 사진 아래에 여백 공간 추가
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 박스 이미지와 텍스트를 겹쳐서 표시할 위젯 생성
        box_widget = QWidget(self)
        box_widget.setFixedSize(1000, 200)
        box_layout = QVBoxLayout(box_widget)

        # 박스 이미지 추가
        self.desc_box_label = QLabel(box_widget)
        box_pixmap = QPixmap("C:\\Users\\hcm\\Desktop\\washing\\box.png")  # 여기에 박스 이미지 경로를 지정하세요
        if not box_pixmap.isNull():
            self.desc_box_label.setPixmap(box_pixmap)
            self.desc_box_label.setFixedSize(1000, 200)  # 박스 이미지 크기 조정
            self.desc_box_label.setScaledContents(True)
        else:
            self.desc_box_label.setText("박스 이미지 로드 실패")

        # 설명 텍스트 추가
        self.desc_label = QLabel(self.desc_text, box_widget)  # 박스 위젯을 부모로 설정
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("""
            color: black;
            font-size: 20px;
            font-weight: bold;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0);
        """)
        self.desc_label.setFixedSize(980, 160)  # 레이블을 박스 크기에 맞춤

        # 레이아웃에 박스 이미지와 설명 텍스트 추가
        box_layout.addWidget(self.desc_box_label)

        layout.addWidget(box_widget, alignment=Qt.AlignCenter)

        # 박스 이미지와 텍스트 아래에 여백 추가
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 닫기 버튼
        self.close_button = QPushButton("닫기", self)
        self.close_button.clicked.connect(self.go_back)
        layout.addWidget(self.close_button, alignment=Qt.AlignCenter)

        # 여백 추가하여 닫기 버튼을 더 아래로 위치
        layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("우리동네 빨래방 위치")
        self.setGeometry(100, 100, 1200, 820)

        # 배경 이미지를 표시할 QLabel 생성
        self.background_label = QLabel(self)
        pixmap = QPixmap("C:/Users/hcm/Desktop/LTC/background.jpg")
        if not pixmap.isNull():
            self.background_label.setPixmap(pixmap)
            self.background_label.setScaledContents(True)
            self.background_label.setGeometry(0, 0, self.width(), self.height())
        else:
            self.background_label.setText("이미지 로드 실패")

        # 스택 위젯 설정
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 메인 화면
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # 중앙 지도 및 버튼 배치 레이아웃
        central_layout = QHBoxLayout()

        # 빨래방 버튼 레이아웃
        left_button_layout = QVBoxLayout()
        right_button_layout = QVBoxLayout()

        # 빨래방 버튼 생성 및 레이아웃에 추가
        self.laundry_buttons = {}
        laundry_names = ["셀피아", "세탁풍경", "워시팡팡 충북대점", "워시팡팡 개신현대점"]
        for i in range(4):
            button = QPushButton(f" {laundry_names[i]}", self)
            button.clicked.connect(self.show_laundry_room)
            self.laundry_buttons[button] = laundry_names[i]
            if i < 2:
                left_button_layout.addWidget(button)
            else:
                right_button_layout.addWidget(button)

        # 학교 지도 사진 영역
        self.map_label = QLabel(self)
        pixmap = QPixmap("C:/Users/hcm/Desktop/LTC/Washing/schoolmap.png")
        if not pixmap.isNull():
            self.map_label.setPixmap(pixmap)
        else:
            self.map_label.setText("이미지 로드 실패")
        self.map_label.setAlignment(Qt.AlignCenter)
        self.map_label.setFixedSize(700, 700)
        self.map_label.setScaledContents(True)

        central_layout.addLayout(left_button_layout)
        central_layout.addWidget(self.map_label, alignment=Qt.AlignCenter)
        central_layout.addLayout(right_button_layout)

        main_layout.addLayout(central_layout)
        main_widget.setLayout(main_layout)

        # 뒤로가기 버튼
        self.back_button = QPushButton("뒤로가기", self)
        self.back_button.setFixedSize(100, 30)
        self.back_button.clicked.connect(self.go_back)

        # 메인 화면 및 버튼을 포함하는 위젯과 레이아웃
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        # 버튼을 좌측 상단에 배치
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button, alignment=Qt.AlignLeft)
        button_layout.addStretch()

        container_layout.addLayout(button_layout)
        container_layout.addWidget(main_widget)
        self.stacked_widget.addWidget(container_widget)

        # 세탁방 화면
        self.laundry_rooms = {}
        laundry_info = [
            {
                "name": "셀피아",
                "photo_path": "C:/Users/hcm/Desktop/washing/sel.png",
                "map_path": "C:/Users/hcm/Desktop/washing/sel_m.png",
                "desc_text": "위치 : 충북 청주시 서원구 내수동로 51 1층\n영업 시간 : 24시간 영업, 연중무휴\n특징 : 세제 무료 공급, 매장 내 화장실 이용 가능"
            },
            {
                "name": "세탁풍경",
                "photo_path": "C:/Users/hcm/Desktop/washing/sp.png",
                "map_path": "C:/Users/hcm/Desktop/washing/sp_m.png",
                "desc_text": "위치 : 충북 청주시 흥덕구 내수동로55번길 10-2 1층\n영업 시간 : 24시간 영업, 연중무휴\n특징 : 회원 등록 시 포인트 적립 가능"
            },
            {
                "name": "워시팡팡 충북대점",
                "photo_path": "C:/Users/hcm/Desktop/washing/washpp_c.png",
                "map_path": "C:/Users/hcm/Desktop/washing/washpp_c_m.png",
                "desc_text": "위치 : 충북 청주시 흥덕구 내수동로 42번길 54 102호\n영업 시간 : 24시간 영업, 연중무휴"
            },
            {
                "name": "워시팡팡 개신현대점",
                "photo_path": "C:/Users/hcm/Desktop/washing/washpp_g.png",
                "map_path": "C:/Users/hcm/Desktop/washing/washpp_g_m.png",
                "desc_text": "위치 : 충북 청주시 서원구 성봉로 226-18 1층\n영업 시간 : 24시간 영업, 연중무휴"
            }
        ]
        for info in laundry_info:
            laundry_room_widget = LaundryRoom(info["name"], info["photo_path"], info["map_path"], self.stacked_widget, info["desc_text"])
            self.stacked_widget.addWidget(laundry_room_widget)
            self.laundry_rooms[info["name"]] = laundry_room_widget

    def show_laundry_room(self):
        sender = self.sender()
        room_name = self.laundry_buttons[sender]
        self.stacked_widget.setCurrentWidget(self.laundry_rooms[room_name])

    def go_back(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
