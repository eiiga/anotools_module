# 実行時引数（コマンドライン引数）のサンプルコード
#
# argparseモジュールを使用して、実行時に指定する引数を複数・多種類扱い、
# 指定したサブコマンドによって処理を分岐させる例。
#
# 【実行方法】
# python/basics ディレクトリに移動してから、以下のように実行する（-mオプションでパッケージとして実行）
#
#   cd python/basics
#   python3 -m execution_arguments greet --name 太郎 --times 3
#   python3 -m execution_arguments add 1 2 3 4
#   python3 -m execution_arguments echo "Hello World" --case upper
#   python3 -m execution_arguments -v echo "Hello World"
#   python3 -m execution_arguments -h

import argparse


# コマンドライン引数を解析するためのパーサーを作成する関数
def build_arg_parser():
    # プログラム全体の説明を設定したパーサーを生成
    parser = argparse.ArgumentParser(
        prog='execution_arguments',
        description='実行時引数のサンプル：指定したコマンド（サブコマンド）に応じて処理を分岐する'
    )

    # 共通で使用するオプション引数（どのサブコマンドでも指定可能）
    # action='store_true'：引数を指定するとTrue、指定しなければFalseになるフラグ引数
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='指定すると解析した引数の内容を出力する'
    )

    # サブコマンド（1番目の引数）を追加するための設定
    # dest='command'：選択されたサブコマンド名がargs.commandに格納される
    # required=True：サブコマンドの指定を必須にする
    subparsers = parser.add_subparsers(dest='command', required=True, help='実行する処理を選択')

    # ------------------------------
    # greetサブコマンド：指定した名前に挨拶するメッセージを出力する処理
    # ------------------------------
    parser_greet = subparsers.add_parser('greet', help='指定した名前に挨拶する')
    # --name：文字列を受け取るオプション引数（未指定時はデフォルト値を使用）
    parser_greet.add_argument('--name', type=str, default='ゲスト', help='挨拶する相手の名前')
    # --times：整数を受け取るオプション引数
    parser_greet.add_argument('--times', type=int, default=1, help='挨拶を繰り返す回数')

    # ------------------------------
    # addサブコマンド：複数の数値を合計する処理
    # ------------------------------
    parser_add = subparsers.add_parser('add', help='指定した数値をすべて合計する')
    # nargs='+'：1つ以上の値をまとめて可変長のリストとして受け取る
    parser_add.add_argument('numbers', type=int, nargs='+', help='合計対象の数値（スペース区切りで複数指定可）')

    # ------------------------------
    # echoサブコマンド：入力した文字列を出力する処理
    # ------------------------------
    parser_echo = subparsers.add_parser('echo', help='入力した文字列を出力する')
    # 位置引数：オプション名なしで指定する必須の引数
    parser_echo.add_argument('message', type=str, help='出力する文字列')
    # choices：指定できる値をリストの中身に制限する
    parser_echo.add_argument(
        '--case', type=str, choices=['upper', 'lower', 'asis'], default='asis',
        help='出力時の文字種変換（upper：大文字、lower：小文字、asis：そのまま）'
    )

    return parser


# greetサブコマンドの処理
def run_greet(args):
    # --timesで指定された回数分、挨拶メッセージを出力
    for _ in range(args.times):
        print(f'こんにちは、{args.name}さん！')


# addサブコマンドの処理
def run_add(args):
    # 受け取った数値リストを合計
    total = sum(args.numbers)
    print(f'{args.numbers} の合計は {total} です')


# echoサブコマンドの処理
def run_echo(args):
    message = args.message

    # --caseの指定内容によって文字列を変換
    if args.case == 'upper':
        message = message.upper()
    elif args.case == 'lower':
        message = message.lower()
    # asisの場合は変換せずそのまま使用

    print(message)


# メイン処理：引数を解析し、コマンドの内容に応じて処理を分岐する
def main():
    # コマンドライン引数を解析
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()

    # -v（--verbose）が指定されている場合は解析結果を出力
    if args.verbose:
        print(f'[verbose] 解析結果：{args}')

    # args.command（指定されたサブコマンド名）によって処理を分岐
    if args.command == 'greet':
        run_greet(args)
    elif args.command == 'add':
        run_add(args)
    elif args.command == 'echo':
        run_echo(args)


if __name__ == '__main__':
    main()
