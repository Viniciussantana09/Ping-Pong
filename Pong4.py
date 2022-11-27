# ----------------------------------------------------------------------IMPORTAR BIBLIOTECAS-------------------------------------------------------------------------------------------
import turtle  # importação da biblioteca turtle
from turtle import *  # importação da biblioteca turtle
import random  # importação da biblioteca ramdom

# -----------------------------------------------------------------------VARIAVEIS-----------------------------------------------------------------------------------------------
posicao = 0  # posição da bola
d = 0  # numero aleátorio da posição
i = 0  # variavel do loop
speed = 1  # variavel da velocidade da bola
ponto_direita = 0
ponto_esquerda = 0
# -----------------------------------------------------------------------CONFIGURAR A TELA--------------------------------------------------------------------------------------------------------
tela = turtle.Screen()  # cria a tela
tela.screensize(600, 400)  # definir tamanho da tela
tela.bgcolor("black")  # define a cor da tela

# ----------------------------------------------------------------------CRIANDO AS RAQUETES-----------------------------------------------------------------------------------------
direita = turtle.Turtle()  # criando a raquete da direita
direita.penup()  # tirando sua caneta
direita.speed(0)  # define a velocidade da criação da raquete
direita.right(90)  # definindo a posição
direita.setpos(650, 0)  # definindo a posição
direita.shape('square')  # definindo forma
direita.color("blue")  # definindo cor


esquerda = turtle.Turtle()  # criando a raquete da esquerda
esquerda.penup()  # tirando sua caneta
esquerda.speed(0)  # define a velocidade da criação da raquete
esquerda.right(90)  # definindo a posição
esquerda.setpos(-650, 0)  # definindo a posição
esquerda.shape('square')  # definindo forma
esquerda.color("red")  # definindo cor


# -------------------------------------------------------------------CRIANDO O MOVIMENTO DAS RAQUETES-------------------------------------------------------------------------------------------
def up():  # função para mover a raquete
    direita.setheading(90)  # muda a direção
    direita.forward(100)  # faz a raquete se mover


def down():  # função para mover a raquete
    direita.setheading(270)  # muda a direção
    direita.forward(100)  # faz a raquete se mover


def cima():  # função para mover a raquete
    esquerda.setheading(90)  # muda a direção
    esquerda.forward(100)  # faz a raquete se mover


def baixo():  # função para mover a raquete
    esquerda.setheading(270)  # muda a direção
    esquerda.forward(100)  # faz a raquete se mover


listen()  # define o foco na tela da tartaruga para capturar eventos
onkey(up, 'Up')  # chama a função up
onkey(down, 'Down')  # chama a função dowm
onkey(cima, 'w')  # chama a função cima
onkey(baixo, 's')  # chama a função baixo
onkey(cima, 'W')  # chama a função cima
onkey(baixo, 'S')  # chama a função baixo

# ----------------------------------------------------------------------CRIAR A BOLA DO JOGO---------------------------------------------------------------------------------------------------------
bola = turtle.Turtle()  # cria a bola
bola.shape("square")  # define a forma da bola
bola.color('white')  # definindo a cor da bola
bola.penup()  # tirar a caneta da bola
bola.speed(1)  # definir velocidade
bola.setpos(0, 0)  # define a posição inicial da bola

# ---------------------------------------------------------------------FUNÇÕES-----------------------------------------------------------------------------------------------------


def decisao():  # função para verificar se a raquete e a bola estão na mesma posição
    global bolay  # variavel que guarda a posição da bola no eixo y
    bolay = bola.ycor()  # recebe a posição da bola
    global direitay  # variavel que guarda a posição da raquete no eixo y
    direitay = direita.ycor()  # recebe a posição da raquete da direita
    global esquerday  # variavel que guarda a posição da raquete no eixo y
    esquerday = esquerda.ycor()  # recebe a posição da raquete da esquerda


def velocidade():  # função para aumentar a velocidade da bola sempre que bater em uma lateral ou raquete
    global speed  # varaivel velocidade da bola
    if speed < 2:  # verifica se a velocidade está abaixo de 2
        speed = speed + 0.05  # incrementa a velocidade da bola
        bola.speed(speed)  # aplica a nova velocidade
    else:
        bola.speed(2)  # aplica a velocidade 2


def pontodireita():  # função para mostrar os pontos da direita
    global ponto_direita
    ponto_direita = ponto_direita + 1  # incrementa mais um ponto para a direita
    print("Azul: " + str(ponto_direita))  # mostra na tela


