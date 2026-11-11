package domain;

/**
 * 【ドメイン層】業務ルールに違反したときに投げる例外。
 *
 * <p>例：「18歳未満は登録できない」「同じメールアドレスは登録できない」など。
 *
 * <p>{@link RuntimeException} を継承しているので「非検査例外」になります。
 * 非検査例外は、呼び出し側で {@code throws} や {@code try-catch} を書くことが強制されません。
 * 今回はプレゼンテーション層でまとめて catch し、エラーメッセージを画面に表示します。
 */
public class BusinessRuleException extends RuntimeException {

  /**
   * @param message 利用者に伝えるエラーメッセージ
   */
  public BusinessRuleException(String message) {
    // 親クラス(RuntimeException)のコンストラクタにメッセージを渡す。
    // あとで getMessage() で取り出せるようになる。
    super(message);
  }
}
