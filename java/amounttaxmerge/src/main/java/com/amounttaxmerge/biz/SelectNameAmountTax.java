package com.amounttaxmerge.biz;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.amounttaxmerge.util.ConnectMysql;
import com.amounttaxmerge.util.NameAmountTaxDao;

public class SelectNameAmountTax {
	
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
	
	
	public List<NameAmountTaxDao> getNameAcountTax(){
		
		List<NameAmountTaxDao> amountTaxList = new ArrayList<NameAmountTaxDao>();
		
		ConnectMysql cm = new ConnectMysql();
		
		try {
			Connection con = cm.mysqlconnection();
		
			Statement stmt = con.createStatement();
			
			ResultSet rs =  stmt.executeQuery(SQL);
			
			while(rs.next()){
				NameAmountTaxDao result_data = new NameAmountTaxDao();
				result_data.setName(rs.getString("A.data_name"));
				result_data.setAmount(rs.getString("B.amount"));
				result_data.setTax(rs.getString("B.tax"));
				amountTaxList.add(result_data);
		      }
			
		}catch(Exception e) {
			System.out.println("データ取得例外エラー：" + e);
		}
		
		return amountTaxList;
	}
}
