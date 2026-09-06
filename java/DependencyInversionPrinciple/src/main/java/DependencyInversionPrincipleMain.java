import ok.EmailSender;
import ok.MessageSender;
import ok.SlackSender;

/**
 * 依存性逆転の原則（DIP: Dependency Inversion Principle）の学習用サンプル。
 *
 * <p>DIP はオブジェクト指向設計の原則集「SOLID」の "D" にあたるもので、内容は次の2つです。
 * <ol>
 *   <li>上位（高レベル）のモジュールは、下位（低レベル）のモジュールに依存してはならない。
 *       両者とも「抽象」に依存すべきである。</li>
 *   <li>「抽象」は「具体的な実装の詳細」に依存してはならない。
 *       「具体的な実装の詳細」が「抽象」に依存すべきである。</li>
 * </ol>
 *
 * <p>ざっくり言うと：
 * <br>「業務の流れを書くクラス」が「メール送信クラス」を直接名指しするのをやめて、
 * 間に {@code interface}（抽象）をはさみ、そこにお互いが依存するようにする、ということです。
 *
 * <h2>このサンプルの登場人物</h2>
 * <pre>
 *   ng パッケージ … DIP に違反した「悪い例」
 *     OrderCompleteService  → EmailSender を new して直接使う（送信手段がメールに固定）
 *
 *   ok パッケージ … DIP を守った「良い例」
 *     MessageSender(interface) … 「通知を送る」という抽象
 *     EmailSender / SlackSender … MessageSender を実装した具体クラス
 *     OrderCompleteService … MessageSender だけに依存し、実物は外から受け取る
 * </pre>
 */
public class DependencyInversionPrincipleMain {

  public static void main(String[] args) {

    System.out.println("========== NG例：具体クラスに直接依存している ==========");
    // 送信手段を選ぶ余地がない。内部で new EmailSender() が固定されている。
    ng.OrderCompleteService ngService = new ng.OrderCompleteService();
    ngService.completeOrder("A-001");
    System.out.println("→ Slackで通知したくなったら OrderCompleteService の中身を書き換えるしかない。");

    System.out.println();
    System.out.println("========== OK例：抽象(MessageSender)に依存している ==========");

    // (1) まずはメールで通知する構成。
    //     「どの送信手段を使うか」を決めるのは "呼び出し側" である main の責務になる。
    MessageSender email = new EmailSender();
    ok.OrderCompleteService okServiceByEmail = new ok.OrderCompleteService(email);
    okServiceByEmail.completeOrder("B-100");

    System.out.println();

    // (2) 次は Slack で通知する構成。
    //     OrderCompleteService のソースは1文字も変えていないのに、通知先を差し替えられた。
    MessageSender slack = new SlackSender("orders");
    ok.OrderCompleteService okServiceBySlack = new ok.OrderCompleteService(slack);
    okServiceBySlack.completeOrder("B-101");

    System.out.println();

    // (3) おまけ：テスト用の「ダミー実装」もその場で渡せる（差し替え自由）。
    //     本物のメールを送らずに、呼ばれた内容だけを確認したい、というテストで役立つ。
    MessageSender fake = message -> System.out.println("[テスト用ダミー] 送信内容を記録しました: " + message);
    ok.OrderCompleteService okServiceForTest = new ok.OrderCompleteService(fake);
    okServiceForTest.completeOrder("B-102");

    System.out.println();
    System.out.println("【まとめ】");
    System.out.println("・高レベル(業務フロー)と低レベル(送信処理)の間に interface を置く。");
    System.out.println("・高レベルは interface だけを見る。実物は外から注入(DI)する。");
    System.out.println("・すると『機能追加・差し替え・テスト』のときに既存クラスを触らずに済む。");
  }
}
