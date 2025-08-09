import os
import pygame as pg
from pytmx.util_pygame import load_pygame


def play():
    # definindo um caminho absoluto para acessar o mapa criado
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')

    # inicializando o pygame
    pg.init()

    # cria uma janela temporária para permitir conversão de imagens
    janela_temp = pg.display.set_mode((1, 1))

    # carregando o mapa do game
    mapa = load_pygame(mapa_path)

    # criando a janela (screen) com o tamanho do mapa
    janela_largura = mapa.width * mapa.tilewidth
    janela_altura = mapa.height * mapa.tileheight
    janela = pg.display.set_mode((janela_largura, janela_altura))

    # definindo o título da janela
    pg.display.set_caption('CIn Bizarre Adventures')

    # definindo o clock (relógio) de exibição da janela (screen)
    clock = pg.time.Clock()

    # definindo a variável de continuação para exibir o mapa
    continuar = True

    while continuar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                continuar = False

        janela.fill((0, 0, 0))  # definindo a cor de fundo da janela (preto)

        # desenha cada tile do mapa
        for camada in mapa.visible_layers:
            if hasattr(camada, 'tiles'):
                for x, y, tile in camada.tiles():
                    janela.blit(
                        tile, (x * mapa.tilewidth, y * mapa.tileheight))

        pg.display.flip()  # atualiza a janela de acordo com os novos conteúdos
        clock.tick(60)  # definindo uma taxa de 60 FPS

    pg.quit()  # fecha o pygame


# chama a função para iniciar o jogo
play()
