package presentation;

import domain.BusinessRuleException;
import domain.Member;
import domain.MemberService;
import java.util.List;

/**
 * 【プレゼンテーション層】利用者からの入力を受け取り、結果を表示するクラス。
 *
 * <p>プレゼンテーション層の役割：
 * <ul>
 *   <li>利用者との「受付窓口」です。Webアプリなら画面やAPI、今回はコンソール出力が該当します。</li>
 *   <li>入力値の<b>形式</b>チェック（空でないか、数字かどうか）や、型の変換（文字列→int）を行います。</li>
 *   <li>結果やエラーを、利用者に分かりやすい形に整えて表示します。</li>
 *   <li>業務ルール（年齢制限など）は書きません。それはドメイン層の仕事です。</li>
 * </ul>
 *
 * <p>「形式チェック」と「業務ルールチェック」の違い：
 * <pre>
 *   形式チェック（ここ）    : "abc" は年齢として数字じゃない → 画面の入力ミス
 *   業務ルール（ドメイン層）: 15歳は登録できない           → 業務上の決まり
 * </pre>
 * 業務ルールをドメイン層にまとめておけば、画面がWebでもスマホでもバッチでも、同じルールが必ず適用されます。
 */
public class MemberController {

  /** 業務処理を依頼する相手（ドメイン層）。 */
  private final MemberService memberService;

  /**
   * @param memberService 会員サービス
   */
  public MemberController(MemberService memberService) {
    this.memberService = memberService;
  }

  /**
   * 会員登録リクエストを処理する。
   *
   * <p>画面のフォームから送られてくる値は、基本的にすべて「文字列」です。
   * そのため引数もあえて全部 String にして、Webフォームからの入力を模しています。
   *
   * @param name     氏名（入力値）
   * @param email    メールアドレス（入力値）
   * @param ageInput 年齢（入力値。文字列のまま受け取る）
   */
  public void register(String name, String email, String ageInput) {
    System.out.println("[Presentation] 会員登録リクエスト受付: name=" + name
        + ", email=" + email + ", age=" + ageInput);

    // ---------- (1) 入力の形式チェック ----------
    // isBlank() は「空文字、またはスペースだけ」の場合に true を返す（Java 11 以降）。
    if (name == null || name.isBlank()) {
      showError("氏名を入力してください。");
      return; // エラーなのでここで処理を終える（ドメイン層は呼ばない）
    }
    if (email == null || !email.contains("@")) {
      showError("メールアドレスの形式が正しくありません。");
      return;
    }

    // ---------- (2) 型の変換（文字列 → 数値） ----------
    int age;
    try {
      // Integer.parseInt は数字以外の文字列を渡すと NumberFormatException を投げる。
      age = Integer.parseInt(ageInput);
    } catch (NumberFormatException e) {
      showError("年齢は数字で入力してください。（入力：" + ageInput + "）");
      return;
    }

    // ---------- (3) ドメイン層に業務処理を依頼 ----------
    try {
      Member member = memberService.register(name, email, age);
      // ---------- (4) 結果を利用者向けに整形して表示 ----------
      System.out.println("[Presentation] 登録が完了しました。会員ID: " + member.id());
    } catch (BusinessRuleException e) {
      // ドメイン層が「業務ルール違反」と判断した場合は、そのメッセージを画面に出す。
      showError(e.getMessage());
    }
  }

  /**
   * 会員一覧を表示する。
   */
  public void showAll() {
    System.out.println("[Presentation] 会員一覧リクエスト受付");
    List<Member> members = memberService.findAll();

    // 表示の形を整えるのはプレゼンテーション層の仕事。
    // String.format は「%d（整数）」「%s（文字列）」の部分に、後ろの引数を順番に埋め込んでくれる。
    // 例えば年齢を「30歳」と表示する、といった見せ方の工夫もここで行う。
    for (Member member : members) {
      System.out.println(String.format("  会員ID:%d  氏名:%s  メール:%s  年齢:%d歳",
          member.id(), member.name(), member.email(), member.age()));
    }
    System.out.println("  （全 " + members.size() + " 件）");
  }

  /**
   * エラーメッセージを表示する共通処理。
   *
   * @param message エラーメッセージ
   */
  private void showError(String message) {
    System.out.println("[Presentation] エラー: " + message);
  }
}
