# Jeiel Lucas Dourado Cavalcante, aluno de Ciência da Computacao 2022.2 (1° semestre), matrícula 539039

from glob import glob
import turtle
import random
import time


velocidadeObjeto = 0
gasolina = 100
velocidadeImagem = 0
score = 0
colidir = False
mover_personagem = 0


#Criação da janela principal e adicionar formas dos personagens
janela = turtle.Screen()
janela.bgcolor('Lightgreen')
janela.setup(width=1100, height=900)
janela.title('Morte da tartaruga - Jogo de FUP')
janela.tracer(0)

janela.addshape('Tartaruga.gif')
janela.addshape('Coracao.gif')
janela.addshape('comida.gif')
janela.addshape('canudo.gif')
janela.addshape('background.gif')
janela.addshape('background2.gif')
janela.addshape('10bolhas.gif')
janela.addshape('9bolhas.gif')
janela.addshape('8bolhas.gif')
janela.addshape('7bolhas.gif')
janela.addshape('6bolhas.gif')
janela.addshape('5bolhas.gif')
janela.addshape('4bolhas.gif')
janela.addshape('3bolhas.gif')
janela.addshape('2bolhas.gif')
janela.addshape('1bolha.gif')
janela.addshape('rede.gif')


#Criação do cenário e personagens
imagem = turtle.Turtle()
imagem.penup()
imagem.speed(0)
imagem.shape('background.gif')
imagem.goto(0, 0)

imagem2 = turtle.Turtle()
imagem2.penup()
imagem2.speed(0)
imagem2.shape('background2.gif')
imagem2.goto(0, 1197)

personagem = turtle.Turtle()
personagem.speed(0)
personagem.shape('Tartaruga.gif')
personagem.penup()
personagem.goto(0, -390)

rede = turtle.Turtle()
rede.speed(0)
rede.penup()
rede.shape('rede.gif')
rede.goto(10, -400)
rede.hideturtle()

combustiveis = ['10bolhas.gif', '9bolhas.gif', '8bolhas.gif', '7bolhas.gif', '6bolhas.gif', '5bolhas.gif', '4bolhas.gif', '3bolhas.gif', '2bolhas.gif', '1bolha.gif', 'explodir.gif']
combustivel = turtle.Turtle()
combustivel.shape(combustiveis[0])
combustivel.penup()
combustivel.goto(450, 0)

obstaculo = turtle.Turtle()
obstaculo.speed(0)
obstaculo.penup()
obstaculo.shape('canudo.gif')
obstaculo.goto(random.randint(-120, 120), 500)

comida = turtle.Turtle()
comida.speed(0)
comida.penup()
comida.shape('comida.gif')
comida.goto(random.randint(-120, 120), 1200)

placar = turtle.Turtle()  # Cria placar do jogo
placar.penup()
placar.goto(-500, 380)
placar.write(f'Score:\n {score}', font=('Times', 22, 'bold'))
placar.hideturtle()

mensagem = turtle.Turtle()
mensagem.hideturtle()
mensagem.penup()
mensagem.goto(-170, 0)
mensagem.write('Aperte espaço para continuar', font=('Times', 23, 'bold'))


