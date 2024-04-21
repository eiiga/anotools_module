import unittest

import check_number

TEST_CASE = 'A'

class TestCheckInputNumber(unittest.TestCase):
    # 各テスト開始前処理
    def setUp(self):
        print(f'{"-"*5}テスト開始{"-"*5}')
        # テスト対象クラスのインスタンス
        self.test_target = check_number.CheckInputNumber()
    
    # 各テスト終了後処理
    def tearDown(self):
        # インスタンスの削除
        del self.test_target
        print(f'{"-"*5}テスト終了{"-"*5}')

    def test_check_input_number(self):
        print(f'{"-"*3}値の確認テスト{"-"*3}')
        
        
        # 成功例
        self.assertEqual(self.test_target.check_input_number(4), 20)
        
        # 失敗例
        # self.assertEqual(self.test_target.check_input_number(4), 10)

    def test_check_input_number_raise(self):
        print(f'{"-"*3}例外の確認テスト{"-"*3}')
        with self.assertRaises(ValueError):
            # 成功例
            self.assertEqual(self.test_target.check_input_number('1'), '5')

            # 失敗例
            # self.assertEqual(self.test_target.check_input_number(1), 5)
    
    # テストをスキップ
    @unittest.skip('skip def')
    def test_check_input_number_skip(self):
        print(f'{"-"*3}確認テスト：skip{"-"*3}')
    
    # 条件が合致すれば、テストをスキップ
    @unittest.skipIf(TEST_CASE=='A', 'skip A case')
    def test_check_input_number_skip_if(self):
        print(f'{"-"*3}確認テスト：skip if{"-"*3}')

if __name__ == '__main__':
    unittest.main()
