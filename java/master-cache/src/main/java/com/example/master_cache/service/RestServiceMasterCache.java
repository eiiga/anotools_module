package com.example.master_cache.service;

import com.example.master_cache.dto.MasterDTO;
import java.util.List;

public interface RestServiceMasterCache {

  public List<MasterDTO> selectAll();
}
