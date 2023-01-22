# -*- Coding: UTF-8 -*-
from datetime import datetime
import tkinter as tk

# 余命を計算
def CountLife(setyear, setmonth, setday):
    end_day = datetime(setyear, setmonth, setmonth)
    today = datetime.now()
    delta = end_day - today
    days = delta.days + 1

    return days


# 生きた日数を計算
def CountLife2(setyear, setmonth, setday):
    birth_day = datetime(setyear, setmonth, setday)
    today = datetime.now()
    delta = today - birth_day
    days = delta.days + 1

    return days

# 生年月日をセット
birth_year = 2000
birth_month = 1
birth_day = 1

# 80および30年後の値をセット
after_year80 = birth_year + 80
after_year30 = birth_year + 30

# 80および30年までの日数を取得
lifeexp1 = CountLife(after_year80, birth_month, birth_day)
lifeexp2 = CountLife(after_year30, birth_month, birth_day)

# 生まれてから何日経過したか取得
lifed = CountLife2(birth_year, birth_month, birth_day)

###########################################
# トップ画面の設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("あと何日？")
canvas = tk.Canvas(base, width=400, height=150, bd=0, highlightthickness=0)
canvas.pack()

# タイトルラベル
l_title1 = tk.Label(base, text="80歳まであと " + str(lifeexp1) + "日", font=("",20))
l_title1.place(x=40, y=20)

l_title2 = tk.Label(base, text="30歳まであと " + str(lifeexp2) + "日", font=("",20))
l_title2.place(x=40, y=50)

l_title3 = tk.Label(base, text="生まれてから  " + str(lifed) + "日", font=("",20))
l_title3.place(x=40, y=80)


base.mainloop()
