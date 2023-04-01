import openpyxl

EXCEL_MST_FILEPATH = './mst/mst_sheet.xlsx'
OUTPUT_DIR = './output/'

MST_SHEET_MAIN = '本紙'

MST_SHEET_START_ROW = 3
MST_SHEET_FILENAME_COL = 2
MST_SHEET_SHEETNAME_COL = 3

def copy_sheet():
    mst_wb = openpyxl.load_workbook(EXCEL_MST_FILEPATH)
    
    mst_ws = mst_wb[MST_SHEET_MAIN]
    
    i_row = MST_SHEET_START_ROW
    
    while mst_ws.cell(i_row, MST_SHEET_FILENAME_COL).value != None:
                
        filename = OUTPUT_DIR + mst_ws.cell(i_row, MST_SHEET_FILENAME_COL).value + '.xlsx'
        sheetname = mst_ws.cell(i_row, MST_SHEET_SHEETNAME_COL).value
        
        output_wb = openpyxl.Workbook()
        
        #tmp_ws = mst_wb.copy_worksheet(mst_wb[sheetname])
        #output_wb.worksheets[0] = tmp_ws
        output_ws = output_wb.active
        output_wb.remove(output_ws)
        
        output_wb._sheets.append(mst_wb[sheetname])
        
        output_wb.save(filename)
        
        i_row += 1
    
    mst_wb.close()


if __name__ == '__main__':
    copy_sheet()