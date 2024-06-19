package com.iojsondata;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

// JSONファイル読み込みクラス
public class InputJsonData {
	
	// JSONファイル読み込み処理
	public void input_json_data() throws JsonProcessingException, IOException{
		ObjectMapper om = new ObjectMapper();
		
		// JSONファイル読み込み
		JsonNode json_data = om.readTree(Paths.get("./data/inputdata.json").toFile());
		
		// JSONの各要素取得
		String id = json_data.get("id").textValue();
		String name = json_data.get("user_name").textValue();
		int age = json_data.get("age").intValue();
		
		// MAPのインスタンス
		Map<String, String> user_data_map = new HashMap<>();
		
		// MAPにJSON情報を格納
		user_data_map.put("id", id);
		user_data_map.put("user_name", name);
		user_data_map.put("age", String.valueOf(age));
		
		// MAPの要素数分繰り返し
		for(String user_data: user_data_map.values()) {
			// JSONのデータを出力
			System.out.println(user_data);
		}
	}

}
