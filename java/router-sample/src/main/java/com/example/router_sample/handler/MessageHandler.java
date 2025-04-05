package com.example.router_sample.handler;

import com.example.router_sample.message.MessagePayload;

public class MessageHandler {

  public void handleA(MessagePayload payload) {
    System.out.println("Aタイプの処理: " + payload.getMessage());
  }

  public void handleB(MessagePayload payload) {
    System.out.println("Bタイプの処理: " + payload.getMessage());
  }

  public void handleDefault(MessagePayload payload) {
    System.out.println("未定義タイプ: " + payload.getMessage());
  }
}

