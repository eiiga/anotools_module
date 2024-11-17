package main;

public class ForAdd20Main {


  public static void main(String[] args) {

    /*
     * 2次元配列の初期値セット [ [1, 2] [3, 4, 5] [6, 7, 8] ]
     */
    final int[][] datas = new int[][] {{1, 2}, {3, 4, 5}, {6, 7, 8}};

    // 合計の初期値をセット
    int total = 0;

    // 配列の要素ブロック分繰り返し
    for (int i = 0; i < datas.length; i++) {

      // 配列の要素分繰り返し
      for (int j = i; j < datas[i].length; j++) {

        // 合計値を加算
        total += datas[i][j];
      }
    }

    // 合計値を出力
    System.out.println("合計値：" + total);

  }
}
