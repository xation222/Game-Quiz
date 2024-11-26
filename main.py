import pygame
import json


def desenhar_botao_iniciar():
    pygame.draw.rect(screen, (0, 255, 0), (posicao_botao[0], posicao_botao[1], largura_botao, altura_botao))
    texto_renderizado = fonte.render(texto_botao, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao[0] + (largura_botao - texto_renderizado.get_width()) // 2,
                                 posicao_botao[1] + (altura_botao - texto_renderizado.get_height()) // 2))


def limpar_tela(cor_fundo):
    screen.fill(cor_fundo)  # Preenche a tela com a cor de fundo
    pygame.display.flip()  # Atualiza a tela para mostrar as mudanças


def tela_de_pergunta():
     print('')


# respostas : 123 321 421 4
with open("textos.json", "r", encoding="utf-8") as arquivo:
    textos = json.load(arquivo)

pygame.init()
screenX = 360
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True

largura_botao = screenX / 2
altura_botao = screenY // 6
posicao_botao = (screenX // 2 - largura_botao // 2, screenY // 2 - altura_botao // 2)
texto_botao = "Iniciar Jogo"

fonte = pygame.font.Font(None, 38)  # None usa a fonte padrão; o número é o tamanho
texto_titulo = textos["telas"]["menu_principal"]
cor_texto = (255, 255, 255)  # Cor branca (R, G, B)

menu = True;
fase = 0;

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    if menu:
        desenhar_botao_iniciar()
        superficie_texto = fonte.render(texto_titulo, True, cor_texto)
        screen.blit(superficie_texto, (20, 90))
    else:
        superficie_texto = fonte.render(texto_titulo, True, cor_texto)
        screen.blit(superficie_texto, (20, 50))

    if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if posicao_botao[0] <= x <= posicao_botao[0] + largura_botao and posicao_botao[1] <= y <= posicao_botao[1] + altura_botao:
                    menu = False
                    fase = 1
                    texto_titulo = textos["perguntas"]["quest01"]
                    print("Iniciando o jogo...")
                    limpar_tela("purple")
                    #tela_de_pergunta()
                    # Aqui você pode colocar a função para iniciar o jogo
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()