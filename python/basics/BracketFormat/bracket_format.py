import logging

# 日付|ログレベル|モジュール名|ファンクション名|メッセージ
LOG_FORMATER = '%(asctime)s|%(levelname)s|%(module)s|%(funcName)s|%(message)s'

# ログレベル
logging.basicConfig(level=logging.INFO, format=LOG_FORMATER)

# 括弧判定処理
def check_bracket_format(chars):
    # チェック対象括弧のセット（key：value = 開き括弧：閉じ括弧）
    bracket_dict = {'{': '}', '[': ']', '(': ')'}
    
    # 閉じ括弧を格納するリスト
    stack_bracket_list = []
    
    # 文字列分繰り返し（1文字ずつ取得）
    for char in chars:
        # 開き括弧判定
        if char in bracket_dict.keys():
            # 閉じ括弧をリストに格納
            stack_bracket_list.append(bracket_dict[char])
        
        # 閉じ括弧判定
        if char in bracket_dict.values():
            # 閉じ括弧リストが空の場合
            if not stack_bracket_list:
                logging.error('「' + char + '」に対応する閉じ括弧がリストに格納されていません')
                return False
            
            # 対象の閉じ括弧が閉じ括弧リストの末端ではない場合
            if char != stack_bracket_list[-1]:
                logging.error('閉じ括弧の順序が不正です')
                logging.error('期待値：' + char + '| 実測値：' + stack_bracket_list[-1])
                return False
            else:
                # 閉じ括弧リストの末端を取り出す
                stack_bracket_list.pop()
    
    # 閉じ括弧リストに括弧が残っている場合
    if stack_bracket_list:
        logging.error('閉じ括弧がリストに残っています')
        logging.error('残っている閉じ括弧：' + str(stack_bracket_list))
        return False
    
    logging.info('チェック問題なし')
    return True


# メイン処理
if __name__ == '__main__':
    data = '{ss[dd]ff(sd{)}}'
    check_bracket_format(data)
