package com.example.master_cache;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@EnableCaching
@SpringBootApplication
public class MasterCacheApplication {

	public static void main(String[] args) {
		SpringApplication.run(MasterCacheApplication.class, args);
	}

}
