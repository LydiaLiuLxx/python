from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet.cell(row=1,column=1).value='ID'