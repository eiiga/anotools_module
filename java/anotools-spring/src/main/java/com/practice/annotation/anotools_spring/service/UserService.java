package com.practice.annotation.anotools_spring.service;

import java.util.concurrent.ThreadLocalRandom;
import org.springframework.stereotype.Service;

@Service
public class UserService {

  public int getUserId() {

    // 1から100までのランダムな数字を返す
    return ThreadLocalRandom.current().nextInt(1, 101);
  }
}
