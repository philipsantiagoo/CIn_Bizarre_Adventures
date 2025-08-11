import pygame as pg
import os
import inventory as inv
from pytmx.util_pygame import load_pygame

from player import Player  
from player2 import Player2
from collision import Coletavel
from lighting import Lighting 


def play(screen):
    pg.init()
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')
    mapa = load_pygame(mapa_path)

    largura = mapa.width * mapa.tilewidth
    altura = mapa.height * mapa.tileheight

    screen = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Mapa com Player")

    clock = pg.time.Clock()

    # Duas luzes independentes
    lighting1 = Lighting((largura, altura), light_radius=25)  # player 1, raio variável
    lighting2 = Lighting((largura, altura), light_radius=80)  # player 2, raio fixo

    walls = []
    for obj in mapa.objects:
        if obj.name == "parede":
            walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height))

    player = Player(position=(380, 700), speed=1.3)
    player2 = Player2(position=(420, 70), speed=1.45)

    coletaveis = [
        Coletavel((360, 608), 'flashlight.png'),
        Coletavel((740, 710), 'flashlight.png'),
        Coletavel((430, 285), 'flashlight.png'),
        Coletavel((772, 490), 'coin.png'),
        Coletavel((385,20), 'coin.png'),
        Coletavel((338,360), 'coin.png'),
        Coletavel((1, 335), 'heart.png'),
        Coletavel((700,224), 'heart.png'),
        Coletavel((170,98), 'heart.png'),
        Coletavel((650,1), 'gasoline.png')
    ]
    
    generator_img = pg.image.load("coletaveis/generator.png").convert_alpha()
    generator_rect = generator_img.get_rect(topleft=(33, 33))

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
        
        screen.blit(generator_img, generator_rect)

        player.update(walls)
        player.draw(screen)

        player2.update(walls)
        player2.draw(screen)

        item_pego = pg.mixer.Sound("sons/collectible.ogg")
        canal_item_pego = pg.mixer.Channel(0)

        for coletavel in coletaveis[:]:  
            coletavel.add_to_screen(screen)
            coletavel.colisao_coletavel(player.rect)
            if getattr(coletavel, 'coletado', False): 
                coletaveis.remove(coletavel)
                pg.mixer.music.set_volume(0.2)
                item_pego.play()
                
        if not canal_item_pego.get_busy():
            pg.mixer.music.set_volume(1.0)

        # Ajusta o raio do lighting1 conforme lanterna
        lanterna = inv.inventario.get('lanterna', 0)
        if lanterna == 1 and lighting1.light_radius != 60:
            lighting1.light_radius = 60
            lighting1.light_surface = pg.Surface((lighting1.light_radius * 2, lighting1.light_radius * 2), pg.SRCALPHA)
            lighting1._create_light_mask()
        elif lanterna == 2 and lighting1.light_radius != 70:
            lighting1.light_radius = 70
            lighting1.light_surface = pg.Surface((lighting1.light_radius * 2, lighting1.light_radius * 2), pg.SRCALPHA)
            lighting1._create_light_mask()
        elif lanterna == 3 and lighting1.light_radius != 75:
            lighting1.light_radius = 75
            lighting1.light_surface = pg.Surface((lighting1.light_radius * 2, lighting1.light_radius * 2), pg.SRCALPHA)
            lighting1._create_light_mask()
        elif lanterna == 0 and lighting1.light_radius != 25:
            lighting1.light_radius = 25
            lighting1.light_surface = pg.Surface((lighting1.light_radius * 2, lighting1.light_radius * 2), pg.SRCALPHA)
            lighting1._create_light_mask()


        # Surface única pra sombra
        dark_surface = pg.Surface((largura, altura), pg.SRCALPHA)
        dark_surface.fill((0, 0, 0, 255))  # opacidade sombra (ajuste)


        # Furo da luz player 1
        lx1 = player.rect.centerx - lighting1.light_radius
        ly1 = player.rect.centery - lighting1.light_radius
        dark_surface.blit(lighting1.light_surface, (lx1, ly1), special_flags=pg.BLEND_RGBA_SUB)

        # Furo da luz player 2 (raio fixo)
        lx2 = player2.rect.centerx - lighting2.light_radius
        ly2 = player2.rect.centery - lighting2.light_radius
        dark_surface.blit(lighting2.light_surface, (lx2, ly2), special_flags=pg.BLEND_RGBA_SUB)


        # Aplica sombra no screen
        screen.blit(dark_surface, (0, 0))


        # Inventário
        inv.mostrar_inventario(screen, inv.imagens_itens, inv.inventario, inv.main_font)

        pg.display.flip()
        clock.tick(60)

    return True
