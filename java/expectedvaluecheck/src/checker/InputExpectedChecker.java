package checker;

import java.util.HashMap;
import constant.CsvHeaderConstant;

// 相互比較クラス
public class InputExpectedChecker {

  /*
   * 期待値 -> 実測値 比較処理
   * 
   * @param expectedDatas 期待値HashMap
   * 
   * @param inputDatas 予測値HashMap
   */
  public static void expectedInputChecker(HashMap<Integer, HashMap<String, String>> expectedDatas,
      HashMap<Integer, HashMap<String, String>> inputDatas) {
    // チェックフラグ（true:比較OK、false：比較NG）
    boolean isData = true;

    // csvヘッダ部要素配列
    final CsvHeaderConstant[] keyHeaders = CsvHeaderConstant.values();

    System.out.println("##### 相互参照：期待値->実測値 #####");

    // 期待値のキー項目分繰り返し
    for (Integer keyCount : expectedDatas.keySet()) {

      // チェックフラグ初期化
      isData = true;

      System.out.println("===== データ：" + keyCount + " =====");

      // csvヘッダ部配列要素分繰り返し
      for (CsvHeaderConstant keyHeader : keyHeaders) {

        // ヘッダ部が日付の項目はチェック対象外
        if (CsvHeaderConstant.TARGET_DATE.equals(keyHeader)) {
          continue;
        }

        // 実測値にデータが存在しない場合
        if (inputDatas.get(keyCount) == null) {

          // 結果出力
          System.out.println("*** " + keyHeader.getCsvHeaderConstant() + " ***");
          System.out
              .println("期待値：" + expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));
          System.out.println("実測値：データなし");

          // チェックフラグNG
          isData = false;

          // 期待値と実測値が異なる場合
        } else if (!expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant())
            .equals(inputDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()))) {

          // 結果出力
          System.out.println("*** " + keyHeader.getCsvHeaderConstant() + " ***");
          System.out
              .println("期待値：" + expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));
          System.out
              .println("実測値：" + inputDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));

          // チェックフラグNG
          isData = false;

        }
      }
      // チェックフラグOKの場合
      if (isData) {
        // 結果出力
        System.out.println("OK");
      }
    }
  }

  /*
   * 実測値 -> 期待値 比較処理
   * 
   * @param expectedDatas 期待値HashMap
   * 
   * @param inputDatas 予測値HashMap
   */
  public static void inputExpectedChecker(HashMap<Integer, HashMap<String, String>> expectedDatas,
      HashMap<Integer, HashMap<String, String>> inputDatas) {

    // チェックフラグ（true:比較OK、false：比較NG）
    boolean isData = true;

    // csvヘッダ部要素配列
    final CsvHeaderConstant[] keyHeaders = CsvHeaderConstant.values();

    System.out.println("##### 相互参照：実測値->期待値 #####");

    for (Integer keyCount : inputDatas.keySet()) {
      if (expectedDatas.get(keyCount) == null) {
        System.out.println("===== データ：" + keyCount + " =====");
        // csvヘッダ部配列要素分繰り返し
        for (CsvHeaderConstant keyHeader : keyHeaders) {
          if (CsvHeaderConstant.TARGET_DATE.equals(keyHeader)) {
            continue;
          }

          System.out.println("*** " + keyHeader.getCsvHeaderConstant() + " ***");
          System.out.println("期待値：データなし");
          System.out
              .println("実測値：" + inputDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));

          // チェックフラグNG
          isData = false;
        }
      }
    }
    // チェックフラグOKの場合
    if (isData) {
      // 結果出力
      System.out.println("OK");
    }
  }
}
