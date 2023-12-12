import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file" , "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('falcon.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Prueba').sheet1


const = 0

while True:
    print("""
Que vas a hacer?

0) Ver
1) Insertar
2) Eliminar
3) Actualizar
4) Salir
""")

    const = int(input("Elige una opción: "))

    if const == 0:
        const_0 = 0
        while True:
            print(""" 
                  
'--------------------------'
                
Que quieres ver?
                  
0) Todas las entradas?
1) Valores de una fila? (Especificar cual)
2) Valores de una columna? (Especificar cual)
3) Valores de celda? (Especificar cuales i.e (2,1) F=2, C=1)
4) Salir                    
                    """)
            
            const_0 = int(input("Elige una opción: "))

            if const_0 == 0:
                print(sheet.get_all_records())
                break
            elif const_0 == 1:
                print(sheet.row_values(int(input("Que fila quieres ver?: "))))
                break
            elif const_0 == 2:
                print(sheet.col_values(int(input("Que columna deseas ver?: "))))
                break
            elif const_0 == 3:
                print(sheet.cell(int(input("Que celda deseas ver? F,C"))))
                break
            elif const_0 == 4:
                break
            else:
                print('Ingresa una opción válida, por favor')
            
                


