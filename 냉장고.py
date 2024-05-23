from PIL import Image, ImageTk, ImageOps, ImageDraw
import tkinter as tk
import tkinter.messagebox as msbox
from tkinter import filedialog  # filedialog 모듈 import
import os

# 이미지 로드 함수
def load_image(image_path, size):
    try:
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)  # Image.ANTIALIAS 대신 Image.LANCZOS 사용
        return image  # ImageTk.PhotoImage 대신 PIL Image 객체 반환
    except Exception as e:
        msbox.showerror("이미지 로드 오류", f"이미지를 로드하는 동안 오류가 발생했습니다: {e}")
        return None

# Tkinter 윈도우 설정
win = tk.Tk()
win.title("나만의 냉장고")
win.geometry("1200x820")

# 이미지 파일 경로
image_paths = {
    "구입 날짜": "C:/Users/chlsk/Desktop/opensw project/구입 날짜.png",
    "기타 메모": "C:/Users/chlsk/Desktop/opensw project/기타 메모.png",
    "유통기한": "C:/Users/chlsk/Desktop/opensw project/유통기한.png",
    "저장": "C:/Users/chlsk/Desktop/opensw project/저장버튼.png",
    "재료 이름": "C:/Users/chlsk/Desktop/opensw project/재료 이름.png",
    "냉장고 사진": "C:/Users/chlsk/Desktop/opensw project/냉장고 사진.png",  # 냉장고 사진 경로 추가
}

# 이미지 로드
ingredient_img = load_image(image_paths["재료 이름"], (630, 130))
date_img = load_image(image_paths["구입 날짜"], (620, 90))
expiry_img = load_image(image_paths["유통기한"], (595, 90))
memo_img = load_image(image_paths["기타 메모"], (600, 300))
save_img = load_image(image_paths["저장"], (100, 60))
fridge_img = load_image(image_paths["냉장고 사진"], (500, 500))  # 냉장고 사진 크기 조정

# 이미지 선택 함수
selected_image = None

def select_image():
    global selected_image
    file_path = filedialog.askopenfilename()
    if file_path:
        img = load_image(file_path, (500, 500))
        if img:
            circular_img = ImageOps.fit(img, (500, 500), Image.LANCZOS)
            mask = Image.new('L', (500, 500), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 500, 500), fill=255)
            circular_img.putalpha(mask)
            circular_img_tk = ImageTk.PhotoImage(circular_img)
            button.config(image=circular_img_tk)
            button.image = circular_img_tk  # 참조를 유지하여 이미지가 GC되지 않도록 함
            selected_image = img

# 레이아웃 설정을 위한 프레임
main_frame = tk.Frame(win)
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=10, pady=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", padx=10, pady=10)

# 냉장고 사진 버튼 생성
if fridge_img:
    fridge_img_tk = ImageTk.PhotoImage(fridge_img)  # PIL 이미지 객체를 Tkinter 이미지 객체로 변환
    button = tk.Button(left_frame, image=fridge_img_tk, command=select_image)
    button.image = fridge_img_tk  # 참조를 유지하여 이미지가 GC되지 않도록 함
    button.pack(pady=10)

# 이미지와 텍스트 입력란 겹치기 함수
def create_image_with_entry(parent, image, entry_width, entry_font_size, entry_x_offset, entry_y_offset):
    canvas = tk.Canvas(parent, width=image.width, height=image.height)
    tk_image = ImageTk.PhotoImage(image)  # PIL 이미지 객체를 Tkinter 이미지 객체로 변환
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image  # 참조를 유지하여 이미지가 GC되지 않도록 함
    canvas.pack()
    
    entry = tk.Entry(parent, width=entry_width, font=("Arial", entry_font_size))
    canvas.create_window(image.width // 2 + entry_x_offset, image.height // 2 + entry_y_offset, window=entry)  # x, y 좌표를 매개변수로 조정
    return entry

def create_image_with_text(parent, image, text_width, text_height, text_x_offset, text_y_offset):
    canvas = tk.Canvas(parent, width=image.width, height=image.height)
    tk_image = ImageTk.PhotoImage(image)  # PIL 이미지 객체를 Tkinter 이미지 객체로 변환
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image  # 참조를 유지하여 이미지가 GC되지 않도록 함
    canvas.pack()
    
    text = tk.Text(parent, width=text_width, height=text_height, font=("Arial", 12))
    canvas.create_window(image.width // 2 + text_x_offset, image.height // 2 + text_y_offset, window=text)  # x, y 좌표를 매개변수로 조정
    return text

# 오른쪽에 이미지와 입력란 추가
entry_width = 20
entry_font_size = 20

# 입력란의 x, y 좌표를 설정
ingredient_x_offset, ingredient_y_offset = 105, 10
date_x_offset, date_y_offset = 107, 1
expiry_x_offset, expiry_y_offset = 95, 9
memo_x_offset, memo_y_offset = 5, 35

if ingredient_img:
    ingredient_frame = tk.Frame(right_frame)
    ingredient_entry = create_image_with_entry(ingredient_frame, ingredient_img, entry_width, entry_font_size, ingredient_x_offset, ingredient_y_offset)
    ingredient_frame.pack(pady=10)

if date_img:
    date_frame = tk.Frame(right_frame)
    date_entry = create_image_with_entry(date_frame, date_img, entry_width, entry_font_size, date_x_offset, date_y_offset)
    date_frame.pack(pady=10)

if expiry_img:
    expiry_frame = tk.Frame(right_frame)
    expiry_entry = create_image_with_entry(expiry_frame, expiry_img, entry_width, entry_font_size, expiry_x_offset, expiry_y_offset)
    expiry_frame.pack(pady=10)

if memo_img:
    memo_frame = tk.Frame(right_frame)
    memo_entry = create_image_with_text(memo_frame, memo_img, 57, 11.2, memo_x_offset, memo_y_offset)  # 폭 80, 높이 20
    memo_frame.pack(pady=10)

# 저장 버튼 추가
if save_img:
    save_button_tk = ImageTk.PhotoImage(save_img)  # PIL 이미지 객체를 Tkinter 이미지 객체로 변환
    save_button = tk.Button(right_frame, image=save_button_tk, command=lambda: save_data())
    save_button.image = save_button_tk  # 참조를 유지하여 이미지가 GC되지 않도록 함
    save_button.pack(pady=10)

def save_data():
    global selected_image
    # 데이터를 저장할 디렉토리 경로 설정
    save_directory = "C:/Users/chlsk/Desktop/opensw project/saved_data"
    os.makedirs(save_directory, exist_ok=True)
    
    # 입력란의 내용 가져오기
    ingredient = ingredient_entry.get()
    date = date_entry.get()
    expiry = expiry_entry.get()
    memo = memo_entry.get("1.0", tk.END).strip()
    
    # 파일명 설정 (재료 이름을 파일명으로 사용)
    base_filename = os.path.join(save_directory, ingredient.replace(" ", "_"))
    
    # 이미지 저장
    if selected_image:
        image_save_path = base_filename + ".png"
        selected_image.save(image_save_path)
    
    # 텍스트 데이터 저장
    text_save_path = base_filename + ".txt"
    with open(text_save_path, "w") as file:
        file.write(f"재료 이름: {ingredient}\n")
        file.write(f"구입 날짜: {date}\n")
        file.write(f"유통기한: {expiry}\n")
        file.write(f"메모: {memo}\n")

    # 저장 완료 메시지
    msbox.showinfo("저장 완료", "데이터가 성공적으로 저장되었습니다.")

win.mainloop()
