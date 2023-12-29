import mysql.connector

# MySQLの接続情報
MYSQL_USER = 'user001'
MYSQL_PASSWORD = 'aaa'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'test_schema'
MYSQL_AUTH = 'mysql_native_password'

# SQL文
SQL_SELECT_QUERY = 'SELECT * FROM test_output_csv_table;'


# Mysql接続・実行クラス
class ConnectMysql:
    def __init__(self):
        self.con = None

    # Mysqlに接続する関数
    def connector_mysql(self):
        try:
            # mysqlに接続
            self.con = mysql.connector.connect(
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                database=MYSQL_DATABASE,
                auth_plugin=MYSQL_AUTH
            )

        # 例外処理
        except Exception as e:
            print('connector_mysql: 例外エラー: ', e)

        finally:
            return self.con


# テーブルからデータを取得するクラス
class SelectData():
    def __init__(self):
        self.rows = None

    # テーブルからデータを取得する関数
    def select_data(self, con):
        # 出力形式は辞書型
        self.cursor = con.cursor(dictionary=True)
        try:
            # SQL実行
            self.cursor.execute(SQL_SELECT_QUERY)

            # 検索結果格納
            self.rows = self.cursor.fetchall()

        # 例外処理
        except Exception as e:
            print('select_data: 例外エラー: ', e)

        finally:
            self.cursor.close()
            return self.rows
