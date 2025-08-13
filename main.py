import pygame as pg
from sys import exit
import inventory as inv
import button
from screen import play
from tutorial import tutorial

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

#cria a tela de vitória
tela_vitoria = pg.image.load("telas/tela_vitoria.jpg")
tela_vitoria = pg.transform.scale(tela_vitoria, (800, 750))


# criacao do botao funcional em si
main_button = button.Button(button_surface, 400, 500, "Play")

tutorial_button = button.Button(button_surface, 400, 600, "Tutorial")

vitoria = 0

executando = True

# game loop
while executando:
    # verifica a posicao do mouse
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        # se o evento for de fechar a janela, ele fecha
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        # se o evento for de clique do mouse, verifica onde foi clicado
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.type == pg.KEYDOWN:  # opcional: sair ao apertar ESC
                if event.key == pg.K_ESCAPE:
                    executando = False
            if main_button.checkForInput(mouse_pos): # se foi clicado no botao de play, inicia o jogo
                pg.mixer.music.load("sons/background.ogg")
                pg.mixer.music.play(-1)  # toca a música em loop
                fechar = play(screen) # inicia o jogo
                if fechar[0]:
                    if fechar[1] == 1:
                        pg.mixer.music.stop()
                        vitoria = 1
                        musica_vitoria = pg.mixer.Sound("sons/victory.ogg")
                        musica_vitoria.play(0)
                        screen.blit(tela_vitoria, (0,0))
                        inv.display_score(screen)  # <<< Mostra o score final
                        pg.display.update()
                        pg.time.delay(6000)
                        vitoria = 0
                    else:
                        vitoria = 0
            if tutorial_button.checkForInput(mouse_pos): # se clicou no botao de tutorial, abre os comandos do jogo
                tutorial(screen)

    if vitoria == 0:
        # atualiza a tela
        screen.blit(background, (0, 0))
        main_button.update()
        main_button.changeColor(mouse_pos)
        tutorial_button.update()
        tutorial_button.changeColor(mouse_pos)
        pg.display.update()

pg.quit()
exit()