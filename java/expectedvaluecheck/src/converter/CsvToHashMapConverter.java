package converter;

import java.io.BufferedReader;
import java.util.HashMap;

import constant.CsvHeaderConstant;

public class CsvToHashMapConverter {

	public static HashMap<Integer, HashMap<String, String>> resultHashMap(final BufferedReader csvFile) {
		// 返却用HashMap
		final HashMap<Integer, HashMap<String, String>> result = new HashMap<>();

		// データ件数カウンタ
		int dataCount = 1;

		// csvファイルの1行
		String readLine = "";
		
		// csvヘッダ部要素配列
		final CsvHeaderConstant[] keys = CsvHeaderConstant.values();

		// csvファイルが存在する場合
		if (csvFile != null) {
			try {
				// csvファイルの中身を1行ずつ繰り返し
				while ((readLine = csvFile.readLine()) != null) {

					// ヘッダー部以外の場合
					if (!readLine.contains(CsvHeaderConstant.ID.getCsvHeaderConstant())) {

						// csvのデータを配列に格納
						String[] items = readLine.split(",");

						// データ部格納用HashMap
						HashMap<String, String> data = new HashMap<>();

						// csvヘッダ部配列要素分繰り返し
						for (int i = 0; i < keys.length; i++) {
							// {ヘッダ部要素名：csvのデータ}形式でデータを格納＝データ部
							data.put(keys[i].getCsvHeaderConstant(), items[i]);
						}
						// 返却用HashMap{データカウンタ：データ部}の形式で格納
						result.put(dataCount, data);

						// カウンタインクリメント
						dataCount++;

					}
				}
			} catch (Exception e) {
				System.out.println("resultHashMap処理例外エラー：" + e);
			}
		}

		return result;

	}

}
