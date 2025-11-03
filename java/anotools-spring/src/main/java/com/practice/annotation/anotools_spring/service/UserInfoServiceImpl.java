package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.repository.UserRepository;
import java.util.List;
import java.util.stream.Collectors;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserInfoServiceImpl implements UserInfoService {

  private final UserRepository userRepository;

  @Override
  public List<UserDTO> selectAllUser() {
    return userRepository.findAll()
        .stream()
        .map(entity -> new UserDTO(entity.getId(), entity.getName(), entity.getMailAddress()))
        .collect(Collectors.toList());
  }
}
