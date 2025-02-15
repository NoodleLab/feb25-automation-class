import openpyxl 
import os

filename="Student_info.xlsx"

wb=openpyxl.Workbook()
sheet= wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Class'
sheet['D1'] = 'ID'

sheet.append(['Rosco', 15, '6', 10001])  

wb.save(filename)


os.system(f'open {filename}')
