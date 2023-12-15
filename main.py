"""
Script para interactuar con hojas de cálculo de Google usando la API de gspread.
Asegúrate de tener el archivo JSON de credenciales (archivo.json) en la ruta de este archivo!.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file" , "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('falcon.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Prueba').sheet1

## Declaramos el manejo de errores en una sola funcion, para asi ahorrarnos codigo y rendimiento

def num(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un valor númerico válido.")
            
## Inicializamos la variable const en 0, ya que esta va a ser redefinida como un entero          
const = 0

## Definimos un bucle while que va a iterar hasta que lo rompamos, cada opcion va a ser definida con un numero
while True:
    print("""
Que vas a hacer?

0) Ver
1) Insertar (Inserta filas o columnas completas)
2) Eliminar
3) Actualizar (Especifico para celdas)
4) Cerrar
""")

## Redefinimos const por un numero entero (utilizando la funcion de arriba)
    const = num("Elige una opción: ")
    
## Empezamos a trabajar con el menu de navegacion donde si el usuario introduce 0 (const == 0), vamos a al apartado de ver
    if const == 0:
        ## Dentro de cada bucle repetimos lo mismo que hicimos fuera, pero solo para un bloque de codigo, que seria para el if en este bloque
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
            
            const_0 = num("Elige una opción: ")

            if const_0 == 0:
                ## sheet.get_all_records() trae todo lo escrito en la hoja
                print(sheet.get_all_records())

            elif const_0 == 1:
                ## sheet.row_values() trae todos los datos de una fila que le pasemos
                print(sheet.row_values(num("Que fila quieres ver?: ")))

            elif const_0 == 2:
                ## sheet.col_values() trae todos los datos de una columna que le pasemos
                print(sheet.col_values(num("Que columna deseas ver?: ")))

            elif const_0 == 3:
                ## sheet.cell() trae los datos de una celda especifica que le pasemos
                print(sheet.cell(num("Que celda deseas ver? Fila: "),num("Columna: ")).value)

            elif const_0 == 4:
                ## Rompemos el bucle y regresamos al menu general
                break
            else:
                print('Ingresa una opción válida, por favor')
                
    elif const == 1:
        ## En este bucle se repite lo mismo del anterior, definimos un const_1 que le puse const_1 porque seria el const del caso 1
        const_1 = 0
        while True:
            
            print(""" 
                  
'--------------------------'
                
Donde quieres insertar?
                  
0) Insertar en fila 
1) Insertar en columna
2) Regresar
                    
                    """)
            
            const_1 = num("Elige una opción: ")
            
            if const_1 == 0:
                ## Definimos una funcion insert() para poder reutilizar este codigo mas tarde sin tener que copiarlo
                def insert():
                    cadena_a_insertar = input('Que deseas insertar?: ')
                    ## sheet.insert_row() nos permite ingresar un dato en una fila especifica
                    sheet.insert_row([cadena_a_insertar], index=num("En que fila?: "))
                    print("La insercion ha sido un exito!") 
                insert()
                
                ## Debajo de este comentario se utiliza la misma estructura que los anteriores bloques, solo que este va a iterar
                ## infinitamente hasta que el usuario le ponga un break, permitiendo al usuario insertar cuantos datos quiera sin necesidad de correr el script
                ## de nuevo.
                
                ## Por ende choicce = 0, asi como al principio const era igual a 0
                choice = 0
                while True:
                    
                    print(""" 
0) Seguir insertando
1) Regresar
                          """)
                    ## Se le preguntara si desea insertar o regresar despues de introducir el primer dato para asi seguir introduciendo o salir
                    choice = num("Insertar(0) o Regresar(1): ")
                    if choice == 0:
                        ## Aqui ejecutamos el codigo que hay arriba dentro de la funcion, para no tener que repetirlo de nuevo
                        insert()
                    elif choice == 1:
                        ## Rompemos el bucle y volvemos al menu de insercion
                        break
                    else:
                        print("Ingrese una opción válida")
                    
                               
            elif const_1 == 1:
                ## Se repiten los mismos pasos que en el bloque anterior, definimos esta funcion para reutilizar codigo
                def insert_col():
                    cadena_a_insertar = input('Que deseas insertar?: ')
                    ## sheeet.insert_cols() inserta datos en una columna que le pasemos
                    sheet.insert_cols([[cadena_a_insertar]], num("En que columna?: "))
                    print("La insercion ha sido un exito!")
                insert_col()
                
                choice = 0
                ## Se repite todo el procesos en un bucle infinito hasta que el usuario seleccione romper entre las opciones, como el anterior bloque
                while True:
                    print(""" 
