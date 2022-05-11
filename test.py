import openpyxl

wb=openpyxl.load_workbook("C:\\Users\\sebda\\OneDrive\\Escritorio\\oop_proyect\\cats_db.xlsx")
sheets=wb.sheetnames
print(wb.active.title)

sh1=wb["Nombres"]

data= sh1['B2'].value
print(data)