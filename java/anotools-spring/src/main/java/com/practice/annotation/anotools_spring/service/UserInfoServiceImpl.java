package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.repository.UserRepository;
import java.util.List;
import java.util.Optional;
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

  @Override
  public Optional<UserDTO> selectOneUser(long id) {
    return userRepository.findOne(id)
        .map(user -> new UserDTO(user.getId(), user.getName(), user.getMailAddress()));

  }

  @Override
  public boolean updateOneUser(UserDTO userDTO) {
    return userRepository.updateOne(userDTO);
  }
}
