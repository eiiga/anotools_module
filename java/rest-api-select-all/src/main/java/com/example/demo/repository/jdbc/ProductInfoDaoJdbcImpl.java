package com.example.demo.repository.jdbc;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import com.example.demo.repository.ProductInfoDao;
import com.example.model.ProductInfo;

@Repository
public class ProductInfoDaoJdbcImpl implements ProductInfoDao {

	@Autowired
	JdbcTemplate jdbc;

	// 全件検索用SQL
	private static final String SELECT_ALL_SQL_STRING = "SELECT * FROM M_PRODUCT_INFORMATION";

	@Override
	public List<ProductInfo> selectAll() throws DataAccessException {

		// 全件取得
		final List<Map<String, Object>> allData = jdbc.queryForList(SELECT_ALL_SQL_STRING);

		// 結果返却用変数
		final List<ProductInfo> productInfoList = new ArrayList<>();

		// 取得したデータ件数分繰り返し
		for (Map<String, Object> map : allData) {

			ProductInfo productInfo = new ProductInfo();

			// 商品コード
			productInfo.setProductCode((String) map.get("product_code"));

			// 商品名
			productInfo.setProductName((String) map.get("product_name"));

			// 金額
			productInfo.setAmount((Integer) map.get("amount"));

			// 返却用リストに詰め替る
			productInfoList.add(productInfo);
		}

		return productInfoList;

	}

}
