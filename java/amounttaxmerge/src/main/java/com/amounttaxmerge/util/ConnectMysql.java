package com.amounttaxmerge.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

// DB接続クラス
public class ConnectMysql {
	
	// DB接続情報
	private static final String DATABASE_NAME = "AmountTaxMerge";
	private static final String JDBC_URL = "jdbc:mysql://127.0.0.1/" + DATABASE_NAME;
	private static final String DB_USER = "user001";
	private static final String DB_PASSWORD = "aaa";
	private static final String DRIVER_NAME = "com.mysql.cj.jdbc.Driver";
	
	// DB接続処理
	public Connection mysqlconnection() {
		
		// コネクション情報初期化
		Connection conn = null;
		
		try {
			// ドライバセット
			Class.forName(DRIVER_NAME);
			
			// DB接続
			conn = DriverManager.getConnection(JDBC_URL, DB_USER, DB_PASSWORD);
			
			// debug code
			// System.out.println("SQL接続成功");
		
		// 例外処理：SQL EXCEPTION
		} catch(SQLException sql_e) {
			// 例外出力
			System.out.println("SQL接続Exception：" + sql_e);
		
		// 例外処理：ClassNotFoundException 
		} catch(ClassNotFoundException class_e) {
			// 例外出力
			System.out.println("ClassException：" + class_e);
		}
		
		// DB接続情報を返す
		return conn;	
	}
}
