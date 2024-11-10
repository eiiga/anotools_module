package main;

import java.io.BufferedReader;
import java.util.HashMap;

import checker.InputExpectedChecker;
import constant.FilePathConstant;
import converter.CsvToHashMapConverter;
import reader.CsvReader;

public class ExpectedValueCheckMain {

	public static void main(String[] args) {

		// インプットファイル読み込み
		BufferedReader inputFile = CsvReader.csvFileReader(FilePathConstant.INPUT_FILEPATH);

		// HashMap形式でデータを格納
		HashMap<Integer, HashMap<String, String>> inputDatas = CsvToHashMapConverter.resultHashMap(inputFile);

		// 期待値ファイル読み込み
		BufferedReader expectedFile = CsvReader.csvFileReader(FilePathConstant.EXPECTED_FILEPATH);

		// HashMap形式でデータを格納
		HashMap<Integer, HashMap<String, String>> expectedDatas = CsvToHashMapConverter.resultHashMap(expectedFile);

		// 相互比較（期待値 -> 実測値）
		InputExpectedChecker.expectedInputChecker(expectedDatas, inputDatas);

		// 相互比較（実測値 -> 期待値）
		InputExpectedChecker.inputExpectedChecker(expectedDatas, inputDatas);
	}
}
