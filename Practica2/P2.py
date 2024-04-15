import FuncionesGraficos as GRAX
import pygame
import sys

pygame.init()
pantalla_info = pygame.display.Info()
RESOLUCION = (pantalla_info.current_w-100, pantalla_info.current_h-100)
PANTALLA = pygame.display.set_mode(RESOLUCION)
MATRIZ = []

MODO, MATRIZ = GRAX.Menu(PANTALLA, RESOLUCION[0], MATRIZ)
while True:
    for EVENTO in pygame.event.get():
        if EVENTO.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        GRAX.dibujarCuadricula(MATRIZ, RESOLUCION, MODO)
        print(EVENTO)
    pygame.display.update()