0) Seguir insertando 
1) Regresar
                          
                          """)
                    
                    choice = num("Insertar(0) o Salir(1): ")
                    if choice == 0:
                        insert_col()
                    elif choice == 1:
                        break
                    else:
                        print("Ingrese una opción válida")
                        
            elif const_1 == 2:
                ## Rompemos el bucle principal y retornamos al menu general
                break
            else:
                print('Ingresa una opción válida, por favor')
                

    elif const == 2:
        ## Este bloque se inicia igual que los anteriores, con una variable const para este bloque "const_2"
        const_2 = 0
        
        ## Se repite el mismo sistema de loop que los anteriores bucles
        while True:
            print("""
Que quieres eliminar?

0) Eliminar fila
1) Eliminar filas
2) Eliminar Columnas
3) Regresar
""")

            const_2 = num("Elige una opción: ")
            
            if const_2 == 0:
                ## Declaramos delete_one_row() para reutilizar el codigo despues.
                def delete_one_row():
                    ## sheet.delete_row() elimina la fila que le pasemos
                    sheet.delete_row(num("Que fila quieres eliminar?: "))
                    print('Fila eliminada con éxito!')
                delete_one_row()
                
                choice = 0
                ## Empezamos otro bucle para que el usuario elimine a su gusto sin tener que ejecutar todo desde el principio
                while True:
                    
                    print(""" 
                          
0) Seguir eliminando
1) Regresar
                          """)
                    ## Despues de cada acciona preguntara al usuario si quiere seguir borrando o regresar
                    choice = num("Eliminar(0) o Regresar(1)")
                    if choice == 0:
                        ## Reutilizamos el codigo de la funcion
                        delete_one_row()
                    elif choice == 1:
                        ## Regresamos al menu anterior
                        break
                    else: print("Introduzca una opción válida, por favor")
                    
            elif const_2 == 1:
                ## Declaramos otra funcion para reutilizar su codigo
                def delete_mult_rows():
                    ## sheet.delete_rows() adquiere 2 parametros y sirve para eliminar un rango entre filas, por ejemplo desde la fila 1 a la fila 4
                    sheet.delete_rows(num("Que filas quieres eliminar? F1: " ), num("F2: "))
                    print("Filas eliminadas con éxito!")
                delete_mult_rows()
                
                choice = 0
                ## Otro bucle para mantener al usuario eliminando a su gusto
                while True:
                    print(""" 
                          
0) Seguir eliminando
1) Regresar
                          
                          """)
                    ## Despues de cada acciona preguntara al usuario si quiere seguir borrando o regresar
                    choice = num("Eliminar(0) o Regresar(1)")
                    
                    if choice == 0:
                        ## Reutilizacion del codigo de la funcion
                        delete_mult_rows()
                    elif choice == 1:
                        ## Regresamos al menu anterior
                        break
                    else: print("Ingrese una opción válida, por favor")
            elif const_2 == 2:
                ## Definimos la funcion para reutilizar su codigo
                def delete_cols():
                    ## sheet.delete_columns() adquiere 2 parametros y elimina las columnas que les pasemos, como la opcion anterior(Eliminar Filas)
                    sheet.delete_columns(num("Que columnas quieres eliminar? C1: "), num("C2: "))
                    print("Columnas eliminadas con éxito!")
                delete_cols()
                
                choice = 0
                ## Creamos el bucle de nuevo
                while True:
                    print(""" 
