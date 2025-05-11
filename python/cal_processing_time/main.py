import json
from collections import defaultdict
from datetime import datetime

LOG_FILE_NAME = './logs/test_sample.log'


def cal_processing_time_main():
    """
    ログファイルから処理名および関数名
    :return: None
    """

    # 開始・終了時間Dict 初期値：{"start": None, "end": None}
    result_dict = defaultdict(lambda: {"start": None, "end": None})

    # ログファイルを読み込み
    with open(LOG_FILE_NAME, "r") as f:

        # 行を読み込み
        lines = f.readlines()

        # 1行ずつ繰り返し
        for line in lines:
            # 改行削除
            remove_lf_line = line.rstrip("\n")

            # 区切りで配列化
            line_list = remove_lf_line.split("|")

            # 時刻を取得
            timestamp = datetime.strptime(line_list[0], "%Y-%m-%d %H:%M:%S,%f")

            # 処理名取得
            process_name = line_list[2]

            # 関数名取得
            function_name = line_list[3]

            # 処理名の開始あり
            if result_dict[process_name]["start"] is None:
                result_dict[process_name]["start"] = timestamp
            else:
                result_dict[process_name]["end"] = timestamp

            # 関数名の開始あり
            if result_dict[function_name]["start"] is None:
                result_dict[function_name]["start"] = timestamp
            else:
                result_dict[function_name]["end"] = timestamp

    # 出力用Dict
    output = {}

    # 開始・終了時間Dictの要素数分繰り返し
    for key, value in result_dict.items():

        # 開始・終了時間取得
        start = value["start"]
        end = value["end"]

        # 差分時間の初期値
        duration = None

        # 開始・終了時間あり
        if start and end:
            duration = (end - start).total_seconds()

        # 出力用Dict作成
        output[key] = {
            "start": start.isoformat() if start is not None else None,
            "end": end.isoformat() if end is not None else None,
            "duration_seconds": duration if duration is not None else None
        }

    # json形式に変換
    json_output = json.dumps(output, indent=2)

    # 結果出力
    print(json_output)


# メイン処理
if __name__ == '__main__':
    cal_processing_time_main()
