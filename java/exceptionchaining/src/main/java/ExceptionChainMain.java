import java.io.IOException;

public class ExceptionChainMain {

  /**
   * 最下層のCause取得処理
   *
   * @param throwable: 例外
   * @return: 最下層のCause
   */
  public static Throwable getRootCause(Throwable throwable) {
    Throwable cause = throwable;

    // 次の階層のcauseがnullになるまで繰り返し
    while (cause.getCause() != null) {
      // 次のcauseをセット
      cause = cause.getCause();
    }
    return cause;
  }

  public static void main(String[] args) {
    // 4段階の例外チェーンを構築
    // Exception -> RuntimeException -> IllegalArgumentException -> IOException
    IOException ioException = new IOException("Disk failure");
    IllegalArgumentException illegalArgumentException = new IllegalArgumentException(
        "Invalid argument", ioException);
    RuntimeException runtimeException = new RuntimeException("Runtime wrapper",
        illegalArgumentException);
    Exception topException = new Exception("Top level exception", runtimeException);

    // 1回 getCause()
    Throwable cause1 = topException.getCause();
    System.out.println("1st cause: " + cause1);

    // 2回 getCause()
    Throwable cause2 = topException.getCause().getCause();
    System.out.println("2nd cause: " + cause2);

    // 3回 getCause()
    Throwable cause3 = topException.getCause().getCause().getCause();
    System.out.println("3rd cause: " + cause3);

    // 4回 getCause(): null
    Throwable cause4 = topException.getCause().getCause().getCause().getCause();
    System.out.println("4rd cause: " + cause4);

    // 最下層のcauseを呼び出し
    System.out.println("最下層 cause: " + getRootCause(topException));
  }
}
