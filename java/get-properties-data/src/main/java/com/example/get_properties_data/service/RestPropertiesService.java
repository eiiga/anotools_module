package com.example.get_properties_data.service;

import com.example.get_properties_data.dto.PropertiesDTO;
import java.util.Map;

public interface RestPropertiesService {
  // propertiesの値を取得
  public PropertiesDTO getPropertiesDTO(String params);
}
