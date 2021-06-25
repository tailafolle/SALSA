import pygame
import random
import time
pygame.init()  # função para iniciar o pygame
icone = pygame.image.load("assets/livroIcon.png")
pygame.display.set_caption("Desvie das bebidas Alcólicas")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/sala.png")
cria = pygame.image.load("assets/cria.png")
cria.set_colorkey((255,255,255))
escalacria = pygame.transform.scale(cria,(200,180))
garrafa = pygame.image.load("assets/garrafa.png")
garrafa.set_colorkey((255,255,255))
escalagarrafa = pygame.transform.scale(garrafa,(180,150))
# [ini] cores em RGB (https://www.rapidtables.com/web/color/RGB_Color.html)
preto = (0, 0, 0)
branco = (255, 255, 255)
# [fim] cores
def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
    message_display("Você Morreu com "+str(desvios)+" desvios")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))
    
def jogo():

    criaPosicaoX = largura * 0.45
    criaPosicaoY = altura * 0.7
    criaLargura = 120
    movimentoX = 0
    garrafaPosicaoX = largura * 0.45
    garrafaPosicaoY = -220
    garrafaLargura = 50
    garrafaAltura = 125
    garrafaVelocidade = 5

    desvios = 0

    while True:
        # [ini] bloco de comando para verificar interação do usuário:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()  # break para executar o fim do código
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        # [fim] bloco de comando para verificar interação do usuário:
        display.fill(branco)  # função para mudar a cor de fundo da tela
        display.blit(fundo, (0, 0))  # inserir imagem da tela
        criaPosicaoX = criaPosicaoX + movimentoX
        if criaPosicaoX < 0:
            criaPosicaoX = 0
        elif criaPosicaoX > 680:
            criaPosicaoX = 680
        # inserir imagem da tela
        display.blit(escalacria, (criaPosicaoX, criaPosicaoY))
        display.blit(escalagarrafa, (garrafaPosicaoX, garrafaPosicaoY))
        garrafaPosicaoY = garrafaPosicaoY + garrafaVelocidade
        # [ini] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        if garrafaPosicaoY > altura:
            garrafaPosicaoY = -80
            garrafaVelocidade += 1
            garrafaPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1
        # [fim] quando ele ultrapassa a barreira (fundo), começa em um lugar novo
        escrevendoPlacar(desvios)
        # [ini]análise de colisão:
        if criaPosicaoY < garrafaPosicaoY + garrafaAltura:
            if criaPosicaoX < garrafaPosicaoX and criaPosicaoX+criaLargura > garrafaPosicaoX or garrafaPosicaoX+garrafaLargura > criaPosicaoX and garrafaPosicaoX+garrafaLargura < criaPosicaoX+criaLargura:
                dead(desvios)
        # [fim]análise de colisão:
        pygame.display.update()
        fps.tick(60)
jogo()
