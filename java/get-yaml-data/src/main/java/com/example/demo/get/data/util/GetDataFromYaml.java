package com.example.demo.get.data.util;

import java.util.ArrayList;
import java.util.List;

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
	public List<String> getDatas() {

		// 返却用リスト
		final List<String> datas = new ArrayList<String>();

		// yamlの値を追加
		datas.add(appVersion);
		datas.add(element1);
		datas.add(element2);
		datas.add(element3_1);
		datas.add(element3_2);

		return datas;

	}
}
