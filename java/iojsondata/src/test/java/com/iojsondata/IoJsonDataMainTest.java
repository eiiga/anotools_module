package com.iojsondata;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

public class IoJsonDataMainTest {

	  // テスト開始前に1回だけ実行される
	  @BeforeAll
	  static void beforeAll() {
	    System.out.println("IoJsonDataMainTest 開始");
	  }
	
	  // テスト開始後に1回だけ実行される
	  @AfterAll
	  static void afterAll() {
	    System.out.println("IoJsonDataMainTest 終了");
	  }
	  
	  @Test
	  void testOutputMain() {
	    System.out.println("output を実行");
	    IoJsonDataMain ijdm = new IoJsonDataMain();
	    
	    // 第1引数: expected 想定される結果
	    // 第2引数: actual 実行結果
	    // 第3引数: message 失敗時に出力するメッセージ
	    String[] exe_arg = {"output"};
	    
	    // assertEquals("", ijdm.main(exe_arg));
	  }
}
