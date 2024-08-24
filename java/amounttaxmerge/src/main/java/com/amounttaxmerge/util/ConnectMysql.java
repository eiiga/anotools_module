package com.amounttaxmerge.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectMysql {
	
	// DB接続情報
	private static final String DATABASE_NAME = "AmountTaxMerge";
	private static final String JDBC_URL = "jdbc:mysql://127.0.0.1/" + DATABASE_NAME;
	private static final String DB_USER = "user001";
	private static final String DB_PASSWORD = "aaa";
	private static final String DRIVER_NAME = "com.mysql.cj.jdbc.Driver";
	
	public Connection mysqlconnection() {
		
		Connection conn = null;
		
		try {
			Class.forName(DRIVER_NAME);
			conn = DriverManager.getConnection(JDBC_URL, DB_USER, DB_PASSWORD);
			
			// debug code
			// System.out.println("SQL接続成功");
			
		} catch(SQLException sql_e) {
			System.out.println("SQL接続Exception：" + sql_e);
		} catch(ClassNotFoundException class_e) { 
			System.out.println("ClassException：" + class_e);
		}
		
		return conn;
		
	}

}
