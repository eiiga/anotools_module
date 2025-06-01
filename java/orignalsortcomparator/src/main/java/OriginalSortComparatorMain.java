import dto.IdNameDto;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import util.OriginalComparator;

public class OriginalSortComparatorMain {

  public static void main(String[] args) {
    IdNameDto[] idNameDto = {
        new IdNameDto(2, "B"),
        new IdNameDto(3, "C"),
        new IdNameDto(1, "A")
    };

    List<IdNameDto> list = new ArrayList<IdNameDto>(Arrays.asList(idNameDto));

    // 自作のソート処理でソート
    list.sort(new OriginalComparator());

    for (IdNameDto d : list) {
      System.out.println(d.getName());
    }
  }
}
