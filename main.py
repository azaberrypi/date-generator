import datetime

max_days = 7  # 最大で何日分の予定を作るか
date_ = [""] * max_days
invalid_date_flag = 0  # 入力ミス検知用
set_month = 0  # init
set_day = 0  # init
year = str(datetime.datetime.now())[:4]
w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

print("**input date like \"0702\" if you want to express July Second.**")
print("if you finish to input date, type \"end\".")
print("")
for i in range(max_days):
    if invalid_date_flag == 1:
        print("input date again: ", end="")
        date_[i - 1] = input()
        if date_[i] == "end":
            max_days = i - 1
            break
        if len(date_[i - 1]) != 4:
            print("always invalid date")
            exit()
        invalid_date_flag = 0
    print("input date : ", end="")
    date_[i] = input()
    # print(i)    # debug
    if date_[i] == "end":
        if i != 0:
            max_days = i
            break
        else:
            exit()
    if len(date_[i]) != 4:
        print("invalid date")
        invalid_date_flag = 1
        continue

print("")
# confirm only small error
for i in range(max_days):
    # month
    if date_[i][0] == "0":
        if date_[i][1] == "0":
            break
        else:
            set_month = int(date_[i][1])
    elif date_[i][0] != "1":
        break
    else:
        set_month = int(date_[i][0]) * 10 + int(date_[i][1])
    # day
    if date_[i][2] == "0":
        if date_[i][3] == "0":
            break
        else:
            set_day = int(date_[i][3])
    elif int(date_[i][2]) > 3:
        break
    else:
        set_day = int(date_[i][2]) * 10 + int(date_[i][3])
    # set dastetime.date()
    dt = datetime.date(int(year), set_month, set_day)
    # print
    print(dt, end=" ")
    print(w_list[dt.weekday()][0])
