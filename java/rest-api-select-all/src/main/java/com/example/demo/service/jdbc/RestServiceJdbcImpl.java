package com.example.demo.service.jdbc;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.repository.ProductInfoDao;
import com.example.demo.service.RestService;
import com.example.model.ProductInfo;

import jakarta.transaction.Transactional;

@Transactional
@Service
public class RestServiceJdbcImpl implements RestService {

	@Autowired
	ProductInfoDao productInfoDao;

	@Override
	public List<ProductInfo> selectAll() {
		return productInfoDao.selectAll();

	}

}
