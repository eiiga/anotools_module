import mysql.connector

# MySQLの接続情報
MYSQL_USER = 'user001'
MYSQL_PASSWORD = 'aaa'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'test_schema'
MYSQL_AUTH = 'mysql_native_password'

# SQL文
SQL_SELECT_HEIGHT_WEIGHT = 'SELECT height, weight ' \
    + 'FROM test_user_height_weight;'


# Mysql接続・実行クラス
class ConnectMysql:
    def __init__(self):
        self.con = None

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


# テーブルから身長・体重を取得するクラス
class SelectUserHeightWeght():
    def __init__(self):
        self.rows = None

    def select_user_height_weight(self, con):
        # 出力形式は辞書型
        self.cursor = con.cursor(dictionary=True)
        try:
            # SQL実行
            self.cursor.execute(SQL_SELECT_HEIGHT_WEIGHT)

            # 検索結果格納
            self.rows = self.cursor.fetchall()

        # 例外処理
        except Exception as e:
            print('select_user_height_weight: 例外エラー: ', e)

        finally:
            self.cursor.close()
            return self.rows
