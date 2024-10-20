#Funciones-----------------------------------------------------------------------------------------♥
#lista para almacenar datos 
datos_control_interno=[]
datos_control_externo=[]
#matrices

#funcion para los datos de control interno 
def control_interno():
    analito_int=int(input("""Ingrese la opción de analito que desea ingresar información:
        1. Amilasa.
        2. Amilasa (en ornia)
        3. Adenosin deaminasa. 
        4. Alanina-aminotransferasa. 
        5. Albúmina. 
        6. Albúmina (en orina).
        7. Fosfatasa alcalina. 
        8. Amonio. 
        9. Antiestreptolisina O. 
        10. Aspartato-aminotransferasa. 
        11. Bilirrubina total. 
        12. Bilirrubina conjugada. 
        13. Complemento C3. 
        14. Complemento C4. 
        15. Calcio. 
        16. Calcio (en orina).
        17. Calcio ionizado. 
        18. Calcio ionizado (B221-2).
        19. Cloruro. 
        20. Cloruro (Cobas B221).
        21. Cloruro (Cobas B221-2).
        22. Cloruro (en orina).
        23. Colesterol. 
        24. Proteína C reactiva. 
        25. Creatina Kinasa. 
        26. Creatina Kinasa MB, actividad. 
        27. Creatinina. 
        28. Creatinina (en orina).
        29. g-Glutamiltransferosa. 
        30. Glucosa. 
        31. Glucosa (en orina).    
        32. Hemoglobina glicada. 
        33. Colesterol HDL. 
        34. Inmunoglobina A. 
        35. Inmunoglobina G. 
        36. Inmunoglobina M. 
        37. Hierro. 
        38. Lactato. 
        39. Lactato-deshidrogenasa. 
        40. Magnesio.  
        Ingrese la opción aqui:  """))
    return analito_int
#funcion para elegir los datos externos.
def control_externo():
    analito_ext=int(input("""Ingrese la opción de analito que desea ingresar información:
        1. Amilasa.
        2. Amilasa (en ornia)
        3. Adenosin deaminasa. 
        4. Alanina-aminotransferasa. 
        5. Albúmina. 
        6. Albúmina (en orina).
        7. Fosfatasa alcalina. 
        8. Amonio. 
        9. Antiestreptolisina O. 
        10. Aspartato-aminotransferasa. 
        11. Bilirrubina total. 
        12. Bilirrubina conjugada. 
        13. Complemento C3. 
        14. Complemento C4. 
        15. Calcio. 
        16. Calcio (en orina).
        17. Calcio ionizado. 
        18. Calcio ionizado (B221-2).
        19. Cloruro. 
        20. Cloruro (Cobas B221).
        21. Cloruro (Cobas B221-2).
        22. Cloruro (en orina).
        23. Colesterol. 
        24. Proteína C reactiva. 
        25. Creatina Kinasa. 
        26. Creatina Kinasa MB, actividad. 
        27. Creatinina. 
        28. Creatinina (en orina).
        29. g-Glutamiltransferosa. 
        30. Glucosa. 
        31. Glucosa (en orina).    
        32. Hemoglobina glicada. 
        33. Colesterol HDL. 
        34. Inmunoglobina A. 
        35. Inmunoglobina G. 
        36. Inmunoglobina M. 
        37. Hierro. 
        38. Lactato. 
        39. Lactato-deshidrogenasa. 
        40. Magnesio.   """))
    return analito_ext
#funcion para ingresar los datos interior y/o externos
def ingresar_datos_analito(analito, tipo_control):
    if tipo_control == "interno":
        # Datos internos
        print(f"Ingrese los datos internos de {analito}.")
        datos_niveles = []
        for nivel in range(1, 4):
            print(f"Ingrese los datos para el nivel {nivel}.")
            nombre = "Lyphochek Assayed Chemistry"
            media_mensual = float(input("Media mensual: "))
            diana = float(input("Diana: "))
            sd = float(input("SD: "))
            cva = float(input("CVa%: "))
            n = float(input("n: "))
            datos_niveles.append([nombre, media_mensual, diana, sd, cva, n])
        datos_control_interno.append([analito, datos_niveles])  # Añade a una lista general (nos ayuda a ahorar en hacer más funciones)
        return datos_control_interno
    elif tipo_control == "externo":
        # Datos externos
        print(f"Ingrese los datos externos de {analito}.")
        datos_corridas = []
        for corrida in range(1, 3):
            print(f"Ingrese los datos para la corrida {corrida}.")
            programa = "Clinical chemistry"
            ciclo = float(input("Ciclo: "))
            muestra = float(input("Muestra: "))
            media_grup = float(input("Media grupo: "))
            dato_lab = float(input("Dato del laboratorio: "))
            sdg = float(input("SD grupo: "))
            cvg = float(input("CV% Grupo: "))
            rm = float(input("RM%DEV: "))
            datos_corridas.append([programa, ciclo, muestra, media_grup, dato_lab, sdg, cvg, rm])
        datos_control_externo.append([analito, datos_corridas])  # Añade a una lista general (nos ayuda a ahorar en hacer más funciones)
        return datos_control_externo
    
#MAIN 
while(True):
    print("Bienvenido al programa de indicadores de desempeño analítico del laboratorio clinico de la sección Química Clínica")
    menu=int(input("""Ingrese la opción de lo que desea realizar: 
        1. Ingreso de datos control de calidad interno. 
        2. Ingreso de datos control de calidad externo. 
        3. Realización de informes de indicadores de desempeño analítico. 
        4. Cambio en las especificaciones.
        5. Salir del programa. \n Ingrese la opción aquí: """))
    if menu==1:                                              #EN PROCESO
        analito_int=control_interno() 
        for i in range (0,40+1):
            ingresar_datos_analito(i,"interno")
    elif menu==2:                                               #EN PROCESO
        analito_ext==control_externo() 
        for i in range (0,40+1):
            ingresar_datos_analito(i,"interno")
    elif menu==3:                                          #NO HEMOS EMPEZADO
        print("aun no llegamos alla")
    elif menu==4:                                          #NO HEMOS EMPEZADO
        print("todavia nada")
    elif menu==5:                                         #NO HEMOS EMPEZADO
        print("Gracias por usar nuestros servicios")
        break
    else:                                                   
        print("Ha seleccionado una opción incorrecta, intente de nuevo.")