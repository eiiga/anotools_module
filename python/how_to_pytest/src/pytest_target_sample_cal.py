class Cal:
    def add_for_num(self, x: int) -> int:
        """
        計算処理：入力値1をループして加算する
        :param x: 入力値1
        :return: 計算結果
        """
        if type(x) is not int:
            raise ValueError

        result_value = 0
        
        for i in range(x):
            result_value += i

        return result_value
