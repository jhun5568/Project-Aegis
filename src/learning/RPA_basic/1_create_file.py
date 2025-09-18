from openpyxl import Workbook
wb = Workbook()
ws = wb.active #현재 활성화된 sheet 가져옴
ws.title = "matarial_sheet" #시트 의 이름을 변경
wb.save("sample.xlsx")
wb.close