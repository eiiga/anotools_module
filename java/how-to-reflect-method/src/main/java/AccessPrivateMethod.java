import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class PrivateMethodClass {

  private String saySecretMessage(String message) {
    return String.format("Secret Message: %s", message);
  }
}

public class AccessPrivateMethod {

  public static void main(String[] args)
      throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
    Class<?> sampleClass = PrivateMethodClass.class;
    Method method = sampleClass.getDeclaredMethod("saySecretMessage", String.class);

    // private method アクセス許可
    method.setAccessible(true);

    Object obj = sampleClass.getDeclaredConstructor().newInstance();
    String result = (String) method.invoke(obj, "accessed private method");

    System.out.println(result);
  }
}
