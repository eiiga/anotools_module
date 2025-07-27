package util;

import constant.CharTypeEnum;

public class ValidateLengthTypeUtil {

  public static boolean isValidateLengthType(String target, int length, CharTypeEnum charType) {

    if (target.isEmpty()) {
      System.out.println("チェック文字列：なし");
      return false;
    }

    // lengthに0を指定した場合は長さ判定を実施しない
    if (length != 0) {
      if (!isLength(target, length)) {
        return false;
      }

    }

    // FREE_TYPEの場合は文字タイプ判定を実施しない
    if (CharTypeEnum.FREE_TYPE != charType) {
      if (!isType(target, charType)) {
        return false;
      }
    }
    return true;
  }

  private static boolean isLength(String target, int length) {
    if (target.length() != length) {
      System.out.println(
          "[文字長さエラー]target.length(): " + target.length() + " |length: " + length);
      return false;
    }
    return true;
  }

  private static boolean isType(String target, CharTypeEnum charType) {
    if (!target.matches(charType.getPattern())) {
      System.out.println(
          "[文字タイプエラー]target: " + target + " |type: " + charType);
      return false;
    }
    return true;
  }
}
