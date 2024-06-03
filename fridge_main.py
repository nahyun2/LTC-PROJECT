from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Tkinter 윈도우 설정
win = tk.Tk()
win.title("나만의 냉장고")
win.geometry("1200x820")

# 이미지 파일 경로
image_path = "C:/Users/chlsk/Desktop/opensw project/재료관리사진/리스트.png"

# 이미지 로드 함수
def load_image(image_path, size):
    try:
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)  # Image.ANTIALIAS 대신 Image.LANCZOS 사용
        return ImageTk.PhotoImage(image)  # PIL Image 객체를 Tkinter 이미지 객체로 변환하여 반환
    except Exception as e:
        messagebox.showerror("이미지 로드 오류", f"이미지를 로드하는 동안 오류가 발생했습니다: {e}")
        return None



# 좌측 상단 버튼 생성
main_button = tk.Button(win, text="메인 화면")
main_button.grid(row=0, column=0, padx=10, pady=10)



# 이미지 로드
image = load_image(image_path, (600, 400))
if image:
    # 이미지를 보여주는 레이블 생성
    image_label = tk.Label(win, image=image)
    image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
'''
# 재료 추가 버튼 생성
add_button = tk.Button(win, text="재료 추가", command=add_ingredient)
add_button.grid(row=2, column=1, padx=10, pady=10)
'''
# 리스트 이미지 위에 표시되는 이미지 버튼
ingredient_button = tk.Button(win)
ingredient_button.grid(row=1, column=1, padx=10, pady=10)

# 열기, 재료 삭제 버튼 생성
open_button = tk.Button(win, text="열기")
open_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(win, text="재료 삭제")
remove_button.grid(row=2, column=2, padx=10, pady=10)

win.mainloop()

