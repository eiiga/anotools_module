import pytest

from src.pytest_target_sample_cal import Cal


# 関数で実行(先頭に`test_`を記載する)
def test_add_for_num():
    cal = Cal()
    # 一致テスト（0 + 1 + ... + 9）
    assert cal.add_for_num(10) == 45

    # 不一致テスト（0 + 1）
    assert cal.add_for_num(2) != 9


def test_add_num_and_double_raise_value_error():
    # 例外テスト
    with pytest.raises(ValueError):
        cal = Cal()
        cal.add_for_num('1')


# クラスで実行(先頭に`Test`を記載する)
class TestCal:
    def test_test_add_num_and_double(self):
        cal = Cal()
        # 一致テスト
        assert cal.add_for_num(1) == 1
