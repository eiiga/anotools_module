package domain;

/**
 * 【ドメイン層】会員を表す「エンティティ」。
 *
 * <p>エンティティとは、業務の世界に登場する「モノ」や「人」をプログラムで表現したものです。
 * ここでは「会員」を表しています。
 *
 * <p>ポイント：
 * <ul>
 *   <li>このクラスは画面（プレゼンテーション層）やデータベース（データアクセス層）のことを一切知りません。</li>
 *   <li>そのため、画面がWebからスマホアプリに変わっても、DBが変わっても、このクラスは書き換え不要です。</li>
 * </ul>
 *
 * <p>Java 16 以降で使える {@code record} を使っています。
 * record は「値を入れて取り出すだけのクラス」を短く書くための構文で、
 * コンストラクタ・getter（{@code id()} や {@code name()}）・equals・toString を自動で作ってくれます。
 *
 * @param id    会員ID（データアクセス層で採番される）
 * @param name  氏名
 * @param email メールアドレス
 * @param age   年齢
 */
public record Member(int id, String name, String email, int age) {
}
