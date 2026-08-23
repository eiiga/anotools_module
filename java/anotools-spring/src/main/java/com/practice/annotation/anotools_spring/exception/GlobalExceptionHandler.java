package com.practice.annotation.anotools_spring.exception;

import com.practice.annotation.anotools_spring.message.ErrorResponseMessage;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

  // 業務例外
  @ExceptionHandler(BusinessException.class)
  public ResponseEntity<ErrorResponseMessage> handleBusinessException(BusinessException e) {
    ErrorResponseMessage error = new ErrorResponseMessage(e.getMessage(), "BUSINESS_ERROR");
    return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
  }

  // 予期しない例外
  @ExceptionHandler(Exception.class)
  public ResponseEntity<ErrorResponseMessage> handleException(Exception e) {
    ErrorResponseMessage error = new ErrorResponseMessage("サーバー内部エラーが発生しました",
        "INTERNAL_ERROR");
    return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
  }
}

