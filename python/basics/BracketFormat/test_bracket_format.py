import unittest

from bracket_format import check_bracket_format

class TestCheckBracketFormat(unittest.TestCase):
    
    def test_nomal(self):
        print(f'{"-"*5}正常系{"-"*5}')
        
        self.assertEqual(check_bracket_format('{ss[dd]ff(sd)}'), True)
    
    def test_abnomal_1(self):
        print(f'{"-"*5}異常系：閉じ括弧リストなし{"-"*5}')
        
        self.assertEqual(check_bracket_format('){ss[dd]ff(sd)}'), False)

    def test_abnomal_2(self):
        print(f'{"-"*5}異常系：閉じ括弧の順序不正{"-"*5}')
        
        self.assertEqual(check_bracket_format('{ss[dd]ff(sd)}{[(])'), False)

    def test_abnomal_3(self):
        print(f'{"-"*5}異常系：閉じ括弧リスト残あり{"-"*5}')
        
        self.assertEqual(check_bracket_format('{ss[dd]ff(sd)}('), False)


if __name__ == '__main__':
    unittest.main()