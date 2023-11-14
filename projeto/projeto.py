import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

PRETO = (0, 0, 0)
AZUL = (0, 191, 255)

ranking = []

fonte1 = pygame.font.SysFont("arial", 32, True, True)
fonte2 = pygame.font.SysFont("arial", 50, True, False)

largura = 1100
altura = 600

fps = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

mahina_frente = pygame.image.load(os.path.join(diretorio_imagens, 'mahina.png')).convert_alpha()
mahina_frente = pygame.transform.scale(mahina_frente, (32 * 6, 32 * 6))
koa_frente = pygame.image.load(os.path.join(diretorio_imagens, 'koa.png')).convert_alpha()
koa_frente = pygame.transform.scale(koa_frente, (32 * 6, 32 * 6))
areia = pygame.image.load(os.path.join(diretorio_imagens, 'areia.png.png')).convert_alpha()
agua = pygame.image.load(os.path.join(diretorio_imagens, 'agua.png')).convert_alpha()
montanha = pygame.image.load(os.path.join(diretorio_imagens, 'montanha.png')).convert_alpha()
nuvem = pygame.image.load(os.path.join(diretorio_imagens, 'nuvem.png')).convert_alpha()
botao = pygame.image.load(os.path.join(diretorio_imagens, 'botao.png')).convert_alpha()
botao = pygame.transform.scale(botao, (56 * 4, 14 * 4))
toledo = pygame.image.load(os.path.join(diretorio_imagens, 'pai.png')).convert_alpha()
toledo = pygame.transform.scale(toledo, (22 * 6, 4 * 6))
mulher = pygame.image.load(os.path.join(diretorio_imagens, 'mae.png')).convert_alpha()
mulher = pygame.transform.scale(mulher, (22 * 6, 4 * 6))
cachorro = pygame.image.load(os.path.join(diretorio_imagens, 'cachorro.png')).convert_alpha()
cachorro = pygame.transform.scale(cachorro, (22 * 6, 4 * 6))
titulo = pygame.image.load(os.path.join(diretorio_imagens, 'titulo.png')).convert_alpha()
titulo = pygame.transform.scale(titulo, (150 * 3.5, 100 * 3.5))
sprite_sheet1 = pygame.image.load(os.path.join(diretorio_imagens, 'koa_andando.png')).convert_alpha()
sprite_sheet2 = pygame.image.load(os.path.join(diretorio_imagens, 'tsunami_movimento.png')).convert_alpha()
sprite_sheet3 = pygame.image.load(os.path.join(diretorio_imagens, 'mahina_andando.png')).convert_alpha()
sprite_sheet0 = pygame.image.load(os.path.join(diretorio_imagens, 'koa_andando.png')).convert_alpha()


