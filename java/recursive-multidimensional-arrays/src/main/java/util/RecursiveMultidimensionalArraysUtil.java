package util;

import java.lang.reflect.Array;

public class RecursiveMultidimensionalArraysUtil {

  // 再帰的に多次元配列を表示するメソッド
  public static void printArray(Object data) {
    // null 判定処理
    if (data == null) {
      return;
    }

    // 配列が存在するか
    if (data.getClass().isArray()) {
      // 配列先頭文字出力
      System.out.print("[");

      // 配列の要素数
      int length = Array.getLength(data);

      // 配列の要素数分繰り返し
      for (int i = 0; i < length; i++) {

        /* 再帰処理：配列のi番目の要素（配列 or 数値）
            ex)
              data: [1, 2, 3], i: 1 -> 2
              data: [[1, 2], [3, 4]], i: 0 -> [1, 2]
         */
        printArray(Array.get(data, i));

        if (i < length - 1) {
          // データ間の場合はカンマ＋スペースを挿入
          System.out.print(", ");
        }
      }

      // 配列末尾文字出力
      System.out.print("]");

    } else {
      // 配列でなければ値を表示
      System.out.print(data);
    }
  }
}
