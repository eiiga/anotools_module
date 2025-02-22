from datetime import datetime, timedelta
import unittest

from get_next_and_last_day.main import is_week_format, date_formatter

WEEK_LIST = ['Sunday',
             'Monday',
             'Tuesday',
             'Wednesday',
             'Thursday',
             'Friday',
             'Saturday']

class IsWeekFormat(unittest.TestCase):
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

class IsDateFormat(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
