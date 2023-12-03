import tkinter as tk
from tkcalendar import Calendar, DateEntry

# 画面サイズの定数
FRAME_WIDTH = 250
FRAME_HEIGHT = 220


# カレンダー作成クラス
class TkCalendaerFrame(tk.Frame):
    # コンストラクタ
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master.title("カレンダー")
        self.master.geometry(f'{FRAME_WIDTH}x{FRAME_HEIGHT}')

        # 日付入力のフォーム作成
        self.data_entry_date = DateEntry(locale='ja_JP')
        self.data_entry_date.place(x=50, y=20)

        # 日付変更ボタンの作成
        self.btn_change_date = tk.Button(
            master,
            text='変更',
            command=self.change_date
        )
        self.btn_change_date.place(x=150, y=15)

        # カレンダーの作成
        self.calender_date = Calendar(
            self.master,
            showweeknumbers=False,
            locale='ja_JP'
        )
        self.calender_date.place(x=10, y=50)

    # 日付変更処理
    def change_date(self):
        # 入力した日付の取得
        target_date = self.data_entry_date.get_date()

        # 入力した日付に対して、カレンダーの日付を移動
        self.calender_date.selection_set(target_date)


# メイン関数
def main():
    # tkinterのインスタンス
    root = tk.Tk()
    # カレンダー作成クラスのインスタンス
    root = TkCalendaerFrame(master=root)
    # 画面表示
    root.mainloop()


# メイン処理
if __name__ == "__main__":
    # メイン関数呼び出し
    main()


# 参考URL
# https://tkcalendar.readthedocs.io/en/stable/howtos.html
# https://dob-kids.com/2021/03/18/python-tkcalender1/
