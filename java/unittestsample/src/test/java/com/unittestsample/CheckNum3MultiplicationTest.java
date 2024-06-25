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
	@DisplayName("入力値を3倍にして返す処理")
	void multipicationTreeTest() {
		  String input_num = "1";
		  
		  int result_num = cn3m.multipicationTree(input_num);
		  
		  int ans_num = 3;
		  		  
		  assertEquals(result_num, ans_num);
	}

}
