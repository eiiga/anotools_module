package ng;

/**
 * 【NG例】注文完了の業務フローを担当する「高レベルモジュール」。
 *
 * <p>問題点：このクラスは {@link EmailSender} という「具体的なクラス」に直接依存しています。
 * <ul>
 *   <li>クラスの内部で {@code new EmailSender()} していて、送信手段が「メール」に固定されている。</li>
 *   <li>あとから「Slackで通知したい」となったら、このクラス自体を書き換える必要がある。</li>
 *   <li>テストのときも本物の EmailSender が動いてしまい、差し替えができない。</li>
 * </ul>
 * これが「高レベルモジュールが低レベルモジュールに依存している」状態で、
 * 依存性逆転の原則（DIP）に違反しているコードです。
 */
public class OrderCompleteService {

  // 具体的なクラスを名指しで持ってしまっている（＝密結合）。
  private final EmailSender emailSender = new EmailSender();

  /**
   * 注文を完了し、購入者へ通知する。
   *
   * @param orderId 注文番号
   */
  public void completeOrder(String orderId) {
    // 本来ここに「在庫を減らす」「注文ステータスを更新する」等の業務処理が入る想定。
    System.out.println("注文 " + orderId + " を完了しました。");

    // 通知手段が EmailSender に固定されている。ここを Slack に変えたい場合、
    // このクラスのソースコードを直接修正するしかない。
    emailSender.sendEmail("ご注文 " + orderId + " を承りました。");
  }
}
