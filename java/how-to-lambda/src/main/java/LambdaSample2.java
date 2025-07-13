import java.util.Arrays;
import java.util.List;

public class LambdaSample2 {

  public static void main(String[] args) {
    List<String> names = Arrays.asList("apple", "banana", "orange");

    // names.forEach(name -> System.out.println(name));
    names.forEach(System.out::println);
  }
}
