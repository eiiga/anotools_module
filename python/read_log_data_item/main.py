LOG_FILE_PATH = './logs/sample.log'


def read_log_file():
    # ログファイルを開く
    with open(LOG_FILE_PATH, 'r', encoding='utf-8') as f:
        # ログファイル内の行数分繰り返し
        for line in f:
            # ログデータを'|'で分割
            log_list = line.strip().split('|')

            # ログ種別の02（データ部）の場合
            if log_list[1] == '02':
                # ログのデータ部を取得
                log_data = log_list[2]
                # 先頭の "data: " を除去
                data_line = log_data.replace("data:", "", 1).strip()

                # key1=value1, key2=value2,...を辞書型に格納
                data = {k.strip(): v.strip() for k, v in
                        (item.split('=') for item in data_line.split(','))}

                print(data)


if __name__ == '__main__':
    read_log_file()
