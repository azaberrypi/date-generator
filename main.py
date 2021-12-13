import datetime

max_days = 7    # 最大で何日分の予定を作るか
day = [""] * max_days
invalid_date_flag = 0  # 入力ミス検知用

print("**input date like \"0702\" if you want to express July Second.**")
for i in range(max_days):
    if invalid_date_flag == 1:
        print("input date again: ", end="")
        day[i-1] = input()
        if day[i] == "end":
            max_days = i - 1
            break
        if len(day[i-1]) != 4:
            print("always invalid date")
            exit()
        invalid_date_flag = 0
    print("input date : ", end = "")
    day[i] = input()
    #print(i)    # debug
    if day[i] == "end":
        if i != 0:
            max_days = i
            break
        else:
            exit()
    if len(day[i]) != 4:
        print("invalid date")
        invalid_date_flag = 1
        continue







dt = datetime.date(2021, 1, 1)
print(dt)

print(type(dt))


w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
print(w_list[dt.weekday()][0]) # 月曜日