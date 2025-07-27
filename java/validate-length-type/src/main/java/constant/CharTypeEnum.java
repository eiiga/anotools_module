package constant;

public enum CharTypeEnum {
  ONLY_DIGITS("^[0-9]+$"),
  ONLY_LOWERCASE("^[a-z]+$"),
  ONLY_UPPERCASE("^[A-Z]+$"),
  ONLY_DIGITS_LOWERCASE("^[0-9a-z]+$"),
  ONLY_DIGITS_UPPERCASE("^[0-9A-Z]+$"),
  ONLY_LOWERCASE_UPPERCASE("^[a-zA-Z]+$"),
  ONLY_DIGITS_LOWERCASE_UPPERCASE("^[0-9a-zA-Z]+$"),
  FREE_TYPE("");

  private final String pattern;

  // コンストラクタ
  CharTypeEnum(String pattern) {
    this.pattern = pattern;
  }

  // ゲッター
  public String getPattern() {
    return pattern;
  }
}
