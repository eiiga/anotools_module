import collections
import glob
import json


# JSONファイル格納パス
JSON_FILE_PATH = './json_data_dir/*.json'


# JSONデータ整形と出力処理
def format_output_json_data(list_data):
    # リストの要素数分繰り返し
    for i, dict_data in enumerate(list_data):
        # 要素数出力
        print(f'{"="*10} json file {i+1} {"="*10}')
        # DICTの要素数分繰り返し
        for dict_key, dict_val in dict_data.items():
            # KEYが「data」の場合
            if dict_key == 'data':
                # KEYを出力
                print(dict_key)
                # 区切り出力
                print(f' {"-"*30}')
                # 「data」の要素数分繰り返し
                for data_key, data_val in dict_val.items():
                    # 「data」のKEYとVALUEを出力
                    print(f' {data_key:15}{data_val}')
                # 区切り出力
                print(f' {"-"*30}')
            else:
                # KEYとVALUEを出力
                print(f'{dict_key:15}{dict_val}')
        # 改行を出力
        print()


# JSONファイル読み込み処理
def input_json_files():
    # JSONデータ格納リスト初期化
    json_data_list = []
    # ファイル名順に読み込み
    json_files = sorted(glob.glob(JSON_FILE_PATH))
    # JSONファイル数分繰り返し
    for json_file in json_files:
        # JSONデータ格納DICTの初期化
        json_dict = {}
        # JSONファイルオープン
        with open(json_file) as jfile:
            # JSONデータ読み込み
            json_data = jfile.read()

        # JSONデータをDICTに変換
        json_dict = json.loads(json_data)
        # DICTの中身をソート
        json_dict = collections.OrderedDict(
            sorted(json_dict.items(), key=lambda d: d[0])
        )
        # JSONデータ格納リストにDICTを格納
        json_data_list.append(json_dict)

    # JSONデータ整形と出力処理
    format_output_json_data(json_data_list)


# メイン処理
if __name__ == '__main__':
    # JSONファイル読み込み処理呼び出し
    input_json_files()

# 参考
# https://qiita.com/michitaka523/items/2e5452fbd1df61df91ef
# https://teshi-learn.com/2021-04/python-glob-glob-sorted/
# https://nansystem.com/python-convert-json-string-to-dict/
