package main;

import sample.SampleInitializer;

public class HowToInitializerMain {

  public static void main(String[] args){

    // 言語科目
    SampleInitializer sampleInitializerUserA = new SampleInitializer("UserA", 50, 40);
    sampleInitializerUserA.getUserSumAverageScore();

    // 言語科目以外
    SampleInitializer sampleInitializerUserB = new SampleInitializer("UserB", 60, 70, 80);
    sampleInitializerUserB.getUserSumAverageScore();

    // 全科目
    SampleInitializer sampleInitializerUserC = new SampleInitializer("UserC", 30, 60, 20, 100, 70);
    sampleInitializerUserC.getUserSumAverageScore();

  }
}