0) Seguir eliminando
1) Regresar    
                          """)
                    ## Pregunta al ususario si seguir eliminando o regresar al menu anterior
                    choice = num("Eliminar(0) o Regresar(1)")
                    
                    if choice == 0:
                        ## Reutilizacion del codigo de la funcion
                        delete_cols()
                    elif choice == 1:
                        ## Regresamos al menu anterior
                        break
                    else: print("Ingrese una opción válida, por favor")
            elif const_2 == 3:
                ## Rompemos el bucle y regresamos al menu principal
                break
            else:
                print("Ingrese una opción válida, por favor")            
            
    elif const == 3:
        
        ## Volvemos a definir una variable local para este bucle y este const es "const_3"
        const_3 = 0
        ## Inicializamos el bucle
        while True:
            print("""
Que vas a actualizar?

0) Una Celda
1) Varias Celdas
2) Regresar

""")

            const_3 = num("Elige una opción: ")
            
            if const_3 == 0:
                ## Definimos la funcion para la utilizacion de este codigo posteriormente
                def update_one_cell():
                    ## sheet.update_cell() nos permite escribir en una tabla especifica y sobreescribir si ya tiene datos, adquiere 3 parametros(fila, columna y valor)
                    sheet.update_cell(num("Inserte la fila: "), num("Inserte la columna: "), input("Introduzca los datos: "))
                    print("Datos actualizado exitosamente! ")
                update_one_cell()
                
                choice = 0
                ## Volvemos a inicializar otro bucle
                while True:
                    print(""" 
0) Seguir actualizando(insertando)
1) Regresar
                          """)
                    
                    ## Pregunta al usuario si seguir actualizando o regresa al menu anterior
                    choice = num("Actualizar(0) o Regresar(1)")
                    
                    if choice == 0:
                        ## Reutilizamos el codigo de la funcion
                        update_one_cell()
                    elif choice == 1:
                        ## Regresamos al menu anterior
                        break
                    else: print("Ingrese una opción válida, por favor")
                        
            elif const_3 == 1:
                ## Definimos esta funcion para reutilizar el codigo posteriormente
                def cell_loop():
                    
                    ## Primero adquirimos 2 valores almacenados en variables diferentes
                    ## Le especificamos al usuario como son las entradas que debe hacer
                    first_cell = input("Introduzca la primera casilla (ejemplo A1): ")
                    second_cell = input("Introduzca la segunda casilla (ejemplo B2): ")
                
                    ## En la variable cell_list almanecamos la accion de seleccionar multiples casillas
                    ## Como si con el mouse arrastraramos de casilla a casilla
                    ## sheet.range() admite 2 parametros, que son los que definimos anteriormente
                    cell_list = sheet.range(f"{first_cell}:{second_cell}")
                    
                    ## Creamos un bucle que para cada casilla seleccionada debemos introducir un dato, este se almacenara en cell.values()
                    ## Y sheet.update_cells() le pasamos todas las casillas que hay dentro de la seleccion
                    ## Este se encargara de llenarlas con lo que escribimos para cada una
                    for cell in cell_list:
                        ## Introducimos los datos
                        cell.value = input("Introduzca lo que quiere escribir: ")
                    ## Se actualizan en cada casilla
                    sheet.update_cells(cell_list)
                    print("Datos actualizados exitosamente! ")
                cell_loop()
                
                choice = 0
                ## Inicializamos el bucle de nuevo
                while True:
                    
                    print(""" 
0) Seguir actualizando
1) Regresar                          
                          """)
                    ## Preguntamos al usuario si quiere seguir actualizando o regresa al menu anterior
                    choice = num("Actualizar(0) o Regresar(1)")
                    
                    if choice == 0:
                        ## Reutilizamos el codigo de la funcion
                        cell_loop()
                    elif choice == 1:
                        ## Regresamos al menu anterior
                        break
                    else: print("Ingrese una opción válida, por favor")
                
            elif const_3 == 2:
                ## Regresamos al menu principal
                break
            
            else: print("Ingrese una opción válida, por favor")
    
    elif const == 4:
        ## Cerramos el programa definitivamente
        print("Programa cerrado")
        break
    
    else: print('Ingrese una opción válida, por favor') ## Si no es un numero, o el numero es mayor que las opciones, se imprimira este mensaje
                
            