package constant;

public enum WarnErrorCode {

  // Warning
  WARN1("WARN1", "0001"),
  WARN2("WARN2", "0002"),
  WARN3("WARN3", "0003"),
  WARN4("WARN4", "0004"),
  WARN5("WARN5", "0005"),

  // Error
  ERROR1("ERROR1", "1001"),
  ERROR2("ERROR2", "1002"),
  ERROR3("ERROR3", "1003"),
  ERROR4("ERROR4", "1004"),
  ERROR5("ERROR5", "1005"),
  ERROR6("ERROR6", "1006"),
  ERROR7("ERROR7", "1007"),
  ERROR8("ERROR8", "1008"),
  ERROR9("ERROR9", "1009"),
  ERROR10("ERROR10", "1010");

  // 変換前WarnErrorコード
  private final String inputCode;

  // 変換後WarnErrorコード
  private final String outputCode;

  /**
   * WarnErrorコード変換Enumコンストラクタ
   *
   * @param inputCode:  変換前WarnErrorコード
   * @param outputCode: 変換後WarnErrorコード
   */
  WarnErrorCode(String inputCode, String outputCode) {
    this.inputCode = inputCode;
    this.outputCode = outputCode;
  }

  // getter: 変換前WarnErrorコード
  public String getInputCode() {
    return inputCode;
  }

  // getter: 変換後WarnErrorコード
  public String getOutputCode() {
    return outputCode;
  }

  /**
   * Warn, Error コードコンバート処理
   *
   * @param targetCode: 変換対象コード
   * @return 変換後コード
   */
  public static String getConvertCode(String targetCode) {
    // enumの要素数分繰り返し
    for (WarnErrorCode warnErrorCode : values()) {
      // 変換対象コードが変換前コードに含まれている場合
      if (warnErrorCode.inputCode.equals(targetCode)) {
        // 変換後コードを返却
        return warnErrorCode.outputCode;
      }
    }
    // 変換対象コードが変換前コードに含まれていない場合は、想定外エラーコードを返す
    return "9999";
  }

}
