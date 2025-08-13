import pygame as pg
from sys import exit
import button

# criacao do bg do botao de play
button_surface = pg.image.load("buttons/botao_padrao.png")
button_surface = pg.transform.scale(button_surface, (280, 100))

back_button = button.Button(button_surface, 400, 650, "Back")

def tutorial(screen):
    tutorial_ativo = True
    while tutorial_ativo:
        # verifica a posicao do mouse
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    tutorial_ativo = False

        screen.fill((0, 0, 0))

        fonte_titulo = pg.font.SysFont("Papyrus", 80, bold=True)
        titulo = fonte_titulo.render("Tutorial", True, "white")

        screen.blit(titulo, (240, 10))

        fonte_texto = pg.font.SysFont("Papyrus", 30)
        texto = [
            "Se você é o player 1:",
            "- Movimente-se usando WASD;",
            "- Seu objetivo é levar a gasolina até o gerador;",
            "- Para ligar o gerador com a gasolina, pressione E.",
            "",
            "Se você é o player 2:",
            "- Use as setas para se mover;",
            "- Use a tecla K para atacar o player 1;",
            "- Seu objetivo é impedir que o player 1 ligue o gerador."
        ]

        for i, linha in enumerate(texto):
            texto_renderizado = fonte_texto.render(linha, True, "white")
            screen.blit(texto_renderizado, (10, 120 + i * 50))

        back_button.update()
        back_button.changeColor(mouse_pos)
        pg.display.update()
