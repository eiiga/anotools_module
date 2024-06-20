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
		
		int subdata1_1 = json_data.get("subdata1").get("subdata1-1").intValue();
		int subdata1_2 = json_data.get("subdata1").get("subdata1-2").intValue();
		
		String subdata2_1_1 = json_data.get("subdata2").get(0).get("subdata2-1-1").textValue();
		String subdata2_1_2 = json_data.get("subdata2").get(0).get("subdata2-1-2").textValue();
		String subdata2_2_1 = json_data.get("subdata2").get(1).get("subdata2-2-1").textValue();
		String subdata2_2_2 = json_data.get("subdata2").get(1).get("subdata2-2-2").textValue();
		String subdata2_3_1 = json_data.get("subdata2").get(2).get("subdata2-3-1").textValue();
		String subdata2_3_2 = json_data.get("subdata2").get(2).get("subdata2-3-2").textValue();
		
		// MAPのインスタンス
		Map<String, String> user_data_map = new HashMap<>();
		
		// MAPにJSON情報を格納
		user_data_map.put("id", id);
		user_data_map.put("user_name", name);
		user_data_map.put("age", String.valueOf(age));
		
		user_data_map.put("subdata1-1", String.valueOf(subdata1_1));
		user_data_map.put("subdata1-2", String.valueOf(subdata1_2));
		
		user_data_map.put("subdata2-1-1", subdata2_1_1);
		user_data_map.put("subdata2-1-2", subdata2_1_2);
		user_data_map.put("subdata2-2-1", subdata2_2_1);
		user_data_map.put("subdata2-2-2", subdata2_2_2);
		user_data_map.put("subdata2-3-1", subdata2_3_1);
		user_data_map.put("subdata2-3-2", subdata2_3_2);
		
		// MAPの要素数分繰り返し
		for(Map.Entry<String, String> user_data: user_data_map.entrySet()) {
			// JSONのデータを出力
			System.out.println(user_data.getKey() + ": " + user_data.getValue());
		}
	}

}
