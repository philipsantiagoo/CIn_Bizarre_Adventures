import pygame as pg
from sys import exit
import inventory as gc
import button
from screen import play


# inicia o pygame
pg.init()

# cria a tela principal do jogo
screen = pg.display.set_mode((800, 750))
background = pg.image.load("telas/tela_inicial.jpg")
background = pg.transform.scale(background, (800, 750))

# define o título da janela
pg.display.set_caption("Main Menu")

# criacao do bg do botao de play
button_surface = pg.image.load("buttons/botao_padrao.png")
button_surface = pg.transform.scale(button_surface, (280, 100))

# criacao do botao funcional em si
main_button = button.Button(button_surface, 400, 600, "Play")
main_font = pg.font.SysFont("Papyrus", 65)

# game loop
while True:
    # verifica a posicao do mouse
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        # se o evento for de fechar a janela, ele fecha
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        # se o evento for de clique do mouse, verifica se o botao foi clicado
        if event.type == pg.MOUSEBUTTONDOWN:
            if main_button.checkForInput(mouse_pos): # se foi clicado, inicia o jogo
                pg.mixer.music.load("sons/background.ogg")
                pg.mixer.music.play(-1)  # toca a música em loop
                play()

    # atualiza a tela
    screen.blit(background, (0, 0))
    main_button.update()
    main_button.changeColor(mouse_pos)
    pg.display.update()
