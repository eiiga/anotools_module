package main;

import constant.CountInListEnum;
import java.util.HashMap;
import java.util.Map;

public class CountInListMain {

  private static final int[] LIST_DATA_1 = {
      1, 2, 6, 7, 4, 2, 4, 7, 8, 3, 3, 0, 5, 3, 2, 1, 5, 6
  };
  private static final int[] LIST_DATA_2 = {
      3, 4, 2, 8, 4, 6, 3, 8, 9, 4, 6, 7, 8, 3, 2, 5, 6, 7, 4, 1
  };

  public static void main(String[] args) {

    // list1の件数を取得
    Map<Integer, Integer> mapData1 = counter(LIST_DATA_1);
    System.out.println(mapData1);

    // list2の件数を取得
    Map<Integer, Integer> mapData2 = counter(LIST_DATA_2);
    System.out.println(mapData2);

    // 結果用Map初期化
    Map<Integer, String> resultMap = new HashMap<>();

    // list1の件数分繰り返し
    for (int numFrom1 : mapData1.keySet()) {
      // list1の値がlist2に存在する場合
      if (mapData2.containsKey(numFrom1)) {
        // list1の件数 > list2の件数
        if (mapData1.get(numFrom1) > mapData2.get(numFrom1)) {
          // FROM_1_LARGEをセット
          resultMap.put(numFrom1, CountInListEnum.FROM_FIRST_LARGE.getCountInListEnum());

        // list1の件数 < list2の件数
        } else if (mapData1.get(numFrom1) < mapData2.get(numFrom1)) {
          // FROM_2_LARGEをセット
          resultMap.put(numFrom1, CountInListEnum.FROM_SECOND_LARGE.getCountInListEnum());

        // list1の件数 = list2の件数
        } else {
          // EQUALをセット
          resultMap.put(numFrom1, CountInListEnum.EQUAL.getCountInListEnum());
        }

      // list1の値がlist2に存在しない場合
      } else {
        // FROM_1_ONLYをセット
        resultMap.put(numFrom1, CountInListEnum.FROM_FIRST_ONLY.getCountInListEnum());
      }
    }

    // リスト2の件数分繰り返し
    for (int numFrom2 : mapData2.keySet()) {
      // list2の値がlist1に存在しない場合
      if (!mapData1.containsKey(numFrom2)) {
        // FROM_2_ONLYをセット
        resultMap.put(numFrom2, CountInListEnum.FROM_SECOND_ONLY.getCountInListEnum());
      }
    }
    // 結果出力
    System.out.println(resultMap);
  }

  /**
   * リスト内の重複する数字をカウントする処理
   * @param targetList: 対象の数字リスト
   * @return Map<Integer, Integer>: 数字ごとの件数
   */
  private static Map<Integer, Integer> counter(int[] targetList) {
    // 返却用MAP
    Map<Integer, Integer> counterMap = new HashMap<>();

    // リストの要素分繰り返し
    for (int data : targetList) {
      // すでにMapに格納ずみの場合
      if (counterMap.containsKey(data)) {
        // 件数を加算
        counterMap.put(data, counterMap.get(data) + 1);

      // Mapに値がない場合
      } else {
        // 新規で1件として格納
        counterMap.put(data, 1);
      }
    }

    return counterMap;
  }
}
