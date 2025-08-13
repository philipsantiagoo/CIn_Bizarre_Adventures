import pygame as pg


pg.init()
screen = pg.display.set_mode((800, 750))
main_font = pg.font.SysFont("Papyrus", 30)

#Score:
score = 0


# Inventário do jogador (começa com 0 de cada tipo)
inventario = {
    "vida": 1,
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
    global score
    if item.tipo in inventario:
        inventario[item.tipo] += 1
        if item.tipo == "moedas":
            score += 100
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

def resetar_inventario():
    inventario["vida"] = 1
    inventario["moedas"] = 0
    inventario["gasolina"] = 0
    inventario["lanterna"] = 0

def display_score(tela):
    # Texto "Score"
    score_font = pg.font.SysFont("Papyrus", 25)
    score_titulo_surf = score_font.render("Score", True, (255, 255, 255))
    score_titulo_rect = score_titulo_surf.get_rect(center=(400, 30))
    tela.blit(score_titulo_surf, score_titulo_rect)


    # Valor do score
    valor_font = pg.font.SysFont("Papyrus", 25)
    score_valor_surf = valor_font.render(str(score), True, (255, 0, 0))
    score_valor_rect = score_valor_surf.get_rect(center=(400, 50))
    tela.blit(score_valor_surf, score_valor_rect)
    
def resetar_score():
    global score
    score = 0