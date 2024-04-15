import pygame
import sys
import FuncionesCSV
import Agentes
import os


INDX = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Menu(PANTALLA, ANCHO, MATRIZ):
    while True:
        for EVENTO in pygame.event.get():
            if EVENTO.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            font = pygame.font.Font("Godzilla.ttf", 40)
            PANTALLA.fill((0, 0, 0))
            B1 = font.render('L-Laberinto', True, (255, 255, 255))
            B2 = font.render('T-Terreno', True, (255, 255, 255))
            B3 = font.render('A-Ajedrez', True, (255, 255, 255))
            PANTALLA.blit(B1, (ANCHO/2-B1.get_width()/2, B1.get_height()/2))
            PANTALLA.blit(B2, (ANCHO/2-B2.get_width()/2, 4*B2.get_height()/2+B1.get_height())) 
            PANTALLA.blit(B3, (ANCHO/2-B2.get_width()/2, 8*B2.get_height()/2+B1.get_height()+B3.get_height()))
            TECLA = pygame.key.get_pressed()
            if TECLA[pygame.K_l]:
                MATRIZ = FuncionesCSV.leerCSV()
                return ("L", MATRIZ)
            if TECLA[pygame.K_t]:
                MATRIZ = FuncionesCSV.leerCSV()
                return ("T", MATRIZ)
        pygame.display.update()

def elegirColorCasilla(modo, clave):
    if modo == "L":
        if clave == 0: #GRIS PARED
            return (155,155,155)
        if clave == 1: #BLANCO 
            return (255,255,255)
        if clave == 9:
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
        if clave == 9:
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

def dibujarCasilla(LADO, COLOR): #ALTO_P -> RESOLUCION[1]
    RELLENO = LADO - 2
    CASILLA = pygame.Surface((LADO,LADO))
    pygame.draw.rect(CASILLA, COLOR, (LADO/2-RELLENO/2,LADO/2-RELLENO/2,RELLENO,RELLENO))
    return CASILLA

def dibujarCuadricula(MATRIZ, RESOLUCION, MODO):
    font = pygame.font.Font("Godzilla.ttf", 20)
    PANTALLA.fill((0, 0, 0))
    #DIBUJAR COORDENADAS
    LADO = int(RESOLUCION[1]/(len(MATRIZ)+1))
    PANTALLA.fill((87, 35, 100))
    for i in range(1, len(MATRIZ)+1, 1):
        B1 = font.render(str(i), True, ((255,255,255)))
        CASILLA = dibujarCasilla(LADO, (255,0,0))
        CASILLA.blit(B1, (LADO/2-B1.get_width()/2, LADO/2-B1.get_height()/2))
        PANTALLA.blit(CASILLA,(0,i*LADO))
    for i in range(1, len(MATRIZ[0])+1, 1):
        B1 = font.render(str(INDX[i-1]), True, ((255,255,255)))
        CASILLA = dibujarCasilla(LADO, (255,0,0))
        CASILLA.blit(B1, (LADO/2-B1.get_width()/2, LADO/2-B1.get_height()/2))
        PANTALLA.blit(CASILLA,(i*LADO, 0))
    for i in range(1, len(MATRIZ[0])+1, 1):
        for j in range(1, len(MATRIZ)+1, 1):
            COLOR = elegirColorCasilla(MODO ,MATRIZ[j-1][i-1])
            CASILLA = dibujarCasilla(LADO, COLOR)
            PANTALLA.blit(CASILLA,(i*LADO, j*LADO))

def marcarMapa(comando, x_celda, y_celda, TAM_CAS):
    font2 = pygame.font.Font("Godzilla.ttf", 15)
    BPI = font2.render('I ', True, (255, 0, 0))
    BPF = font2.render(' F', True, (255, 0, 0))
    BX = font2.render('X', True, (255, 0, 0))
    BV = font2.render('  V', True, (255, 0, 0))
    BO = font2.render('O', True, (255, 0, 0))
    OFFY = TAM_CAS*y_celda
    if comando == "INICIO":
        PANTALLA.blit(BPI, ((TAM_CAS*x_celda)+BPI.get_width()/3,OFFY + BPI.get_height()/4))
    if comando == "FINAL":
        PANTALLA.blit(BPF, ((TAM_CAS*x_celda)+BPI.get_width()/3 + BPF.get_width(),OFFY + BPI.get_height()/4))
    if comando == "ACTUAL":
        PANTALLA.blit(BX, ((TAM_CAS*x_celda)+BPI.get_width()/3 + BPF.get_width(),OFFY + BPI.get_height()/4))
    if comando == "VISITADO":
        PANTALLA.blit(BV, ((TAM_CAS*x_celda)+BV.get_width()/3,OFFY + BV.get_height()/4 + BV.get_height()))
    if comando == "DECIDIDO":
        PANTALLA.blit(BO, ((TAM_CAS*x_celda)+BV.get_width()/3,OFFY + BV.get_height()/4 + BV.get_height()))

