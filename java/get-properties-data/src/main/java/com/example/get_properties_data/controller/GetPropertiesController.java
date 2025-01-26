package com.example.get_properties_data.controller;

import com.example.get_properties_data.dto.PropertiesDTO;
import com.example.get_properties_data.service.RestPropertiesService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GetPropertiesController {

  @Autowired
  private RestPropertiesService restPropertiesService;

  @GetMapping("/rest/sample/{param}")
  public PropertiesDTO getPropertiesData(@PathVariable String param) {
    return restPropertiesService.getPropertiesDTO(param);
  }
}