#Funções utilizadas
def principal():
    fuel()
    colisao_borda()
    colisao_comida()
    colisao_obstaculo()
    animacoes_do_jogo(imagem, imagem2)
    janela.update()
    janela.ontimer(principal, 1000//75)


def move_to_left():
    x = personagem.xcor()
    x -= mover_personagem
    personagem.setx(x)


def move_to_right():
    x = personagem.xcor()
    x += mover_personagem
    personagem.setx(x)


def colisao_obstaculo():
    global colidir
    px = personagem.xcor()
    py = personagem.ycor()
    ox = obstaculo.xcor()
    oy = obstaculo.ycor()
    distancia = ((px - ox) ** 2 + (py - oy) ** 2) ** 0.5
    if obstaculo.ycor() < -550:
        obstaculo.goto(random.randint(-120, 120), 550)
    if distancia < 50:
        stop()
        obstaculo.goto(random.randint(-120, 120), 550)
        rede.goto(personagem.xcor()+10, -400)
        rede.showturtle()
        colidir = True


def colisao_borda():
    global colidir
    xP2 = personagem.xcor()
    if xP2 >= 180 or xP2 <= -165:
        stop()
        personagem.setx(0)
        rede.goto(personagem.xcor()+10, -400)
        rede.showturtle()
        colidir = True


def colisao_comida():
    global score, gasolina
    px = personagem.xcor()
    py = personagem.ycor()
    cx = comida.xcor()
    cy = comida.ycor()
    d = ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5
    if d < 50:
        comida.goto(random.randint(-120, 120), random.randint(1100, 1300))
        score += 10
        placar.clear()
        placar.write(f'Score:\n {score}', font=('Times', 22, 'bold'))
        if gasolina + 4 >= 100:
            gasolina = 100
        else:
            gasolina += 4
    if comida.ycor() < -800: 
        comida.goto(random.randint(-120, 120), random.randint(1100, 1300))


def animacoes_do_jogo(imagem1, imagem2):
    global score, gasolina
    imagem1.sety(imagem1.ycor() - velocidadeImagem)
    imagem2.sety(imagem2.ycor() - velocidadeImagem)
    comida.sety(comida.ycor() - velocidadeObjeto)
    obstaculo.sety(obstaculo.ycor() - velocidadeObjeto)
    ox = obstaculo.xcor()
    oy = obstaculo.ycor()
    cx = comida.xcor()
    cy = comida.ycor()
    distancia = ((cx - ox) ** 2 + (cy - oy) ** 2) ** 0.5
    if imagem1.ycor() <= -1197:
        imagem1.sety(1197)
        score += 10
        placar.clear()
        placar.write(f'Score:\n {score}', font=('Times', 22, 'bold'))
        gasolina -= 3
    if imagem2.ycor() <= -1197:
        score += 10
        placar.clear()
        placar.write(f'Score:\n {score}', font=('Times', 22, 'bold'))
        imagem2.sety(1197)
        gasolina -= 3
    if gasolina <= 0:
        perder()
    if distancia <= 35:
        obstaculo.goto(random.randint(-120, 120), 500)


def stop():
    global velocidadeImagem, velocidadeObjeto, mover_personagem
    velocidadeObjeto = 0
    velocidadeImagem = 0
    mover_personagem = 0
    mensagem.write('Aperte espaço para continuar', font=('Times', 23, 'bold'))


def start_game():
    global velocidadeImagem, velocidadeObjeto, gasolina, colidir, mover_personagem
    velocidadeObjeto = 5
    velocidadeImagem = 7
    mover_personagem = 15
    if colidir == True:
        gasolina -= 5
        rede.hideturtle()
        colidir = False
    mensagem.clear()


def fuel():
    global gasolina
    if gasolina > 90:
        combustivel.shape(combustiveis[0])
    elif gasolina > 80:
        combustivel.shape(combustiveis[1])
    elif gasolina > 70:
        combustivel.shape(combustiveis[2])
    elif gasolina > 60:
        combustivel.shape(combustiveis[3])
    elif gasolina > 50:
        combustivel.shape(combustiveis[4])
    elif gasolina > 40:
        combustivel.shape(combustiveis[5])
    elif gasolina > 30:
        combustivel.shape(combustiveis[6])
    elif gasolina > 20:
        combustivel.shape(combustiveis[7])
    elif gasolina > 10:
        combustivel.shape(combustiveis[8])
    elif gasolina <= 10:
        combustivel.shape(combustiveis[9])
    

def perder():
    janela.bye()


#Leitura de teclas
janela.onkeypress(move_to_left, 'Left')
janela.onkeypress(move_to_right, 'Right')
janela.onkeypress(start_game, 'space')
janela.listen()

#Executando as primeiras funções
principal()


#Laço do janela
janela.mainloop()
