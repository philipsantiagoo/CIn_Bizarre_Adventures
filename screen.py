import pygame as pg
import os
import inventory as inv
from pytmx.util_pygame import load_pygame

from player import Player  
from collision import Coletavel 


def play():
    pg.init()
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')
    mapa = load_pygame(mapa_path)

    largura = mapa.width * mapa.tilewidth
    altura = mapa.height * mapa.tileheight
    screen = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Mapa com Player")

    clock = pg.time.Clock()

    walls = []
    for obj in mapa.objects:
        if obj.name == "parede":
            walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height))

    player = Player(position=(380, 700), speed=1.4)
    coletaveis = [
        Coletavel((360, 608), 'flashlight.png'),
        Coletavel((772, 490), 'coin.png'),
        Coletavel((385,20), 'coin.png'),
        Coletavel((338,360), 'coin.png'),
        Coletavel((1, 335), 'heart.png'),
        Coletavel((700,224), 'heart.png'),
        Coletavel((170,98), 'heart.png')
    ]

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for layer in mapa.visible_layers:
            if hasattr(layer, 'tiles'):
                for x, y, tile in layer.tiles():
                    screen.blit(tile, (x * mapa.tilewidth, y * mapa.tileheight))

        player.update(walls)
        player.draw(screen)

        for coletavel in coletaveis[:]:  
            coletavel.add_to_screen(screen)
            coletavel.colisao_coletavel(player.rect)
            if getattr(coletavel, 'coletado', False): 
                coletaveis.remove(coletavel)

        inv.mostrar_inventario(screen, inv.imagens_itens, inv.inventario, inv.main_font)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
