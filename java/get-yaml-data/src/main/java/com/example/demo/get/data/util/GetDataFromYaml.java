package com.example.demo.get.data.util;

import java.util.Map;
import java.util.TreeMap;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class GetDataFromYaml {

	/* application.yamlの値を取得 */
	@Value("${app.version}")
	private String appVersion;

	@Value("${app.data.element1}")
	private String element1;

	@Value("${app.data.element2}")
	private String element2;

	@Value("${app.data.element3.element3-1}")
	private String element3_1;

	@Value("${app.data.element3.element3-2}")
	private String element3_2;

	/*
	 * yamlのデータ取得処理
	 * 
	 * @reurn yamlのデータ配列
	 */
	public Map<String, String> getDatas() {

		// 返却用リスト
		final Map<String, String> datas = new TreeMap<String, String>();

		// yamlの値を追加
		datas.put("version", appVersion);
		datas.put("element1", element1);
		datas.put("element2", element2);
		datas.put("element3-1", element3_1);
		datas.put("element3-2", element3_2);

		return datas;

	}
}
