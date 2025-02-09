package com.example.master_cache.service;

import com.example.master_cache.dto.MasterDTO;
import com.example.master_cache.repository.MasterCacheRepository;
import java.util.List;
import java.util.stream.Collectors;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RestServiceMasterCacheImpl implements RestServiceMasterCache {

  private final MasterCacheRepository repository;

  @Override
  @Cacheable("master")
  public List<MasterDTO> selectAll() {
    return repository.find()
        .stream()
        .map(entity -> new MasterDTO(entity.getId(), entity.getData()))
        .collect(Collectors.toList());

  }

}
