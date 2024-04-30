
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
            # 閉じ括弧リストがからの場合
            if not stack_bracket_list:
                print(char + 'に対応する括弧がリストに格納されていません')
                return False
            
            # 対象の閉じ括弧が閉じ括弧リストの末端ではない場合
            if char != stack_bracket_list[-1]:
                print('期待値：' + char + '実測値：' + stack_bracket_list[-1])
                return False
            else:
                # 閉じ括弧リストの末端を取り出す
                stack_bracket_list.pop()
    
    # 閉じ括弧リストに括弧が残っている場合
    if stack_bracket_list:
        print('閉じ括弧が残っています：')
        [print(c, end=',') for c in stack_bracket_list]
        return False
    
    print('チェック問題なし')
    return True


# メイン処理
if __name__ == '__main__':
    data = '{ss[dd]ff(sd)}]'
    print(check_bracket_format(data))
