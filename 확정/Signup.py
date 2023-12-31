import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import database
import join


class ReservationApp:
    
    def __init__(self, master=None):
        self.root = tk.Toplevel(master) if master else tk.Tk()
        self.root.title('회원가입')
        self.root.geometry('600x750')
        
        # self.myVar1 = tk.IntVar()
        
        self.seat_buttons = {}
        self.row_num = 16
        self.col_num = 0
        
        self.current_seat = None
        self.payment_amount = 0  # 새로운 변수 추가

        self.create_widgets()

    def create_widgets(self):
        def printMy():
            print(self.myVar1.get())
        
        self.myVar1 = tk.IntVar()
        
        # id와 password, 요금제 그리고 Join 버튼의 UI를 만드는 부분
        tk.Label(self.root, text="Username : ").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Password : ").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="요금제 선택 ").grid(row=8, column=0, padx=10, pady=10)

        
        self.ent_PHN = tk.Entry(self.root)
        self.ent_PHN.grid(row=0, column=1, padx=10, pady=10)
        self.ent_PS = tk.Entry(self.root, show='*')
        self.ent_PS.grid(row=2, column=1, padx=10, pady=10)
        
        
        tk.Radiobutton(self.root, text=f'2시간 : {database.menu(database.event_Value)["2h"]}원', variable=self.myVar1, value=2, tristatevalue=2, command=printMy).grid(row=8, column=1, padx=10, pady=10)
        
        tk.Radiobutton(self.root, text=f'4시간 : {database.menu(database.event_Value)["4h"]}원', variable=self.myVar1, value=10, tristatevalue=10, command=printMy).grid(row=9, column=1, padx=10, pady=10)
        
        tk.Radiobutton(self.root, text=f'6시간 : {database.menu(database.event_Value)["6h"]}원', variable=self.myVar1, value=20, tristatevalue=20, command=printMy).grid(row=10, column=1, padx=10, pady=10)
        
        tk.Radiobutton(self.root, text=f'12시간 : {database.menu(database.event_Value)["12h"]}원', variable=self.myVar1, value=30, tristatevalue=30, command=printMy).grid(row=11, column=1, padx=10, pady=10)
        tk.Radiobutton(self.root, text=f'1일 : {database.menu(database.event_Value)["1 day"]}원', variable=self.myVar1, value=40, tristatevalue=40, command=printMy).grid(row=12, column=1, padx=10, pady=10)
        tk.Radiobutton(self.root, text=f'7일 : {database.menu(database.event_Value)["7 day"]}원', variable=self.myVar1, value=50, tristatevalue=50, command=printMy).grid(row=13, column=1, padx=10, pady=10)
        
        tk.Radiobutton(self.root, text=f'30일 : {database.menu(database.event_Value)["30 day"]}원', variable=self.myVar1, value=60, tristatevalue=60, command=printMy).grid(row=14, column=1, padx=10, pady=10)
        
        for seat, status in database.seat_status.items():
            button_color = 'green' if status else 'red'  # 사용 가능한 좌석인 경우 녹색, 아닌 경우 빨간색
            button = tk.Button(self.root, text=str(seat), width=10, height=2, command=lambda s=seat: self.passSeatN(s), bg=button_color)
            
            # 사용 불가능한 좌석인 경우 버튼을 비활성화
            if not status:
                button.config(state=tk.DISABLED)
                
            button.grid(row=self.row_num, column=self.col_num, padx=5, pady=5)
            self.seat_buttons[seat] = button

            self.col_num += 1
            if self.col_num == 5:
                self.col_num = 0
                self.row_num += 1
        print(666)
        tk.Button(self.root, text="Check", command=self.check).grid(row=28, column=1, padx=10, pady=10)

        self.root.mainloop()

    def check(self):
        self.toggle_seat(self.current_seat)
        self.myTime()
        self.sumPrice()
        print(self.myVar1.get())
        # self.set_price()#
        phone_number = self.ent_PHN.get()
        if phone_number in database.user_data:
            messagebox.showwarning('Join', '이미 있는 아이디 입니다')
        else:
            self.register()
            self.open_next_window()
    def passSeatN(self, seat):
        self.current_seat = seat

    def toggle_seat(self, seat):
        # self.current_seat = seat
        database.seat_status[self.current_seat] = not database.seat_status[seat]
        button_color = 'green' if database.seat_status[self.current_seat] else 'red'
        self.seat_buttons[self.current_seat].configure(bg=button_color)

    def open_next_window(self):
        self.set_price()
        top = tk.Toplevel()
        top.title('Reservation')
        self.payment(top)

    def register(self):
        phone_number = self.ent_PHN.get()
        password = self.ent_PS.get()

        start1_time = datetime.now()
        order_time = self.myTime()
        end_time1 = datetime.now() + order_time
        
        start_time = self.changeDateS(str(start1_time))
        end_time = self.changeDateS(str(end_time1))
        seat_number = self.current_seat
        
        
        join.join(phone_number, password, start_time, end_time, seat_number)
        
    def changeDateS(self, a):
        date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
        # datetime 객체를 원하는 형식의 문자열로 변환
        formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S.%f')
        return formatted_date
    # 문자열->date 형식으로 변환 함수
    def changeDateD(self, a):
        date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
        return date_object

    def myTime(self):
        if self.myVar1.get() == 2:
            return timedelta(hours=2)
        elif self.myVar1.get() == 10:
            return timedelta(hours=4)
        elif self.myVar1.get() == 20:
            return timedelta(hours=6)
        elif self.myVar1.get() == 30:
            return timedelta(hours=12)
        elif self.myVar1.get() == 40:
            return timedelta(days=1)
        elif self.myVar1.get() == 50:
            return timedelta(days=7)
        else:
            return timedelta(days=30)

    def sumPrice(self):
        if self.myVar1.get() == 2:
            database.sumSales += database.menu(database.event_Value)["2h"]
            
        elif self.myVar1.get() == 10:
            database.sumSales += database.menu(database.event_Value)["4h"]
            
        elif self.myVar1.get() == 20:
            database.sumSales += database.menu(database.event_Value)["6h"]
            
        elif self.myVar1.get() == 30:
            database.sumSales += database.menu(database.event_Value)["12h"]
            
        elif self.myVar1.get() == 40:
            database.sumSales += database.menu(database.event_Value)["1 day"]
            
        elif self.myVar1.get() == 50:
            database.sumSales += database.menu(database.event_Value)["7 day"]
            
        else:
            database.sumSales += database.menu(database.event_Value)["30 day"]
            
            
    def set_price(self):
        if self.myVar1.get() == 2:
            self.payment_amount = database.menu(database.event_Value)["2h"]
            
        elif self.myVar1.get() == 10:
            self.payment_amount = database.menu(database.event_Value)["4h"]
            
        elif self.myVar1.get() == 20:
            self.payment_amount = database.menu(database.event_Value)["6h"]
            
        elif self.myVar1.get() == 30:
            self.payment_amount = database.menu(database.event_Value)["12h"]
            
        elif self.myVar1.get() == 40:
            self.payment_amount = database.menu(database.event_Value)["1 day"]
            
        elif self.myVar1.get() == 50:
            self.payment_amount = database.menu(database.event_Value)["7 day"]
            
        else:
            self.payment_amount = database.menu(database.event_Value)["30 day"]
            
                
    def payment(self, master):
        #함수
        def button_click1():
            label_var.set("결제가 완료되었습니다.")
            # root.quit()
            # root.destroy()
            
        def button_click2():
            self.changeTransmit()
        
        #
        root = master
        root.title("라벨과 버튼 예제")
        # root.geometry('800x600')

        label_var = tk.StringVar()
        label_var.set(f"결제 금액: {self.payment_amount}")
        label = tk.Label(root, textvariable=label_var, font=('Helvetica', 16))
        label.grid(row=0, column=0, columnspan=2, pady=20)
            
        button1 = tk.Button(root, text="카드", command=button_click1)
        button1.grid(row=1, column=0, pady=10, padx=10)

        button2 = tk.Button(root, text="현금", command=button_click2)
        button2.grid(row=1, column=1, pady=10, padx=10)
        
        root.mainloop()
    def changeTransmit(self):
        global row_num1, col_num1  # 전역 변수로 선언
        row_num1 = 6
        col_num1 = 0
            
        root = tk.Tk()
        root.title('회원가입')
        root.geometry('600x750')

        tk.Label(root, text="투입하는 현금 입력 : ").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="계좌 : ").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(root, text="예금주명 : ").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(root, text="은행 : ").grid(row=6, column=0, padx=10, pady=10)

        self.ent_Cash = tk.Entry(root)
        self.ent_Cash.grid(row=0, column=1, padx=10, pady=10)
        ent_account = tk.Entry(root)
        ent_account.grid(row=2, column=1, padx=10, pady=10)
        ent_accountH = tk.Entry(root)
        ent_accountH.grid(row=4, column=1, padx=10, pady=10)
        selected_button = tk.StringVar()

        def create_buttons():
            global row_num1, col_num1  # 전역 변수로 선언
            banks = ['하나', 'IBK', '국민', '신한', '외환', '우리', '한국시티', '카카오', '신협', '토스']
            for bank in banks:
                button = tk.Checkbutton(root, text=bank, variable=selected_button, onvalue=bank, offvalue='')
                button.grid(row=row_num1, column=col_num1, padx=5, pady=5)
                col_num1 += 1
                if col_num1 == 5:
                    col_num1 = 0
                    row_num1 += 1
            tk.Button(root, text="Check", command=Check2).grid(row=row_num1, column=col_num1, padx=10, pady=10)

        # def getBank_selection():
        #     selected_bank = selected_button.get()
        #     print(f"Selected Bank: {selected_bank}")
        def Check2():
            self.afterchange()
        create_buttons()


        root.mainloop()
        
    def afterchange(self):
            root = tk.Tk()
            root.title('이체완료')
            cash = self.ent_Cash.get()
            change = int(cash) - self.payment_amount
            #잔금변수 추가
            tk.Label(root, text=f"잔금 : {change}원").grid(row=0, column=0, padx=10, pady=10)
            tk.Label(root, text="이체완료").grid(row=1, column=0, padx=10, pady=10)
            root.mainloop()