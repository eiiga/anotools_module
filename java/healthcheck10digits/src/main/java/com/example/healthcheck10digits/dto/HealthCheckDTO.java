package com.example.healthcheck10digits.dto;

import java.time.LocalDateTime;
import lombok.Value;

@Value
public class HealthCheckDTO {
  String rand10Digits;
  LocalDateTime timeStampNow;
}
