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
