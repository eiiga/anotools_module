import psutil
import threading
import datetime


# N分間隔で測定
INTERVAL_MIN = 1
# 最計測時間（分）を指定
MAX_MIN = 60

def check_cpu_memory():
    cpu_data = psutil.cpu_percent(percpu=True)
    print(cpu_data)
    # print(datetime.datetime.now(), 
    #       psutil.virtual_memory() )

if __name__ == '__main__':
    check_cpu_memory()
    

# 参考URL
# https://pg-chain.com/python-psutil
# https://qiita.com/john-rocky/items/a0452e6fdb7639b5d044