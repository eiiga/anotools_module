package com.practice.annotation.anotools_spring.repository;

import com.practice.annotation.anotools_spring.entity.UserEntity;
import java.util.List;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserRepository {

  List<UserEntity> findAll();
}
