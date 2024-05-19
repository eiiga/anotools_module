package main;

import java.util.Scanner;

import exception.InvalidAgeException;

/*
 * 年齢判定メインクラス
 */
public class AgeJudgmentMain {
	public static void main(String[] args) {
		int age;	// 年齢初期値
		
		// 入力値の設定
		Scanner scanner = new Scanner(System.in);
		System.out.println("年齢を入力してください:");
		
		try {
			// 整数判定
			if (scanner.hasNextInt()) {
				age = scanner.nextInt();
			}else {
				throw new InvalidAgeException("入力値が整数ではありません。", scanner.next());
			}

			// マイナス判定
			if (age < 0) {
				throw new InvalidAgeException("入力値がマイナスの値です。", String.valueOf(age));
			} else {
				System.out.println("年齢は" + age + "才です");
			}

		} catch (InvalidAgeException e) {
			System.out.println("例外エラー：" + e );

		}finally {
			scanner.close();
		}
	}
}
