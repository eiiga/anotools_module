package com.example.demo.get.data.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.get.data.service.RestService;

@RestController
public class GetXmlController {

	@Autowired
	RestService restService;

	// xmlデータを取得()
	@GetMapping("/rest/get/xmldata")
	public Map<String, String> getXmlDatas() {
		return restService.getDataFromXMList();
	}
}
