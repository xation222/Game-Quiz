import pygame
import json

def fase1():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest01"]
    texto_botao_resposta1 = textos["respostas"]["quest01"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest01"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest01"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest01"]["resposta4"]


def fase2():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest02"]
    texto_botao_resposta1 = textos["respostas"]["quest02"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest02"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest02"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest02"]["resposta4"]


def fase3():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest03"]
    texto_botao_resposta1 = textos["respostas"]["quest03"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest03"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest03"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest03"]["resposta4"]


def fase4():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest04"]
    texto_botao_resposta1 = textos["respostas"]["quest04"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest04"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest04"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest04"]["resposta4"]


def fase5():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest05"]
    texto_botao_resposta1 = textos["respostas"]["quest05"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest05"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest05"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest05"]["resposta4"]


def fase6():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest06"]
    texto_botao_resposta1 = textos["respostas"]["quest06"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest06"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest06"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest06"]["resposta4"]


def fase7():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest07"]
    texto_botao_resposta1 = textos["respostas"]["quest07"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest07"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest07"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest07"]["resposta4"]


def fase8():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest08"]
    texto_botao_resposta1 = textos["respostas"]["quest08"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest08"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest08"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest08"]["resposta4"]


def fase9():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest09"]
    texto_botao_resposta1 = textos["respostas"]["quest09"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest09"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest09"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest09"]["resposta4"]


def fase10():
    global texto_titulo
    global texto_botao_resposta1 
    global texto_botao_resposta2
    global texto_botao_resposta3
    global texto_botao_resposta4 
    texto_titulo = textos["perguntas"]["quest10"]
    texto_botao_resposta1 = textos["respostas"]["quest10"]["resposta1"]
    texto_botao_resposta2 = textos["respostas"]["quest10"]["resposta2"]
    texto_botao_resposta3 = textos["respostas"]["quest10"]["resposta3"]
    texto_botao_resposta4 = textos["respostas"]["quest10"]["resposta4"]


def gameover():
    global texto_titulo
    global resultado_calculado
    global resultado
    if resultado_calculado == False:
        for c in range(len(respostas_corretas)):
            if respostas_jogador[c] == respostas_corretas[c]:
                resultado += 1
        resultado_calculado = True
        resultado = str(resultado*10)
    
    texto_titulo = "Fim do Jogo"
    superficie_texto2 = fonte.render("Você acertou " + resultado + "%", True, cor_texto)
    screen.blit(superficie_texto2, (20, 190))


def desenhar_botao_iniciar():
    global mouse_pressionado
    pygame.draw.rect(screen, (0, 255, 0), (posicao_botao[0], posicao_botao[1], largura_botao, altura_botao,))
    texto_renderizado = fonte.render(texto_botao, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao[0] + (largura_botao - texto_renderizado.get_width()) // 2,
                                 posicao_botao[1] + (altura_botao - texto_renderizado.get_height()) // 2))
    
    if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressionado == False:
            x, y = event.pos
            if posicao_botao[0] <= x <= posicao_botao[0] + largura_botao and posicao_botao[1] <= y <= posicao_botao[1] + altura_botao:
                global menu
                global fase 
                
                menu = False
                fase += 1
                mouse_pressionado = True


def desenhar_botoes_respostas():
    global mouse_pressionado
    pygame.draw.rect(screen, (0, 0, 255), (posicao_botao_resposta1["botao1-x"], posicao_botao_resposta1["botao1-y"], tamanho_botao_resposta["largura"], tamanho_botao_resposta["altura"]))
    texto_renderizado = fonte_respostas.render(texto_botao_resposta1, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao_resposta1["botao1-x"] + (tamanho_botao_resposta["largura"] - texto_renderizado.get_width()) // 2,                       posicao_botao_resposta1["botao1-y"] + (tamanho_botao_resposta["altura"] - texto_renderizado.get_height()) // 2))
    
    pygame.draw.rect(screen, (0, 0, 255), (posicao_botao_resposta2["botao1-x"], posicao_botao_resposta2["botao1-y"], tamanho_botao_resposta["largura"], tamanho_botao_resposta["altura"]))
    texto_renderizado = fonte_respostas.render(texto_botao_resposta2, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao_resposta2["botao1-x"] + (tamanho_botao_resposta["largura"] - texto_renderizado.get_width()) // 2,                       posicao_botao_resposta2["botao1-y"] + (tamanho_botao_resposta["altura"] - texto_renderizado.get_height()) // 2))

    pygame.draw.rect(screen, (0, 0, 255), (posicao_botao_resposta3["botao1-x"], posicao_botao_resposta3["botao1-y"], tamanho_botao_resposta["largura"], tamanho_botao_resposta["altura"]))
    texto_renderizado = fonte_respostas.render(texto_botao_resposta3, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao_resposta3["botao1-x"] + (tamanho_botao_resposta["largura"] - texto_renderizado.get_width()) // 2,                       posicao_botao_resposta3["botao1-y"] + (tamanho_botao_resposta["altura"] - texto_renderizado.get_height()) // 2))

    pygame.draw.rect(screen, (0, 0, 255), (posicao_botao_resposta4["botao1-x"], posicao_botao_resposta4["botao1-y"], tamanho_botao_resposta["largura"], tamanho_botao_resposta["altura"]))
    texto_renderizado = fonte_respostas.render(texto_botao_resposta4, True, cor_texto)
    screen.blit(texto_renderizado, (posicao_botao_resposta4["botao1-x"] + (tamanho_botao_resposta["largura"] - texto_renderizado.get_width()) // 2,                       posicao_botao_resposta4["botao1-y"] + (tamanho_botao_resposta["altura"] - texto_renderizado.get_height()) // 2))

    if event.type == pygame.MOUSEBUTTONDOWN and mouse_pressionado == False:
        x, y = event.pos
        global fase 
        if posicao_botao_resposta1["botao1-x"] <= x <= posicao_botao_resposta1["botao1-x"] + tamanho_botao_resposta["largura"] and posicao_botao_resposta1["botao1-y"] <= y <= posicao_botao_resposta1["botao1-y"] + tamanho_botao_resposta["altura"]:
            fase += 1
            respostas_jogador.append(1)
            mouse_pressionado = True

        if posicao_botao_resposta2["botao1-x"] <= x <= posicao_botao_resposta2["botao1-x"] + tamanho_botao_resposta["largura"] and posicao_botao_resposta2["botao1-y"] <= y <= posicao_botao_resposta2["botao1-y"] + tamanho_botao_resposta["altura"]:
            fase += 1
            respostas_jogador.append(2)
            mouse_pressionado = True

        if posicao_botao_resposta3["botao1-x"] <= x <= posicao_botao_resposta3["botao1-x"] + tamanho_botao_resposta["largura"] and posicao_botao_resposta3["botao1-y"] <= y <= posicao_botao_resposta3["botao1-y"] + tamanho_botao_resposta["altura"]:
            fase += 1
            respostas_jogador.append(3)
            mouse_pressionado = True

        if posicao_botao_resposta4["botao1-x"] <= x <= posicao_botao_resposta4["botao1-x"] + tamanho_botao_resposta["largura"] and posicao_botao_resposta4["botao1-y"] <= y <= posicao_botao_resposta4["botao1-y"] + tamanho_botao_resposta["altura"]:
            fase += 1
            respostas_jogador.append(4)
            mouse_pressionado = True


with open("textos.json", "r", encoding="utf-8") as arquivo:
    textos = json.load(arquivo)

pygame.init()
screenX = 360
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True

# botao iniciar
largura_botao = screenX / 2
altura_botao = screenY // 6
posicao_botao = (screenX // 2 - largura_botao // 2, screenY // 2 - altura_botao // 2)
texto_botao = "Iniciar Jogo"

#botoes de resposta
tamanho_botao_resposta = {"largura": 150, "altura": 50}
posicao_botao_resposta1 = {"botao1-x": 20, "botao1-y": 200}
posicao_botao_resposta2 = {"botao1-x": 190, "botao1-y": 200}
posicao_botao_resposta3 = {"botao1-x": 20, "botao1-y": 300}
posicao_botao_resposta4 = {"botao1-x": 190, "botao1-y": 300}
texto_botao_resposta1 = textos["respostas"]["quest01"]["resposta1"]
texto_botao_resposta2 = textos["respostas"]["quest01"]["resposta2"]
texto_botao_resposta3 = textos["respostas"]["quest01"]["resposta3"]
texto_botao_resposta4 = textos["respostas"]["quest01"]["resposta4"]


fonte = pygame.font.Font(None, 38)  # None usa a fonte padrão; o número é o tamanho
fonte_respostas = pygame.font.Font(None, 24)
texto_titulo = textos["telas"]["menu_principal"]
cor_texto = (255, 255, 255)  # Cor branca (R, G, B)

menu = True
fase = 0

respostas_jogador = []
respostas_corretas = [1,2,3,3,2,1,4,2,1,4]
resultado_calculado = False
resultado = 0
mouse_pressionado = False
fasefinal = False

while running:
    screen.fill("purple")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP: # variável de controle para a quantidade de cliques do mouse
            mouse_pressionado = False
    
    # selecionando fase
    if fase == 1:
        fase1()
    if fase == 2:
        fase2()
    if fase == 3:
        fase3()
    if fase == 4:
        fase4()
    if fase == 5:
        fase5()
    if fase == 6:
        fase6()
    if fase == 7:
        fase7()
    if fase == 8:
        fase8()
    if fase == 9:
        fase9()
    if fase == 10:
        fase10()
    if fase == 11:
        fasefinal = True
        gameover()
    #desenhando titulo e botao
    if menu:
        desenhar_botao_iniciar()
        superficie_texto = fonte.render(texto_titulo, True, cor_texto)
        screen.blit(superficie_texto, (20, 90))
    else:
        linhas = texto_titulo.split("\n") # a maldita quebra de linha
        y = 50
        for linha in linhas:
            superficie_texto = fonte.render(linha, True, cor_texto)
            screen.blit(superficie_texto, (20, y))
            y += fonte.get_height()
        if fasefinal == False:
            desenhar_botoes_respostas()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()