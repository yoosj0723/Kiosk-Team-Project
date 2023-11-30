import tkinter as tk
import database

def manager():
    # 블랙리스트
    def BlackList():
        #총판매액
        def Sales():
            label = tk.Label(root, text=f"총 매출: {database.sumSales}원")
            label.pack(pady=10)
            
        #이벤트
        def Event():
            def toggle():
                if var.get():
                    label.config(text="Status: On")
                    database.event_Value = 0
                else:
                    label.config(text="Status: Off")
                    database.event_Value = 1

            var = tk.BooleanVar()
            var.set(True)  # 초기 상태: On

            # On/Off 버튼 생성
            checkbox = tk.Checkbutton(root, text="Event", variable=var, command=toggle)
            checkbox.pack(pady=10)

            # 상태 표시 레이블
            label = tk.Label(root, text="Status: On")
            label.pack(pady=10)
            
        sorted_items = sorted(database.black_list.items(), key=lambda x: x[1]['warnning'], reverse=True)

        # 'warning' 값을 +1 하는 함수
        def increment_warning(key):
            database.black_list[key]['warnning'] += 1
            refresh_display()

        # 정렬된 결과를 Label로 출력하고 각 항목에 대한 버튼 추가
        def refresh_display():
            for widget in root.winfo_children():
                widget.destroy()
            
            Sales()
            Event()

            for key, value in sorted_items:
                label_text = f"Key: {key}, Warnning: {value['warnning']}"
                label = tk.Label(root, text=label_text)
                label.pack()

                # 각 항목에 대한 버튼 추가
                button = tk.Button(root, text=f"Increment Warning for {key}",command=lambda k=key: increment_warning(k))
                button.pack()
        refresh_display()

    # Tkinter 창 생성
    root = tk.Tk()
    root.title("관리자")
    root.geometry('600x400')
    BlackList()

    # 창 실행
    root.mainloop()