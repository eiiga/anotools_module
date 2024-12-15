package com.example.healthcheck10digits.util;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class Rand10DigitsUtilTest {

  @Test
  @DisplayName("乱数の10桁検証")
  void get10DigitsNumber() {
    Rand10DigitsUtil rand10DigitsUtil = new Rand10DigitsUtil();
    // 第1引数: expected 想定される結果
    // 第2引数: actual 実行結果
    // 第3引数: message 失敗時に出力するメッセージ
    final String actual = rand10DigitsUtil.get10DigitsNumber();
    final String ngMessage = "10桁検証";
    assertEquals(10, actual.length(), ngMessage);
  }
}