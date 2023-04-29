import datetime
import os
import sys
import time

# 環境ごとにコマンドの定数を設定
# Windowsの場合は音を鳴らすためにモジュールを追加でimport
if os.name == 'nt':
    CMD_CLEAR = 'cls'
    import winsound
    START_PLAYSOUND_NAME = 'SystemAsterisk'
    END_PLAYSOUND_NAME = 'SystemExclamation'
# macの場合
elif os.name == 'posix':
    CMD_CLEAR = 'clear'
    CMD_START_WORK_SOUND = 'afplay /System/Library/Sounds/Blow.aiff'
    CMD_START_REST_SOUND = 'afplay /System/Library/Sounds/Submarine.aiff'
# 上記以外は終了
else:
    sys.exit()

# 文言の定数
MSG_CTRL_C = '終了する場合は ctrl + c を押してください'
MSG_WORK_TIME = '作業時間：'
MSG_REST_TIME = '休憩時間：'

# 開始音出力関数
def start_sound(is_flg):
    # windowsの場合
    if os.name == 'nt':
        # 作業開始の場合
        if is_flg:
            winsound.PlaySound(START_PLAYSOUND_NAME, winsound.SND_ALIAS)
        # 休憩開始の場合
        else:
            winsound.PlaySound(END_PLAYSOUND_NAME, winsound.SND_ALIAS)
    # macの場合
    elif os.name == 'posix':
        # 作業開始の場合
        if is_flg:
            os.system(CMD_START_WORK_SOUND)
        # 作業終了の場合
        else:
            os.system(CMD_START_REST_SOUND)


# タイマーカウント関数    
def count_timer(Is_flg, kind_tmp_time, msg_time):
    # 開始音出力
    start_sound(Is_flg)
            
    # 時間が0になるまで繰り返し
    while kind_tmp_time.strftime("%H:%M:%S") != "00:00:00":
                
        # コンソール初期化処理
        os.system(CMD_CLEAR)
                
        # 文言と残り時間を出力
        print(MSG_CTRL_C)
        print(msg_time, kind_tmp_time.strftime("%H:%M:%S"))
                
        # 1秒待機
        time.sleep(1)
                
        # 作業時間を1秒マイナス
        kind_tmp_time = kind_tmp_time - datetime.timedelta(seconds=1)
    
    # フラグを反転させて返す
    return not Is_flg


# タイマー開始処理関数
def start_timer(timer_list):
    # True:作業 False:休憩
    is_work_time = True
    
    # 作業時間（分）を取得
    work_time = int(timer_list[0])
   
    # 60分以上の換算処理
    work_hour, work_min = divmod(work_time, 60)
    
    # 休憩時間（分）を取得
    rest_time = int(timer_list[1])
    
    # 60分以上の換算処理
    rest_hour, rest_min = divmod(rest_time, 60)
   
    # 無限ループ
    while True:
        # 作業時間と休憩時間を今日日付＋時刻に変換
        tmp_work_time = datetime.datetime.combine(datetime.datetime.today(),datetime.time(work_hour, work_min))
        tmp_rest_time = datetime.datetime.combine(datetime.datetime.today(),datetime.time(rest_hour, rest_min))
        
        # 作業時間の場合
        if is_work_time:
            is_work_time = count_timer(is_work_time, tmp_work_time, MSG_WORK_TIME)
        
        # 休憩時間の場合
        else:
            is_work_time = count_timer(is_work_time, tmp_rest_time, MSG_REST_TIME)


# タイマーセットアップ関数
def setup_timer():
    
    # コンソール初期化処理
    os.system(CMD_CLEAR)
    
    # 作業時間と休憩時間を格納する配列初期化
    input_timer_list =[]

    # 作業時間と休憩時間を入力
    input_work_time = input("作業時間（分）を入力してください：")
    input_rest_time = input("休憩時間（分）を入力してください：")
    
    # 配列に作業時間と休憩時間を格納
    input_timer_list.append(input_work_time)
    input_timer_list.append(input_rest_time)
    
    # 作業時間と休憩時間の配列を返す
    return input_timer_list
    

# メイン処理
if __name__ == '__main__':
    # タイマーセットアップ関数呼び出し
    input_timer_list = setup_timer()
    
    # タイマー開始処理関数呼び出し
    start_timer(input_timer_list)