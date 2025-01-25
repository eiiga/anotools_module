package com.example.get_properties_data.config;

import com.example.get_properties_data.dto.PropertiesDTO;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:conf/sampleC.properties")
public class GetSampleCConfig {

  @Value("${sample.c.title}")
  private String titleC;

  @Value("${sample.c.data}")
  private String dataC;

  @Value("${sample.c.value}")
  private String valueC;

  @Value("${sample.c.message}")
  private String messageC;

  /**
   * プロパティサンプルC読み込み処理
   *
   * @return PropertiesDTO
   */
  public PropertiesDTO setPropertiesSampleCDTO() {

    PropertiesDTO propertiesData = new PropertiesDTO();

    propertiesData.setTitle(titleC);
    propertiesData.setData(dataC);
    propertiesData.setValue(Integer.parseInt(valueC));
    propertiesData.setMessage(messageC);

    return propertiesData;
  }

}
