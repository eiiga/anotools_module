package constant;

public enum CsvHeaderConstant {

  // ID
  ID("id"),

  // value1
  VALUE1("value1"),

  // value2
  VALUE2("value2"),

  // value3
  VALUE3("value3"),

  // 日付
  DATE("date(YYYYMMDD)");

  // フィールド変数
  private final String header;

  // コンストラクタ
  private CsvHeaderConstant(String header) {
    this.header = header;

  }

  // ゲッター
  public String getCsvHeaderConstant() {
    return header;
  }

}
