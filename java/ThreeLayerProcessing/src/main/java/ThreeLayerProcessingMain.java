import dataaccess.InMemoryMemberRepository;
import domain.MemberRepository;
import domain.MemberService;
import presentation.MemberController;

/**
 * 3層アーキテクチャ（3-Layer Architecture）の学習用サンプル。
 *
 * <p>3層アーキテクチャとは、アプリケーションの処理を役割ごとに3つの「層」に分けて作る設計手法です。
 * 役割ごとに分けることで「どこに何が書いてあるか」が分かりやすくなり、
 * 1つの層を変更しても他の層への影響を小さく抑えられます。
 *
 * <h2>3つの層と、このサンプルでの担当クラス</h2>
 * <pre>
 *   [プレゼンテーション層] presentation パッケージ
 *       MemberController         … 入力の受付・形式チェック・結果表示
 *            |
 *            | 呼び出す
 *            v
 *   [ドメイン層] domain パッケージ
 *       MemberService            … 業務ルール（年齢制限・重複禁止）
 *       Member                   … 会員エンティティ
 *       MemberRepository         … 保存の窓口（インターフェース）
 *            ^
 *            | 実装する（implements）
 *            |
 *   [データアクセス層] dataaccess パッケージ
 *       InMemoryMemberRepository … データの保存・検索
 * </pre>
 *
 * <p>処理の流れ（会員登録の場合）：
 * <ol>
 *   <li>プレゼンテーション層が入力を受け取り、形式をチェックして int などに変換する</li>
 *   <li>ドメイン層が業務ルールをチェックする</li>
 *   <li>データアクセス層がデータを保存する</li>
 *   <li>結果が逆順に戻ってきて、プレゼンテーション層が画面に表示する</li>
 * </ol>
 *
 * <p>このクラス（main）は、各層の部品を組み立てて動かす「組み立て係」です。
 * Spring Framework などを使う実務では、この組み立てをフレームワークが自動で行ってくれます。
 */
public class ThreeLayerProcessingMain {

  public static void main(String[] args) {

    // ===== 部品の組み立て =====
    // 下の層から順に作り、上の層へ渡していく。
    // ドメイン層は MemberRepository（インターフェース）型で受け取るので、
    // 将来DB版の実装に変えたくなったら、この1行を差し替えるだけで済む。
    MemberRepository repository = new InMemoryMemberRepository(); // データアクセス層
    MemberService service = new MemberService(repository);        // ドメイン層
    MemberController controller = new MemberController(service);  // プレゼンテーション層

    // ===== ケース1：正常に登録できる =====
    System.out.println("===== ケース1：正常な登録 =====");
    controller.register("山田太郎", "yamada@example.com", "30");
    System.out.println();
    controller.register("佐藤花子", "sato@example.com", "25");
    System.out.println();

    // ===== ケース2：プレゼンテーション層で弾かれる（入力の形式エラー） =====
    // ドメイン層・データアクセス層まで処理が届かないことをログで確認してみよう。
    System.out.println("===== ケース2：入力の形式エラー（プレゼンテーション層で検出） =====");
    controller.register("鈴木一郎", "suzuki@example.com", "abc");
    System.out.println();
    controller.register("", "noname@example.com", "40");
    System.out.println();

    // ===== ケース3：ドメイン層で弾かれる（業務ルール違反） =====
    System.out.println("===== ケース3：業務ルール違反（ドメイン層で検出） =====");
    // 年齢制限違反：データアクセス層は呼ばれない
    controller.register("高橋次郎", "takahashi@example.com", "15");
    System.out.println();
    // メールアドレス重複：重複確認のためにデータアクセス層の SELECT は呼ばれるが、INSERT はされない
    controller.register("山田花子", "yamada@example.com", "28");
    System.out.println();

    // ===== ケース4：一覧表示 =====
    System.out.println("===== ケース4：会員一覧の表示 =====");
    controller.showAll();
  }
}
