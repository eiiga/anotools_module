import configparser
import json
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg


# マスタiniファイルの相対パス
MST_INI_FILEPATH = r'./DEF/mst.ini'

ANS_CSV_FILEPATH = r'./ANS/ansewr.csv'

def read_mst():
    """
    処理名：
        マスタ読み込み処理
    引数：
        なし
    戻り値：
        年代（配列）
        部署名（配列）
        役職名（配列）
        評価（配列）
        アンケート内容（配列）
    """
    # iniファイル読み込みインスタンス
    mst_ini = configparser.ConfigParser()
    # マスタファイル読み込み
    mst_ini.read(MST_INI_FILEPATH, encoding='utf-8')
    # 年代読み込み
    mst_ages = json.loads(mst_ini.get('AGE', 'AGES'))
    # 部署名読み込み
    mst_busyo = json.loads(mst_ini.get('BUSYO', 'BUSYO_NAME'))
    # 役職名読み込み
    mst_yakusyoku = json.loads(mst_ini.get('YAKUSYOKU', 'YAKUSYOKU_NAME'))
    # 評価読み込み
    mst_hyouka = json.loads(mst_ini.get('HYOUKA', 'HYOUKA_STATE'))
    # アンケート内容読み込み
    mst_question = json.loads(mst_ini.get('QUESTION', 'QUESTION_DATA'))
    
    return mst_ages, mst_busyo, mst_yakusyoku, mst_hyouka, mst_question


def MakeCsvAnswer():
    """
    処理名：
        解答結果csv出力
    引数：
        なし
    戻り値：
        なし
    """
    # 解答結果を配列に格納
    answer_list = [[
        combobox_age.current(),
        combobox_busyo.current(),
        combobox_yakusyoku.current(),
        radiobtn_value_1.get(),
        radiobtn_value_2.get(),
        radiobtn_value_3.get()
        ]]
    # 解答結果をセット
    result_data = pd.DataFrame(answer_list)
    # csv出力（追記）
    result_data.to_csv(ANS_CSV_FILEPATH, index=False, header=False, mode='a')
    
    msg.showinfo("解答送信", "解答の送信が完了しました")

# メイン処理
if __name__ == '__main__':
    # マスタデータの読み込み
    age_list, busyo_list, yakusyoku_list, hyouka_list, question_list = read_mst()
    
    # tkinterのインスタンス
    base = tk.Tk()
    # タイトル設定
    base.title("アンケート")
    # 画面幅の設定
    base.geometry("700x350")
    
    # ラジオボタンの値を保持
    radiobtn_value_1 = tk.IntVar()
    radiobtn_value_2 = tk.IntVar()
    radiobtn_value_3 = tk.IntVar()
    
    # 年代に関する設定（ラベルとリスト）
    label_age = tk.Label(base, text="年代")
    label_age.place(x=20, y=40) 
    combobox_age = ttk.Combobox(base, width=6, justify='center', state='readonly')
    combobox_age["values"] = (age_list)
    combobox_age.current(0)
    combobox_age.place(x=60, y=40)
    
    # 部署に関する設定（ラベルとリスト）
    label_busyo = tk.Label(base, text="部署")
    label_busyo.place(x=20, y=80) 
    combobox_busyo = ttk.Combobox(base, width=6, justify='center', state='readonly')
    combobox_busyo["values"] = (busyo_list)
    combobox_busyo.current(0)
    combobox_busyo.place(x=60, y=80)

    # 役職に関する設定
    label_yakusyoku = tk.Label(base, text="役職")
    label_yakusyoku.place(x=20, y=120) 
    combobox_yakusyoku = ttk.Combobox(base, width=6, justify='center', state='readonly')
    combobox_yakusyoku["values"] = (yakusyoku_list)
    combobox_yakusyoku.current(0)
    combobox_yakusyoku.place(x=60, y=120)

    # 質問（ラベル）と解答（ラジオボタン）に関する設定

    # y座標の初期値
    y_place = 160
    
    # 質問（配列）分繰り返し
    for i in range(len(question_list)):
        # 質問ラベルをセット
        label_question = tk.Label(base, text=question_list[i])
        label_question.place(x=20, y=y_place)
        
        # x座標の初期値
        x_place = 30
        
        # 解答（配列）分繰り返し
        for j in range(len(hyouka_list)) :
            # 解答結果を保持する変数を設定
            if i == 0:
                radiobtn_value = radiobtn_value_1 
            elif i == 1:
                radiobtn_value = radiobtn_value_2
            elif i == 2:
                radiobtn_value = radiobtn_value_3
           
           # 解答ラジオボタンに関する設定
            radiobtn_hyouka = ttk.Radiobutton(
                base,
                text=hyouka_list[j],
                value=j,
                variable=radiobtn_value)           
            radiobtn_hyouka.place(x=x_place, y=y_place+20)

            # x座標のインクリメント
            x_place += 100

        # y座標のインクリメント
        y_place += 40

    # 送信ボタンの設定
    btn_answer = tk.Button(base, text="送信", command=MakeCsvAnswer)
    btn_answer.place(x=20, y=y_place+30)

    # 画面の表示
    base.mainloop()