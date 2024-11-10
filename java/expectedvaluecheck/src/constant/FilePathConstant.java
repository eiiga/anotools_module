package constant;

public enum FilePathConstant {

  // インプットファイルパス
  INPUT_FILEPATH("input/case.csv"),

  // 期待値ファイルパス
  EXPECTED_FILEPATH("expected/expected.csv");

  // フィールド変数
  private final String filePath;

  // コンストラクタ
  private FilePathConstant(String filePath) {
    this.filePath = filePath;
  }

  // ゲッター
  public String getFilePathConstant() {
    return filePath;
  }
}
