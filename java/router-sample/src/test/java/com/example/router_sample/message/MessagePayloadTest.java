package com.example.router_sample.message;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

@TestInstance(Lifecycle.PER_CLASS)
public class MessagePayloadTest {

  private final MessagePayload payload;

  public MessagePayloadTest() {
    payload = new MessagePayload("A", "Test Message");
  }

  @Test
  @DisplayName("正常系：getType()")
  void getTypeTest() {
    assertEquals("A", payload.getType());
  }

  @Test
  @DisplayName("正常系：getMessage()")
  void getMessageTest() {
    assertEquals("Test Message", payload.getMessage());
  }

}
