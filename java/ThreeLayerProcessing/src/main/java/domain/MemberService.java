package domain;

import java.util.List;

/**
 * 【ドメイン層】会員に関する「業務ルール（ビジネスロジック）」をまとめたクラス。
 *
 * <p>ドメイン層の役割：
 * <ul>
 *   <li>アプリの中心となる「業務のルール」を書く場所です。</li>
 *   <li>例：「18歳未満は会員登録できない」「同じメールアドレスで二重登録できない」</li>
 *   <li>画面の見た目（文字の表示方法）やデータの保存方法は知りません。</li>
 * </ul>
 *
 * <p>このクラスはデータの保存に {@link MemberRepository}（インターフェース）だけを使い、
 * 具体的な実装クラス（dataaccess パッケージのクラス）を一度も名指ししていません。
 * 実物はコンストラクタで外から受け取ります（これを「依存性の注入（DI）」と呼びます）。
 */
public class MemberService {

  /** 会員登録できる最低年齢。マジックナンバー（意味の分からない数値の直書き）を避けるため定数にする。 */
  private static final int MIN_AGE = 18;

  /** データの保存・取得を任せる相手。final にすることで、後から別のものに差し替えられないようにする。 */
  private final MemberRepository memberRepository;

  /**
   * コンストラクタ。使うリポジトリを外から受け取る。
   *
   * @param memberRepository 会員リポジトリ（実装は何でもよい）
   */
  public MemberService(MemberRepository memberRepository) {
    this.memberRepository = memberRepository;
  }

  /**
   * 会員を登録する。
   *
   * <p>業務ルールを順番にチェックし、すべて満たした場合だけ保存を依頼します。
   * ルール違反があれば {@link BusinessRuleException} を投げて処理を中断します。
   *
   * @param name  氏名
   * @param email メールアドレス
   * @param age   年齢
   * @return 登録された会員
   * @throws BusinessRuleException 業務ルールに違反した場合
   */
  public Member register(String name, String email, int age) {

    // ルール1：年齢制限。18歳未満は登録できない。
    if (age < MIN_AGE) {
      throw new BusinessRuleException(MIN_AGE + "歳未満の方は会員登録できません。（入力：" + age + "歳）");
    }

    // ルール2：メールアドレスの重複禁止。
    // findByEmail は Optional を返すので、isPresent() で「見つかったかどうか」を判定できる。
    if (memberRepository.findByEmail(email).isPresent()) {
      throw new BusinessRuleException("メールアドレス「" + email + "」は既に登録されています。");
    }

    // すべてのルールをクリアしたので、保存はデータアクセス層にお任せする。
    // ドメイン層は「保存して」とお願いするだけで、どこにどう保存されるかは気にしない。
    return memberRepository.save(name, email, age);
  }

  /**
   * 全会員を取得する。
   *
   * <p>今回は特別な業務ルールがないので、リポジトリの結果をそのまま返しています。
   * 将来「退会済みの会員は除く」などのルールが増えたら、ここに書き足します。
   *
   * @return 会員一覧
   */
  public List<Member> findAll() {
    return memberRepository.findAll();
  }
}
