import tkinter as tk
# from tkinter import ttk
from tkcalendar import Calendar, DateEntry

FRAME_WIDTH = 250
FRAME_HEIGHT = 220


class TkCalendaerFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master.title("カレンダー")
        self.master.geometry(f'{FRAME_WIDTH}x{FRAME_HEIGHT}')

        # calendar_style = ttk.Style()
        # calendar_style.theme_use('clam')
        # calendar_style.configure(
        #     'my.DataEntry',
        #     fieldbackground = ''
        # )

        self.data_entry_date = DateEntry(style='my.DateEntry')
        # self.data_entry_date = DateEntry()
        self.data_entry_date.place(x=50, y=10)

        self.calender_date = Calendar(
            self.master, 
            showweeknumbers=False, 
            background='White', 
            foreground='black', 
            selectforeground='blue'
        )
        self.calender_date.place(x=10, y=50)


def main():
    root = tk.Tk()
    root = TkCalendaerFrame(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()


# 参考URL
# https://tkcalendar.readthedocs.io/en/stable/howtos.html
# https://dob-kids.com/2021/03/18/python-tkcalender1/
