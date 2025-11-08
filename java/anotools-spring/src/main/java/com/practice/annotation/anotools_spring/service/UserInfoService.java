package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import java.util.List;
import java.util.Optional;

public interface UserInfoService {

  public List<UserDTO> selectAllUser();

  public Optional<UserDTO> selectOneUser(long id);

  public boolean updateOneUser(UserDTO userDto);
}
