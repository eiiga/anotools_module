package exception;

/*
 * 年齢判定例外クラス
 */
public class InvalidAgeException extends Exception{
	//　警告を回避するための宣言
	private static final long serialVersionUID = 1L;
	
	// コンストラクタ
	public InvalidAgeException(String exception_message, String input_data){
		// Exceptionクラスのコンストラクタ呼び出し
		super(exception_message + "入力値：" + input_data);
	}
}
