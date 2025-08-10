import pygame as pg
import os
import inventory as inv
from pytmx.util_pygame import load_pygame

from player import Player  
from collision import Coletavel
from lighting import Lighting 


def play(screen):
    pg.init()
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')
    mapa = load_pygame(mapa_path)

    largura = mapa.width * mapa.tilewidth
    altura = mapa.height * mapa.tileheight

    # ajusta o tamanho da janela para o tamanho do mapa
    screen = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Mapa com Player")

    clock = pg.time.Clock()

    # escuro aqui
    lighting = Lighting((largura, altura), light_radius = 25)

    walls = []
    for obj in mapa.objects:
        if obj.name == "parede":
            walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height))

    player = Player(position=(380, 700), speed=1.3)

    coletaveis = [ # posicao dos coletaveis no mapa
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

        item_pego = pg.mixer.Sound("sons/collectible.ogg")
        canal_item_pego = pg.mixer.Channel(0)

        for coletavel in coletaveis[:]:  
            coletavel.add_to_screen(screen)
            coletavel.colisao_coletavel(player.rect)
            if getattr(coletavel, 'coletado', False): 
                coletaveis.remove(coletavel)
                pg.mixer.music.set_volume(0.2)  # abaixa o volume da musica
                item_pego.play() # toca musiquinha de q pegou o coletavel
                

        if not canal_item_pego.get_busy():
            pg.mixer.music.set_volume(1.0) # volta o volume da musica


        # iluminação, se pegou a lanterna teve sorte e a visão aumenta
        if inv.inventario.get('lanterna', 0) > 0:
            if lighting.light_radius != 60:
                lighting.light_radius = 60
                lighting.light_surface = pg.Surface((lighting.light_radius * 2, lighting.light_radius * 2), pg.SRCALPHA)
                lighting._create_light_mask()
        else:
            if lighting.light_radius != 25:
                lighting.light_radius = 25
                lighting.light_surface = pg.Surface((lighting.light_radius * 2, lighting.light_radius * 2), pg.SRCALPHA)
                lighting._create_light_mask()


        # camuflagem
        lighting.draw_light(screen, player.rect.center)

        # inventário
        inv.mostrar_inventario(screen, inv.imagens_itens, inv.inventario, inv.main_font)

        pg.display.flip()
        clock.tick(60)

    return True