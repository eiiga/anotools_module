package com.example.router_sample.handler;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

import com.example.router_sample.message.MessagePayload;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

@TestInstance(Lifecycle.PER_CLASS)
public class MessageHandlerTest {

  @Test
  @DisplayName("正常系：handleA")
  void handleATestNormal() {
    MessagePayload payload = new MessagePayload("A", "Test Message");
    MessageHandler handler = new MessageHandler();
    assertDoesNotThrow(() -> handler.handleA(payload));
  }

  @Test
  @DisplayName("正常系：handleB")
  void handleBTestNormal() {
    MessagePayload payload = new MessagePayload("B", "Test Message");
    MessageHandler handler = new MessageHandler();
    assertDoesNotThrow(() -> handler.handleB(payload));
  }

  @Test
  @DisplayName("正常系：handleDefault")
  void handleDefaultTestNormal() {
    MessagePayload payload = new MessagePayload("C", "Test Message");
    MessageHandler handler = new MessageHandler();
    assertDoesNotThrow(() -> handler.handleDefault(payload));
  }
}
