import calendar
from datetime import datetime
from typing import Optional


# 曜日リスト
WEEK_LIST = ['Sunday',
             'Monday',
             'Tuesday',
             'Wednesday',
             'Thursday',
             'Friday',
             'Saturday']


def is_week_format(week: str) -> bool:
    """
    曜日判定処理
     paramが曜日リストに含まれているか判定
    :param week: 曜日
    :return: True/False
    """
    return week in WEEK_LIST


def date_formatter(year: int, month: int, day: int) -> Optional[datetime]:
    """
    日付フォーマット処理
    :param year: 年
    :param month: 月
    :param day: 日
    :return: True: 日付型/ False: None
    """
    try:
        # 日付変換して返す
        return datetime.strptime(
            f'{str(year)}-{str(month)}-{str(day)}', '%Y-%m-%d')

    except Exception as e:
        # 日付に変換できなかった場合の例外処理
        print(e)
        return None


def print_day(target_date: datetime) -> None:
    """
    結果出力処理
    :param target_date: 検索結果の日付
    :return: None
    """
    print(target_date.strftime('%Y-%m-%d (%A)'))


def search_day(
        year: int, month: int, day: int, weekday: str,
        point: int, is_leap_year: bool) -> None:
    """
    対象日付検索処理
    :param year: 年
    :param month: 月
    :param day: 日
    :param weekday: 曜日
    :param point: 加算減算値（-1/1）
    :param is_leap_year: 閏年判定フラグ(True/False)
    :return: None
    """
    # 閏年なら、閏年判定で取得した年で判定ループ
    if is_leap_year:
        year = get_leapdays(year, point)
        # インプットの曜日と一致するまで繰り返し
        while weekday != date_formatter(year, month, day).strftime('%A'):
            year = get_leapdays(year + point, point)
    # 閏年以外ならインクリメント/デクリメント
    else:
        # インプットの曜日と一致するまで繰り返し
        while weekday != date_formatter(year, month, day).strftime('%A'):
            year = year + point

    print_day(date_formatter(year, month, day))

def get_leapdays(year: int, point: int):
    while not calendar.isleap(year):
        year = year + point

    return year


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

    # 曜日判定処理して曜日でないなら処理終了
    if not is_week_format(weekday):
        return

    # 閏年ではない場合
    if not is_leap_year:
        # 日付のフォーマットチェックしてNGなら終了
        if date_formatter(dt_default_year, month, day) is None:
            return

    # 処理日と入力した月日と曜日が一致した場合
    if (dt_now.month, dt_now.day) == (month, day) \
            and dt_now.strftime('%A') == weekday:

        # 直近過去の日付を検索（ex 処理年が2024なら2023スタート）
        search_day(
            dt_default_year - 1, month, day, weekday, -1, is_leap_year)

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
    elif  (dt_now.month, dt_now.day) > (month, day):
        # 直近過去の日付を検索（ex 処理年が2024なら2024スタート）
        search_day(
            dt_default_year, month, day, weekday, -1, is_leap_year )

        # 直近未来の日付を検索（ex 処理年が2024なら2025からスタート）
        search_day(
            dt_default_year + 1, month, day, weekday, 1, is_leap_year)


if __name__ == '__main__':
    main(2,29,'Saturday')
