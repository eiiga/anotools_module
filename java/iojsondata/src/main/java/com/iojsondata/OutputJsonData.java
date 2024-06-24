package com.iojsondata;

import java.io.IOException;
import java.util.ArrayList;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

// JSONデータ作成＆出力クラス
public class OutputJsonData {
	
	// JSONデータ作成＆出力処理
	public void output_json_data() throws JsonProcessingException, IOException {
		// ユーザデータクラスをインスタンス
		UserData user_data = new UserData();
		UserSubData1 user_sub_data1 = new UserSubData1();
		UserSubData2 user_sub_data2_1 = new UserSubData2();
		UserSubData2 user_sub_data2_2 = new UserSubData2();
		UserSubData2 user_sub_data2_3 = new UserSubData2();
		
		// ユーザデータをそれぞれセット
		user_data.id = "001";
		user_data.user_name = "hoge hoge";
		user_data.age = 20;
		
		user_sub_data1.subdata1_1 = 789;
		user_sub_data1.subdata1_2 = 101112;
		
		user_data.subdata1 = user_sub_data1;
		
		user_sub_data2_1.subdata2_1 = "JKL";
		user_sub_data2_1.subdata2_2 = "jkl";

		user_sub_data2_2.subdata2_1 = "MNO";
		user_sub_data2_2.subdata2_2 = "mno";

		user_sub_data2_3.subdata2_1 = "PQR";
		user_sub_data2_3.subdata2_2 = "pql";
		
		user_data.subdata2 = new ArrayList<UserSubData2>();
		user_data.subdata2.add(user_sub_data2_1);
		user_data.subdata2.add(user_sub_data2_2);
		user_data.subdata2.add(user_sub_data2_3);

		
		// ユーザデータをJSON形式に整形して出力
		ObjectMapper mapper = new ObjectMapper();
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		String output_json_data = mapper.writeValueAsString(user_data);
		System.out.println(output_json_data);
	}
	
}
