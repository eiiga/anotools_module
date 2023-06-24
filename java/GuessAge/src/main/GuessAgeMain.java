package main;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class GuessAgeMain {
	
	//  初期最高齢を設定
	private static final int MAX_AGE = 122;
	
	// メイン処理
	public static void main(String[] args) {
		
		// 初期値セット
		int chk_age_index = 0;
		int chk_num = 0;
		
		// 年齢配列の初期をセット
		int[] age_array = new int[MAX_AGE + 1];
		for(int i = 0; i < MAX_AGE + 1; i++ ) {
			age_array[i] = i;
		}
		
		// フラグの初期値セット
		boolean is_guess_age = false;
		
		// ランダムとスキャナーのインスタンス
		Random rand = new Random();
		Scanner scan = new Scanner(System.in);
		
		try {
			// 年齢正解するまで繰り返し
			while(!is_guess_age) {
				// ランダムなインデックス番号を取得...(1)
				chk_age_index = rand.nextInt(age_array.length);
				
				// 年齢を出力し、ユーザに年齢が合っているか入力してもらう
				System.out.print("あなたの年齢は「" + age_array[chk_age_index] + "」才ですか？：");
				chk_num = scan.nextInt();
				
				// 入力値判定
				switch(chk_num) {
					// 0：年齢が低い場合
					case 0:
						// 配列を編成しなおす「インデックス：(1)から最大未満」
						age_array = Arrays.copyOfRange(age_array, chk_age_index + 1, age_array.length);
						break;

					// 1：正解の場合
					case 1:
						System.out.println("あなたの年齢は「" + age_array[chk_age_index] + "」才です");
						// フラグ変更してループを抜ける
						is_guess_age = true;
						break;

						// 年齢が高い場合
					case 2:
						// 配列を編成しなおす「インデックス：0から(1)未満まで」
						age_array = Arrays.copyOfRange(age_array, 0, chk_age_index);
						break;
					
					//  0から2以外を入力した場合
					default:
						System.out.println("0〜2を入力してください");
						break;
				}
			}

		// 例外処理
		}catch(Exception e) {
			System.out.println("例外エラー：" + e);

			// 終了処理
		}finally {
			// スキャナーをクローズ
			scan.close();
		}
	}
}
