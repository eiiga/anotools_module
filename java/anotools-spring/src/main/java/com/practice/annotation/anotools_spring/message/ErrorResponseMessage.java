package com.practice.annotation.anotools_spring.message;

import java.time.LocalDateTime;
import lombok.Value;

@Value
public class ErrorResponseMessage {

  String message;
  String errorCode;
  String timestamp;

  public ErrorResponseMessage(String message, String errorCode) {
    this.message = message;
    this.errorCode = errorCode;
    this.timestamp = LocalDateTime.now().toString();
  }

}

