package com.practice.annotation.anotools_spring.service;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import java.util.List;

public interface UserService {

  public int getUserRandomId();

  public List<UserDTO> selectAllUser();
}
