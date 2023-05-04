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

# SQL(SELECT)
SQL_SELECT_ALL = "SELECT * FROM test_table"
SQL_SELECT_WHERE = SQL_SELECT_ALL + " WHERE table_id = %s"

# プルダウンの設定値
BASE_LIST_SELECT_KBN = ['ALL', 'ID']

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
            , database=MYSQL_DATABASE
            , auth_plugin=MYSQL_AUTH
        )
        
    except Exception as e:
        # 例外エラーはコンソールへ出力
        print(e)
        
    finally:
        return con

# 検索処理
def select_table(conn):
    # 検索結果初期化
    rows = None
    
    try:
        # カーソル作成：出力形式は辞書型
        cursor = conn.cursor(dictionary=True)
        
        # プルダウン[ALL]：WHERE句なしで検索
        if select_kbn.get() == BASE_LIST_SELECT_KBN[0]:
            # select実行
            cursor.execute(SQL_SELECT_ALL)

        # プルダウン[ID]：WHERE句つきで検索
        elif select_kbn.get() == BASE_LIST_SELECT_KBN[1]:
            # 入力値を取得
            param = select_id.get()
            # select 実行
            cursor.execute(SQL_SELECT_WHERE, (param,))   

        # 全件取得
        rows = cursor.fetchall()  

        # カーソルクローズ
        cursor.close
    
    except Exception as e:
        # 例外エラーはコンソールへ出力
        print(e)
    
    finally:
        return rows


# 検索ボタン押下処理
def btn_select_click():
    # treeviwの初期化
    tree.delete(*tree.get_children())

    # Mysql接続処理
    connector = connector_mysql()
    
    # Mysql接続失敗処理
    if connector == None:
        msg.showinfo("DB接続エラー", "データベース接続に失敗しました。")
              
        return
    
    # 検索処理
    row_data = select_table(connector)
    
    # 検索失敗処理    
    if row_data == None:
        msg.showinfo("DBエラー", "SELECTに失敗しました。")
        
        return

    # 検索結果出力
    if len(row_data) == 0:
        msg.showinfo("検索結果", "検索結果：0件です")
    else:
        for row in row_data:
            tree.insert(parent="", index="end", values=(row["user_id"], row["user_name"]))


# メイン処理
if __name__ == '__main__':
    # ウィンドウの設定
    base = tk.Tk()
    base.title("ID検索")
    canvas = tk.Canvas(base, width=550, height=400, bd=0, highlightthickness=0)
    canvas.pack()

    #入力値を保持
    select_kbn = tk.StringVar()
    select_id = tk.StringVar()

    #検索フォーム
    cb_select_kbn = ttk.Combobox(base, state="readonly", width=5, values=BASE_LIST_SELECT_KBN, textvariable=select_kbn)
    cb_select_kbn.set(BASE_LIST_SELECT_KBN[0])
    cb_select_kbn.place(x=100, y=20)
    tx_String_search_data = tk.Entry(base, textvariable=select_id)
    tx_String_search_data.place(x=180, y=20)

    # 検索ボタン
    btn_search_all = tk.Button(base, text="検索", command=btn_select_click)
    btn_search_all.place(x=380, y=25)

    # Treeviewの設定
    tree = ttk.Treeview(base, columns=(0, 1))
    tree["show"] = "headings"
    tree.column(0, width=200)
    tree.column(1, width=300)
    tree.heading(0, text='ID')
    tree.heading(1, text='Name')
    tree.place(x=10, y=100)

    # 画面表示
    base.mainloop()