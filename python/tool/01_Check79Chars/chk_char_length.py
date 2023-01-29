import os

# 定数関連
CHECK_FILE_PATH = './INPUT'
RESULT_FILE_NAME = './RESULT/check_result.txt'
CHEK_CHAR_LENGTH = 80

def check_chars_length():
    '''
    文字数チェック処理
    概要：
        INPUTディレクトリ配下のファイルについて、
        1行あたりの文字数が規定数以内かチェックし、
        規定数以上であれば、該当のモジュール名、
        行数と文字数をRESULTファイルに出力する。
    引数：
        なし
    戻り値：
        なし
    INPUT：
        「./INPUT」ディレクトリ配下（サブディレクトリも含む）のファイル
    OUTPUT
        判定NGリストファイル（./RESULT/check_result.txt）
    '''
    # 出力用ファイルを上書きモードで開く
    with open(RESULT_FILE_NAME, 'w') as out:
        # インプットフォルダ（サブディレクトリ含む）分繰り返し
        for current_dir, sub_dir, file_list in os.walk(CHECK_FILE_PATH):
            # ファイルの数だけ繰り返し
            for file_name in file_list:
                # ファイルのパスをセット
                tmp_file_path = current_dir + '/' + file_name
                # ファイル名を出力
                out.write(tmp_file_path)
                # 改行
                out.write('\n')
                # 読み込みファイルを開く
                with open(tmp_file_path, 'r') as f:
                    # ファイルの行数分繰り返し
                    for i, line_str in enumerate(f):
                        # 1行当たりの文字数が規定より大きい場合
                        if len(line_str) >= CHEK_CHAR_LENGTH:
                            # 出力用の行数と文字数をセット
                            # ＊「i」は0始まりなのでインクリメント
                            chk_value = str(i+1) \
                                + '行目：' \
                                + str(len(line_str)) \
                                + '文字'
                            # 判定NGを出力
                            out.write(chk_value)
                            # 改行
                            out.write('\n')
                # 改行
                out.write('\n')


# メイン処理
if __name__ == '__main__':
    check_chars_length()