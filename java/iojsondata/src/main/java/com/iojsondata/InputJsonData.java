package com.iojsondata;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class InputJsonData {
	
	public void input_json_data() throws JsonProcessingException, IOException{
		ObjectMapper om = new ObjectMapper();
		
		JsonNode json_data = om.readTree(Paths.get("./data/inputdata.json").toFile());
		
		String id = json_data.get("id").textValue();
		String name = json_data.get("user_name").textValue();
		int age = json_data.get("age").intValue();
		
		Map<String, String> user_data_map = new HashMap<>();
		
		
		
		user_data_map.put("id", id);
		user_data_map.put("user_name", name);
		user_data_map.put("age", String.valueOf(age));
		
		
		for(String user_data: user_data_map.values()) {
			System.out.println(user_data);
		}
	}

}
