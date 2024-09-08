package com.example.demo.get.data.service;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.get.data.util.GetDataFromYaml;

@Service("RestServiceImpl")
public class RestServiceImpl implements RestService {

	@Autowired
	GetDataFromYaml getDataFromYaml;

	@Override
	public Map<String, String> getDataFromYamList() {

		return getDataFromYaml.getDatas();
	}
}
