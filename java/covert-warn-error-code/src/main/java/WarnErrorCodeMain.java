import constant.WarnErrorCode;

public class WarnErrorCodeMain {

  public static void main(String[] args) {
    // Warnサンプル
    String warnSampleCode3 = "WARN3";
    System.out.printf("warnSampleCode3(before): %s%n", warnSampleCode3);
    System.out.printf("warnSampleCode3(after): %s%n",
        WarnErrorCode.getConvertCode(warnSampleCode3));
    System.out.println("###########################");

    // Errorサンプル
    String errorSampleCode7 = "ERROR7";
    System.out.printf("errorSampleCode7(before): %s%n", errorSampleCode7);
    System.out.printf("errorSampleCode7(after): %s%n",
        WarnErrorCode.getConvertCode(errorSampleCode7));
    System.out.println("###########################");

    // 想定外サンプル
    String otherSampleCode = "AAAAAA";
    System.out.printf("otherSampleCode(before): %s%n", otherSampleCode);
    System.out.printf("otherSampleCode(after): %s%n",
        WarnErrorCode.getConvertCode(otherSampleCode));
    System.out.println("###########################");
  }
}
