package ng;

/**
 * 【NG例】メール送信を担当する「低レベルモジュール（＝具体的な処理の担当者）」。
 *
 * <p>「低レベル」とは "レベルが低い＝ダメ" という意味ではなく、
 * 「実際の細かい処理（メールを送る、DBに保存する等）を行う部品」という意味です。
 * 逆に「高レベルモジュール」は、それらの部品を使って業務の流れを組み立てる側を指します。
 */
public class EmailSender {

  /**
   * メールを送信する（ここでは学習用に、送った内容をコンソールに表示するだけ）。
   *
   * @param message 送りたい本文
   */
  public void sendEmail(String message) {
    System.out.println("[メール送信] " + message);
  }
}