def marcarPuntos(puntos, modo, tam_cas):
    for i in range(0, len(puntos), 1):
        x = puntos[i][0]+1
        y = puntos[i][1]+1
        marcarMapa(modo, x, y, tam_cas)


pygame.init()
pygame.display.set_caption('P2 Inteligencia Artifical')
pantalla_info = pygame.display.Info()
RESOLUCION = (pantalla_info.current_w-500, pantalla_info.current_h-500)
PANTALLA = pygame.display.set_mode(RESOLUCION)
MATRIZ = []
font = pygame.font.Font("Godzilla.ttf", 15)

MODO, MATRIZ = Menu(PANTALLA, RESOLUCION[0], MATRIZ)
LADO = int(RESOLUCION[1]/(len(MATRIZ)+1))
ESTADO = "MODIFICAR_MAPA"
POSTXT = font.render("", True, (255,255,255))
PI = [0,0]

while True:
    for EVENTO in pygame.event.get():
        TECLA = pygame.key.get_pressed()
        MOUSE_POS = (int(pygame.mouse.get_pos()[0]/LADO), int(pygame.mouse.get_pos()[1]/LADO))
        if EVENTO.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ESTADO == "MODIFICAR_MAPA":
            POSTXT = font.render("Modifica el mapa(E-Aceptar)", True, (255,255,255))
            if EVENTO.type == pygame.MOUSEBUTTONDOWN:
                MATRIZ = cambiarColorCasilla(MATRIZ, MOUSE_POS[1]-1, MOUSE_POS[0]-1, MODO)
            elif TECLA[pygame.K_e]:
                ESTADO = "POS_INI"
            dibujarCuadricula(MATRIZ, RESOLUCION, MODO)
        elif ESTADO == "POS_INI":
            if MOUSE_POS[0]<=len(MATRIZ[0]) and MOUSE_POS[1] <=len(MATRIZ): 
                POSTXT = font.render("Posicion Inicial: (" + INDX[MOUSE_POS[0]-1] + ", " + str(MOUSE_POS[1]) + ")", True, (255,255,255))
                if EVENTO.type == pygame.MOUSEBUTTONDOWN:
                    PI = MOUSE_POS
                    ESTADO = "POS_FIN"
            dibujarCuadricula(MATRIZ, RESOLUCION, MODO)
        elif ESTADO == "POS_FIN":
            if MOUSE_POS[0]<=len(MATRIZ[0]) and MOUSE_POS[1] <=len(MATRIZ): 
                POSTXT = font.render("Posicion Final: (" + INDX[MOUSE_POS[0]-1] + ", " + str(MOUSE_POS[1]) + ")", True, (255,255,255))
                if EVENTO.type == pygame.MOUSEBUTTONDOWN:
                    PF = MOUSE_POS
                    A1 = Agentes.AgenteL(MATRIZ, PI, PF)
                    ESTADO = "RECORRER"
            dibujarCuadricula(MATRIZ, RESOLUCION, MODO)
        elif ESTADO == "RECORRER":
                if A1.PA[0] == A1.PF[0] and A1.PA[1] == A1.PF[1]:
                    ESTADO = "META"
                else:
                    POSTXT = font.render("", True, (255,255,255))
                    A1.AutomaticoProfundidad()    
                    dibujarCuadricula(A1.CONOCIDO, RESOLUCION, MODO)
                    POSTXT = font.render("Posicion Actual: (" + str(A1.PA[0]) + ", " + str(A1.PA[1]) + ")", True, (255,255,255))
                    marcarMapa("INICIO", A1.PI[0], A1.PI[1], LADO)
                    marcarMapa("FINAL", A1.PF[0], A1.PF[1], LADO)
                    marcarMapa("ACTUAL", A1.PA[0], A1.PA[1], LADO)
                    marcarPuntos(A1.LD, "DECIDIDO", LADO)
                    marcarPuntos(A1.LV, "VISITADO", LADO)

        elif ESTADO == "META":
            PANTALLA.fill((0, 0, 0))
            font = pygame.font.Font("Godzilla.ttf", 40)
            POSTXT = font.render("META ALCANZADA", True, (255,255,255))
            

        PANTALLA.blit(POSTXT, (RESOLUCION[0]-POSTXT.get_width(), POSTXT.get_height()))
    pygame.display.update()