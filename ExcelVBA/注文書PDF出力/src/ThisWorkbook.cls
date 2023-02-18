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

' PDF出力パス・ファイル名関係の定数
Private Const STR_PDF As String = "PDF"
Private Const STR_CHUMONSYO As String = "注文書"
Private Const PDF_KAKUCHOSHI As String = ".pdf"

' エクセルの行列に関する定数（注文番号）
Private Const CHUMON_NO_AREA As String = "Z2"

' 「PDF出力」ボタン押下時の処理
Public Sub btn_click_output_pdf()

    Dim sht_chumon As Worksheet     ' 「注文書」シート
    Dim chumon_no As String         ' 注文番後
    Dim output_fullpath As String   ' PDF出力ファイル名（フルパス）
    
On Error GoTo btn_click_output_pdf_err
      
    ' 「注文書」シートをセット
    Set sht_chumon = ThisWorkbook.Worksheets("注文書")
    
    ' 「注文書」シートにフォーカス
    With sht_chumon
        
        ' 注文番号を取得
        chumon_no = .Range(CHUMON_NO_AREA).Value
        
        ' 出力ファイル名をフルパスでセット
        ' (カレントディレクトリ)\PDF\注文書_<注文番号>.pdf
        output_fullpath = ThisWorkbook.Path & "\" & STR_PDF & "\" _
            & STR_CHUMONSYO & "_" & chumon_no & PDF_KAKUCHOSHI
        
        ' PDFで保存
        .ExportAsFixedFormat Type:=xlTypePDF, _
            Filename:=output_fullpath
        
    
    End With
    
    ' 完了メッセージ出力
    MsgBox "PDF出力完了"
    
    ' 終了処理へ
    GoTo btn_click_output_pdf_exit

' 例外処理
btn_click_output_pdf_err:
    ' 例外エラー内容出力
    MsgBox "例外エラー：管理者へお問い合わせください" & vbCrLf _
        & Err.Description
    
    ' 終了処理へ
    GoTo btn_click_output_pdf_exit

' 終了処理
btn_click_output_pdf_exit:
    
    ' シートオブジェクトの解放
    Set sht_chumon = Nothing

End Sub

