package com.example.get_properties_data.config;

import com.example.get_properties_data.dto.PropertiesDTO;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:conf/sampleB.properties")
public class GetSampleBConfig {

  @Value("${sample.b.title}")
  private String titleB;

  @Value("${sample.b.data}")
  private String dataB;

  @Value("${sample.b.value}")
  private String valueB;

  @Value("${sample.b.message}")
  private String messageB;

  /**
   * プロパティサンプルB読み込み処理
   *
   * @return PropertiesDTO
   */
  public PropertiesDTO setPropertiesSampleBDTO() {

    PropertiesDTO propertiesData = new PropertiesDTO();

    propertiesData.setTitle(titleB);
    propertiesData.setData(dataB);
    propertiesData.setValue(Integer.parseInt(valueB));
    propertiesData.setMessage(messageB);

    return propertiesData;
  }

}
