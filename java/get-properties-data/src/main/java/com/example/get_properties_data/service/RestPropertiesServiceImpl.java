package com.example.get_properties_data.service;

import com.example.get_properties_data.config.GetSampleAConfig;
import com.example.get_properties_data.config.GetSampleBConfig;
import com.example.get_properties_data.config.GetSampleCConfig;
import com.example.get_properties_data.dto.PropertiesDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class RestPropertiesServiceImpl implements RestPropertiesService {

  @Autowired
  private GetSampleAConfig getSampleAConfig;

  @Autowired
  private GetSampleBConfig getSampleBConfig;

  @Autowired
  private GetSampleCConfig getSampleCConfig;

  @Value("${sample.common.header}")
  private String header;

  /**
   * プロパティ情報取得処理 URLに応じてプロパティの値をセットする
   *
   * @param params: URL：a, b, c, other
   * @return PropertiesDTO
   */
  @Override
  public PropertiesDTO getPropertiesDTO(String params) {

    // 返却用DTO
    PropertiesDTO resultDTO = null;

    // paramごとにプロパティをセットする
    if ("a".equals(params)) {
      resultDTO = getSampleAConfig.setPropertiesSampleADTO();
    } else if ("b".equals(params)) {
      resultDTO = getSampleBConfig.setPropertiesSampleBDTO();
    } else if ("c".equals(params)) {
      resultDTO = getSampleCConfig.setPropertiesSampleCDTO();
    } else {
      resultDTO = setOthers();
    }

    // 共通のヘッダ情報をセットする
    resultDTO.setHeader(header);

    return resultDTO;

  }

  /**
   * プロパティ情報その他のセット処理 - NGのメッセージをセットする
   *
   * @return PropertiesDTO
   */
  private PropertiesDTO setOthers() {

    PropertiesDTO others = new PropertiesDTO();

    // メッセージにNG情報をセット
    others.setMessage("NG: Please choose a, b, or c in URL.");

    return others;

  }
}