class Personagem(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.sprites = []
        for i in range(20):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.x = 490
        self.y = 423
        self.rect.topleft = self.x, self.y
        self.andando = False
        self.andando_direita = False
        self.andando_esquerda = False
        self.pulando = False
        self.pulo_altura = 25
        self.pulo_contagem = 0
        self.no_ar = False
        self.vivo = True
        self.pontos = 0

    def update(self):
        if tsunami.x == 450 and personagem.y < 290 and self.vivo:
            self.pontos += 10

        if self.y > 423:
            self.y = 423
            self.speed_y = 0
            self.no_ar = False

        if self. y < 420:
            self.no_ar = True

        if self.pulando:
            self.speed_y = -5
            self.pulo_contagem += 1

            if not self.andando:
                self.index_lista = 0

            if self.pulo_contagem > self.pulo_altura:
                self.pulando = False
                self.pulo_contagem = 0

        if self.index_lista > 3 and not self.andando:
            self.index_lista = 0

        if self.index_lista > 11 and self.andando_direita:
            self.index_lista = 4
            self.speed_x = 3

        elif self.index_lista > 19 and self.andando_esquerda:
            self.index_lista = 12
            self.speed_x = -3

        if telas.morto:
            if len(ranking) == 5:
                if self.pontos > min(ranking):
                    ranking.remove(min(ranking))
                    ranking.append(self.pontos)
            else:
                ranking.append(self.pontos)

        self.y += self.speed_y
        self.speed_y += 0.2
        self.index_lista += 0.12
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.scale(self.image, (32 * 3.5, 32 * 3.5))


class Tsunami(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for i in range(4):
            img = sprite_sheet2.subsurface((i * 32, 0), (32, 32))
            self.sprites.append(img)

        self.index_lista = 0
        self.image = self.sprites[self.index_lista]
        self.image = pygame.transform.scale(self.image, (32 * 6, 32 * 6))
        self.rect = self.image.get_rect()
        self.speed_x = 5
        self.speed_y = 0
        self.x = 1500
        self.y = 360
        self.nivel = 0
        self.rect.topleft = self.x, self.y

    def update(self):
        if self.index_lista > 3:
            self.index_lista = 0
        if self.x <= -200:
            self.x = 1500
        if self.x == 450 and personagem.y > 290:
            personagem.vivo = False
            telas.morto = True

        if personagem.pontos > 100 and self.nivel == 0:
            self.speed_x = 6
            self.nivel += 1
        elif personagem.pontos > 200 and self.nivel == 1:
            self.speed_x = 10
            self.nivel += 1
        elif personagem.pontos > 300 and self.nivel == 2:
            self.speed_x = 12
            self.nivel += 1

        self.index_lista += 0.12
        self.image = self.sprites[int(self.index_lista)]
        self.image = pygame.transform.scale(self.image, (32 * 6, 32 * 6))


class Botao:
    def __init__(self, x, y, texto):
        self.retangulo = pygame.Rect(x, y, botao.get_width(), botao.get_height())
        self.rect = botao.get_rect()
        self.x = x
        self.y = y
        self.texto = texto
        self.fonte = pygame.font.SysFont("arial", 32, True, True)
        self.rect.topleft = self.x, self.y
        self.renderizar_texto()

    def renderizar_texto(self):
        self.texto_imagem = self.fonte.render(self.texto, True, (PRETO))
        self.texto_rect = self.texto_imagem.get_rect(center=self.rect.center)

    def desenhar(self, tela):
        tela.blit(botao, self.rect.topleft)
        tela.blit(self.texto_imagem, self.texto_rect)

    def update(self):
        if event.type == pygame.MOUSEBUTTONDOWN and telas.menu and personagem.vivo and event.button == 1:
            if self.retangulo.collidepoint(pygame.mouse.get_pos()):

                if self.texto == 'jogar':
                    telas.jogar = False
                    telas.menu = False
                    telas.ranking = False
                    telas.morto = False
                    telas.selecao = True

                if self.texto == 'ranking':
                    telas.morto = False
                    telas.menu = False
                    telas.jogar = False
                    telas.selecao = False
                    telas.ranking = True

        elif event.type == pygame.MOUSEBUTTONDOWN and telas.morto and event.button == 1:
            if self.retangulo.collidepoint(pygame.mouse.get_pos()):

                if self.texto == 'menu':
                    telas.morto = False
                    telas.ranking = False
                    telas.jogar = False
                    telas.selecao = False
                    telas.menu = True

                if self.texto == 'reiniciar':
                    personagem.vivo = True
                    telas.jogar = True
                    telas.menu = False
                    telas.morto = False
                    telas.selecao = False
                    telas.ranking = False

        elif event.type == pygame.MOUSEBUTTONDOWN and ranking and event.button == 1:
            if self.retangulo.collidepoint(pygame.mouse.get_pos()):
                if self.texto == 'voltar':
                    personagem.vivo = True
                    telas.jogar = False
                    telas.morto = False
                    telas.ranking = False
                    telas.menu = True


class BotaoPersonagem:
    def __init__(self, x, y, imagem, sprite_sheet):
        self.imagem = imagem
        self.retangulo = pygame.Rect(x, y, imagem.get_width(), imagem.get_height())
        self.rect = imagem.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
        self.sprite_sheet = sprite_sheet
        self.jogador = 'a'

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)

    def update(self):
        if event.type == pygame.MOUSEBUTTONDOWN and telas.selecao and event.button == 1:
            if self.retangulo.collidepoint(pygame.mouse.get_pos()):
                self.jogador = self.imagem
                personagem.vivo = True


class Telas:
    def __init__(self):
        self.menu = False
        self.ranking = False
        self.selecao = False
        self.jogar = False
        self.morto = False


class Coletavel:
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.retangulo = pygame.Rect(x, y, imagem.get_width(), imagem.get_height())
        self.rect = imagem.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y

    def update(self):
        self.x -= personagem.speed_x // 2
        self.rect.topleft = self.x, self.y
        if personagem.x >= self.x and personagem.y >= 410:
            self.x += 100000
            self.rect.topleft = self.x, self.y
            personagem.pontos += 100

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)


tsunami_animacao = pygame.sprite.Group()
tsunami = Tsunami()
tsunami_animacao.add(tsunami)

mae = Coletavel(3000, 500, mulher)
pai = Coletavel(6000, 500, toledo)
cao = Coletavel(10000, 500, cachorro)

personagem_animacao = pygame.sprite.Group()
personagem = Personagem(sprite_sheet1)

x = -1000
y = -300

