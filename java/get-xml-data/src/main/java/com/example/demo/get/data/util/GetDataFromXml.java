package com.example.demo.get.data.util;

import java.util.Map;
import java.util.TreeMap;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.stereotype.Component;

import com.example.demo.get.data.bean.GetDataBean;

@Component
public class GetDataFromXml {

	public Map<String, String> getDatas() {

		// context.xmlのロード
		ApplicationContext context = new ClassPathXmlApplicationContext("service-context.xml");

		// Beanの取得
		GetDataBean getDataBean = (GetDataBean) context.getBean("GetDataFromXml#1");

		// 返却用リスト
		final Map<String, String> datas = new TreeMap<String, String>();

		// xmlの値を追加
		datas.put("version", getDataBean.getAppVersion());
		datas.put("element1", getDataBean.getElement1());
		datas.put("element2", getDataBean.getElement2());
		datas.put("element3-1", getDataBean.getElement3_1());
		datas.put("element3-2", getDataBean.getElement3_2());

		((ClassPathXmlApplicationContext) context).close();

		return datas;

	}
}
