import pygame as pg
import os
import inventory as inv
from pytmx.util_pygame import load_pygame

from player import Player  # supondo que Player tá num arquivo separado player.py

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

    player = Player(position=(100, 100), speed=1.3)

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
        inv.mostrar_inventario(screen, inv.imagens_itens, inv.inventario, inv.main_font)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
