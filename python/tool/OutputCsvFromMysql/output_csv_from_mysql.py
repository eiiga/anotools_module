import csv
from datetime import datetime

from connect_mysql import ConnectMysql, SelectData


# 出力ディレクトリパス
OUTPUT_DIR = './output_dir/'


# Keyを取得する関数
def get_dict_keys(list_data):
    # 返却用リストの初期化
    dict_keys = []

    # リストデータ分繰り返し
    for data in list_data:
        # 辞書データ分繰り返し
        for key in data.keys():
            # 返却用リストにKeyが存在していない場合
            if key not in dict_keys:
                # 返却用リストにKeyを追加
                dict_keys.append(key)

    # 返却用リストを返す
    return dict_keys


# mysqlからデータをcsvに出力する関数
def output_csv_from_mysql():
    # Mysql接続・実行クラスのインスタンス
    sql_connect = ConnectMysql()
    # Mysqlに接続する関数実行
    connect_info = sql_connect.connector_mysql()

    # テーブルからデータを取得するクラスのインスタンス
    select_user = SelectData()
    # テーブルからデータを取得する関数実行
    result_datas = select_user.select_data(connect_info)

    # Keyを取得する関数実行
    filed_names = get_dict_keys(result_datas)

    # 現在時刻取得
    now_date = datetime.now()

    # 出力するファイル名をセット
    output_file_path = OUTPUT_DIR + now_date.strftime('%Y%m%d_%H%M%S') + '.csv'

    # 出力ファイルを追記モードでオープン
    with open(output_file_path, 'a') as output_file:
        # 辞書→csvライブラリの呼び出し
        writer = csv.DictWriter(output_file, fieldnames=filed_names)
        # ヘッダーを出力
        writer.writeheader()
        # データ部を出力
        writer.writerows(result_datas)


# メイン処理
if __name__ == '__main__':
    # mysqlからデータをcsvに出力する関数実行
    output_csv_from_mysql()
