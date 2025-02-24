from datetime import datetime

from util.get_next_and_last_day_util import is_week_format, date_formatter, \
    search_day, print_day


def main(month: int, day: int, weekday: str) -> None:
    # 処理日を取得
    dt_now = datetime.now()

    # debug code: 作業日が閏年の2/29のケース
    # test_date = '2036-02-29 13:49:37'
    # dt_now = datetime.strptime(test_date, '%Y-%m-%d %H:%M:%S')

    # 閏年フラグ初期化
    is_leap_year = False

    # デフォルトの年は処理日付の年
    dt_default_year = dt_now.year

    # 2/29なら閏年判定
    if month == 2 and day == 29:
        is_leap_year = True
    else:
        # 日付のフォーマットチェックしてNGなら終了
        if date_formatter(dt_default_year, month, day) is None:
            return

    # 曜日判定処理して曜日でないなら処理終了
    if not is_week_format(weekday):
        return

    # 処理日と入力した月日と曜日が一致した場合
    if (dt_now.month, dt_now.day) == (month, day):

        # 直近過去の日付を検索（ex 処理年が2024なら2023スタート）
        search_day(
            dt_default_year - 1, month, day, weekday, -1, is_leap_year)

        # 曜日が一緒の場合
        if dt_now.strftime('%A') == weekday:
            # 処理日を出力
            print_day(date_formatter(dt_default_year, month, day))

        # 直近未来の日付を検索（ex 処理年が2024なら2025からスタート）
        search_day(
            dt_default_year + 1, month, day, weekday, 1, is_leap_year)

    # 処理日 < 入力した月日の場合
    elif (dt_now.month, dt_now.day) < (month, day):
        # 直近過去の日付を検索（ex 処理年が2024なら2023スタート）
        search_day(
            dt_default_year - 1, month, day, weekday, -1, is_leap_year)

        # 直近未来の日付を検索（ex 処理年が2024なら2024からスタート）
        search_day(
            dt_default_year, month, day, weekday, 1, is_leap_year)

    # 処理日 > 入力した月日の場合
    elif (dt_now.month, dt_now.day) > (month, day):
        # 直近過去の日付を検索（ex 処理年が2024なら2024スタート）
        search_day(
            dt_default_year, month, day, weekday, -1, is_leap_year)

        # 直近未来の日付を検索（ex 処理年が2024なら2025からスタート）
        search_day(
            dt_default_year + 1, month, day, weekday, 1, is_leap_year)


if __name__ == '__main__':
    # ここの日付と曜日を操作する
    main(2, 29, 'Wednesday')
