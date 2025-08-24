public class XorEncryptDecryptMain {

  /**
   * XOR暗号処理
   *
   * @param data: 暗号・復号化対象
   * @param key:  暗号・復号化キー
   * @return: 暗号・復号済みデータ
   */
  private static byte[] xorProcess(byte[] data, byte key) {
    // 暗号化対象データ桁分のバイト配列をセット
    byte[] result = new byte[data.length];

    // データの桁数分繰り返し
    for (int i = 0; i < data.length; i++) {
      // XOR
      result[i] = (byte) (data[i] ^ key);
    }
    return result;
  }

  public static void main(String[] args) {
    // 暗号化対象文字列をセット
    String message = "SecretMessage";

    // 鍵 (XOR 用): 範囲は -128 ～ 127
    byte key = 0x5A;

    // 暗号化
    byte[] encrypted = xorProcess(message.getBytes(), key);

    // 暗号化データをバイト表示
    System.out.println("暗号化データ:");
    for (byte b : encrypted) {
      System.out.print((b & 0xFF) + " ");
    }
    System.out.println();

    // 暗号化バイトデータを文字列変換し表示
    String resultEncrypted = new String(encrypted);
    System.out.println("暗号化結果: " + resultEncrypted);

    // 復号化（同じ処理をもう一度）
    byte[] decrypted = xorProcess(encrypted, key);

    // 復号化結果を文字列変換し表示
    String result = new String(decrypted);
    System.out.println("復号化結果: " + result);
  }

}
