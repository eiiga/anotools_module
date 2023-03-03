package fnc;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import dto.PathInfoDTO;

// ディレクトリ作成クラス
public class MkdirsFnc {
	/* ディレクトリ作成処理
	 * ・処理概要
	 * 		入力した定義ファイル（フルパス）をインプットに
	 * 		出力ディレクトリ（フルパス）ディレクトリを作成する
	 * ・引数：
	 * 		ディレクトリ作成DTOクラス
	 * ・戻り値：
	 * 		なし
	 */
	public void makedirs(PathInfoDTO pathdto) {
		// 処理完了メッセージの初期値セット
		String result_message = "";
		try {
			
			// Fileクラスをインスタンス（定義ファイル）
			File def = new File(pathdto.getStrDefPath());
			// FileReaderクラスのインスタンス
			FileReader fr = new FileReader(def);
			// BufferedReaderクラスのインスタンス
			BufferedReader br = new BufferedReader(fr);
			
			// 定義ファイルの1行目を文字列として格納
			String read_line = br.readLine();
			
			// 定義ファイルの行数分繰り返し
			while(read_line != null) {
				
				// 出力ディレクトリ（フルパス）＋定義ファイルの内容
				String out_dir = pathdto.getStrOutPath() + "/" + read_line;
				// Fileクラスのインスタンス（出力ディレクトリ）
				File make_dirs_path = new File(out_dir);
				// ディレクトリ作成（サブディレクトリ含む）
				make_dirs_path.mkdirs();
				// 定義ファイルの次の行を文字列として格納
				read_line = br.readLine();
			}
			
			// BufferedReaderクラスをクローズ
			br.close();
			
			// 処理完了メッセージ格納（正常系）
			result_message = "完了！";
		
		// 例外処理
		}catch(Exception e){
			// 処理完了メッセージ格納（異常系）
			result_message = "エラー：" + e;
		
		// 終了処理
		}finally {
			// 処理完了メッセージをディレクトリ作成DTOクラスにセット
			pathdto.setResultMsg(result_message);
		}
	}
}
