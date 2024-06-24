package com.unittestsample;

public class CheckNum3Multiplication {
	
	// 入力値が整数かを判定する処理
	public Boolean isCheckNumInt(String num) {
		
		// 入力値がnullか否か
		if (num == null) {
			return false;
		}
		
		try {
			// 整数判定
			Integer.parseInt(num);
		} catch (NumberFormatException e) {
			System.out.println("例外エラー：" + e);
			return false;
		}
		
		
		return true;
	}
	
	
	// 入力値を3倍にして返す処理
	public int multipicationTree(String num) {
		
		return Integer.parseInt(num) * 3;
		
	}
}
