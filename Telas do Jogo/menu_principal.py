import pygame as pg
from sys import exit
import button_class as bcs


def play():
    pg.display.set_caption("Game Screen")

    while True:
        play_mouse_pos = pg.mouse.get_pos()
        screen.fill("#000000")  # Clear the screen with black

        play_text = main_font.render("Game Screen", True, "white")
        play_text_rect = play_text.get_rect(center=(400, 375))
        screen.blit(play_text, play_text_rect)

        back_button = bcs.Button(button_surface, 400, 650, "Back")
        back_button.update()
        back_button.changeColor(play_mouse_pos)
        back_button.checkForInput(play_mouse_pos)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button.checkForInput(play_mouse_pos):
                    return
            pg.display.update()


pg.init()
screen = pg.display.set_mode((800, 750))
background = pg.image.load("Telas do Jogo/tela_inicial.jpg")
background = pg.transform.scale(background, (800, 750))
pg.display.set_caption("Main Menu")

button_surface = pg.image.load("Botões/botao_start.png")
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
