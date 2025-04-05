package com.example.router_sample;

import com.example.router_sample.message.MessagePayload;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.support.MessageBuilder;

@SpringBootApplication
public class RouterSampleApplication {

  public static void main(String[] args) {
    SpringApplication.run(RouterSampleApplication.class, args);
  }

  @Bean
  public CommandLineRunner run(@Qualifier("inputChannel") MessageChannel inputChannel) {
    return args -> {
      MessagePayload payload = new MessagePayload("C", "ルーティングテスト");
      Message<?> message = MessageBuilder.withPayload(payload).build();
      inputChannel.send(message);
    };
  }


}
