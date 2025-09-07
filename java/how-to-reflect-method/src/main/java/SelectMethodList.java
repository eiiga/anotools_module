import java.lang.reflect.Method;

class MethodList {

  public void method1() {
    // nop
  }

  private int method2(int num) {
    return num * 2;
  }

  protected String method3() {
    return "hello";
  }
}

public class SelectMethodList {

  public static void main(String[] args) {
    Class<?> sampleClass = MethodList.class;

    // 宣言されたすべてのメソッド（private含む）
    for (Method m : sampleClass.getDeclaredMethods()) {
      System.out.println("Declared: " + m);
    }
  }
}
