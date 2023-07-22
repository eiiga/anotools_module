package main;


import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;

public class ReadPropertiesMain {
	
	// プロパティファイルのパス
	private static final String CONF_FILE_PATH = "conf/sample_setting.properties";
	
	// プロパティクラスのインスタンス
	private static final Properties properties = new Properties();
	
	// キー項目
	private static final String KEY_WORD_AAA = "key_word_aaa";
	private static final String KEY_WORD_BBB = "key_word_bbb";
	private static final String KEY_WORD_CCC = "key_word_ccc";
	private static final String URL_DATA = "url_data";
	
	// メイン処理
	public static void main(String[] args) {
		try {
			// プロパティファイルの読み込み
			properties.load(Files.newBufferedReader(Paths.get(CONF_FILE_PATH), StandardCharsets.UTF_8));
			
			// キー項目に対する値を出力
			System.out.println(properties.getProperty(KEY_WORD_AAA));
			System.out.println(properties.getProperty(KEY_WORD_BBB));
			System.out.println(properties.getProperty(KEY_WORD_CCC));
			System.out.println(properties.getProperty(URL_DATA));
		
		// 例外処理
		}catch(Exception e) {
			System.out.println("例外エラー：" + e);
		}
		

	}

}
