from tkinter import *
import tkinter as tk
from datetime import datetime, timedelta


#좌석 빈자리 유무/ 초기 자리 상태를 나타내는 딕셔너리 (True: 배정되지 않음, False: 배정됨)
seat_status = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True}


#가격표
def menu(a):
    if a == 0:
        return {'2h': 1000, '4h': 1500, '6h': 2500, '12h': 5000, '1 day': 4000, '7 day': 12500, '30 day': 60000}
    else:
        return {'2h': 2000, '4h': 3000, '6h': 5000, '12h': 10000, '1 day': 8000, '7 day': 25000, '30 day': 120000}

# 이벤트
event_Value = 1

##사용자 데이터
user_data = {
    '12345678' : {
        'password': '1111',
        'seat_number': 1,
        'start_time': '2023-12-01 12:34:56.789012',
        'end_time': '2023-12-31 12:34:56.789012'
    },
    '22222222' : {
        'password': '1111',
        'seat_number': 2,
        'start_time': '2023-12-01 12:34:56.789012',
        'end_time': '2023-12-13 12:34:56.789012'
    },
    '33333333' : {
        'password': '1111',
        'seat_number': 3,
        'start_time': '2023-12-01 12:34:56.789012',
        'end_time': '2023-12-15 12:34:56.789012'
    }
    
}

# date->문자열형식으로 변환 함수
def changeDateS(a):
    date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    # datetime 객체를 원하는 형식의 문자열로 변환
    formatted_date = date_object.strftime('%Y-%m-%d %H:%M:%S.%f')
    return formatted_date
# 문자열->date 형식으로 변환 함수
def changeDateD(a):
    date_object = datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
    return date_object

#자동 로그아웃, 퇴실
for username, user_info in user_data.items():
    end_time = changeDateD(user_info['end_time'])
    current_time = datetime.now()

    # 시간 차이 계산
    time_difference = end_time - current_time
    
    if time_difference == 0:
        del user_data[username]
        seat = user_data[username]['seat_number']
        seat_status[seat] = not seat_status[seat]


#매출 확인
sumSales = 0

#블랙리스트
black_list = {}
for username, user_info in black_list.items():
    warnning = user_info['warning']
    if warnning >= 5:
        del user_data[username]