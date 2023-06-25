package main;

import java.util.Scanner;

public class MakePyramidMain {
	
	// ピラミッドのマークとスペースをセット
	private static final String PYRAMID_MARK = "*";
	private static final String PYRAMID_SPACE = " ";
	
	// スペースをプロットする関数
	private static String PlotSpace(String input_str, int total_step, int now_step) {
		
		// 「トータルの段数」 - 「現在の段数」分、スペースを付与する
		for(int j = total_step - now_step; j > 0; j--) {
			input_str = input_str + PYRAMID_SPACE;
		}
		
		return input_str;
	}
	
	// ピラミッドマークをプロットする関数
	private static String PlotMark(String input_str, int now_step) {
		
		// 「現在の段数」x 2 - 1 個分、マークを付与する
		for(int k = 0; k < 2 * now_step - 1; k++) {
			input_str = input_str + PYRAMID_MARK;
		}
		
		return input_str;
	}
	
	
	// メイン処理
	public static void main(String[] args) {
		
		// スキャナーのインスタンス
		Scanner scan = new Scanner(System.in);
		
		try {
			
			// ユーザに段数を入力してもらう
			System.out.println("何段のピラミッドを作成しますか？：");
			int total_step = scan.nextInt();
			
			// 入力した段数分繰り返し
			for(int i = 1; i <= total_step; i++) {
				// 出力用の文字列初期化
				String output_step = "";
				
				// 左側のスペース部分を付与
				output_step = PlotSpace(output_step, total_step, i);
				
				// ピラミッドのマーク部分を付与
				output_step = PlotMark(output_step, i);
				
				// 右側のスペース部分を付与
				output_step = PlotSpace(output_step, total_step, i);
				
				// 作成したピラミッドの段を出力
				System.out.println(output_step);
			}
		
		// 例外処理
		}catch(Exception e) {
			System.out.println("例外エラー：" + e);
		
		// 終了処理
		}finally {
			// スキャナークローズ
			scan.close();
		}
		
		
	}
	

}
