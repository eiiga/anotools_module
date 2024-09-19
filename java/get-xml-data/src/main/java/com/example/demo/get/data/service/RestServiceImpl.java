package com.example.demo.get.data.service;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.get.data.util.GetDataFromXml;

@Service("RestServiceImpl")
public class RestServiceImpl implements RestService {

	@Autowired
	GetDataFromXml getDataFromXml;

	@Override
	public Map<String, String> getDataFromXMList() {

		return getDataFromXml.getDatas();
	}
}
