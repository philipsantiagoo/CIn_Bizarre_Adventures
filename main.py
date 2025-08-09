import pygame as pg
from sys import exit
import button_class as bcs
from display_map import play


pg.init()
screen = pg.display.set_mode((800, 750))
background = pg.image.load("telas/tela_inicial.jpg")
background = pg.transform.scale(background, (800, 750))
pg.display.set_caption("Main Menu")


button_surface = pg.image.load("buttons/botao_padrao.png")
button_surface = pg.transform.scale(button_surface, (280, 100))


main_button = bcs.Button(button_surface, 400, 600, "Play")
main_font = pg.font.SysFont("Papyrus", 70)


while True:
    mouse_pos = pg.mouse.get_pos()

    play_button = pg.Rect(280, 575, 250, 70)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if main_button.checkForInput(mouse_pos):
                play()

    screen.blit(background, (0, 0))
    main_button.update()
    main_button.changeColor(mouse_pos)
    pg.display.update()
