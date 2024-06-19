package com.iojsondata;

import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

// JSONデータ作成＆出力クラス
public class OutputJsonData {
	
	// JSONデータ作成＆出力処理
	public void output_json_data() throws JsonProcessingException, IOException {
		// ユーザデータクラスをインスタンス
		UserData user_data = new UserData();
		
		// ユーザデータをそれぞれセット
		user_data.id = "001";
		user_data.user_name = "hoge hoge";
		user_data.age = 20;
		
		// ユーザデータをJSON形式に整形して出力
		ObjectMapper om = new ObjectMapper();
		om.enable(SerializationFeature.INDENT_OUTPUT);
		String output_json_data = om.writeValueAsString(user_data);
		System.out.println(output_json_data);
	}
	
}
