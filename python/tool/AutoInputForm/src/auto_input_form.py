import os

import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By


# htmlファイルの格納場所
HTML_FILE_PATH = 'template/index.html'

# confファイルの格納場所
CONFIG_FILE_PATH = './conf/template_info.conf'

# confの設定内容のセクション情報
CONF_SECTION_TEMPLATE = 'template'

# confの設定内容のkey情報
CONF_KEY_USERNAME       = 'username'        # ユーザ名
CONF_KEY_USERNAME_KANA  = 'username_kana'   # ユーザ名（カナ）
CONF_KEY_COMPANY_NAME   = 'company_name'    # 会社名
CONF_KEY_EMAIL_ADDRESS  = 'email_address'   # メールアドレス
CONF_KEY_TEL_NO         = 'tel_no'          # 電話番号


# conf情報取得処理
def read_conf_file():
    # 返却用Dict
    template_info_dict ={}

    # ConfigParserオブジェクトの生成
    config = configparser.ConfigParser()

    # confファイルの読み込み
    config.read(CONFIG_FILE_PATH)

    # セクションの取得
    config_section = config[CONF_SECTION_TEMPLATE]

    # confの情報をDictに格納
    template_info_dict[CONF_KEY_USERNAME]       = config_section.get(CONF_KEY_USERNAME)
    template_info_dict[CONF_KEY_USERNAME_KANA]  = config_section.get(CONF_KEY_USERNAME_KANA)
    template_info_dict[CONF_KEY_COMPANY_NAME]   = config_section.get(CONF_KEY_COMPANY_NAME)
    template_info_dict[CONF_KEY_EMAIL_ADDRESS]  = config_section.get(CONF_KEY_EMAIL_ADDRESS)
    template_info_dict[CONF_KEY_TEL_NO]         = config_section.get(CONF_KEY_TEL_NO)

    return template_info_dict


# HTML自動反映処理
def output_from_conf_to_html():
    # conf情報取得処理呼び出し
    template_info_dict = read_conf_file()
    
    # mac用
    chrome = webdriver.Chrome()
    # Windows用：chromedriverのパスを指定
    # chrome = webdriver.Chrome("ここにパスを記載する")
    
    # カレントディレクトリを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    html_file_full_path = os.path.join(current_dir, "..", HTML_FILE_PATH)
    
    chrome.get("file://" + html_file_full_path)

    # HTMLのIDを取得
    html_id_username        = chrome.find_element(By.ID, CONF_KEY_USERNAME)
    html_id_username_kana   = chrome.find_element(By.ID, CONF_KEY_USERNAME_KANA)
    html_id_company_name    = chrome.find_element(By.ID, CONF_KEY_COMPANY_NAME)
    html_id_email_address   = chrome.find_element(By.ID, CONF_KEY_EMAIL_ADDRESS)
    html_id_tel_no          = chrome.find_element(By.ID, CONF_KEY_TEL_NO)
    
    # HTMLに値を設定
    html_id_username.send_keys(template_info_dict[CONF_KEY_USERNAME])
    html_id_username_kana.send_keys(template_info_dict[CONF_KEY_USERNAME_KANA])
    html_id_company_name.send_keys(template_info_dict[CONF_KEY_COMPANY_NAME])
    html_id_email_address.send_keys(template_info_dict[CONF_KEY_EMAIL_ADDRESS])
    html_id_tel_no.send_keys(template_info_dict[CONF_KEY_TEL_NO])


# メイン処理
if __name__ == '__main__':
    output_from_conf_to_html()