import pandas as pd
import gspread
from openpyxl import workbook
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
1) Insertar (Inserta filas o columnas completas)
2) Eliminar
3) Actualizar (Especifico para celdas)
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
4) Regresar
                    
                    """)
            
            const_0 = int(input("Elige una opción: "))

            if const_0 == 0:
                print(sheet.get_all_records())

            elif const_0 == 1:
                print(sheet.row_values(int(input("Que fila quieres ver?: "))))

            elif const_0 == 2:
                print(sheet.col_values(int(input("Que columna deseas ver?: "))))

            elif const_0 == 3:
                print(sheet.cell(int(input("Que celda deseas ver? Fila: ")),int(input("Columna: "))).value)
            elif const_0 == 4:
                break
            else:
                print('Ingresa una opción válida, por favor')
                
    elif const == 1:
        const_1 = 0
        while True:
            
            print(""" 
                  
'--------------------------'
                
Donde quieres insertar?
                  
0) Insertar en fila 
1) Insertar en columna
2) Regresar
                    
                    """)
            
            const_1 = int(input("Elige una opción: "))
            
            if const_1 == 0:
                cadena_a_insertar = input('Que deseas insertar?: ')
                sheet.insert_row([cadena_a_insertar], index=int(input("En que fila?: ")))
                print("La insercion ha sido un exito!") 
                               
            elif const_1 == 1:
                cadena_a_insertar = input('Que deseas insertar?: ')
                sheet.insert_cols([[cadena_a_insertar]], int(input("En que columna?: ")))
                print("La insercion ha sido un exito!")
            elif const_1 == 2:
                break
            else:
                print('Ingresa una opción válida, por favor')
                
### Siguiente paso es iterar sobre los bloques de insercion

    elif const == 2:
        const_2 = 0
        
        while True:
            print("""
Que quieres eliminar?

0) Eliminar fila
1) Eliminar filas
2) Eliminar Columnas
3) Regresar
""")

            const_2 = int(input("Elige una opción: "))
            
            if const_2 == 0:
                sheet.delete_row(int(input("Que fila quieres eliminar?: ")))
                print('Fila eliminada con éxito!')
            elif const_2 == 1:
                sheet.delete_rows(int(input("Que filas quieres eliminar? F1: " )), int(input("F2: ")))
                print("Filas eliminadas con éxito!")
            elif const_2 == 2:
                sheet.delete_columns(int(input("Que columnas quieres eliminar? C1: ")), int(input("C2: ")))
                print("Columnas eliminadas con éxito!")
            elif const_2 == 3:
                break
            else:
                print("Ingrese una opción válida, por favor")            
            
    elif const == 3:
        const_3 = 0
        while True:
            print("""
Que vas a actualizar?

0) Una Celda
1) Varias Celdas
2) Regresar

""")

            const_3 = int(input("Elige una opción: "))
            
            if const_3 == 0:
                sheet.update_cell(int(input("Inserte la fila: ")), int(input("Inserte la columna: ")), input("Introduzca los datos: "))
                print("Datos actualizado exitosamente! ")
                
            elif const_3 == 1:
                first_cell = input("Introduzca la primera casilla (ejemplo A1): ")
                second_cell = input("Introduzca la segunda casilla (ejemplo B2): ")
                
                cell_list = sheet.range(f"{first_cell}:{second_cell}")
                for cell in cell_list:
                    cell.value = input("Introduzca lo que quiere escribir: ")
                sheet.update_cells(cell_list)
                
                print("Datos actualizados exitosamente! ")
            elif const_3 == 2:
                break
            
            else: print("Ingrese una opción válida, por favor")
            
    ### Siguiente paso es iterar sobre los bloques de Actualizacion
    
    elif const == 4:
        break
    
    else: print('Ingrese una opción válida, por favor')
                
            
                
                
            
                


