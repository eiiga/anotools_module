"""
疎結合のメリットを確認するテストコード

疎結合の大きなメリットの 1 つが「テストのしやすさ」です。
OrderService は Notifier の約束（send メソッド）さえ守っていれば何でも受け取れるので、
本物のメール送信の代わりに「送った内容を記録するだけの偽物（テストダブル）」を渡せます。
これにより、実際にメールを送らずに OrderService の動きだけを確認できます。

実行方法（このファイルがあるディレクトリで）:
    python -m pytest test_loose_coupling.py -v
"""

import pytest

from loose_coupling import Notifier, OrderService


class FakeNotifier(Notifier):
    """
    テスト用の偽物の通知部品

    実際には何も送信せず、「誰に・何を送ろうとしたか」をリストに記録するだけ。
    Notifier を継承して send() を実装しているので、OrderService にそのまま渡せます。
    """

    def __init__(self) -> None:
        # 送信内容を (宛先, メッセージ) のタプルで貯めておくリスト
        self.sent: list[tuple[str, str]] = []

    def send(self, to: str, message: str) -> None:
        self.sent.append((to, message))


def test_注文すると通知が1回送られる():
    # 準備: 偽物の部品を作って OrderService に注入する
    fake = FakeNotifier()
    service = OrderService(fake)

    # 実行
    service.place_order("tanaka", "ノートPC")

    # 検証: 偽物に記録された内容を確認する
    assert fake.sent == [("tanaka", "ノートPC のご注文ありがとうございます")]


def test_戻り値は送信したメッセージ():
    service = OrderService(FakeNotifier())

    result = service.place_order("suzuki", "マウス")

    assert result == "マウス のご注文ありがとうございます"


def test_sendを実装しない部品はインスタンス化できない():
    # 約束事（抽象メソッド send）を守っていないクラス
    class BrokenNotifier(Notifier):
        pass

    # pytest.raises: ブロック内で指定した例外が発生することを確認する
    with pytest.raises(TypeError):
        BrokenNotifier()
