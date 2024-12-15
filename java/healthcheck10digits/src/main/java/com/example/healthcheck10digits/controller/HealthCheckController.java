package com.example.healthcheck10digits.controller;

import java.time.LocalDateTime;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.example.healthcheck10digits.dto.HealthCheckDTO;
import com.example.healthcheck10digits.util.Rand10DigitsUtil;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/health")
public class HealthCheckController {

  @GetMapping
  public HealthCheckDTO healthCheckDTO(){
    // 10桁生成クラスのインスタンス
    Rand10DigitsUtil rand10DigitsUtil = new Rand10DigitsUtil();

    // 10桁乱数と現在時刻を返す
    return new HealthCheckDTO(rand10DigitsUtil.get10DigitsNumber(), LocalDateTime.now());
  }

}
