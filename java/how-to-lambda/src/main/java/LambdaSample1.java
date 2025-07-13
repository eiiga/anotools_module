import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class LambdaSample1 {

  public static void main(String[] args) {
    // 引数あり、戻り値あり
    Function<Integer, Integer> square = x -> x * x;
    System.out.println(square.apply(5));

    // 引数あり、戻り値なし
    Consumer<String> printer = message -> System.out.println("メッセージ: " + message);
    printer.accept("こんにちは");

    // 引数なし、戻り値あり
    Supplier<Double> randomSupplier = () -> Math.random();
    System.out.println(randomSupplier.get());

    // 引数あり、戻り値Boolean
    Predicate<Integer> judgement = num -> {
      int result = num + 3;
      return result == 9;
    };
    System.out.println(judgement.test(6));

    // 引数なし、戻り値なし
    Runnable task = () -> System.out.println("実行中...");
    task.run();

  }

}
