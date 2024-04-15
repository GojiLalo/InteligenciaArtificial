import pygame
import FuncionesCSV as fscv


pygame.init()
INDX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
P_ALTO = 720
P_ANCHO = 1280
TAM_CAS = 32 #Definir el tamaño de una casilla
PANTALLA = pygame.display.set_mode((P_ANCHO, P_ALTO))
PANTALLA2 = pygame.display.set_mode((P_ANCHO, P_ALTO))
ESTADO = "MENU_INICIO"

def dibujarMenuInicio():
    PANTALLA.fill((0, 0, 0))
    font = pygame.font.Font("Godzilla.ttf", 40)
    B1 = font.render('L-Laberinto', True, (255, 255, 255))
    B2 = font.render('T-Terreno', True, (255, 255, 255))
    B3 = font.render('A-Ajedrez', True, (255, 255, 255))
    PANTALLA.blit(B1, (P_ANCHO/2-B1.get_width()/2, B1.get_height()/2))
    PANTALLA.blit(B2, (P_ANCHO/2-B2.get_width()/2, B2.get_height()/2+B1.get_height()) )
    PANTALLA.blit(B3, (P_ANCHO/2-B2.get_width()/2, B2.get_height()/2+B1.get_height()+B3.get_height()))
    
    pygame.display.update()
    
def elegirColorCasilla(modo, clave):
    if modo == "L":
        if clave == 0: #GRIS PARED
            return (155,155,155)
        if clave == 1: #BLANCO 
            return (255,255,255)
        if clave == 104:
            return (0,0,0)
    if modo == "T":
        if clave == 0: #GRIS MONTAÑA
            return (155,155,155)
        if clave == 1: #CAFE TIERRA
            return (161,130,98)
        if clave == 2: #AZUL AGUA
            return (0,0,255)
        if clave == 3: #AMARILLO ARENA
            return (229,190,1)
        if clave == 4: #VERDE BOSQUE
            return (0,143,57)
        if clave == 104:
            return (0,0,0)
    if modo == "A":
        if clave == 0: #BLANCAS
            return (229,190,1)
        if clave == 1: #NEGRAS 
            return (161,130,98)
def cambiarColorCasilla(matriz, x, y, modo):
    if 0 <= x < len(matriz[0]) and 0 <= y < len(matriz):
        if modo == "T":
            matriz[x][y] = matriz[x][y] + 1
            if matriz[x][y] == 5:
                matriz[x][y] = 0
        if modo == "L":
            if matriz[x][y] == 1:
                matriz[x][y] = 0
            elif matriz[x][y] == 0:
                matriz[x][y] = 1
    return matriz
        
        
def llenarCasilla(x,y, color):
    pygame.draw.rect(PANTALLA, color, (x,y,TAM_CAS-4, TAM_CAS-4))
    
def dibujarCuadricula(matriz, modo):
    font = pygame.font.Font("Godzilla.ttf", 15)
    ancho = len(matriz[0])
    alto = len(matriz)
    contx = 0
    conty = 0
    PANTALLA.fill((87, 35, 100))
    pygame.draw.rect(PANTALLA, (0,0,0), ((TAM_CAS-3),(TAM_CAS-3),ancho*(TAM_CAS-3), alto*(TAM_CAS-3)))
    for i in range((TAM_CAS-3), (ancho+1)*(TAM_CAS-3), (TAM_CAS-3)):
        llenarCasilla(i, 2, (255,0,0))
        PANTALLA.blit(font.render(INDX[contx], True, ((255,255,255))), (i+5, 2))
        contx = contx + 1
    contx = 1;
    for i in range((TAM_CAS-3), (alto+1)*(TAM_CAS-3), (TAM_CAS-3)):
        llenarCasilla(2, i, (255,0,0))
        PANTALLA.blit(font.render(str(contx), True, ((255,255,255))), (7, i+5))
        contx = contx + 1
    contx = 0
    conty = 0
    for i in range((TAM_CAS-3), (ancho+1)*(TAM_CAS-3), (TAM_CAS-3)):
        for j in range((TAM_CAS-3), (alto+1)*(TAM_CAS-3), (TAM_CAS-3)):
            color = elegirColorCasilla(modo, matriz[conty][contx])
            llenarCasilla(i, j, color)
            conty = conty + 1
        conty = 0
        contx = contx + 1
        
