package com.iojsondata;

import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;


public class IoJsonDataMain {
	public static void main(String[] args) throws JsonProcessingException, IOException {
		
		System.out.println("----- JSONデータ入出力処理 -----");
		
		if("output".equals(args[0])) {
		
			// jsonデータ出力処理
			OutputJsonData ojd = new OutputJsonData();
			ojd.output_json_data();
		
		}else if("input".equals(args[0])) {
			// jsonデータ入力処理
			InputJsonData ijd = new InputJsonData();
			ijd.input_json_data();
		}else {
			System.out.println("第一実行引数は「output」もしくは「input」を入力してください");
		}
		
	}
}
