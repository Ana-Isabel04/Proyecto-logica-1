#Funciones-----------------------------------------------------------------------------------------♥

#F2-SubMenu_Ensayos
def menu_ensayos():
    n=int(input("""En que sección del laboratorio desea realizar los ensayos
            ➜ 1. Orinas. 
            ➜ 2. Coagulación. 
            ➜ 3. Química Sanguinea.
            ➜ 4. Inmunologia. 
            ➜ 5. Microbiología. 
            ➜ 6. Hematologia.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
    match n: 
        case 1: 
            orinas()
        case 2: 
            coagulacion()
        case 3:
            quimica_sanguinea()
        case 4:
            inmunologia()
        case 5: 
            microbiologia()
        case 6:
            hematologia()

#OPCIONES DEL SUBMENU DE ENSAYOS
def orinas():
    examen=int(input("""Desea realizar
            ➜ 1. Citoquimico de orina. 
            ➜ 2. Proteinas de Bence Jones.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
def coagulacion():
    examen=int(input("""Desea realizar
            ➜ 1. TPT.
            ➜ 2. Dímero D.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
def quimica_sanguinea():
    examen=int(input("""Desea realizar
            ➜ 1. Glucosa. 
            ➜ 2. Colesterol total.
            ➜ 3. Colesterol HDL.
            ➜ 4. Triglicéridos. 
            ➜ 5. Hierro. 
            ➜ 6. Fosfatasa alcalina.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
def inmunologia():
    examen=int(input("""Desea realizar
            ➜ 1. TSH.
            ➜ 2. T4L.
            ➜ 3. Ferritina.
            ➜ 4. Vitamina B12.
            ➜ 5. T3.
            ➜ 6. Hemoclasificación.
            ➜ 7. VDRL.
            ➜ 8. FTA.
            ➜ 9. PIE.
            ➜ 10. Cocaina. 
            ➜ 11. Marihuana.
            ➜ 12. Benzodiazepinas.
            ➜ 13. Morfina. 
            ➜ 14. Dengue.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
def microbiologia():
    examen=int(input("""Desea realizar
            ➜ 1. H1N1.
            ➜ 2. Virus Sincitial.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
def hematologia():
    examen=int(input("""Desea realizar
            ➜ 1. Cuadro Hemático.
            ➜ 2. Leishmania.
            ➜ 3. Clostridium.
            ➜ 4. Test de Hansen.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
    
#SUBMENU DE INFORMES
def menu_informes():
    print("aun no esta hecho pero no quiero que quede por error")

#ALARMAS CONTROLADOR 
def alarma_controles():
    valor_control=int(input("Ingrese el valor que indica la maquina sobre los controles: "))


#ALARMA CALIBRADOR

#MAIN
print("Bienvenido al programa de control de requisitos del laboratorio clinico")
while(True): #Hace que se repita el menú hasta que demos la opción de salir del programa.
    n=int(input("""Ingrese la opción que desea realizar el día de hoy: 
        ➜ 1. Realizar ensayos de control de requisitos.
        ➜ 2. Realizar informes. 
        ➜ 3. Ninguna de las anteriores.\nIngrese la opción aquí: """))
    print("………………………………………………………………………………………………………………………………………………………………………………………………………………♥")
    if (n==1):
        menu_ensayos() #llama al subprograma que tiene las opciones de ensayos.
    elif (n==2):
         menu_informes()
    elif(n==3):
        print("Muchas gracias por usar nuestros servicios, vuelva prontro")
        break 
    else:
        print("Ha seleccionado una opción que no existe en el menú. Intente de nuevo.")
