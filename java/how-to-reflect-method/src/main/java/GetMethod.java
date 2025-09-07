import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class SampleClass {

  public void sayHelloName(String name) {
    System.out.printf("Hello %s !!%n", name);
  }
}

public class GetMethod {

  public static void main(String[] args)
      throws NoSuchMethodException, InvocationTargetException, InstantiationException,
      IllegalAccessException {
    // classを取得
    Class<?> sampleClass = SampleClass.class;

    // メソッドを取得
    Method method = sampleClass.getMethod("sayHelloName", String.class);

    // インスタンス作成
    Object obj = sampleClass.getDeclaredConstructor().newInstance();

    // メソッドを実行
    method.invoke(obj, "AAA");
  }

}
