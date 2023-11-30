from database import user_data, black_list

# join
def join(a,b,c,d,e):
    Username = a
    Password = b
    Start_time = c
    End_time = d
    Seat_number = e
    Warnning = 0

    user_data[Username] = {
        'password': Password,
        'seat_number': Seat_number,
        'start_time': Start_time,
        'end_time': End_time
    }
    black_list[Username] = {'warnning': Warnning}



