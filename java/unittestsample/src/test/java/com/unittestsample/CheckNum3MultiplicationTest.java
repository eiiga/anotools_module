package com.unittestsample;


import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class CheckNum3MultiplicationTest{
	
	private CheckNum3Multiplication cn3m;
	
	// コンストラクタ
	public CheckNum3MultiplicationTest() {
		cn3m = new CheckNum3Multiplication();
	}

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		System.out.println("=====テスト開始=====");
	}

	@AfterAll
	static void tearDownAfterClass() throws Exception {
		System.out.println("=====テスト終了=====");
	}
	
	@Test
	@DisplayName("入力値が整数か判定処理---正常系---")
	void isCheckNumIntTest1() {
		  String input_num = "10";  
		  		  
		  assertTrue(cn3m.isCheckNumInt(input_num));
	}
	
	@Test
	@DisplayName("入力値が整数か判定処理---異常系(null)---")
	void isCheckNumIntTest2() {
		  String input_num = null;  
		  		  
		  assertFalse(cn3m.isCheckNumInt(input_num));
	}
	
	@Test
	@DisplayName("入力値が整数か判定処理---異常系(整数ではない)---")
	void isCheckNumIntTest3() {
		  String input_num = "11.11";  
		  		  
		  assertFalse(cn3m.isCheckNumInt(input_num));
	}	
	
	@Test
	@DisplayName("入力値を3倍にして返す処理")
	void multipicationThreeTest() {
		  String input_num = "1";  
		  int ans_num = 3;
		  		  
		  assertEquals(cn3m.multipicationThree(input_num), ans_num);
	}

}
