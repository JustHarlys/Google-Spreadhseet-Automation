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
                print(sheet.cell(int(input("Que celda deseas ver? F,C"))))
                
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
9) Regresar
                    
                    """)
            
            
            const_1 == int(input("Elige una opción: "))
            
            
            if const_1 == 0:
                cadena_a_insertar = input('Que deseas insertar?')
                sheet.insert_row([cadena_a_insertar], index=int(input("En que fila?: ")))
                print("La insercion ha sido un exito!") 
                               
            elif const_1 == 1:
                cadena_a_insertar = input('Que deseas insertar?')
                sheet.insert_cols([cadena_a_insertar], index=int(input("En que columna?: ")))
                print("La insercion ha sido un exito!")
                
            elif const_1 == 2:
                break
            else:
                print('Ingresa una opción válida, por favor')
            # La opcion de regresar no funciona, corregirla

            
    
    
    
    
    
    
    
    
    elif const == 4:
        break
    
    else: print('Ingrese una opción válida, por favor')
                
            
                
                
            
                


