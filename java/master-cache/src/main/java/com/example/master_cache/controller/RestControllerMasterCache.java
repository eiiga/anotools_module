package com.example.master_cache.controller;

import com.example.master_cache.dto.MasterDTO;
import com.example.master_cache.service.RestServiceMasterCache;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class RestControllerMasterCache {

  private final RestServiceMasterCache service;

  @GetMapping("/rest/master")
  public List<MasterDTO> getListMasterDto() {
    return service.selectAll();
  }

}
