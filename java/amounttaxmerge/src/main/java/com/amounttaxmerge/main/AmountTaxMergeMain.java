package com.amounttaxmerge.main;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import com.amounttaxmerge.biz.SelectNameAmountTax;
import com.amounttaxmerge.util.NameAmountTaxDao;

public class AmountTaxMergeMain {
	
	// メイン処理
	public static void main(String[] args) {
		
		// 商品名・金額・税取得クラスインスタンス
		SelectNameAmountTax snat = new SelectNameAmountTax();
		
		// 商品名・金額・税DAOのリストに取得結果を格納
		List<NameAmountTaxDao> select_datas = snat.getNameAcountTax();
		
		// 出力用MAP
		Map<String, Integer> output_map_data = new TreeMap<>();
		
		// 取得したデータ分繰り返し
		for(NameAmountTaxDao data : select_datas) {
			
			// 商品名・金額・税取得
			String name = data.getName();
			int amount = Integer.parseInt(data.getAmount());
			int tax = Integer.parseInt(data.getTax());
			
			// 金額＋税算出
			int data_total = amount + tax;
			
			// 商品名がすでにMAPに存在している場合
			if(output_map_data.containsKey(name)) {
				// MAPから合計金額を取得し、加算
				int total = output_map_data.get(name) + data_total;
				// MAPの合計金額を更新
				output_map_data.replace(name, total);
				
			// 商品名がMAPに存在していない場合
			}else {
				// MAPへ商品名と金額を格納
				output_map_data.put(name, data_total);
			}
		}
		
		// MAP分繰り返し
		for(Map.Entry<String, Integer> entry : output_map_data.entrySet()) {
			// 「商品名：合計金額」を出力
			System.out.println(entry.getKey() + "：" + entry.getValue());
		}
	}
}
