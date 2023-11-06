import datetime
import psutil
import schedule
import time


# N分間隔で測定
INTERVAL_SEC= 60
# 出力用のヘッダーをセット
HEADER_INFO = 'time,cpu(%),memory(%)'

# CPUとMemoryの使用率を出力する関数
def check_cpu_memory():
    # 現在時刻を取得
    now_time = datetime.datetime.now()
    # CPU使用率を取得
    cpu_data = psutil.cpu_percent(interval=1)
    # Memoryを取得
    mem_data = psutil.virtual_memory()
    
    # カンマ区切りで「時間、CPU使用率、メモリ使用率」を出力
    print(now_time, cpu_data, mem_data.percent, sep=',')


# メイン処理
if __name__ == '__main__':
    # ヘッダーを出力
    print(HEADER_INFO)
    
    # 1分間隔で「CPUとMemoryの使用率を出力する関数」を実行
    schedule.every(1).minutes.do(check_cpu_memory)

    # 無限ループ
    while True:
        # スケジューラを定期実行
        schedule.run_pending()
        
        # 無限ループで実行し続けによる処理負荷がかからないように待機させる
        time.sleep(30)
    

# 参考URL
# https://pg-chain.com/python-psutil
# https://qiita.com/john-rocky/items/a0452e6fdb7639b5d044
# https://di-acc2.com/programming/python/4574/