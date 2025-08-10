#Bibliotecas e arquivos importados
import pygame as pg
import inventory as inv
import os
from pytmx.util_pygame import load_pygame


#Classe dos coletaveis
class Coletavel(pg.sprite.Sprite):


    #atributos iniciais dos coletáveis
    def __init__(self, posicao_coletavel, nome_arquivo_coletavel):  #COLOCAR A EXTENSÃO DO ARQUIVO NO NOME
        super().__init__()


        #atributo de superficie do coletável
        self.surface = pg.image.load(f'coletaveis/{nome_arquivo_coletavel}').convert_alpha()


        #atributo do retângulo do coletável
        self.rect = self.surface.get_rect(topleft = posicao_coletavel)


        #atributo para verificar coletável:
        self.coletado = False


        #caso seja a imagem dos corações, define o atributo tipo do coletável como 'vida'
        if nome_arquivo_coletavel == 'heart.png':
            self.tipo = 'vida'
       
        #caso seja a imagem das moedas, define o atributo tipo do coletável como 'moedas'
        elif nome_arquivo_coletavel == 'coin.png':
            self.tipo = 'moedas'
       
        #caso seja a imagem do galão de gasolina, define o atributo tipo do coletável como 'gasolina'
        elif nome_arquivo_coletavel == 'gasoline.png':
            self.tipo = 'gasolina'
       
        #caso seja a imagem da lanterna, define o atributo tipo do coletável como 'lanterna'
        elif nome_arquivo_coletavel == 'flashlight.png':
            self.tipo = 'lanterna'


    #propriedade de colisão dos coletáveis
    def colisao_coletavel(self, hitbox_player):


        #caso haja colisão com o player irá adicionar o coletável ao inventário
        if not self.coletado and self.rect.colliderect(hitbox_player):
            inv.coletar_item(self)
            self.coletado = True


    #propriedade que adiciona o coletável na tela
    def add_to_screen(self, tela):
        if not self.coletado:
            tela.blit(self.surface,self.rect)


#Função main: sem ela o coletável não aparece na tela (basicamente só copiei do arquivo player e fiz algumas alterações kkkkk não sei muito sobre ela kkkk)
def main():
    pg.init()
    base_path = os.path.dirname(os.path.abspath(__file__))
    mapa_path = os.path.join(base_path, 'mapa', 'map.tmx')
    mapa = load_pygame(mapa_path)


    largura = mapa.width * mapa.tilewidth
    altura = mapa.height * mapa.tileheight
    screen = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Mapa com coletaveis")


    clock = pg.time.Clock()


    walls = []
    for obj in mapa.objects:
        if obj.name == "parede":
            walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height))


    coletavel = Coletavel(posicao_coletavel=(170, 100), nome_arquivo_coletavel='flashlight.png')


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


        coletavel.add_to_screen(screen)


        pg.display.flip()
        clock.tick(60)


    '''pg.quit()
    exit()'''


if __name__ == "__main__":
    main()
