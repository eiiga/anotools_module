package main;

import java.util.Random;

import constant.MultiplicationConstant;

public class MultiplicationMain {

	public static void main(String[] args) {

		// 1 ~ 100までの乱数を生成
		Random rnd = new Random();
		int value = rnd.nextInt(101) + 1;

		System.out.println("初期値：" + value);

		for (MultiplicationConstant mc : MultiplicationConstant.values()) {

			System.out.println(value + ", " + mc + ": " + mc.getMultiplicationConstant(value));
		}

	}
}
