-- 商品情報マスタテーブル
CREATE TABLE IF NOT EXISTS M_PRODUCT_INFORMATION(
	product_code VARCHAR(4) PRIMARY KEY,
	product_name VARCHAR(50),
	amount INT
);