package util;

import dto.IdNameDto;
import java.util.Comparator;

public class OriginalComparator implements Comparator<IdNameDto> {

  // 大きい順に変更
  @Override
  public int compare(IdNameDto data1, IdNameDto data2) {
    if (data1.getId() < data2.getId()) {
      // 1: data2が前
      return 1;
    }

    if (data1.getId() > data2.getId()) {
      // -1: data1が前
      return -1;
    }
    // 変更なし
    return 0;
  }
}
