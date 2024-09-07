package com.example.demo.get.data.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.get.data.service.RestService;

@RestController
public class GetYamlController {

	@Autowired
	RestService restService;

	// yamlデータを取得()
	@GetMapping("/rest/get/yamldata")
	public List<String> getYamlDatas() {
		return restService.getDataFromYamList();
	}

}
