package constant;

// チェックコード定数
public enum MultiplicationConstant {

	// 定数
	CODE_FIRST(1), CODE_SECOND(2), CODE_THIRD(3), CODE_FOURTH(4), CODE_FIFTH(5);

	// フィールド変数
	private final int multiplicationCode;

	// コンストラクタ
	private MultiplicationConstant(int multiplicationCode) {
		this.multiplicationCode = multiplicationCode;
	}

	// ゲッター
	public int getMultiplicationConstant(final int num) {

		return multiplicationCode * num;
	}

}
