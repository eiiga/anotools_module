package com.example.demo.controlller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.RestService;
import com.example.model.ProductInfo;

@RestController
public class PruductInfoRestController {

	@Autowired
	RestService service;

	// 全件取得
	@GetMapping("/rest/get")
	public List<ProductInfo> getUserMany() {
		// 全件取得
		return service.selectAll();
	}

}
