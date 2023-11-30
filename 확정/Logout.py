import database
import tkinter as tk
from tkinter import *
from datetime import datetime, timedelta
#Date함수
def changeDateS(a):
    date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    # datetime 객체를 원하는 형식의 문자열로 변환
    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S.%f')
    return formatted_date
# 문자열->date 형식으로 변환 함수
def changeDateD(a):
    date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    return date_object


def logout():
    #check 버튼
    def check2():
        username = ent_PHN.get()
        password = ent_PS.get()
        # root2.quit()
        # root2.destroy()
        if username in database.user_data and database.user_data[username]['password'] == password:
            #자리 상태 변경
            seat = database.user_data[username]['seat_number']
            database.seat_status[seat] = not database.seat_status[seat]
            
            end_time = changeDateD(database.user_data[username]['end_time'])
            current_time = datetime.now()
            # 시간 차이 계산
            time_difference = end_time - current_time
            
            
            root3 = tk.Tk()
            root3.title('로그아웃 성공')
            tk.Label(root3, text="Username : ").grid(row=0, column=0, padx=10, pady=10)
            tk.Label(root3, text=f"로그아웃 성공!").grid(row=1, column=0,padx=10, pady=10)
            tk.Label(root3, text=f'남은시간 : {time_difference}').grid(row=2, column=0, padx=10, pady=10)
        else:
            root4 = tk.Tk()
            root4.title('로그아웃 실패')
            tk.Label(root4, text="잘못된 사용자 이름 또는 비밀번호입니다.").grid(row=0, column=0, padx=10, pady=10)

    root2 = tk.Tk()
    root2.title('Logout')
    tk.Label(root2, text="Username : ").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(root2, text="Password : ").grid(row=2, column=0, padx=10, pady=10)

    ent_PHN = tk.Entry(root2)
    ent_PHN.grid(row=0, column=1, padx=10, pady=10)
    ent_PS = tk.Entry(root2, show='*')
    ent_PS.grid(row=2, column=1, padx=10, pady=10)


    tk.Button(root2, text = "Check", command=check2).grid(row = 11, column = 1, padx = 10, pady = 10)
