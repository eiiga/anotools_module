package ok;

/**
 * 【OK例】メールで通知する具体的な実装（低レベルモジュール）。
 *
 * <p>{@link MessageSender} を implements しているので、
 * 「MessageSender が欲しい場所」ならどこにでも渡せる。
 */
public class EmailSender implements MessageSender {

  @Override
  public void send(String message) {
    System.out.println("[メール送信] " + message);
  }
}
