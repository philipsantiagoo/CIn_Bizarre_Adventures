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
    inv.resetar_inventario()
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')
    mapa = load_pygame(mapa_path)

    largura = mapa.width * mapa.tilewidth
    altura = mapa.height * mapa.tileheight

    screen = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Menu")

    clock = pg.time.Clock()

    img_derrota = pg.image.load("telas/tela_derrota.jpg").convert()  # abre a imagem
    img_derrota = pg.transform.scale(img_derrota, (largura, altura))

    # Duas luzes independentes
    lighting1 = Lighting((largura, altura), light_radius=25)  # player 1, raio variável
    lighting2 = Lighting((largura, altura), light_radius=80)  # player 2, raio fixo

    walls = []
    for obj in mapa.objects:
        if obj.name == "parede":
            walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height))

    player = Player(position=(380, 700), speed=2)
    player2 = Player2(position=(420, 70), speed=1.5)
    
    #Lista original de coletáveis:
    coletaveis_originais = [
    ("flashlight.png", (360, 608)),
    ("flashlight.png", (740, 710)),
    ("flashlight.png", (430, 285)),
    ("coin.png", (772, 490)),
    ("coin.png", (385, 20)),
    ("coin.png", (338, 360)),
    ("heart.png", (1, 335)),
    ("heart.png", (700, 224)),
    ("heart.png", (170, 98)),
    ("gasoline.png", (650, 1))
        ]
    
    #Criando coletáveis a partir da lista original:
    coletaveis = [Coletavel(pos, nome) for nome, pos in coletaveis_originais]
    
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

        # --- Colisão entre Player e Player2 ---
        if player.rect.colliderect(player2.rect) and player2.hit():
            # Reduz 1 de vida
            inv.inventario["vida"] -= 1

            # Volta os jogadores para as posições iniciais
            player.rect.topleft = (380, 700)

            # Remover todas as lanternas que já estavam na tela (as que sobraram)
            coletaveis = [c for c in coletaveis if c.tipo != "lanterna"]

            # Recriar lanternas originais
            for nome, pos in coletaveis_originais:
                if nome == "flashlight.png":
                    coletaveis.append(Coletavel(pos, nome))

            # Resetar lanternas no inventário
            inv.inventario["lanterna"] = 0  

            # Verifica se a vida acabou
            if inv.inventario["vida"] <= 0:

                pg.mixer.music.stop()
                musica_derrota = pg.mixer.Sound('sons/defeat.ogg')
                musica_derrota.play(0)

                #Tela de derrota
                screen.blit(img_derrota, (0, 0))
                quadrado_texto = pg.Rect(0, 600, largura, 300)
                pg.draw.rect(screen, "#656565", quadrado_texto)
                fonte = pg.font.SysFont("Papyrus", 45, bold=True)
                texto = fonte.render("Fala baixo que eu tô fazendo chamada...", True, "#FF2F2F")
                screen.blit(texto, (quadrado_texto.x + 20, quadrado_texto.y + 10))
                pg.display.update()

                #Esperando 5 segundo antes de voltar para o menu:
                pg.time.delay(5000)
                
                running = False
                vitoria = 0  # derrota

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

        #lógica de vitória
        if inv.inventario.get('gasolina') > 0 and player.rect.colliderect(generator_rect) and player.interact():
            running = False
            vitoria = 1
        
        pg.display.flip()
        clock.tick(60)

    return [True, vitoria]
