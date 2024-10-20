package main;

import java.util.Random;

import constant.MultiplicationConstant;

public class MultiplicationMain {

	public static void main(String[] args) {

		// 1 ~ 100までの乱数を生成
		Random rnd = new Random();
		int value = rnd.nextInt(101) + 1;

		// 初期値出力
		System.out.println("初期値：" + value);

		// 定数分繰り返し
		for (MultiplicationConstant mc : MultiplicationConstant.values()) {

			// 計算結果出力
			System.out.println(value + ", " + mc + ": " + mc.getMultiplicationConstant(value));
		}

	}
}
