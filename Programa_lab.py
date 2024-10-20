#Funciones-----------------------------------------------------------------------------------------♥
#lista para almacenar datos 
datos_control_interno=[]
datos_control_externo=[]
#matrices
matriz_variacion_biologica = [
    ["Amilasa", [8.70, 28.30, 0.31]],
    ["Amilasa (en orina)", [94.00, 46.00, 2.04]],
    ["Adenosin deaminasa", [11.70, 25.50, 0.46]],
    ["Alanina-aminotransferasa", [19.40, 41.60, 0.47]],
    ["Albúmina", [3.20, 4.75, 0.67]],
    ["Albúmina (en orina)", [35.00, 35.00, 1.00]],
    ["Fosfatasa alcalina", [6.45, 26.10, 0.25]],
    ["Amonio", [0, 0, 0]],
    ["Antiestreptolisina O", [0, 0, 0]],
    ["Aspartato-aminotransferasa", [12.30, 23.10, 0.53]],
    ["Bilirrubina total", [21.80, 28.40, 0.77]],
    ["Bilirrubina conjugada", [36.80, 43.20, 0.85]],
    ["Complemento C3", [5.20, 15.60, 0.33]],
    ["Complemento C4", [8.90, 33.40, 0.27]],
    ["Calcio", [1.90, 2.80, 0.68]],
    ["Calcio (en orina)", [26.20, 27.00, 0.97]],
    ["Calcio ionizado", [1.70, 1.90, 0.89]],
    ["Calcio ionizado (B221-2)", [1.70, 1.90, 0.89]],
    ["Cloruro", [1.20, 1.50, 0.80]],
    ["Cloruro (Cobas B221)", [1.20, 1.50, 0.80]],
    ["Cloruro (Cobas B221-2)", [1.20, 1.50, 0.80]],
    ["Cloruro (en orina)", [0, 0, 0]],
    ["Colesterol", [5.95, 15.30, 0.39]],
    ["Proteína C reactiva", [42.20, 76.30, 0.55]],
    ["Creatina Kinasa", [22.80, 40.00, 0.57]],
    ["Creatina Kinasa MB, actividad", [19.70, 24.30, 0.81]],
    ["Creatinina", [5.95, 14.70, 0.40]],
    ["Creatinina (en orina)", [11.00, 23.00, 0.48]],
    ["g-Glutamiltransferosa", [13.40, 42.15, 0.32]],
    ["Glucosa", [5.60, 7.50, 0.75]],
    ["Glucosa (en orina)", [0, 0, 0]],
    ["Hemoglobina glicada", [1.85, 5.70, 0.32]],
    ["Colesterol HDL", [7.30, 21.20, 0.34]],
    ["Inmunoglobina A", [5.40, 35.90, 0.15]],
    ["Inmunoglobina G", [4.50, 16.50, 0.27]],
    ["Inmunoglobina M", [5.90, 47.30, 0.12]],
    ["Hierro", [26.50, 23.20, 1.14]],
    ["Lactato", [27.20, 16.70, 1.63]],
    ["Lactato-deshidrogenasa", [8.60, 14.70, 0.59]],
    ["Magnesio", [3.60, 6.40, 0.56]]
]
matriz_cv = [
    ["Amilasa", [4.35, 6.53, 2.18]],
    ["Amilasa (en orina)", [47.00, 70.50, 23.50]],
    ["Adenosin deaminasa", [5.85, 8.78, 2.93]],
    ["Alanina-aminotransferasa", [9.70, 14.55, 4.85]],
    ["Albúmina", [1.60, 2.40, 0.80]],
    ["Albúmina (en orina)", [17.50, 26.25, 9.90]],
    ["Fosfatasa alcalina", [3.23, 4.84, 1.61]],
    ["Amonio", [0, 0, 0]],
    ["Antiestreptolisina O", [0, 0, 0]],
    ["Aspartato-aminotransferasa", [6.15, 9.23, 3.08]],
    ["Bilirrubina total", [10.90, 16.35, 5.45]],
    ["Bilirrubina conjugada", [18.40, 27.60, 9.20]],
    ["Complemento C3", [2.60, 3.90, 1.30]],
    ["Complemento C4", [4.45, 6.68, 2.23]],
    ["Calcio", [0.95, 1.43, 0.48]],
    ["Calcio (en orina)", [13.10, 19.65, 6.55]],
    ["Calcio ionizado", [0.85, 1.28, 0.43]],
    ["Calcio ionizado (B221-2)", [0.85, 1.28, 0.43]],
    ["Cloruro", [0.60, 0.90, 0.30]],
    ["Cloruro (Cobas B221)", [0.60, 0.90, 0.30]],
    ["Cloruro (Cobas B221-2)", [0.60, 0.90, 0.30]],
    ["Cloruro (en orina)", [0, 0, 0]],
    ["Colesterol", [2.98, 4.46, 1.49]],
    ["Proteína C reactiva", [21.10, 31.65, 10.55]],
    ["Creatina Kinasa", [11.40, 17.10, 5.70]],
    ["Creatina Kinasa MB, actividad", [9.85, 14.78, 4.93]],
    ["Creatinina", [2.98, 4.46, 1.49]],
    ["Creatinina (en orina)", [5.50, 8.25, 2.75]],
    ["g-Glutamiltransferosa", [6.70, 10.05, 3.35]],
    ["Glucosa", [2.80, 4.20, 1.40]],
    ["Glucosa (en orina)", [0.93, 1.39, 0.46]],
    ["Hemoglobina glicada", [3.65, 5.48, 1.83]],
    ["Colesterol HDL", [2.70, 4.05, 1.35]],
    ["Inmunoglobina A", [2.25, 3.38, 1.13]],
    ["Inmunoglobina G", [3.00, 4.40, 1.48]],
    ["Inmunoglobina M", [13.25, 19.88, 6.63]],
    ["Hierro", [13.60, 20.40, 6.80]],
    ["Lactato", [4.30, 6.45, 2.15]],
    ["Lactato-deshidrogenasa", [1.80, 2.70, 0.90]]
]
matriz_bias=[
    ["Amilasa", [7.40 11.10, 3.70]],
    ["Amilasa (en orina)", [26.16, 39.24, 13.08]],
    ["Adenosin deaminasa", [7.01, 10.52, 3.51]],
    ["Alanina-aminotransferasa", [11.48, 17.21, 5.74]],
    ["Albúmina", [1.43, 2.15, 0.72]],
    ["Albúmina (en orina)", [12.37, 18.56, 7.00]],
    ["Fosfatasa alcalina", [6.72, 10.08, 3.36]],
    ["Amonio", [0, 0, 0]],  # Valores cero
    ["Antiestreptolisina O", [0, 0, 0]],  # Valores cero
    ["Aspartato-aminotransferasa", [6.54, 9.81, 3.27]],
    ["Bilirrubina total", [8.95, 13.43, 4.48]],
    ["Bilirrubina conjugada", [14.19, 21.28, 7.09]],
    ["Complemento C3", [4.11, 6.17, 2.06]],
    ["Complemento C4", [8.64, 12.96, 4.32]],
    ["Calcio", [0.85, 1.27, 0.42]],
    ["Calcio (en orina)", [9.41, 14.11, 4.70]],
    ["Calcio ionizado", [0.64, 0.96, 0.32]],
    ["Calcio ionizado (B221-2)", [0.64, 0.96, 0.32]],
    ["Cloruro", [0.48, 0.72, 0.24]],
    ["Cloruro (Cobas B221)", [0.48, 0.72, 0.24]],
    ["Cloruro (Cobas B221-2)", [0.48, 0.72, 0.24]],
    ["Cloruro (en orina)", [0, 0, 0]],  # Valores cero
    ["Colesterol", [4.10, 6.20, 2.05]],
    ["Proteína C reactiva", [21.80, 32.70, 10.90]],
    ["Creatina Kinasa", [11.51, 17.27, 5.76]],
    ["Creatina Kinasa MB, actividad", [7.82, 11.73, 3.91]],
    ["Creatinina", [3.96, 5.95, 1.98]],
    ["Creatinina (en orina)", [6.37, 9.56, 3.19]],
    ["g-Glutamiltransferosa", [11.06, 16.59, 5.53]],
    ["Glucosa", [2.34, 3.51, 1.17]],
    ["Glucosa (en orina)", [0, 0, 0]],  # Valores cero
    ["Hemoglobina glicada", [1.50, 2.25, 0.75]],
    ["Colesterol HDL", [5.61, 8.41, 2.80]],
    ["Inmunoglobina A", [9.08, 13.61, 4.54]],
    ["Inmunoglobina G", [4.28, 6.41, 2.14]],
    ["Inmunoglobina M", [11.92, 17.87, 5.96]],
    ["Hierro", [8.81, 13.21, 4.40]],
    ["Lactato", [7.98, 11.97, 3.99]],
    ["Lactato-deshidrogenasa", [4.26, 6.39, 2.13]],
    ["Magnesio", [1.84, 2.75, 0.92]]
]
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