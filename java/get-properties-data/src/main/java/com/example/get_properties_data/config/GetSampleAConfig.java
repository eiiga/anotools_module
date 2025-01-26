package com.example.get_properties_data.config;

import com.example.get_properties_data.dto.PropertiesDTO;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:conf/sampleA.properties")
public class GetSampleAConfig {

  @Value("${sample.a.title}")
  private String titleA;

  @Value("${sample.a.data}")
  private String dataA;

  @Value("${sample.a.value}")
  private String valueA;

  @Value("${sample.a.message}")
  private String messageA;

  /**
   * プロパティサンプルA読み込み処理
   *
   * @return PropertiesDTO
   */
  public PropertiesDTO setPropertiesSampleADTO() {

    PropertiesDTO propertiesData = new PropertiesDTO();

    propertiesData.setTitle(titleA);
    propertiesData.setData(dataA);
    propertiesData.setValue(Integer.parseInt(valueA));
    propertiesData.setMessage(messageA);

    return propertiesData;
  }

}
