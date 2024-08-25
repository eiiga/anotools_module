package com.amounttaxmerge.biz;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.amounttaxmerge.util.ConnectMysql;
import com.amounttaxmerge.util.NameAmountTaxDao;

// 商品名・金額・税取得クラス
public class SelectNameAmountTax {
	
	// 商品名・金額・税取得SQL
	private static final String SQL = "select "
			+ "    A.data_name, "
			+ "    B.amount, "
			+ "    B.tax "
			+ "from"
			+ "    m_data_name A, "
			+ "    t_amount_tax B "
			+ "where"
			+ "    A.id = B.data_id "
			+ "order by "
			+ "    A.data_name "
			+ ";";
	
	// 商品名・金額・税取得処理
	public List<NameAmountTaxDao> getNameAcountTax(){
		
		//  商品名・金額・税DAOのリスト
		List<NameAmountTaxDao> amountTaxList = new ArrayList<NameAmountTaxDao>();
		
		// DB接続クラスインスタンス
		ConnectMysql cm = new ConnectMysql();
		
		try {
			// DB接続
			Connection con = cm.mysqlconnection();
			
			// ステートメントをセット
			Statement stmt = con.createStatement();
			
			// SQL実行
			ResultSet rs =  stmt.executeQuery(SQL);
			
			// 実行件数分繰り返し
			while(rs.next()){
				// 商品名・金額・税DAOのインスタンス
				NameAmountTaxDao result_data = new NameAmountTaxDao();
				
				// 商品名・金額・税をセット
				result_data.setName(rs.getString("A.data_name"));
				result_data.setAmount(rs.getString("B.amount"));
				result_data.setTax(rs.getString("B.tax"));
				
				// 商品名・金額・税DAOのリストに格納
				amountTaxList.add(result_data);
		      }
		//  例外処理
		}catch(Exception e) {
			// 例外エラー出力
			System.out.println("データ取得例外エラー：" + e);
		}
		
		// 商品名・金額・税DAOのリストを返却
		return amountTaxList;
	}
}
