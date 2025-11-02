package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.repository.UserRepository;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

  private final UserRepository userRepository;

  @Override
  public int getUserId() {

    // 1から100までのランダムな数字を返す
    return ThreadLocalRandom.current().nextInt(1, 101);
  }

  @Override
  public List<UserDTO> selectAllUser() {
    return userRepository.findAll()
        .stream()
        .map(entity -> new UserDTO(entity.getId(), entity.getName(), entity.getMailAddress()))
        .collect(Collectors.toList());
  }
}