botao1 = Botao(425, 330, 'reiniciar')
botao2 = Botao(425, 428, 'menu')
botao3 = Botao(425, 330, 'jogar')
botao4 = Botao(425, 428, 'ranking')
botao5 = BotaoPersonagem(350, 300, koa_frente, sprite_sheet1)
botao6 = BotaoPersonagem(550, 300, mahina_frente, sprite_sheet3)
botao7 = Botao(425, 428, 'voltar')
telas = Telas()
telas.menu = True

while True:

    areia = pygame.transform.scale(areia, (550 * 8, 300 * 3))
    agua = pygame.transform.scale(agua, (550 * 6, 300 * 2))
    nuvem = pygame.transform.scale(nuvem, (550 * 3, 300 * 2))
    montanha = pygame.transform.scale(montanha, (550 * 6, 300 * 2))

    if telas.menu and personagem.vivo:
        tela.fill(AZUL)
        tela.blit(titulo, (275, 0))
        botao3.desenhar(tela)
        botao4.desenhar(tela)

    if telas.selecao and personagem.vivo:
        tela.fill(AZUL)
        botao5.desenhar(tela)
        botao6.desenhar(tela)
        mensagem = "escolha seu personagem"
        texto1 = fonte1.render(mensagem, False, PRETO)
        tela.blit(texto1, (360, 150))
        pygame.display.flip()

        if botao6.jogador == mahina_frente:
            personagem_animacao.remove(personagem)
            personagem = Personagem(sprite_sheet3)
            personagem_animacao.add(personagem)
            telas.jogar = True
            telas.selecao = False
            pygame.display.flip()

        elif botao5.jogador == koa_frente:
            personagem_animacao.remove(personagem)
            personagem = Personagem(sprite_sheet1)
            personagem_animacao.add(personagem)
            telas.jogar = True
            telas.selecao = False
            pygame.display.flip()

    if telas.ranking:
        tela.fill(AZUL)
        i = 1
        y = 50
        for x in ranking:
            mensagem = "{}o lugar - {}".format(i, x)
            texto = fonte2.render(mensagem, False, PRETO)
            i += 1
            tela.blit(texto, (300, y))
            y += 50
        botao7.desenhar(tela)
        pygame.display.flip()

    if personagem.vivo and telas.jogar:
        tela.fill(AZUL)
        tela.blit(nuvem, (x * 0.5, -200))
        tela.blit(montanha, (x * 0.68, -120))
        tela.blit(agua, (x * 0.8, -80))
        tela.blit(areia, (x, y))
        mae.desenhar(tela)
        pai.desenhar(tela)
        cao.desenhar(tela)
        mensagem1 = " " + str(personagem.pontos) + " "
        texto1 = fonte2.render(mensagem1, False, PRETO)
        tela.blit(texto1, (50, 30))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if personagem.vivo and telas.jogar:
            if x < -2000:
                x = -1000

            if x > -100:
                x = -1000

            if event.type == pygame.KEYDOWN:
                personagem.andando = True

                if event.key == pygame.K_d:
                    personagem.speed_x = 3
                    personagem.index_lista = 4
                    personagem.andando_direita = True
                    personagem.andando_esquerda = False

                elif event.key == pygame.K_a:
                    personagem.speed_x = -3
                    personagem.index_lista = 12
                    personagem.andando_esquerda = True
                    personagem.andando_direita = False

                if event.key == pygame.K_SPACE and not personagem.no_ar:
                    personagem.no_ar = True
                    if not personagem.pulando:
                        personagem.pulando = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d and not personagem.pulando:
                    personagem.speed_x = 0
                    personagem.andando_direita = False
                    personagem.andando = False

                if event.key == pygame.K_a and not personagem.pulando:
                    personagem.speed_x = 0
                    personagem.andando_esquerda = False
                    personagem.andando = False

        if telas.morto:
            tsunami.x = 1500
            tela.fill(AZUL)
            mensagem3 = "Você se afogou!"
            texto3 = fonte2.render(mensagem3, False, PRETO)
            tela.blit(texto3, (350, 150))
            botao1.desenhar(tela)
            botao2.desenhar(tela)
            telas.jogar = False
            pygame.display.flip()

    if personagem.vivo and telas.jogar:
        tsunami.update()
        personagem_animacao.update()
        x -= personagem.speed_x
        personagem.rect.topleft = personagem.x, personagem.y
        personagem_animacao.draw(tela)
        tsunami_animacao.draw(tela)
        tsunami_animacao.update()
        tsunami.x -= tsunami.speed_x
        tsunami.rect.topleft = tsunami.x, tsunami.y
        mae.update()
        pai.update()
        cao.update()
        pygame.display.flip()

    botao1.update()
    botao2.update()
    botao3.update()
    botao4.update()
    botao5.update()
    botao6.update()
    botao7.update()

    fps.tick(60)
    pygame.display.flip()