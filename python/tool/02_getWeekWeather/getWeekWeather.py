import csv
import requests

from bs4 import BeautifulSoup

# データNo（東京）
DATA_NO = '4410'
# Yahooの天気URL
URL = 'https://weather.yahoo.co.jp/weather/jp/13/' + DATA_NO + '.html'


def get_week_weather():
    '''
    1週間の天気を取得する
        
    Parameters
    ----------
    なし
    
    Returns
    -------
    1週間の天気（List）

    '''
    # Yahooの天気サイトへ接続
    r = requests.get(URL)
    # BeautifulSoupのインスタンス
    bs = BeautifulSoup(r.text, 'html.parser')
    
    # HTMLの週間天気classをセット
    temperature_data = bs.find(class_='yjw_table')
    
    # 1週間の天気を配列に格納
    week_data = [
        i.strip() for i in temperature_data.text.splitlines() if i.strip() != ''
        ]

    return week_data


def output_csv(week_weather_data):
    '''
    CSVファイルに出力する処理
    
    Parameters
    ----------
    1週間の天気（List）
    
    Returns
    -------
    なし
    
    Output File
    -----------
    week_weather.csv
    
    '''

    # 出力用csvファイルを開く
    with open('week_weather.csv', 'w') as f:
        # csv.writerをインスタンス
        output = csv.writer(f)
        # 1週間の天気情報をcsvファイルに出力
        output.writerow(week_weather_data)


# メイン処理
if __name__ == '__main__':
    
    # 1週間の天気情報を取得
    week_weather_data = get_week_weather()
    
    # csvファイルに出力
    output_csv(week_weather_data)