package reader;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import constant.FilePathConstant;

// CSVファイル読み込みクラス
public class CsvReader {

  /*
   * CSVファイル読み込み処理
   * 
   * @input ファイルパス
   * 
   * @return BufferedReader
   */
  public static BufferedReader csvFileReader(final FilePathConstant path) {

    try {
      // ファイルオブジェクト生成
      final File csvFile = new File(path.getFilePathConstant());

      // FileReaderオブジェクト生成
      final FileReader fReader = new FileReader(csvFile);

      // BufferedReaderオブジェクトを返却
      return new BufferedReader(fReader);

    } catch (Exception e) {
      System.out.println("csvFileReader例外エラー：" + e);

      return null;
    }
  }
}