def marcarMapa(comando, x_celda, y_celda):
    font = pygame.font.Font("Godzilla.ttf", 15)
    font2 = pygame.font.Font("Godzilla.ttf", 10)
    if comando == "INICIO":
        B1 = font.render('PUNTO INICIAL:' + INDX[x_celda] + str(y_celda+1) + '   A-Aceptar', True, (255, 255, 255))
        BPI = font2.render('I', True, (255, 0, 0))
        PANTALLA.blit(B1, (100, 650))
        PANTALLA.blit(BPI, (((PI[0]+1)*(TAM_CAS-3)) +7, ((PI[1]+1)*(TAM_CAS-3)+1) + 2))
    if comando == "FINAL":
        B2 = font.render('PUNTO FINAL:' + INDX[x_celda] + str(y_celda+1) + '   S-Aceptar', True, (255, 255, 255))
        BPF = font2.render('F', True, (255, 0, 0))
        PANTALLA.blit(B2, (100, 680))
        PANTALLA.blit(BPF, (((x_celda+1)*(TAM_CAS-3)) + 13, ((y_celda+1)*(TAM_CAS-3)+1) + 2))
    if comando == "ACTUAL":
        BX = font2.render('X', True, (255, 0, 0))
        PANTALLA.blit(BX, (((x_celda+1)*(TAM_CAS-3)) + 1, ((y_celda+1)*(TAM_CAS-3)+1) + 13))
    if comando == "VISITADO":
        BV = font2.render('V', True, (255, 0, 0))
        PANTALLA.blit(BV, (((x_celda+1)*(TAM_CAS-3)) + 12, ((y_celda+1)*(TAM_CAS-3)+1) + 13))
    if comando == "DECISION":
        BO = font2.render('O', True, (255, 0, 0))
        PANTALLA.blit(BO, (((x_celda+1)*(TAM_CAS-3)) + 20, ((y_celda+1)*(TAM_CAS-3)+1) + 13))
    pygame.display.update()

def crearMascara(ALTO, ANCHO):
    mascara = [[104] * ANCHO for i in range(ALTO)]
    return mascara

def sensor4dir(matriz, mascara, y, x):
    cont = 0
    if (x<len(matriz))and(y<len(matriz)):
        mascara[x][y] = matriz[x][y]
        if x > 0:
            mascara[x - 1][y] = matriz[x - 1][y]
            cont += 1
        if x < len(matriz) - 1:
            mascara[x + 1][y] = matriz[x + 1][y]
            cont += 1
        if y > 0:
            mascara[x][y - 1] = matriz[x][y - 1]
            cont += 1
        if y < len(matriz[0]) - 1:
            mascara[x][y + 1] = matriz[x][y + 1]
            cont += 1
    return cont

def moverse(x, y, direccion, ALTO, ANCHO):
    if direccion == "ARRIBA": #RESTAR A Y
        if y == 0:
            return[x, y]
        else:
            return[x, y-1]
    if direccion == "ABAJO": #SUMAR A Y
        if y < ALTO-1:
            return[x, y+1]
        else:
            return[x, y]
    if direccion == "IZQUIERDA": #RESTAR A X
        if x == 0:
            return[x, y]
        else:
            return[x-1, y]
    if direccion == "DERECHA": #SUMAR A Y
        if y < ANCHO-1:
            return[x+1, y]
        else:
            return[x, y]

def marcarPuntos(puntos, modo):
    for i in range(0, len(puntos), 1):
        marcarMapa(modo, puntos[i][0], puntos[i][1])
        
