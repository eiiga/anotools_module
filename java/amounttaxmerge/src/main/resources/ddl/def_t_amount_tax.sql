-- 金額・税テーブル
CREATE TABLE t_amount_tax (
	data_id CHAR(4) NOT NULL,
	amount VARCHAR(10) NOT NULL,
	tax VARCHAR(5) NOT NULL,
	FOREIGN KEY data_id_foreign_key(data_id) REFERENCES m_data_name(id)
);
