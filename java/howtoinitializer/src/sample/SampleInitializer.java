package sample;

public class SampleInitializer {

  private String userName;
  private int scoreJapanese;
  private int scoreEnglish;
  private int scoreMath;
  private int scoreScience;
  private int scoreHistory;
  private int[] scoreList;

  // 初期化子
  {
    System.out.println("====ユーザの合計・平均点算出クラス呼び出し====");
  }

  /* 言語科目のコンストラクタ
      @param ユーザ名
      @param 国語
      @param 英語
   */
  public SampleInitializer(String userName, int scoreJapanese, int scoreEnglish) {
    this.userName = userName;
    this.scoreJapanese = scoreJapanese;
    this.scoreEnglish = scoreEnglish;
    this.scoreList = new int[]{this.scoreJapanese, this.scoreEnglish};
  }

  /* 言語科目以外のコンストラクタ
      @param ユーザ名
      @param 数学
      @param 科学
      @param 歴史
   */
  public SampleInitializer(String userName, int scoreMath, int scoreScience, int scoreHistory) {
    this.userName = userName;
    this.scoreMath = scoreMath;
    this.scoreScience = scoreScience;
    this.scoreHistory = scoreHistory;
    this.scoreList = new int[]{this.scoreMath, this.scoreScience, this.scoreHistory};

  }

  /* 全科目のコンストラクタ
      @param ユーザ名
      @param 国語
      @param 英語
      @param 数学
      @param 科学
      @param 歴史
   */
  public SampleInitializer(String userName, int scoreJapanese, int scoreEnglish, int scoreMath,
      int scoreScience, int scoreHistory) {
    this.userName = userName;
    this.scoreJapanese = scoreJapanese;
    this.scoreEnglish = scoreEnglish;
    this.scoreMath = scoreMath;
    this.scoreScience = scoreScience;
    this.scoreHistory = scoreHistory;
    this.scoreList = new int[]{this.scoreJapanese, this.scoreEnglish, this.scoreMath, this.scoreScience, this.scoreHistory};
  }

  // 合計点を算出する処理
  private int calSum(){
    // 返却用合計値
    int sum = 0;

    // 得点リスト分繰り返し
    for (int score: this.scoreList){

      // 得点を加算する
      sum += score;
    }
    return sum;
  }

  // 平均点を算出する処理
  private double calAverage(){
    if (this.scoreList.length == 0){
      return 0;
    }
    return (double) calSum() / this.scoreList.length;
  }

  // ユーザの合計・平均を出力する処理
  public void getUserSumAverageScore(){
    System.out.println("ユーザ名：" + this.userName);
    System.out.println("合計点：" + calSum());
    System.out.println("平均点：" + calAverage());

  }

}