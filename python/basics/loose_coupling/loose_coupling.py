"""
疎結合（Loose Coupling）のサンプルコード

【疎結合とは？】
プログラムの部品（クラスや関数）同士の「つながり（依存）」を弱くする設計の考え方です。
反対の言葉は「密結合（Tight Coupling）」で、部品同士が強く結びついている状態を指します。

【例】
- 密結合：壁に直接はんだ付けされた電球。電球を LED に替えたいだけなのに、壁ごと工事が必要。
- 疎結合：ソケット式の電球。ソケット（＝決められた形・約束事）に合えば、
          白熱電球でも LED でも差し替えるだけで使える。

プログラムでは、この「ソケット（約束事）」を「インターフェース」と呼びます。
Python では abc モジュールの抽象基底クラス（ABC）や、typing.Protocol で表現できます。

【このサンプルの題材】
「注文が完了したらお客様に通知を送る」という処理を、
  1. 密結合で書いた場合
  2. 疎結合で書いた場合
の 2 パターンで実装し、違いを比べます。
"""

# abc: 抽象基底クラス（Abstract Base Class）を作るための標準モジュール
#   ABC            : 抽象クラスを作るときに継承する親クラス
#   abstractmethod : 「子クラスで必ず実装してね」という印（デコレータ）
from abc import ABC, abstractmethod


# =============================================================================
# 1. 密結合（悪い例）
# =============================================================================

class EmailSender:
    """メールを送信するクラス（本物の送信の代わりに print で表現）"""

    def send_email(self, address: str, message: str) -> None:
        print(f"[メール] {address} 宛て: {message}")


class TightlyCoupledOrderService:
    """
    注文処理クラス（密結合版）

    【問題点】
    - クラスの中で EmailSender() を直接生成している（＝EmailSender に強く依存）
    - 「メールではなく SMS で通知したい」となったら、このクラスのコードを書き換える必要がある
    - テストを実行するたびに（本物なら）実際にメールが送られてしまう
    """

    def __init__(self) -> None:
        # ★ここが密結合の原因：使う部品を自分で決め打ちで作っている
        self.sender = EmailSender()

    def place_order(self, customer: str, item: str) -> None:
        print(f"注文受付: {customer} 様 / 商品: {item}")
        # メソッド名 send_email にまで依存している
        self.sender.send_email(customer, f"{item} のご注文ありがとうございます")


# =============================================================================
# 2. 疎結合（良い例）
# =============================================================================

# -----------------------------------------------------------------------------
# 2-1. インターフェース（約束事）を定義する
# -----------------------------------------------------------------------------
class Notifier(ABC):
    """
    通知手段の「約束事」を表す抽象クラス

    「通知する部品なら、send(宛先, メッセージ) というメソッドを必ず持っていること」
    というルールだけを決めています。
    “どうやって送るか” は一切書きません。それは子クラスの仕事です。
    """

    @abstractmethod
    def send(self, to: str, message: str) -> None:
        # 中身は書かない（pass でも ... でもよい）
        # @abstractmethod を付けたメソッドを実装していない子クラスは、
        # インスタンスを作ろうとした時点でエラー（TypeError）になります。
        ...


# -----------------------------------------------------------------------------
# 2-2. 約束事に従った「具体的な部品」を作る
# -----------------------------------------------------------------------------
class EmailNotifier(Notifier):
    """メールで通知する部品"""

    def send(self, to: str, message: str) -> None:
        print(f"[メール] {to} 宛て: {message}")


class SmsNotifier(Notifier):
    """SMS で通知する部品"""

    def send(self, to: str, message: str) -> None:
        print(f"[SMS] {to} 宛て: {message}")


class SlackNotifier(Notifier):
    """Slack で通知する部品（後から追加しても OrderService の修正は不要！）"""

    def __init__(self, channel: str) -> None:
        self.channel = channel

    def send(self, to: str, message: str) -> None:
        print(f"[Slack #{self.channel}] @{to}: {message}")


# -----------------------------------------------------------------------------
# 2-3. 部品を「外から受け取る」クラスを作る
# -----------------------------------------------------------------------------
class OrderService:
    """
    注文処理クラス（疎結合版）

    【ポイント】
    - 通知の部品を自分で作らず、コンストラクタの引数で「外から受け取る」
      → この手法を「依存性の注入（Dependency Injection / DI）」と呼びます
    - 型ヒントは具体的なクラス（EmailNotifier など）ではなく、
      約束事（Notifier）にしている
      → 「Notifier の約束を守っていれば何でも OK」という意味になる
    - OrderService はメールなのか SMS なのかを知らない（知る必要がない）
    """

    def __init__(self, notifier: Notifier) -> None:
        # ★外から渡された部品をそのまま保持するだけ
        self.notifier = notifier

    def place_order(self, customer: str, item: str) -> str:
        print(f"注文受付: {customer} 様 / 商品: {item}")
        message = f"{item} のご注文ありがとうございます"
        # 約束事で決めた send() だけを呼ぶ。中身がどう動くかは部品次第
        self.notifier.send(customer, message)
        # テストしやすいように、送ったメッセージを戻り値で返しておく
        return message


# =============================================================================
# 3. 動作確認
# =============================================================================
def main() -> None:
    print("=" * 60)
    print("1. 密結合の例")
    print("=" * 60)
    # 通知手段はメールに固定。変えたければ TightlyCoupledOrderService を書き換えるしかない
    tight_service = TightlyCoupledOrderService()
    tight_service.place_order("tanaka@example.com", "ノートPC")

    print()
    print("=" * 60)
    print("2. 疎結合の例")
    print("=" * 60)
    # 同じ OrderService クラスのまま、渡す部品を変えるだけで通知手段を切り替えられる
    # どの部品を使うかを「使う側（ここでは main 関数）」が決めているのがポイント
    notifiers: list[Notifier] = [
        EmailNotifier(),
        SmsNotifier(),
        SlackNotifier(channel="orders"),
    ]
    for notifier in notifiers:
        # クラス名を表示して、どの部品を差し込んだか分かるようにする
        print(f"--- 差し込んだ部品: {type(notifier).__name__} ---")
        service = OrderService(notifier)
        service.place_order("tanaka", "ノートPC")

    print()
    print("=" * 60)
    print("3. 約束事を守らない部品はエラーになる")
    print("=" * 60)

    # send() を実装し忘れた（約束を守っていない）クラス
    class BrokenNotifier(Notifier):
        pass

    try:
        BrokenNotifier()
    except TypeError as e:
        # 「抽象メソッド send を実装していないのでインスタンス化できない」というエラー
        print(f"TypeError: {e}")


# このファイルを直接実行したときだけ main() を呼ぶ
# （他のファイルから import されたときは実行されない）
if __name__ == "__main__":
    main()
