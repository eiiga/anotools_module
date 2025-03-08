package main;

import constant.CountInListEnum;
import java.util.HashMap;
import java.util.Map;

public class CountInListMain {

  private static final int[] LIST_DATA_1 = {
      1, 2, 6, 7, 4, 2, 4, 7, 8, 3, 3, 0, 5, 3, 2, 1, 5, 6
  };
  private static final int[] LIST_DATA_2 = {
      3, 4, 2, 8, 4, 6, 3, 8, 9, 4, 6, 7, 8, 3, 2, 5, 6, 7, 4, 1,
  };

  public static void main(String[] args) {

    Map<Integer, Integer> mapData1 = counter(LIST_DATA_1);
    System.out.println(mapData1);

    Map<Integer, Integer> mapData2 = counter(LIST_DATA_2);
    System.out.println(mapData2);

    Map<Integer, String> resultMap = new HashMap<>();

    for (int numFrom1 : mapData1.keySet()) {
      // list1の値がlist2に存在する場合
      if (mapData2.containsKey(numFrom1)) {
        // list1の件数 > list2の件数
        if (mapData1.get(numFrom1) > mapData2.get(numFrom1)) {
          resultMap.put(numFrom1, CountInListEnum.FROM_FIRST_LARGE.getCountInListEnum());

        // list1の件数 < list2の件数
        } else if (mapData1.get(numFrom1) < mapData2.get(numFrom1)) {
          resultMap.put(numFrom1, CountInListEnum.FROM_SECOND_LARGE.getCountInListEnum());

        // list1の件数 = list2の件数
        } else {
          resultMap.put(numFrom1, CountInListEnum.EQUAL.getCountInListEnum());
        }

      // list1の値がlist2に存在しない場合
      } else {
        resultMap.put(numFrom1, CountInListEnum.FROM_FIRST_ONLY.getCountInListEnum());
      }
    }

    for (int numFrom2 : mapData2.keySet()) {
      // list2の値がlist1に存在しない場合
      if (!mapData1.containsKey(numFrom2)) {
        resultMap.put(numFrom2, CountInListEnum.FROM_SECOND_ONLY.getCountInListEnum());
      }
    }

    System.out.println(resultMap);
  }

  private static Map<Integer, Integer> counter(int[] targetList) {
    Map<Integer, Integer> counterMap = new HashMap<>();

    for (int data : targetList) {
      if (counterMap.containsKey(data)) {
        counterMap.put(data, counterMap.get(data) + 1);
      } else {
        counterMap.put(data, 1);
      }
    }

    return counterMap;
  }
}
