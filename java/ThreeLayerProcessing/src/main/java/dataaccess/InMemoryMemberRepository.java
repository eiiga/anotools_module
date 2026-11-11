package dataaccess;

import domain.Member;
import domain.MemberRepository;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * 【データアクセス層】会員データをメモリ上に保存するリポジトリの実装。
 *
 * <p>データアクセス層の役割：
 * <ul>
 *   <li>データベースやファイルなど「データの置き場所」とのやり取りを担当します。</li>
 *   <li>業務ルール（年齢制限など）は一切書きません。言われた通りに保存・検索するだけです。</li>
 * </ul>
 *
 * <p>本来はここで SQL を発行して DB に保存しますが、学習用に環境構築なしで動くよう、
 * {@link Map} を「なんちゃってDBテーブル」として使っています。
 *
 * <p>ドメイン層の {@link MemberRepository} を {@code implements}（実装）しているのがポイントです。
 * 将来本物のDBを使うときは、例えば {@code JdbcMemberRepository} という別クラスを作り、
 * 同じく MemberRepository を実装すれば、ドメイン層を1行も変えずに差し替えられます。
 */
public class InMemoryMemberRepository implements MemberRepository {

  /**
   * 会員データの保存先（DBのテーブル代わり）。キーが会員ID、値が会員。
   *
   * <p>{@link LinkedHashMap} は「入れた順番」を覚えてくれる Map です。
   * 普通の HashMap だと順番がバラバラになるため、一覧表示の順序を安定させる目的で使っています。
   */
  private final Map<Integer, Member> table = new LinkedHashMap<>();

  /** 次に割り当てる会員ID。DBの「自動採番（AUTO_INCREMENT）」の代わり。 */
  private int nextId = 1;

  @Override
  public Member save(String name, String email, int age) {
    // IDを採番してから会員オブジェクトを作る。nextId++ は「今の値を使ってから1増やす」という意味。
    Member member = new Member(nextId++, name, email, age);
    table.put(member.id(), member);

    // 実際のDBアクセスのイメージが湧くように、発行されるであろうSQLをログとして表示する。
    System.out.println("  [DataAccess] INSERT INTO member VALUES ("
        + member.id() + ", '" + name + "', '" + email + "', " + age + ")");
    return member;
  }

  @Override
  public Optional<Member> findByEmail(String email) {
    System.out.println("  [DataAccess] SELECT * FROM member WHERE email = '" + email + "'");

    // Stream API を使った検索。
    //   values()      : Map に入っている全会員を取り出す
    //   stream()      : 1件ずつ流れ作業で処理できる形にする
    //   filter(...)   : 条件（メールアドレスが一致）に合うものだけ残す
    //   findFirst()   : 最初の1件を Optional に入れて返す（無ければ空の Optional）
    return table.values().stream()
        .filter(member -> member.email().equals(email))
        .findFirst();
  }

  @Override
  public List<Member> findAll() {
    System.out.println("  [DataAccess] SELECT * FROM member");

    // 内部の Map をそのまま渡すと、呼び出し側に中身を書き換えられてしまう恐れがある。
    // そこで新しい List にコピーして返す（防御的コピー）。
    return new ArrayList<>(table.values());
  }
}
