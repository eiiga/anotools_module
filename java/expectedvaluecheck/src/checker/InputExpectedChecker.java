package checker;

import java.util.HashMap;

import constant.CsvHeaderConstant;

public class InputExpectedChecker {

	public static void expectedInputChecker(HashMap<Integer, HashMap<String, String>> expectedDatas,
			HashMap<Integer, HashMap<String, String>> inputDatas) {

		boolean isData = true;

		// csvヘッダ部要素配列
		final CsvHeaderConstant[] keyHeaders = CsvHeaderConstant.values();

		if (!expectedDatas.equals(inputDatas)) {

			System.out.println("##### 相互参照：期待値->実測値 #####");

			for (Integer keyCount : expectedDatas.keySet()) {

				isData = true;

				System.out.println("===== データ：" + keyCount + " =====");
				// csvヘッダ部配列要素分繰り返し
				for (CsvHeaderConstant keyHeader : keyHeaders) {

					if (CsvHeaderConstant.DATE.equals(keyHeader)) {
						continue;
					}

					if (inputDatas.get(keyCount) == null) {
						System.out.println("*** " + keyHeader.getCsvHeaderConstant() + " ***");
						System.out.println("期待値：" + expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));
						System.out.println("実測値：データなし");

						isData = false;

					} else if (!expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant())
							.equals(inputDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()))) {
						System.out.println("*** " + keyHeader.getCsvHeaderConstant() + " ***");
						System.out.println("期待値：" + expectedDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));
						System.out.println("実測値：" + inputDatas.get(keyCount).get(keyHeader.getCsvHeaderConstant()));

						isData = false;

					}
				}

				if (isData) {
					System.out.println("OK");
				}

			}
		}
	}

	public static void inputExpectedChecker(HashMap<Integer, HashMap<String, String>> expectedDatas,
			HashMap<Integer, HashMap<String, String>> inputDatas) {

		System.out.println("##### 相互参照：実測値->期待値 #####");

		// TODO: 相互参照：実測値->期待値を実装
	}

}
