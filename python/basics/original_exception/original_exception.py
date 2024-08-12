
# 独自例外処理クラス：Exceptionを継承
class NameContainNumberException(Exception):
    pass


# 名前に数字を含むか確認する処理
def check_number_in_your_name(your_name):
    # 名前に数字を含むか判定
    is_your_name = any(chr.isdigit() for chr in your_name)
    
    # 数字あり
    if is_your_name:
        raise NameContainNumberException(your_name)
    # 数字なし
    else:
        return 0


# メイン処理
if __name__ == '__main__':
    # チェック対象の名前リスト
    sample_names = ['hoge', 'huga2', 'hoge3', 'huga']

    # 名前リスト分繰り返し
    for sample_name in sample_names:
        # 正常なら戻り値を出力
        try:
            print(check_number_in_your_name(sample_name))
            print('==========')
        # 異常なら対象の名前を出力
        except NameContainNumberException as ine:
            print(f'名前に数字が含まれています：{ine}')
            print('==========')
