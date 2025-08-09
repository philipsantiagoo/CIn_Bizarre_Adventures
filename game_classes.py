import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 750))
main_font = pg.font.SysFont("Papyrus", 70)

# Classe para botões
class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

# Inventário do jogador (começa com 0 de cada tipo)
inventario = {
    "vida": 0,
    "moedas": 0,
    "gasolina": 0,
	"lanterna": 0
}

# Imagens dos itens
imagens_itens = {
	"vida": pg.image.load("coletaveis/heart.png"),
	"moedas": pg.image.load("coletaveis/coin.png"),
	"gasolina": pg.image.load("coletaveis/gasoline.png"),
	"lanterna": pg.image.load("coletaveis/flashlight.png")
}

# Redimensiona as imagens dos itens
for tipo, img in imagens_itens.items():
	imagens_itens[tipo] = pg.transform.scale(img, (40, 40))  # Ajuste o tamanho conforme necessário

# Função para adicionar item no inventário
def coletar_item(item):
    if item.tipo in inventario:
        inventario[item.tipo] += 1
    else:
        inventario[item.tipo] = 1

# Função para mostrar o inventário na tela
def mostrar_inventario(tela, imagens, inventario, fonte):
    x = 750
    y = 35
    for tipo, img in imagens.items():
        tela.blit(img, (x, y))
        qtd = inventario.get(tipo, 0)
        texto = fonte.render(str(qtd), True, "#FFFFFF")
        tela.blit(texto, (x - img.get_width() + 20, y))
        y += img.get_height() + 30
