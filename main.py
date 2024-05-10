# Configurações iníciais
import pygame
import random

# Inicializar o pygame
pygame.init()
# Criar o nome da janela 
pygame.display.set_caption("Snake")
# Atribuindo os valores da screen da tela
largura,altura = 600,400
# Passando as informações da screen em forma de tupla é criando uma tela
tela = pygame.display.set_mode((largura,altura))
# Controle do tempo carregar as informações sem travamentos
tempo = pygame.time.Clock()


# Definindo as cores  em um padrão RGB

# Tela
preta = (0,0,0)
# Cobra
branca = (255,255,255)
# Pontuação
vermelho = (255,0,0)
# Comida
verde = (0,255,0)
# Pontuação também
roxo = (255,0,255)

# Parâmetros da snake 
tamanho_quadrado = 20
# Velocidade de movimentod a snake após o início do game 
velocidade_cobra = 15

# Gerando as posições do eixo x e eixo y da comida.

def gerar_comida():
    # Posições da comida, nós, assegurando para que a comida não passe da janela definida subtraindo com um quadrado

    comida_x = round(random.randrange(0,largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0,altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x,comida_y

def desenhar_comida(tamanho,comida_x,comida_y):
    # Desenhar o retângulo da comida
    pygame.draw.rect(tela,verde,[comida_x,comida_y, tamanho,tamanho])


def desenhar_cobra(tamanho,pixels):
    for pixel in pixels:
        # Desenhando o retângulo da cobra 
        pygame.draw.rect(tela,branca,[pixel[0],pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao) :
    fonte = pygame.font.SysFont("CageWorld",30)
    # True -> para o desenho do texto fique mais bonito
    texto = fonte.render(f"Score: {pontuacao}",True,roxo)
    # Inserir o texto na dela
    tela.blit(texto,[1,1])

def selecionar_velocidade(tecla) :
    if tecla == pygame.K_DOWN:
        # Seta para baixo eixo y +
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        # Seta para cima eixo y -
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        # Seta para direita eixo x +
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        # Seta para esquerda eixo x -
        velocidade_x =  - tamanho_quadrado
        velocidade_y = 0


    return velocidade_x, velocidade_y

def rodar_jogo() :
    # Incialização
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    # A cobra começa parada 
    velocidade_x = 0
    # A cobra começa parada 
    velocidade_y = 0

    # Tamanho inícial da snake
    tamanho_cobra = 1
    # O valor das posições dos quadrados que são referênte a pixels
    pixels = []


    comida_x, comida_y = gerar_comida()

    # Criar um loop infinito
    while not fim_jogo:

        # Criando a tela é preenchendo com uma cor
        tela.fill(preta)

        # Cada que o usuário clica no mouse, teclado é passando para essa função é iramos percorrer esse  evento para variável 'evento'.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x,velocidade_y = selecionar_velocidade(evento.key)

        

        # Desenhar a comida 
        desenhar_comida(tamanho_quadrado,comida_x,comida_y)

        # Atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True


        # Atualizar a posição da cobra 
        x += velocidade_x
        y += velocidade_y

        # Desenhar a snake
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
            # Deletar o primeiro pixel é acrescentar um nobo pixel 
            pixels.pop(0)

        #  Usando slice para sempre desconsiderar o ultimo quadrado da snake 
        for pixel in pixels[:-1]:
           #print("debugging:",pixel)
            # x,y é o pixel que a cobra está,caso bater nela mesmo irá encerrar o jogo 
            if pixel == [x,y]:
                fim_jogo = True
        
        # Desenhar o retângulo da snake
        desenhar_cobra(tamanho_quadrado,pixels)

        # Desenhar a pontuação do jogo
        desenhar_pontuacao(tamanho_cobra - 1)


        # Atualizaçaõ da tela do jogo 
        pygame.display.update()

        # Criar uma nova comida  caso a snake tenha comido a comida anterior 
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x,comida_y = gerar_comida()


        tempo.tick(velocidade_cobra)


rodar_jogo()