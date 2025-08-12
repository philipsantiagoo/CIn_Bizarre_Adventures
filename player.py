import pygame as pg
import os


# definindo a classe player que controla o personagem principal
class Player(pg.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.speed = speed
        self.direction = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # coletando as imagens da pasta
        self.images = {
            'down': [
                pg.image.load(os.path.join('personagens','player_1', 'frente', 'f1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'frente', 'f2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'frente', 'f3.png')).convert_alpha()
            ],
            'up': [
                pg.image.load(os.path.join('personagens', 'player_1', 'costas', 'c1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'costas', 'c2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'costas', 'c3.png')).convert_alpha()
            ],
            'left': [
                pg.image.load(os.path.join('personagens', 'player_1', 'esquerda', 'e1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'esquerda', 'e2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'esquerda', 'e3.png')).convert_alpha()
            ],
            'right': [
                pg.image.load(os.path.join('personagens', 'player_1', 'direita', 'd1.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'direita', 'd2.png')).convert_alpha(),
                pg.image.load(os.path.join('personagens', 'player_1', 'direita', 'd3.png')).convert_alpha()
            ]
        }

        self.image = self.images[self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)


    # função para controlar o personagem por meio dos botões (W, A, S, D) do teclado
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


    # função para controlar os movimentos no plano cartesiano
    # walls são as paredes atribuídas pelo mapa no tiled
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


    # controla a animação do personagem
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images[self.direction]):
            self.frame_index = 0
        self.image = self.images[self.direction][int(self.frame_index)]


    # captura o movimento do personagem por frame
    def update(self, walls):
        directionX, directionY = self.handle_input()

        if directionX != 0 or directionY != 0:
            self.move(directionX, directionY, walls)

            if self.rect.right > 800:
                self.rect.right = 800
            if self.rect.bottom > 750:
                self.rect.bottom = 750

            self.animate()
        else:
            self.frame_index = 0
            self.image = self.images[self.direction][self.frame_index]



    # desenha o personagem na tela
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    #interação
    def interact(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_e]:
            return True