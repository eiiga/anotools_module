package constant;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

@TestInstance(Lifecycle.PER_CLASS)
public class WarnErrorCodeTest {

  @Test
  @DisplayName("正常系：すべてのWarn網羅")
  void warnCodeTestNormal() {
    for (int i = 1; i <= 5; i++) {
      String inputWarn = "WARN" + i;
      System.out.printf("ケース%s: %s%n", i, inputWarn);
      assertEquals(WarnErrorCode.getConvertCode(inputWarn), String.format("%04d", i));
    }
  }

  @Test
  @DisplayName("正常系：すべてのError網羅")
  void errorCodeTestNormal() {
    for (int i = 1; i <= 10; i++) {
      String inputError = "ERROR" + i;
      System.out.printf("ケース%s: %s%n", i, inputError);
      assertEquals(WarnErrorCode.getConvertCode(inputError), "1" + String.format("%03d", i));
    }
  }

  @Test
  @DisplayName("正常系：想定外コード：ABC1")
  void otherCodeTestNormal() {
    assertEquals(WarnErrorCode.getConvertCode("ABC1"), "9999");

  }

  @Test
  @DisplayName("正常系：想定外コード：Warn6")
  void otherWarnCodeTestNormal() {
    assertEquals(WarnErrorCode.getConvertCode("WARN6"), "9999");

  }

  @Test
  @DisplayName("正常系：想定外コード：ERROR11")
  void otherErrorCodeTestNormal() {
    assertEquals(WarnErrorCode.getConvertCode("ERROR11"), "9999");

  }


}
