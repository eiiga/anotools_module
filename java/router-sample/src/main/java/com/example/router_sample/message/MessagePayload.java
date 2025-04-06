package com.example.router_sample.message;

public class MessagePayload {

  private final String type;
  private final String message;

  public MessagePayload(String type, String message) {
    this.type = type;
    this.message = message;
  }

  public String getType() {
    return type;
  }

  public String getMessage() {
    return message;
  }
}
