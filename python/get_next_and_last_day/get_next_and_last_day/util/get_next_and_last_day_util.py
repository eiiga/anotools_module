import calendar
from datetime import datetime
from typing import Optional

from get_next_and_last_day.const.get_next_and_last_day_const import WEEK_LIST


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
    """
    閏年を算出する処理
    :param year: 年
    :param point: 加算減算値（-1/1）
    :return: 年（閏年）
    """

    # 閏年になるまで繰り返し
    while not calendar.isleap(year):
        year = year + point

    return year
