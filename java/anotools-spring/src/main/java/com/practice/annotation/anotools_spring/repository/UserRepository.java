package com.practice.annotation.anotools_spring.repository;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.entity.UserEntity;
import java.util.List;
import java.util.Optional;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserRepository {

  List<UserEntity> findAll();

  Optional<UserEntity> findOne(long id);

  boolean updateOne(UserDTO userDTO);
}
