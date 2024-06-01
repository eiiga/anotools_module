import logging


# 開始・終了文字列
START_VALUE = 'ABC'
END_VALUE = 'XYZ'

# 日付|ログレベル|モジュール名|ファンクション名|メッセージ
LOG_FORMATER = '%(asctime)s|%(levelname)s|%(module)s|%(funcName)s|%(message)s'

# ログレベル
logging.basicConfig(level=logging.INFO, format=LOG_FORMATER)

# 開始終了文字列判定
def split_start_end_value(input_str):
    # 初期値
    check_value = ''    # 開始終了文字列判定用
    result_value = ''   # 実行結果出力用
    is_data = False     # 開始終了フラグ

    # 文字列を1文字ずつ繰り返す
    for i in input_str:
        # 開始終了文字列判定用文字列が2文字より大きい
        if len(check_value) > 2:
            # 先頭の1文字を削除し、1文字追加（3文字をキープ）
            check_value = check_value[1:] + i
        else:
            # 1文字追加
            check_value += i

        # 開始文字列の場合
        if START_VALUE == check_value:
            # すでにTrueの場合はNG
            if is_data:
                logging.error('開始-終了の間に開始文字列があります：' + input_str)
                return 1
            # 開始終了フラグをTrue
            is_data = True
            # 実行結果に開始文字列を追加
            result_value += check_value

            continue

        # 終了文字列の場合
        elif END_VALUE == check_value:
            # すでにFalseの場合はNG
            if not is_data:
                logging.error('開始の前に終了文字列があります：' + input_str)
                return 1
            # 開始終了フラグをFalse
            is_data = False

            # 終端文字を追加（最後の1文字だけ）
            result_value += i
            
            continue

        if is_data:
            # 1文字追加
            result_value += i

    logging.info('実行結果：' + result_value)

    return 0


# メイン処理
if __name__ == '__main__':
    data1 = 'SRFSABCDEFGHIJKLMNOPQRSTUVWXYZ11'
    data2 = 'SRFSABCDEFABCGHIJKLMNOPQRSTUVWXYZ11'
    data3 = 'SRXYZFSABCDEFGHIJKLMNOPQRSTUVWXYZ11'
    split_start_end_value(data1)
    split_start_end_value(data2)
    split_start_end_value(data3)
