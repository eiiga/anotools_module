# 整数かチェックして5倍にするクラス
class CheckInputNumber(object):
    def check_input_number(self, number):
        if type(number) is not int:
            raise ValueError

        return number * 5