def pontoesquerda():  # função para mostrar os pontos da esquerda
    global ponto_esquerda
    global ponto_direita
    ponto_esquerda = ponto_esquerda + 1  # incrementa mais um ponto para a esquerda
    ponto_direita = ponto_direita - 1
    print("Vermelho: " + str(ponto_esquerda))  # mostra na tela
# ---------------------------------------------------------------------CRIANDO O MOVIMENTO------------------------------------------------------------------------------------------------------------
while i == 0:
    pontod = turtle.Turtle()
    if ponto_direita == 0:
        placardireita = ["0.gif"]
    if ponto_direita == 1:
        placardireita = ["1.gif"]
    if ponto_direita == 2:
        placardireita = ["2.gif"]
    if ponto_direita == 3:
        placardireita = ["3.gif"]
    if ponto_direita == 4:
        placardireita = ["4.gif"]
    if ponto_direita == 5:
        placardireita = ["5.gif"]
    pdireita = [600, 300]
    pontod.speed(1000)
    pontod.penup()
    for numerodireita, posi in zip(placardireita, pdireita):
        turtle.register_shape(numerodireita)
        pontod.shape(numerodireita)
        pontod.setpos(pdireita)
        pontod.stamp()

    pontoe = turtle.Turtle()
    if ponto_esquerda == 0:
        placaresquerda = ["0esquerda.gif"]
    if ponto_esquerda == 1:
        placaresquerda = ["1esquerda.gif"]
    if ponto_esquerda == 2:
        placaresquerda = ["2esquerda.gif"]
    if ponto_esquerda == 3:
        placaresquerda = ["3esquerda.gif"]
    if ponto_esquerda == 4:
        placaresquerda = ["4esquerda.gif"]
    if ponto_esquerda == 5:
        placaresquerda = ["5esquerda.gif"]
    pesquerda = [-600, 300]
    pontoe.speed(1000)
    pontoe.penup()
    for numeroesquerda, posi in zip(placaresquerda, pesquerda):
        turtle.register_shape(numeroesquerda)
        pontoe.shape(numeroesquerda)
        pontoe.setpos(pesquerda)
        pontoe.stamp()
        
    bola.speed(1)    
    bola.setpos(650, d)#movimento da bola para a direita
    posicao = 650 #grava a ultima posição da bola
    decisao()
    if bolay == direitay: # verifica se a posição da raquete e da bola são iguais                        
        move = random.randint(1,2)

        if move == 1:#move para cima
            d = random.randrange(-400, 400, 100)
            bola.setpos(d, 400)
            posicao = 650
            velocidade()

            if posicao == 650:                
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(-650, d)#move a bola para a direita
                posicao = 650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
            else:
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(650, d)#move a bola para a esquerda
                posicao = -650 #grava a ultima posição da bola                        
                velocidade()
                decisao()

        if move == 2:#move para baixo
            d = random.randrange(-400, 400, 100)#numero aleatorio da posição do eixo x
            bola.setpos(d, -400) #move a bola para baixo
            posicao = 650 #grava a ultima posição da bola
            velocidade()

            if posicao == 650:                
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(-650, d)#move a bola para a direita
                posicao = 650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
            else:
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(650, d)#move a bola para a esquerda
                posicao = -650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
    else:
        bola.speed(1000)
        bola.home()
        pontoesquerda()
        if ponto_direita >= 6 or ponto_esquerda >= 6:
            i = i + 1

    if bolay == esquerday: # verifica se a posição da raquete e da bola são iguais                        
        move = random.randint(1,2)

        if move == 1:#move para cima
            d = random.randrange(-400, 400, 100)
            bola.setpos(d, 400)
            posicao = -650
            velocidade()

            if posicao == -650:                
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(650, d)#move a bola para a direita
                posicao = -650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
            else:
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(-650, d)#move a bola para a esquerda
                posicao = 650 #grava a ultima posição da bola                        
                velocidade()
                decisao()

        if move == 2:#move para baixo
            d = random.randrange(-400, 400, 100)
            bola.setpos(d, -400)
            posicao = -650
            velocidade()

            if posicao == -650:                
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(650, d)#move a bola para a direita
                posicao = -650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
            else:
                d = random.randrange(-400, 400, 100)#numero aletorio da posição do eixo y
                bola.setpos(-650, d)#move a bola para a esquerda
                posicao = 650 #grava a ultima posição da bola                        
                velocidade()
                decisao()
    else:
        bola.speed(1000)
        bola.home()
        pontodireita()
        if ponto_direita >= 6 or ponto_esquerda >= 6:
            i = i + 1
