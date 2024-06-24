package com.iojsondata;

import java.util.List;

// ユーザデータクラス
public class UserData {
	public String id;			// ユーザID
	public String user_name;	// ユーザ名
	public int age;				// 年齢
	public UserSubData1 subdata1;	// サブデータ1
	public List<UserSubData2> subdata2;	// サブデータ2
}
