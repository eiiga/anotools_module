import logging

# ログ出力フォーマットを設定
# 日付：[ログレベル]:[モジュール名]:[ファンクション名]:メッセージ
FORMMATER = '%(asctime)s:[%(levelname)s]:[%(module)s]:[%(funcName)s]:%(message)s'



# ログ出力サンプル関数
def logging_sample_fnc():
    # 処理開始
    logging.info('start: logging_sample_fnc')
    
    try:
        data1 = 1
        
        if data1 == 1:
            # debugレベルでdata1を出力
            logging.debug('data1 = %s', data1)
        
        data2 = 0
        
        if data2 != 1:
            # warningレベルでdata2を出力
            logging.warning('[different value] data2 = %s', data2)

        # 強制的に例外へ
        raise
    
    # 例外処理
    except :
        # errorレベルで出力
        logging.error('例外エラー')
    
    finally:
        # 処理終了
        logging.info('end: logging_sample_fnc')

if __name__ == '__main__':
    # DEBUGレベルでログ出力
    # logging.basicConfig(filename='level_debug.log', level=logging.DEBUG, format=FORMMATER)
    # logging_sample_fnc()
    
    # INFOレベルでログ出力
    logging.basicConfig(filename='level_info.log', level=logging.INFO, format=FORMMATER)
    logging_sample_fnc()