def acomodarPiezas(TAM_CAS):
    TAM_PIEZA = TAM_CAS - 20
    PN = pygame.image.load('Piezas\\PN.svg')
    PB = pygame.image.load('Piezas\\PB.svg')
    TN = pygame.image.load('Piezas\\TN.svg')
    TB = pygame.image.load('Piezas\\TB.svg')
    CN = pygame.image.load('Piezas\\CN.svg')
    CB = pygame.image.load('Piezas\\CB.svg')
    AN = pygame.image.load('Piezas\\AN.svg')
    AB = pygame.image.load('Piezas\\AB.svg')
    RN = pygame.image.load('Piezas\\RN.svg')
    RB = pygame.image.load('Piezas\\RB.svg')
    QN = pygame.image.load('Piezas\\QN.svg')
    QB = pygame.image.load('Piezas\\QB.svg')
    
    PN = pygame.transform.smoothscale(PN, (TAM_PIEZA,TAM_PIEZA))
    PB = pygame.transform.smoothscale(PB, (TAM_PIEZA,TAM_PIEZA))
    TN = pygame.transform.smoothscale(TN, (TAM_PIEZA,TAM_PIEZA))
    TB = pygame.transform.smoothscale(TB, (TAM_PIEZA,TAM_PIEZA))
    CN = pygame.transform.smoothscale(CN, (TAM_PIEZA,TAM_PIEZA))
    CB = pygame.transform.smoothscale(CB, (TAM_PIEZA,TAM_PIEZA))
    AN = pygame.transform.smoothscale(AN, (TAM_PIEZA,TAM_PIEZA))
    AB = pygame.transform.smoothscale(AB, (TAM_PIEZA,TAM_PIEZA))
    RN = pygame.transform.smoothscale(RN, (TAM_PIEZA,TAM_PIEZA))
    RB = pygame.transform.smoothscale(RB, (TAM_PIEZA,TAM_PIEZA))
    QN = pygame.transform.smoothscale(QN, (TAM_PIEZA,TAM_PIEZA))
    QB = pygame.transform.smoothscale(QB, (TAM_PIEZA,TAM_PIEZA))
    
    #ACOMODAR PEONES
    for i in range(1,9,1):
        PANTALLA.blit(PN,(((80*i)-(i*2),TAM_CAS*2)))
        PANTALLA.blit(PB,(((80*i)-(i*2),(TAM_CAS*7)-10)))
        
    #ACOMODAR TORRES
    PANTALLA.blit(TN,(TAM_CAS*1,TAM_CAS*1))
    PANTALLA.blit(TN,((TAM_CAS*8)-15,TAM_CAS*1))
    PANTALLA.blit(TB,(TAM_CAS*1,(TAM_CAS*8)-10))
    PANTALLA.blit(TB,((TAM_CAS*8)-15,(TAM_CAS*8)-10))
    
    #ACOMODAR CABALLOS
    PANTALLA.blit(CN,(TAM_CAS*2,TAM_CAS*1))
    PANTALLA.blit(CN,((TAM_CAS*7)-15,TAM_CAS*1))
    PANTALLA.blit(CB,(TAM_CAS*2,(TAM_CAS*8)-10))
    PANTALLA.blit(CB,((TAM_CAS*7)-15,(TAM_CAS*8)-10))
    
    #ACOMODAR ALFILES
    PANTALLA.blit(AN,(TAM_CAS*3,TAM_CAS*1))
    PANTALLA.blit(AN,((TAM_CAS*6)-15,TAM_CAS*1))
    PANTALLA.blit(AB,(TAM_CAS*3,(TAM_CAS*8)-10))
    PANTALLA.blit(AB,((TAM_CAS*6)-15,(TAM_CAS*8)-10))
    
    #ACOMODAR REYES
    PANTALLA.blit(RB,((TAM_CAS*4)-5,TAM_CAS*1))
    PANTALLA.blit(RN,((TAM_CAS*4)-5,(TAM_CAS*8)-10))
    
    #ACOMODAR REINAS
    PANTALLA.blit(QB,((TAM_CAS*5)-5,TAM_CAS*1))
    PANTALLA.blit(QN,((TAM_CAS*5)-5,(TAM_CAS*8)-10))
    
