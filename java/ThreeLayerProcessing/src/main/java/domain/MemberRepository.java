package domain;

import java.util.List;
import java.util.Optional;

/**
 * 【ドメイン層】会員データの「保存・取得」の窓口を表すインターフェース。
 *
 * <p>「リポジトリ（Repository）」は、データの保管庫という意味です。
 * ドメイン層は「会員を保存したい」「メールアドレスで探したい」という<b>やりたいこと</b>だけを
 * ここに宣言し、<b>どうやって</b>保存するか（DB？ファイル？メモリ？）は決めません。
 *
 * <p>なぜインターフェースをドメイン層に置くのか？
 * <pre>
 *   素朴に作ると依存の向きはこうなります：
 *     プレゼンテーション層 → ドメイン層 → データアクセス層
 *   これだと、DBの都合が変わるたびにドメイン層（業務ルール）まで影響を受けてしまいます。
 *
 *   そこで「インターフェースはドメイン層が持ち、データアクセス層がそれを実装する」形にすると：
 *     プレゼンテーション層 → ドメイン層 ← データアクセス層
 *   となり、一番大事な業務ルールが、DBなどの技術的な詳細に振り回されなくなります。
 *   （これを「依存性逆転の原則（DIP）」と呼びます）
 * </pre>
 */
public interface MemberRepository {

  /**
   * 会員を新しく保存し、IDが採番された会員を返す。
   *
   * @param name  氏名
   * @param email メールアドレス
   * @param age   年齢
   * @return IDが付与された会員
   */
  Member save(String name, String email, int age);

  /**
   * メールアドレスで会員を探す。
   *
   * <p>戻り値の {@link Optional} は「値があるかもしれないし、無いかもしれない」を表す箱です。
   * null を返すよりも「見つからない場合がある」ことが型で明確になり、
   * null チェック漏れによるエラー（NullPointerException）を防ぎやすくなります。
   *
   * @param email メールアドレス
   * @return 見つかった会員（見つからなければ空の Optional）
   */
  Optional<Member> findByEmail(String email);

  /**
   * 登録済みの全会員を返す。
   *
   * @return 会員の一覧
   */
  List<Member> findAll();
}
