package ok;

/**
 * 【OK例】「通知を送る」という役割だけを定義した抽象（インターフェース）。
 *
 * <p>DIP のポイントは「具体的なクラスではなく、この抽象に依存させること」です。
 * <ul>
 *   <li>高レベルモジュール（{@link OrderCompleteService}）は、この {@code MessageSender} だけを知っていればよい。</li>
 *   <li>低レベルモジュール（{@link EmailSender} / {@link SlackSender}）は、この抽象を「実装する」側にまわる。</li>
 * </ul>
 * こうすると、両者が矢印の向きとして「抽象」を指すようになり、
 * 高レベル→低レベル だった依存の向きが "逆転" します。これが「依存性逆転」の名前の由来です。
 */
public interface MessageSender {

  /**
   * 通知を1件送信する。
   *
   * @param message 送りたい本文
   */
  void send(String message);
}
