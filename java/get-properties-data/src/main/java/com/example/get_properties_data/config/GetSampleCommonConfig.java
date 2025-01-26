package com.example.get_properties_data.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

/**
 * プロパティサンプル共通読み込みクラス
 */
@Configuration
@PropertySource("classpath:conf/sampleCommon.properties")
public class GetSampleCommonConfig {

}
