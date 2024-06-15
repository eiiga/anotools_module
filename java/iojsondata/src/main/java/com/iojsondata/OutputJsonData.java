package com.iojsondata;

import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;


public class OutputJsonData {
		
	public void output_json_data() throws JsonProcessingException, IOException {
		UserData user_data = new UserData();
		
		user_data.id = "001";
		user_data.user_name = "hoge hoge";
		user_data.age = 20;
		
		ObjectMapper om = new ObjectMapper();
		om.enable(SerializationFeature.INDENT_OUTPUT);
		
		String output_json_data = om.writeValueAsString(user_data);
		System.out.println(output_json_data);
	}
	
}
