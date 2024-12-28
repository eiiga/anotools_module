import unittest

from main.minimum_number_of_money_main import cal_minimum_number


class TestCalMinimunNumbet(unittest.TestCase):
    # 1万円
    def test_cal_minimum_number_10000(self):

        test_total = 10000
        expected = {
            10000: 1, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 5000円
    def test_cal_minimum_number_5000(self):

        test_total = 5000
        expected = {
            10000: 0, 5000: 1, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 1000円
    def test_cal_minimum_number_1000(self):

        test_total = 1000
        expected = {
            10000: 0, 5000: 0, 1000: 1, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 500円
    def test_cal_minimum_number_500(self):

        test_total = 500
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 1, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 100円
    def test_cal_minimum_number_100(self):

        test_total = 100
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 1,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 50円
    def test_cal_minimum_number_50(self):

        test_total = 50
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 1, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 10円
    def test_cal_minimum_number_10(self):

        test_total = 10
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 1, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 5円
    def test_cal_minimum_number_10(self):

        test_total = 5
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 1, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 1円
    def test_cal_minimum_number_1(self):

        test_total = 1
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 1
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 0円
    def test_cal_minimum_number_1(self):

        test_total = 0
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # マイナス
    def test_cal_minimum_number_minus(self):

        test_total = -99999999
        expected = {
            10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0,
            50: 0, 10: 0, 5: 0, 1: 0
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)

    # 全て1ずつカウント
    def test_cal_minimum_number_all_one_count(self):

        test_total = 16666
        expected = {
            10000: 1, 5000: 1, 1000: 1, 500: 1, 100: 1,
            50: 1, 10: 1, 5: 1, 1: 1
            }
        actual = cal_minimum_number(test_total)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
