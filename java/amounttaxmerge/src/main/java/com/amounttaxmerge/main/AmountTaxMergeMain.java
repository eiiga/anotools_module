package com.amounttaxmerge.main;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import com.amounttaxmerge.biz.SelectNameAmountTax;
import com.amounttaxmerge.util.NameAmountTaxDao;

public class AmountTaxMergeMain {
	
	
	public static void main(String[] args) {
		
		SelectNameAmountTax snat = new SelectNameAmountTax();
		
		List<NameAmountTaxDao> select_datas = snat.getNameAcountTax();
		
		Map<String, Integer> output_map_data = new TreeMap<>();
		
		for(NameAmountTaxDao data : select_datas) {
			
			String name = data.getName();
			int amount = Integer.parseInt(data.getAmount());
			int tax = Integer.parseInt(data.getTax());
			
			int data_total = amount + tax;
			
			if(output_map_data.containsKey(name)) {
				int total = output_map_data.get(name) + data_total;
				
				output_map_data.replace(name, total);
			}else {
				output_map_data.put(name, data_total);
			}
			
		}
		
		for(Map.Entry<String, Integer> entry : output_map_data.entrySet()) {
			System.out.println(entry.getKey() + "：" + entry.getValue());
		}
		
		
	}
}
