# execution_arguments（実行時引数サンプル）のunittest
#
# 【実行方法】
# python/basics ディレクトリに移動してから、以下のように実行する
#
#   cd python/basics
#   python3 -m unittest execution_arguments.test_execution_arguments

import io
import unittest
from contextlib import redirect_stdout

from execution_arguments.__main__ import build_arg_parser, run_greet, run_add, run_echo, main


class TestExecutionArguments(unittest.TestCase):

    # 1. greet（デフォルト）
    def test_greet_default(self):
        print(f'{"-"*5}1. greet（デフォルト）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['greet'])

        # デフォルト値の確認
        self.assertEqual(args.name, 'ゲスト')
        self.assertEqual(args.times, 1)

        # 標準出力をキャプチャして内容を確認
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_greet(args)

        self.assertEqual(stdout.getvalue(), 'こんにちは、ゲストさん！\n')

    # 2. greet（--name --times指定）
    def test_greet_with_name_and_times(self):
        print(f'{"-"*5}2. greet（--name --times指定）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['greet', '--name', '太郎', '--times', '3'])

        self.assertEqual(args.name, '太郎')
        self.assertEqual(args.times, 3)

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_greet(args)

        expected = 'こんにちは、太郎さん！\n' * 3
        self.assertEqual(stdout.getvalue(), expected)

    # 3. add
    def test_add(self):
        print(f'{"-"*5}3. add{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['add', '1', '2', '3', '4'])

        self.assertEqual(args.numbers, [1, 2, 3, 4])

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_add(args)

        self.assertEqual(stdout.getvalue(), '[1, 2, 3, 4] の合計は 10 です\n')

    # 4. echo（デフォルト：asis）
    def test_echo_default_asis(self):
        print(f'{"-"*5}4. echo（デフォルト：asis）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['echo', 'Hello World'])

        self.assertEqual(args.case, 'asis')

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_echo(args)

        self.assertEqual(stdout.getvalue(), 'Hello World\n')

    # 5. echo（--case upper）
    def test_echo_case_upper(self):
        print(f'{"-"*5}5. echo（--case upper）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['echo', 'Hello World', '--case', 'upper'])

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_echo(args)

        self.assertEqual(stdout.getvalue(), 'HELLO WORLD\n')

    # 6. echo（--case lower）
    def test_echo_case_lower(self):
        print(f'{"-"*5}6. echo（--case lower）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['echo', 'Hello World', '--case', 'lower'])

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            run_echo(args)

        self.assertEqual(stdout.getvalue(), 'hello world\n')

    # 7. -v（verboseフラグ）：main()経由でverbose出力とサブコマンド出力の両方を確認
    def test_verbose_flag(self):
        print(f'{"-"*5}7. -v（verboseフラグ）{"-"*5}')

        parser = build_arg_parser()
        args = parser.parse_args(['-v', 'echo', 'Hello World'])

        self.assertTrue(args.verbose)

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            if args.verbose:
                print(f'[verbose] 解析結果：{args}')
            run_echo(args)

        output_lines = stdout.getvalue().splitlines()
        self.assertTrue(output_lines[0].startswith('[verbose] 解析結果：'))
        self.assertEqual(output_lines[1], 'Hello World')

    # 8. -h（ヘルプ）：argparseはヘルプ表示後にSystemExit(0)を送出する
    def test_help_option(self):
        print(f'{"-"*5}8. -h（ヘルプ）{"-"*5}')

        parser = build_arg_parser()
        stdout = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            with redirect_stdout(stdout):
                parser.parse_args(['-h'])

        self.assertEqual(cm.exception.code, 0)
        self.assertIn('usage: execution_arguments', stdout.getvalue())

    # 9. サブコマンド未指定（異常系）：argparseはエラー時にSystemExit(2)を送出する
    def test_command_required_error(self):
        print(f'{"-"*5}9. サブコマンド未指定（異常系）{"-"*5}')

        parser = build_arg_parser()

        with self.assertRaises(SystemExit) as cm:
            parser.parse_args([])

        self.assertEqual(cm.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
