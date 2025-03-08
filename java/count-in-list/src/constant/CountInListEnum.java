package constant;

public enum CountInListEnum {

  FROM_FIRST_LARGE("FROM_1_LARGE"),
  FROM_SECOND_LARGE("FROM_2_LARGE"),
  FROM_FIRST_ONLY("FROM_1_LARGE_ONLY"),
  FROM_SECOND_ONLY("FROM_2_LARGE_ONLY"),
  EQUAL("EQUAL");

  private final String fromData;

  private CountInListEnum(String fromData) {
    this.fromData = fromData;
  }

  public String getCountInListEnum() {
    return fromData;
  }

}
