package com.example.demo.repository;

import java.util.List;

import org.springframework.dao.DataAccessException;

import com.example.model.ProductInfo;

public interface ProductInfoDao {

	// 商品情報マスタテーブル全件を取得
	public List<ProductInfo> selectAll() throws DataAccessException;

}
