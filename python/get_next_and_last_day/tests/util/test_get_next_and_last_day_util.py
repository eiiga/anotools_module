import io
import sys
from datetime import datetime, timedelta
import unittest

from get_next_and_last_day.util.get_next_and_last_day_util import \
    is_week_format, date_formatter, print_day, get_leapdays, search_day

WEEK_LIST = ['Sunday',
             'Monday',
             'Tuesday',
             'Wednesday',
             'Thursday',
             'Friday',
             'Saturday']

class TestIsWeekFormat(unittest.TestCase):
    """
    曜日判定処理 テストクラス
    """
    def setUp(self):
        self.test_now = datetime.now()

    def test_is_week_format_now(self):
        self.assertEqual(is_week_format(
            self.test_now.strftime('%A')), True)

    def test_is_week_format_next_day(self):
        test_tomorrow = self.test_now + timedelta(days=1)
        self.assertEqual(
            is_week_format(test_tomorrow.strftime('%A')), True)

    def test_is_week_format_all_week(self):
        for week in WEEK_LIST:
            self.assertEqual(is_week_format(week), True)

    def test_is_week_format_non_week(self):
        self.assertEqual(is_week_format('week'), False)


class TestDateFormatter(unittest.TestCase):
    """
    日付フォーマット処理 テストクラス
    """

    def test_date_formatter_ok(self):
        self.assertEqual(
            date_formatter(2025, 2, 22),
            datetime(2025, 2, 22))

    def test_date_formatter_ok_str_padding_0(self):
        self.assertEqual(
            date_formatter('0190', '02', '01'),
            datetime(190, 2, 1))

    def test_date_formatter_leap_day(self):
        self.assertEqual(
            date_formatter(2024,2,29),
            datetime(2024, 2, 29)
        )

    def test_date_formatter_non_day(self):
        self.assertEqual(
            date_formatter(2025,2,29),
            None
        )
    def test_date_formatter_non_month(self):
        self.assertEqual(
            date_formatter(2025,14,9),
            None
        )

    def test_date_formatter_non_year(self):
        self.assertEqual(
            date_formatter(-2025,2,9),
            None
        )


class TestPrintDay(unittest.TestCase):
    """
    結果出力処理 テストクラス
    """
    def setUp(self):
        test_date = '2025-02-23 12:34:56'
        self.dt_now = datetime.strptime(test_date, '%Y-%m-%d %H:%M:%S')

    def test_print_day_ok(self):
        # 例外が発生しない確認
        try:
            print_day(self.dt_now)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_print_day_AttributeError(self):
        # 例外が発生する確認
        with self.assertRaises(AttributeError):
            print_day("aaaa")


class TestSearchDay(unittest.TestCase):
    def test_search_day_20240222_increment(self):
        # 例外が発生しない確認
        try:
            search_day(2024, 2, 22, 'Saturday', 1, False)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_search_day_20240222_decrement(self):
        # 例外が発生しない確認
        try:
            search_day(2024, 2, 22, 'Saturday', -1, False)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_search_day_21240222_increment(self):
        # 例外が発生しない確認
        try:
            search_day(2124, 2, 22, 'Saturday', 1, False)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_search_day_21240222_decrement(self):
        # 例外が発生しない確認
        try:
            search_day(2124, 2, 22, 'Saturday', -1, False)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_search_day_20240229_increment(self):
        # 例外が発生しない確認
        try:
            search_day(2024, 2, 29, 'Saturday', 1, True)
        except Exception as e:
            self.fail("例外発生：" + str(e))

    def test_search_day_20240229_decrement(self):
        # 例外が発生しない確認
        try:
            search_day(2024, 2, 29, 'Saturday', -1, True)
        except Exception as e:
            self.fail("例外発生：" + str(e))

class TestGetLeapdays(unittest.TestCase):
    """
    閏年を算出する処理 テストクラス
    """
    def test_get_leapdays_increment_ok(self):
        self.assertEqual(get_leapdays(2025, 1), 2028)

    def test_get_leapdays_decrement_ok(self):
        self.assertEqual(get_leapdays(2025, -1), 2024)

    def test_get_leapdays_increment_ok_1000(self):
        self.assertEqual(get_leapdays(998, 1), 1004)

    def test_get_leapdays_decrement_ok_1000(self):
        self.assertEqual(get_leapdays(1001, -1), 996)

if __name__ == '__main__':
    unittest.main()
