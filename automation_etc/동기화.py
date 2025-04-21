#엑셀파일 찾기(하위까지)
def search(dirName):
    for (path, dir, files) in os.walk(FILE_DIR):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.xlsm':
                if '~$' not in filename:
                    fileLists.append(path + '/' + filename)
#원하는 컬럼만 찾아서 기록하기
def checkColumn(fileName,sheetName,columnNames):
    resultColumnNum =[]
    book = xlrd.open_workbook(fileName)
    sheetDatas = book.sheet_by_name(sheetName)
    rowData = sheetDatas.row_values(0)
    ncol = sheetDatas.ncols
    for col in range (ncol):
        if rowData[col] in columnNames:
            resultColumnNum.append(col)
    return resultColumnNum
#숫자체크
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#정수체크
def isInt(val):
    if float(val).is_integer():
        return True
    else:
        return False
