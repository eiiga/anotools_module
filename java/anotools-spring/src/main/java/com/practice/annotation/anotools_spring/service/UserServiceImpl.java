package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.repository.UserRepository;
import java.util.concurrent.ThreadLocalRandom;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

  private final UserRepository userRepository;

  @Override
  public int getUserRandomId() {

    // 1から100までのランダムな数字を返す
    return ThreadLocalRandom.current().nextInt(1, 101);
  }

}
