import tkinter as tk
from Login import login
from Signup import ReservationApp
from Manager import manager
from Logout import logout

def main():
    # 사진
    img = None  # 전역 변수로 초기화


    def button_clicked1():
        ReservationApp()


    def button_clicked2():
        login()


    def button_clicked3():
        logout()


    def button_clicked4():
        manager()


    # Tkinter 윈도우 생성
    root = tk.Tk()
    root.title('Button Example')
    root.geometry('600x750')

    ## 이미지 추가
    # image_path = 'C:\\Users\\in\\Desktop\\Kiosk\\Kiosk-Team-Project\\사진\\signature.png'
    # image_path = ('C:/Users/in/Desktop/Kiosk/Kiosk-Team-Project/사진/signature.png')
    image_path = ('C:/Users/in/Desktop/Kiosk/Kiosk-Team-Project/asset/signature.png')
    img = tk.PhotoImage(file=image_path)
    img = img.subsample(5, 7)
    img_label = tk.Label(root, image=img)
    img_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=6)

    ### 중앙에 위치하는 프레임 생성
    center_frame = tk.Frame(root)
    center_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")  # row 값 수정
    root.columnconfigure(0, weight=1)  # column 0을 수평으로 확장

    ### 첫 번째 버튼
    button1 = tk.Button(center_frame, text="회원가입", command=button_clicked1, width=20, height=10)
    button1.grid(row=0, column=0, padx=10, pady=20, columnspan=2, sticky="nsew")  # padx 값 수정

    ### 두 번째 버튼
    button2 = tk.Button(center_frame, text="로그인", command=button_clicked2, width=20, height=10)
    button2.grid(row=0, column=2, padx=10, pady=20, columnspan=2, sticky="nsew")  # padx 값 수정

    ### 세 번째 버튼
    button3 = tk.Button(center_frame, text="로그아웃", command=button_clicked3, width=20, height=10)
    button3.grid(row=0, column=4, padx=10, pady=20, columnspan=2, sticky="nsew")  # padx 값 수정

    ### 네 번째 버튼
    button4 = tk.Button(center_frame, text="manager", command=button_clicked4, width=6, height=2)
    button4.grid(row=1, column=2, padx=20, pady=20, columnspan=2, sticky="nsew")  # row 값 및 padx 값 수정

    ### Tkinter 메인 루프 시작
    root.mainloop()

if __name__ == "__main__":
    main()
