package com.example.healthcheck10digits.util;

public class Rand10DigitsUtil {

  public String get10DigitsNumber(){

    // 9,999,999,999までの乱数を生成
    final  long randNum =  (long)(Math.random() * 10_000_000_000L);

    // 10桁に満たない場合は左側を0でパディングして返す
    return String.format("%010d", randNum);
  }

}
