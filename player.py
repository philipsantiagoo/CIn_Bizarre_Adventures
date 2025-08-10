import pygame as pg
import os
from pytmx.util_pygame import load_pygame
from sys import exit

class Player(pg.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.speed = speed
        self.direction = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.images = {
            'down': [
                pg.image.load(os.path.join('personagem', 'frente', 'f1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'frente', 'f2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'frente', 'f3.png')).convert_alpha()
            ],
            'up': [
                pg.image.load(os.path.join('personagem', 'costas', 'c1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'costas', 'c2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'costas', 'c3.png')).convert_alpha()
            ],
            'left': [
                pg.image.load(os.path.join('personagem', 'esquerda', 'e1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'esquerda', 'e2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'esquerda', 'e3.png')).convert_alpha()
            ],
            'right': [
                pg.image.load(os.path.join('personagem', 'direita', 'd1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'direita', 'd2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagem', 'direita', 'd3.png')).convert_alpha()
            ]
        }

        self.image = self.images[self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)


    def handle_input(self):
        keys = pg.key.get_pressed()
        directionX, directionY = 0, 0

        # Reset direction só se alguma tecla for pressionada
        # para evitar erro de direção errada

        if keys[pg.K_w]:
            directionY = -self.speed
            self.direction = 'up'
        elif keys[pg.K_s]:
            directionY = self.speed
            self.direction = 'down'
        elif keys[pg.K_a]:
            directionX = -self.speed
            self.direction = 'left'
        elif keys[pg.K_d]:
            directionX = self.speed
            self.direction = 'right'
        else:
            # Nenhuma tecla pressionada, manter a direção atual
            directionX, directionY = 0, 0

        return directionX, directionY


    def move(self, directionX, directionY, walls):
        # Movimento X
        self.rect.x += directionX
        for wall in walls:
            if self.rect.colliderect(wall):
                if directionX > 0:
                    self.rect.right = wall.left
                elif directionX < 0:
                    self.rect.left = wall.right

        # Movimento Y
        self.rect.y += directionY
        for wall in walls:
            if self.rect.colliderect(wall):
                if directionY > 0:
                    self.rect.bottom = wall.top
                elif directionY < 0:
                    self.rect.top = wall.bottom


    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images[self.direction]):
            self.frame_index = 0
        self.image = self.images[self.direction][int(self.frame_index)]


    def update(self, walls):
        directionX, directionY = self.handle_input()

        if directionX != 0 or directionY != 0:
            self.move(directionX, directionY, walls)
            self.animate()
        else:
            self.frame_index = 0
            self.image = self.images[self.direction][self.frame_index]


    def draw(self, surface):
        surface.blit(self.image, self.rect)


def main():
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

    player = Player(position=(100, 100), speed=3)

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

        pg.display.flip()
        clock.tick(60)

    '''pg.quit()
    exit()'''


if __name__ == "__main__":
    main()
