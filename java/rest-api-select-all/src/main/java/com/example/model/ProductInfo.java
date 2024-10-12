package com.example.model;

import lombok.Data;

@Data
public class ProductInfo {
	// 商品コード
	private String productCode;

	// 商品名
	private String productName;

	// 金額
	private int amount;
}
