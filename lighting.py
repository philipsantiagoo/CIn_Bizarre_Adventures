import pygame

class Lighting:
    def __init__(self, screen_size, light_radius = 25):
        self.screen_width, self.screen_height = screen_size
        self.light_radius = light_radius

        # Superfície para luz (gradiente radial)
        self.light_surface = pygame.Surface((light_radius * 2, light_radius * 2), pygame.SRCALPHA)
        self._create_light_mask()  # <-- gera o gradiente

    def _create_light_mask(self):
        """Cria um gradiente circular suave."""
        for r in range(self.light_radius, 0, -1):
            alpha = int(255 * (1 - (r / self.light_radius)))  
            pygame.draw.circle(
                self.light_surface,
                (0, 0, 0, alpha),
                (self.light_radius, self.light_radius),
                r
            )

    def draw_light(self, target_surface, player_pos):
        """
        Desenha a máscara de luz sobre a tela.
        player_pos: posição do jogador no mundo.
        """
        # Camada preta sobre tudo
        dark_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        dark_surface.fill((0, 0, 0, 255))  # 200 = opacidade da escuridão

        # Posição da luz (centraliza no player)
        light_x = player_pos[0] - self.light_radius
        light_y = player_pos[1] - self.light_radius

        # "Fura" o buraco da luz
        dark_surface.blit(self.light_surface, (light_x, light_y), special_flags=pygame.BLEND_RGBA_SUB)

        # Desenha por cima da tela final
        target_surface.blit(dark_surface, (0, 0))
