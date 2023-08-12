import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

TITLE_NAME = 'ファイル ドラック＆ドロップ'

# メイン画面クラス
class MainFrame(TkinterDnD.Tk):
    # コンストラクタ
    def __init__(self):
        
        #親クラス：TkinterDnD.Tkのコンストラクタ呼び出し
        super().__init__()
        
        # 画面サイズ
        frame_width = 600
        frame_height = 600
        self.geometry(f'{frame_width}x{frame_height}')
        
        # 画面サイズ固定したい場合
        # self.minsize(frame_width, frame_height)
        # self.maxsize(frame_width, frame_height)
        
        # タイトル
        self.title(f'{TITLE_NAME}')
        
        # フレーム（クラスのインスタンス）
        self.frame_drag_drop = frameDragDrop(self)
        
        # 配置（上下左右全表示）
        self.frame_drag_drop.grid(
            column=0
            , row=0
            , padx=5
            , pady=5
            , sticky=(tk.E, tk.W, tk.S, tk.N) 
        )
        
        # 画面サイズに合わせてフレームの大きさも伸縮
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

# ラベルクラス
class frameDragDrop(tk.LabelFrame):
    # コンストラクタ
    def __init__(self, parent):
        # 継承元も初期化
        super().__init__(parent)
        
        # テキストボックスを無効化でセット（折り返しなし）
        self.textbox = tk.Text(self, wrap=tk.NONE)
        self.textbox.insert(0.0, "Drag & Drop Here!!")
        self.textbox.configure(state='disabled')
                
        # ドラッグ&ドロップ
        self.textbox.drop_target_register(DND_FILES)
        self.textbox.dnd_bind('<<Drop>>', self.funcDragAndDrop)
        
        # スクロールバー設定（縦）
        self.yscrollbar = tk.Scrollbar(
            self
            , orient=tk.VERTICAL
            , command=self.textbox.yview
        )
        self.textbox['yscrollcommand'] = self.yscrollbar.set
        
        # スクロールバー設定（横）
        self.xscrollbar = tk.Scrollbar(
            self
            , orient=tk.HORIZONTAL
            , command=self.textbox.xview
        )
        self.textbox['xscrollcommand'] = self.xscrollbar.set


        # 配置
        self.textbox.grid(
            column=0
            , row=0
            , sticky=(tk.E, tk.W, tk.S, tk.N)
        )
        self.yscrollbar.grid(column=1, row=0, sticky=(tk.S, tk.N))
        self.xscrollbar.grid(column=0, row=1, sticky=(tk.E, tk.W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    
    # ドラッグ&ドロップした時の処理
    def funcDragAndDrop(self, event):
        try:
            # テキストボックスのエリアを有効化し初期化
            self.textbox.configure(state='normal')
            self.textbox.delete(0.0, tk.END)
            
            # ファイルオープン
            with open(event.data) as f:
                # 1行ずつ読み込み
                for line in f:
                    # 1行の文字を取得
                    line = line.strip()
                    # テキストボックスに出力（改行コード：\n）
                    self.textbox.insert(tk.END, f"{line}\n")

        # 例外処理
        except Exception as e:
            self.textbox.insert(tk.END,f"エラー：{e}")
        

# メイン処理
if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()
    