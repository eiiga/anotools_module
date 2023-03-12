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

' 定数
Private Const START_TASK_ROW As Integer = 3         ' タスク開始行
Private Const TASK_COL As Integer = 2               ' タスク名列
Private Const TASK_STATUS_COL As Integer = 3        ' 進捗度列
Private Const START_COLOR_COL As Integer = 4        ' 進捗ステータス列

Private Const STANDARD_COLOR_ROW As Integer = 3     ' 基準色行
Private Const STANDARD_COLOR_COL As Integer = 16    ' 基準色列

Private Const COLOR_DEFULT_WHITE As Long = 16777215 ' 色コード：塗りつぶしなし

' 「色塗り」ボタン押下時の処理
Public Sub btn_click_color()

    Dim sht_main As Worksheet   ' シート
    Dim i_row As Integer        ' タスク行カウンタ
    Dim color_code As Long      ' 基準色コード
    Dim status_value As Integer ' ステータス値
    Dim i_status As Integer     ' ステータスカウンタ
    Dim i_color_col As Integer  ' ステータス列カウンタ
    Dim task_name As String     ' タスク名
    
    ' 例外エラーハンドリング
    On Error GoTo btn_click_color_err
    
    ' 「main」シートをセット
    Set sht_main = ThisWorkbook.Sheets("main")
    
    ' タスク行カウンタ初期値セット
    i_row = START_TASK_ROW
    
    ' 「main」シートにフォーカス
    With sht_main
        
        ' 基準色コード取得
        color_code = .Cells(STANDARD_COLOR_ROW, STANDARD_COLOR_COL).Interior.Color
        
        ' タスクの数だけ繰り返し
        Do Until .Cells(i_row, TASK_COL).Value = ""
            
            ' ステータス列カウンタ初期化
            i_color_col = START_COLOR_COL
            
            ' タスク名を取得
            task_name = .Cells(i_row, TASK_COL).Value
            
            ' ステータス値を取得
            status_value = .Cells(i_row, TASK_STATUS_COL) \ 10
            
            ' ステータス値 < 0 もしくは ステータス値 > 10 の場合
            If status_value < 0 Or status_value > 10 Then
                
                ' 入力エラーを出力
                MsgBox "入力エラー：" & task_name & vbCrLf & _
                    "進捗度（％）の値は0～100までを入力してください"
                
                ' 終了処理へ移動
                GoTo btn_click_color_exit
                
            End If
            
            ' 10回繰り返し
            For i_status = 1 To 10
                
                ' ステータス値内の場合
                If i_status <= status_value Then
                    ' 基準色で色塗り
                    .Cells(i_row, i_color_col).Interior.Color = color_code
                
                Else
                    ' 塗りつぶしなしで色塗り
                    .Cells(i_row, i_color_col).Interior.Color = COLOR_DEFULT_WHITE
                
                End If
                
                ' ステータス列カウンタインクリメント
                i_color_col = i_color_col + 1
            
            Next i_status
            
            タスク行カウンタインクリメント
            i_row = i_row + 1
        Loop
    
    End With
    
    ' 終了処理へ移動
    GoTo btn_click_color_exit

' 例外処理
btn_click_color_err:
    
    ' 例外エラー出力
    MsgBox "例外エラー" & vbCrLf & _
        Err.Description
        
    ' 終了処理へ移動
    GoTo btn_click_color_exit
    
' 終了処理
btn_click_color_exit:
    
    ' 「main」シートオブジェクト解放
    Set sht_main = Nothing

End Sub
