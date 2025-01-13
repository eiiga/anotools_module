package main;

import sample.SampleInitializer;

public class HowToInitializerMain {

  public static void main(String[] args){

    SampleInitializer sampleInitializerUserA = new SampleInitializer("UserA", 50, 40);
    sampleInitializerUserA.getUserSumAverageScore();

    SampleInitializer sampleInitializerUserB = new SampleInitializer("UserB", 60, 70, 80);
    sampleInitializerUserB.getUserSumAverageScore();

    SampleInitializer sampleInitializerUserC = new SampleInitializer("UserC", 30, 60, 20, 100, 70);
    sampleInitializerUserC.getUserSumAverageScore();

  }
}
