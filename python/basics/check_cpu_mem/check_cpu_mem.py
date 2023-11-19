import logging
import psutil
import threading

# 日時：ログレベル：スレッド名：モジュール名：関数名：メッセージを出力する
LOGGING_FORMAT = '%(asctime)s:' \
    + '[%(levelname)s]:' \
    + '[%(threadName)s]:'  \
    + '[%(module)s]:' \
    + '[%(funcName)s]:' \
    + '%(message)s'

# ログレベル：デバッグ
logging.basicConfig(
    level=logging.DEBUG, format=LOGGING_FORMAT
)

# N秒間隔で測定
INTERVAL_SEC= 59

# CPUとMemoryの使用率を出力する関数
def check_cpu_memory(event):
    while not event.wait(INTERVAL_SEC):
        # CPU使用率を取得
        cpu_data = psutil.cpu_percent(interval=1)
        # Memoryを取得
        mem_data = psutil.virtual_memory()
        
        log_msg =  str(cpu_data) + ": " + str(mem_data.percent)
        
        # 「CPU使用率、メモリ使用率」を出力
        logging.debug(log_msg)

# メイン処理
if __name__ == '__main__':
     # 1分間隔で「CPUとMemoryの使用率を出力する関数」を実行
    event = threading.Event()
    t = threading.Thread(target=check_cpu_memory, args=(event, ))
    
    t.start()
    

# 参考URL
# https://pg-chain.com/python-psutil
# https://qiita.com/john-rocky/items/a0452e6fdb7639b5d044
# https://di-acc2.com/programming/python/4574/