import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file" , "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('falcon.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Prueba').sheet1

# access data
#print(sheet.get_all_records())
#print(sheet.row_values(3))
#print(sheet.col_values(1))
# print(sheet.cell(2,1).value)

# insert data
sheet.insert_row(['Cats', 'Dogs'], 3)
sheet.insert_cols

# delete row
# sheet.delete_row(3)

#update cell
# sheet.update_cell(2,1, 'Jejeje')

# Look for a value
# cell = sheet.find('Jejeje')
# print(cell.value)
# print(cell.row)
# print(cell.col)


# Look for a value with a 'for' loop  - Brings every related value
# cell_list = sheet.find('Jejeje')
# for cell in cell_list:
    # print(cell.value)
    # print(cell.row)
    # print(cell.col)