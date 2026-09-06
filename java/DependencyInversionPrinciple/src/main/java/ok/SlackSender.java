package ok;

/**
 * 【OK例】Slackで通知する具体的な実装（低レベルモジュール）。
 *
 * <p>ポイント：この新しい送信手段を追加しても、
 * 高レベルモジュール（{@link OrderCompleteService}）は一切変更しなくてよい。
 * 「機能追加のときに既存コードを触らなくて済む」のが DIP の実利です。
 */
public class SlackSender implements MessageSender {

  /** 投稿先チャンネル名。コンストラクタで受け取り、送信先を柔軟に変えられるようにしている。 */
  private final String channel;

  public SlackSender(String channel) {
    this.channel = channel;
  }

  @Override
  public void send(String message) {
    System.out.println("[Slack投稿] #" + channel + " : " + message);
  }
}
