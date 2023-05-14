VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisWorkbook"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Option Explicit

' シート名の定数
Private Const SHEET_NAME_MAIN As String = "main"

' [main]シートの定数
Private Const MAINSHT_INPUT_FOLDER_ROW As Integer = 4   ' インプットフォルダ行
Private Const MAINSHT_INPUT_FOLDER_COL As Integer = 4   ' インプットフォルダ列

Private Const MAINSHT_ZIPFILE_ROW As Integer = 9        ' zipファイル開始行
Private Const MAINSHT_ZIPFILE_NAME_COL As Integer = 3        ' zipファイル名列
Private Const MAINSHT_ZIPFILE_PW_COL As Integer = 4        ' zipファイルpw列

' フォルダ名の定数
Private Const OUTPUT_DIR_NAME As String = "\output\"
Private Const SEVENZIP_EXE_PATH As String = "C:\Program Files\7-Zip\7z.exe"


'「フォルダ選択」ボタン押下処理
Public Sub btn_click_input_folder()
    
    Dim current_dir     As String       ' カレントディレクトリパス
    Dim sht_main        As Worksheet    ' [main]シート
    Dim input_folder    As String       ' インプットフォルダ
    Dim zip_file        As String       ' zipファイル名
    Dim i_row           As Integer      ' 行カウンタ
    
    On Error GoTo btn_click_input_folder_err
    
    ' カレントディレクトリ取得
    current_dir = ThisWorkbook.Path
    
    ' [main]シートをセット
    Set sht_main = ThisWorkbook.Worksheets(SHEET_NAME_MAIN)
    
    ' 行カウンタ初期値セット
    i_row = MAINSHT_ZIPFILE_ROW
    
    ' 「インプットフォルダ」の値初期化
    sht_main.Cells(MAINSHT_INPUT_FOLDER_ROW, MAINSHT_INPUT_FOLDER_COL).Value = ""
    
    ' [main]シートにフォーカス
    With sht_main
        
        ' ファイル名が空白になるまで繰り返し
        Do While .Cells(i_row, MAINSHT_ZIPFILE_NAME_COL).Value <> ""
            
            ' ファイル名とパスワードを初期化
            .Cells(i_row, MAINSHT_ZIPFILE_NAME_COL).Value = ""
            .Cells(i_row, MAINSHT_ZIPFILE_PW_COL).Value = ""
            
            ' 行カウンタインクリメント
            i_row = i_row + 1
            
        Loop
    
    End With
    
    ' FileDialog
    With Application.FileDialog(msoFileDialogFolderPicker)
        '最初に表示されるフォルダパスを指定:カレントディレクトリ
        .InitialFileName = current_dir
        
        'ダイアログのタイトルを指定
        .Title = "フォルダを選択してください"
        
        'ダイアログを表示、結果を確認
        If .Show = -1 Then
            
            '選択されたフォルダパスを取得
            input_folder = .SelectedItems(1)
        
        End If
        
    End With
    
    
    ' [main]シートにフォーカス
    With sht_main
        
        ' 「インプットフォルダ」をセット
        .Cells(MAINSHT_INPUT_FOLDER_ROW, MAINSHT_INPUT_FOLDER_COL).Value = input_folder
        
        ' インプットフォルダ内のzipファイルを取得
        zip_file = Dir(input_folder & "\" & "*.zip")
        
        ' 行カウンタ初期化
        i_row = MAINSHT_ZIPFILE_ROW
        
        ' zipファイル名が空になるまで繰り返し
        Do While zip_file <> ""
            ' ファイル名を出力
            .Cells(i_row, MAINSHT_ZIPFILE_NAME_COL).Value = zip_file
            
            ' 次のzipファイルを取得
            zip_file = Dir()
            
            ' 行カウンタをインクリメント
            i_row = i_row + 1
        
        Loop
    
    
    End With
     
    GoTo btn_click_input_folder_exit
    
' 例外処理
btn_click_input_folder_err:
    
    ' 例外エラーを出力
    MsgBox Err.Description

' 終了処理
btn_click_input_folder_exit:
    
    ' シートオブジェクトを解放
    Set sht_main = Nothing

End Sub


' 「解凍」ボタン押下処理
Public Sub btn_click_unfreeze()
    
    Dim current_dir             As String       ' カレントディレクトリパス
    Dim sht_main                As Worksheet    ' [main]シート
    Dim i_row                   As Integer      ' 行カウンタ
    Dim input_folder_path       As String       ' inputフォルダパス
    Dim zip_file_name           As String       ' ファイル名
    Dim zip_file_pw             As String       ' パスワード
    Dim output_dir              As String       ' outputフォルダ
    Dim zip_file_name_fullpath  As String       ' ファイル名（フルパス）
    Dim unfreeze_cmd            As String       ' 解凍コマンド
    Dim shell_obj               As Integer      ' Shellコマンド実行結果
    
    On Error GoTo btn_click_unfreeze_err
    
    ' [main]シートをセット
    Set sht_main = ThisWorkbook.Worksheets(SHEET_NAME_MAIN)
    
    ' カレントディレクトリ取得
    current_dir = ThisWorkbook.Path
    
    ' outputフォルダパスをセット
    output_dir = current_dir & OUTPUT_DIR_NAME
    
    ' 行カウンタ初期化
    i_row = MAINSHT_ZIPFILE_ROW
    
    ' [main]シートにフォーカス
    With sht_main
        
        ' 「インプットフォルダ」パスを取得
        input_folder_path = .Cells(MAINSHT_INPUT_FOLDER_ROW, MAINSHT_INPUT_FOLDER_COL).Value
        
        ' zipファイル名が空になるまで繰り返し
        Do While .Cells(i_row, MAINSHT_ZIPFILE_NAME_COL).Value <> ""
            
            ' zipファイル名とパスワードを取得
            zip_file_name = .Cells(i_row, MAINSHT_ZIPFILE_NAME_COL).Value
            zip_file_pw = .Cells(i_row, MAINSHT_ZIPFILE_PW_COL).Value
            
            ' zipファイルをフルパスでセット
            zip_file_name_fullpath = input_folder_path & "\" & zip_file_name
            
            ' 解凍コマンドをセット（7z.exe）
            ' x：解凍
            ' -y：クエリに対して全てyes
            ' -p：パスワードを指定
            ' -o：パスを指定（出力先、解凍対象）
            unfreeze_cmd = SEVENZIP_EXE_PATH _
                    & " x -y -p" _
                    & zip_file_pw _
                    & " -o" _
                    & output_dir _
                    & Space(1) _
                    & zip_file_name_fullpath
                        
            ' コマンド実行(vbHide：非表示で実行)
            shell_obj = Shell(unfreeze_cmd, vbHide)
            
                        
            ' 行カウンタインクリメント
            i_row = i_row + 1
        
        Loop
    
    End With
    
    ' 処理完了メッセージ出力
    MsgBox "完了"
    
    GoTo btn_click_unfreeze_exit

' 例外処理
btn_click_unfreeze_err:
    
    ' 例外エラー出力
    MsgBox Err.Description

' 終了処理
btn_click_unfreeze_exit:
    
    ' シートオブジェクト解放
    Set sht_main = Nothing

End Sub
