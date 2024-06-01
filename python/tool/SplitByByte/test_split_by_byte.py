import logging
import unittest

from split_by_byte import split_by_n_bytes

# 日付|ログレベル|モジュール名|ファンクション名|メッセージ
LOG_FORMATER = '%(asctime)s|%(levelname)s|%(module)s|%(funcName)s|%(message)s'

# ログレベル
logging.basicConfig(level=logging.INFO, format=LOG_FORMATER)


class TestSplitByNByte(unittest.TestCase):

    def test_nomal(self):
        logging.info(f'{"-"*5}正常系{"-"*5}')

        input_data = 'SRFSABCDEFGHIJKLMNOPQRSTUVWXYZ11'
        logging.info('input_data: ' + input_data)

        self.assertEqual(split_by_n_bytes(input_data), 0)

    def test_abnomal_1(self):
        logging.info(f'{"-"*5}異常系{"-"*5}')

        input_data = 'SRFSABCDEFABCGHIJKLMNOPQRSTUVWXYZ11'
        logging.info('input_data: ' + input_data)

        self.assertEqual(split_by_n_bytes(input_data), 1)

    def test_abnomal_2(self):
        logging.info(f'{"-"*5}異常系{"-"*5}')

        input_data = 'SRFSABCDEFGHIJKLMNOPQRSTUVWXYZ11XYZ'
        logging.info('input_data: ' + input_data)

        self.assertEqual(split_by_n_bytes(input_data), 1)

if __name__ == '__main__':
    unittest.main()
