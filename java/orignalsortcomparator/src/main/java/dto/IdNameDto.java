package dto;

public class IdNameDto {

  private int id;
  private String name;

  // コンストラクタ
  public IdNameDto(int id, String name) {
    this.id = id;
    this.name = name;
  }

  public int getId() {
    return id;
  }

  public String getName() {
    return name;
  }

}
