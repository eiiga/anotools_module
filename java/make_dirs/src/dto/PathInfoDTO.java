package dto;

import java.io.Serializable;

// ディレクトリ作成DTOクラス
public class PathInfoDTO  implements Serializable{
	
	/*
	 *	フィールド
	 *	・定義ファイルパス（フルパス）
	 *	・出力ディレクトリパス（フルパス）
	 *	・処理完了メッセージ
	 */
	private String str_def_path;
	private String str_out_path;
	private String result_msg;
	
	// 定義ファイルパスのゲッターとセッター
	public String getStrDefPath() {
		return str_def_path;
	}
	public void setStrDefPath(String str_def_path) {
		this.str_def_path = str_def_path;
	}
	
	// 出力ディレクトリのゲッターとセッター
	public String getStrOutPath() {
		return str_out_path;
	}
	public void setStrOutPath(String str_out_path) {
		this.str_out_path = str_out_path;
	}
	
	// 処理完了メッセージのゲッターとセッター
	public String getResultMsg() {
		return result_msg;
	}
	public void setResultMsg(String result_msg) {
		this.result_msg = result_msg;
	}
}