matriz = []
while True:
    font = pygame.font.Font("Godzilla.ttf", 40)
    for event in pygame.event.get():
        tecla = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
           pygame.quit()
           quit()
        if ESTADO == "MENU_INICIO": 
            dibujarMenuInicio()
            if tecla[pygame.K_l]:
                matriz = fscv.leerCSV()
                modo = "L"
                ESTADO = "LABERINTO"
            if tecla[pygame.K_t]:
                matriz = fscv.leerCSV()
                modo = "T"
                ESTADO = "TERRENO"
            if tecla[pygame.K_a]:
                matriz = fscv.convertirCSV("Tablero.csv")
                TAM_CAS = 80
                modo = "A"
                ESTADO = "AJEDREZ"
        if ESTADO == "AJEDREZ":
            dibujarCuadricula(matriz, modo)
            acomodarPiezas(TAM_CAS)
            pygame.display.update()
        if ESTADO == "LABERINTO":
            B1 = font.render('E-Aceptar mapa', True, (255, 255, 255))
            dibujarCuadricula(matriz, modo)
            PANTALLA.blit(B1, (100, 650))
            pygame.display.update()
            if tecla[pygame.K_e]:
                ESTADO = "DET_INI"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_celda = (x - (TAM_CAS - 3)) // (TAM_CAS - 3)
                y_celda = (y - (TAM_CAS - 3)) // (TAM_CAS - 3)
                ESTADO = "CAMBIAR"
        if ESTADO == "TERRENO":
            B1 = font.render('E-Aceptar mapa', True, (255, 255, 255))
            dibujarCuadricula(matriz, modo)
            PANTALLA.blit(B1, (100, 650))
            if tecla[pygame.K_e]:
                ESTADO = "DET_INI"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_celda = (x - (TAM_CAS - 3)) // (TAM_CAS - 3)
                y_celda = (y - (TAM_CAS - 3)) // (TAM_CAS - 3)
                ESTADO = "CAMBIAR"
            pygame.display.update()
        if ESTADO == "CAMBIAR":
            matriz = cambiarColorCasilla(matriz, y_celda, x_celda, modo)
            #print(x_celda,y_celda, matriz[x_celda][y_celda])
            if modo == "L":
                ESTADO = "LABERINTO"
            if modo == "T":
                ESTADO = "TERRENO"
        if ESTADO == "DET_INI":
            dibujarCuadricula(matriz, modo)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_celda = (x - (TAM_CAS - 3)) // (TAM_CAS - 3)
                y_celda = (y - (TAM_CAS - 3)) // (TAM_CAS - 3)
                #print(x_celda,y_celda)
            PI = [x_celda, y_celda]
            marcarMapa("INICIO", PI[0], PI[1])
            if tecla[pygame.K_a]:
                ESTADO = "DET_FIN"
        if ESTADO == "DET_FIN":
            dibujarCuadricula(matriz, modo)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_celda = (x - (TAM_CAS - 3)) // (TAM_CAS - 3)
                y_celda = (y - (TAM_CAS - 3)) // (TAM_CAS - 3)
                #print(x_celda,y_celda)
            PF = [x_celda, y_celda]
            marcarMapa("INICIO", PI[0], PI[1])
            marcarMapa("FINAL", PF[0], PF[1])
            if tecla[pygame.K_s]:
                ESTADO = "DIBUJAR MASCARA"
        if ESTADO == "DIBUJAR MASCARA":
            PA = PI
            decididos = []
            visitados = []
            mascara = crearMascara(len(matriz), len(matriz))
            libres = sensor4dir(matriz, mascara, PA[0], PA[1])

            #MOVERSE HACIA ARRIBA 1 ESPACIO
            visitados.append(PA)
            PA = moverse(PA[0], PA[1], "DERECHA", len(matriz), len(matriz))
            libres = sensor4dir(matriz, mascara, PA[0], PA[1])
            if libres > 1:
                decididos.append(PA)

            #MOVERSE HACIA ARRIBA 1 ESPACIO
            visitados.append(PA)
            PA = moverse(PA[0], PA[1], "DERECHA", len(matriz), len(matriz))
            libres = sensor4dir(matriz, mascara, PA[0], PA[1])
            if libres > 1:
                decididos.append(PA)

            #MOVERSE HACIA ARRIBA 1 ESPACIO
            visitados.append(PA)
            PA = moverse(PA[0], PA[1], "ARRIBA", len(matriz), len(matriz))
            libres = sensor4dir(matriz, mascara, PA[0], PA[1])
            if libres > 1:
                decididos.append(PA)

            #MOVERSE HACIA ARRIBA 1 ESPACIO
            visitados.append(PA)
            PA = moverse(PA[0], PA[1], "ARRIBA", len(matriz), len(matriz))
            libres = sensor4dir(matriz, mascara, PA[0], PA[1])
            if libres > 1:
                decididos.append(PA)

            dibujarCuadricula(mascara, modo)
            
            marcarMapa("INICIO",PI[0], PI[1])
            marcarMapa("ACTUAL", PA[0], PA[1])

            #MARCAR VISITADOS
            marcarPuntos(visitados, "VISITADO")
            marcarPuntos(decididos, "DECISION")
            pygame.display.update()
            if tecla[pygame.K_SPACE]:
                print(libres)