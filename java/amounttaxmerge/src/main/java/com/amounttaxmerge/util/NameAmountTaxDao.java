package com.amounttaxmerge.util;

public class NameAmountTaxDao {

	private String name;	// 商品名
	private String amount;	// 金額
	private String tax;		// 税
	
	// 商品名
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	// 金額
	public String getAmount() {
		return this.amount;
	}
	
	public void setAmount(String amount) {
		this.amount = amount;
	}
	
	// 税
	public String getTax() {
		return this.tax;
	}
	
	public void setTax(String tax) {
		this.tax = tax;
	}

}
