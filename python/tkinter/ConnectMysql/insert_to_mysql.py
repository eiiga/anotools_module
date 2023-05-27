import mysql.connector
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg


# MySQLの接続情報
MYSQL_USER = 'user001'
MYSQL_PASSWORD = 'aaa'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'test_schema'
MYSQL_AUTH = 'mysql_native_password'

# SQL(INSERT)
SQL_INSERT = "INSERT INTO test_table (user_id, user_name) VALUES (%s, %s);"

# Mysql接続処理
def connector_mysql():
    # 接続情報の初期化
    con = None

    try:
        # mysqlに接続
        con = mysql.connector.connect(
            user=MYSQL_USER
            , password=MYSQL_PASSWORD
            , host=MYSQL_HOST
            , port=MYSQL_PORT
            , database=MYSQL_DATABASE
            , auth_plugin=MYSQL_AUTH
        )
        
    except Exception as e:
        # 例外エラーはコンソールへ出力
        print(e)
        
    finally:
        return con


# 登録ボタン押下処理
def btn_insert_click():
    # Mysql接続処理
    connector = connector_mysql()
    
    # Mysql接続失敗処理
    if connector == None:
        msg.showinfo("DB接続エラー", "データベース接続に失敗しました。")
              
        return
    



# メイン処理
if __name__ == '__main__':
    # ウィンドウの設定
    base = tk.Tk()
    base.title("ID登録")
    canvas = tk.Canvas(base, width=300, height=120, bd=0, highlightthickness=0)
    canvas.pack()

    #入力値を保持
    insert_id = tk.StringVar()
    insert_name = tk.StringVar()

    #登録フォーム
    l_id = tk.Label(base, text="ユーザID")
    l_id.place(x=20, y=20)
    tx_id = tk.Entry(base, textvariable=insert_id)
    tx_id.place(x=100, y=20)

    l_name = tk.Label(base, text="ユーザ名")
    l_name.place(x=20, y=40)
    tx_name = tk.Entry(base, textvariable=insert_name)
    tx_name.place(x=100, y=40)


    # 登録ボタン
    btn_search_all = tk.Button(base, text="登録", command=btn_insert_click)
    btn_search_all.place(x=120, y=80)

    # 画面表示
    base.mainloop()