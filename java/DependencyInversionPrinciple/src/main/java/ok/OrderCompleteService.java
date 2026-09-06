package ok;

/**
 * 【OK例】注文完了の業務フローを担当する「高レベルモジュール」。
 *
 * <p>NG例との違いは1点だけ：
 * <b>具体的なクラス（EmailSender など）ではなく、抽象 {@link MessageSender} に依存している</b>こと。
 *
 * <ul>
 *   <li>{@code new} で送信手段を作らず、コンストラクタで「外から受け取る」（＝依存性の注入 / DI）。</li>
 *   <li>メール・Slack・テスト用のダミーなど、何を渡すかは呼び出し側の自由。</li>
 *   <li>このクラスは「通知する」という約束（インターフェース）だけを知っていればよい。</li>
 * </ul>
 */
public class OrderCompleteService {

  // 抽象への参照だけを持つ。中身が何なのか（メールかSlackか）はこのクラスは知らない。
  private final MessageSender messageSender;

  /**
   * @param messageSender 使いたい通知手段。呼び出し側が決めて渡す（コンストラクタ・インジェクション）。
   */
  public OrderCompleteService(MessageSender messageSender) {
    this.messageSender = messageSender;
  }

  /**
   * 注文を完了し、購入者へ通知する。
   *
   * @param orderId 注文番号
   */
  public void completeOrder(String orderId) {
    // 本来ここに「在庫を減らす」「注文ステータスを更新する」等の業務処理が入る想定。
    System.out.println("注文 " + orderId + " を完了しました。");

    // 実際の送信手段が何であっても、呼び出し方は同じ1行で済む。
    messageSender.send("ご注文 " + orderId + " を承りました。");
  }
}
