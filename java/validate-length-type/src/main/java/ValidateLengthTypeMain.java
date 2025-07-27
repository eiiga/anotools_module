import static util.ValidateLengthTypeUtil.isValidateLengthType;

import constant.CharTypeEnum;

public class ValidateLengthTypeMain {

  public static void main(String[] args) {
    String onlyDigitsTrue = "12398";
    String onlyLowerCaseTrue = "abcdxyz";
    String onlyUpperCaseTrue = "EGDYSHKF";
    String onlyDigitsLowerCaseTrue = "1a2s3d";
    String onlyDigitsUpperCaseTrue = "F4G5H6JKL";
    String onlyLowerUpperCaseTrue = "eFb";
    String onlyDigitsLowerUpperCaseTrue = "7iB8oN9pM0";
    String lengthFalse = "q2F";
    String typeFalse = "@]la";
    String emptyFalse = "";
    String freeLengthTypeTrue = "sdizhfsiuefhsoiefj]odsifj-3549[][@:";

    // 数字のみ（OK）
    System.out.println(
        "onlyDigitsTrue: " + onlyDigitsTrue + ": " +
            isValidateLengthType(onlyDigitsTrue, 5, CharTypeEnum.ONLY_DIGITS));

    System.out.println("====================");

    // 小文字のみ（OK）
    System.out.println(
        "onlyLowerCaseTrue: " + onlyLowerCaseTrue + ": " +
            isValidateLengthType(onlyLowerCaseTrue, 7, CharTypeEnum.ONLY_LOWERCASE));

    System.out.println("====================");

    // 大文字のみ（OK）
    System.out.println(
        "onlyUpperCaseTrue: " + onlyUpperCaseTrue + ": " +
            isValidateLengthType(onlyUpperCaseTrue, 8, CharTypeEnum.ONLY_UPPERCASE));

    System.out.println("====================");

    // 数字・小文字のみ（OK）
    System.out.println(
        "onlyDigitsLowerCaseTrue: " + onlyDigitsLowerCaseTrue + ": " +
            isValidateLengthType(onlyDigitsLowerCaseTrue, 6, CharTypeEnum.ONLY_DIGITS_LOWERCASE));

    System.out.println("====================");

    // 数字・大文字のみ（OK）
    System.out.println(
        "onlyDigitsUpperCaseTrue: " + onlyDigitsUpperCaseTrue + ": " +
            isValidateLengthType(onlyDigitsUpperCaseTrue, 9, CharTypeEnum.ONLY_DIGITS_UPPERCASE));

    System.out.println("====================");

    // 小文字・大文字のみ（OK）
    System.out.println(
        "onlyLowerUpperCaseTrue: " + onlyLowerUpperCaseTrue + ": " +
            isValidateLengthType(onlyLowerUpperCaseTrue, 3,
                CharTypeEnum.ONLY_LOWERCASE_UPPERCASE));

    System.out.println("====================");

    // 数字・小文字・大文字のみ（OK）
    System.out.println(
        "onlyDigitsLowerUpperCaseTrue: " + onlyDigitsLowerUpperCaseTrue + ": " +
            isValidateLengthType(onlyDigitsLowerUpperCaseTrue, 10,
                CharTypeEnum.ONLY_DIGITS_LOWERCASE_UPPERCASE));

    System.out.println("====================");

    // 長さチェック（NG）
    System.out.println(
        "lengthFalse: " + lengthFalse + ": " +
            isValidateLengthType(lengthFalse, 99,
                CharTypeEnum.ONLY_DIGITS_LOWERCASE_UPPERCASE));

    System.out.println("====================");

    // タイプチェック（NG）
    System.out.println(
        "typeFalse: " + typeFalse + ": " +
            isValidateLengthType(typeFalse, 4,
                CharTypeEnum.ONLY_DIGITS_LOWERCASE_UPPERCASE));

    System.out.println("====================");

    // チェック文字列なし（NG）
    System.out.println(
        "emptyFalse: " + emptyFalse + ": " +
            isValidateLengthType(emptyFalse, 12,
                CharTypeEnum.ONLY_DIGITS));

    System.out.println("====================");

    // 文字長さ・タイプチェックなし（OK）
    System.out.println(
        "freeLengthTypeTrue: " + freeLengthTypeTrue + ": " +
            isValidateLengthType(freeLengthTypeTrue, 0,
                CharTypeEnum.FREE_TYPE));

  }
}
