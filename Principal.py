# Jeiel Lucas Dourado Cavalcante, aluno de Ciência da Computacao 2022.2 (1° semestre)

import turtle
import random
import time

# Variaveis usadas
vidas = 3
velocidadeObjeto = 0.4
gasolina = 100
velocidadeImagem = 0.7
score = 0

# Abrir e configurar Janela
janela = turtle.Screen()
janela.bgcolor('Lightgreen')
janela.setup(width=1100, height=900)
janela.title('Morte da tartaruga - Jogo de FUP')
janela.tracer(0)  # Atualização de tela

# Adicionar estilos
janela.addshape('Tartaruga.gif')
janela.addshape('Coracao.gif')
janela.addshape('comida.gif')
janela.addshape('canudo.gif')
janela.addshape('background.gif')
janela.addshape('background2.gif')
janela.addshape('perder.gif')

# Definir os personagens
personagem = turtle.Turtle()  # Cria personagem principal
personagem.speed(0)
personagem.shape('Tartaruga.gif')
personagem.penup()
personagem.goto(0, -390)

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

combustivel = turtle.Turtle()
combustivel.penup()
combustivel.goto(420, 30)
combustivel.hideturtle()
combustivel.goto(450, 0)
combustivel.write(f'Fuel:\n {gasolina}', font=('Italic', 20, 'bold'))

obstaculo = turtle.Turtle()
obstaculo.speed(0)
obstaculo.penup()
obstaculo.shape('canudo.gif')
obstaculo.goto(random.randint(-120, 120), 350)

comida = turtle.Turtle()
comida.speed(0)
comida.penup()
comida.shape('comida.gif')
comida.goto(random.randint(-120, 120), 1200)

placar = turtle.Turtle()  # Cria placar do jogo
placar.penup()
placar.goto(-500, 380)
placar.write(0, font=('Times', 22, 'bold'))
placar.hideturtle()

mensagem = turtle.Turtle()
mensagem.hideturtle()
mensagem.penup()
mensagem.goto(-170, 0)


# Funções
def move_to_left():
    x = personagem.xcor()
    x -= 15
    personagem.setx(x)


def move_to_right():
    x = personagem.xcor()
    x += 15
    personagem.setx(x)


def colisao_obstaculo():
    global gasolina
    px = personagem.xcor()
    py = personagem.ycor()
    ox = obstaculo.xcor()
    oy = obstaculo.ycor()
    distancia = ((px - ox) ** 2 + (py - oy) ** 2) ** 0.5
    if obstaculo.ycor() < -440:
        obstaculo.goto(random.randint(-120, 120), 400)
    if distancia < 50:
        gasolina -= 3
        obstaculo.goto(random.randint(-120, 120), 400)
        stop()


def colisao_borda():
    global gasolina
    xP2 = personagem.xcor()
    if xP2 >= 180 or xP2 <= -165:
        gasolina -= 6
        stop()
        time.sleep(1)
        personagem.setx(0)


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
        placar.write(score, font=('Times', 22, 'bold'))
        if gasolina + 4 >= 100:
            gasolina = 100
            combustivel.clear()
            combustivel.write(f'Fuel:\n {gasolina}', font=('Italic', 20, 'bold'))
        else:
            gasolina += 4
    if comida.ycor() < -800: 
        comida.goto(random.randint(-120, 120), random.randint(1100, 1300))


def animacoes_do_jogo(a, b):
    global score, gasolina
    a.sety(a.ycor() - velocidadeImagem)
    b.sety(b.ycor() - velocidadeImagem)
    comida.sety(comida.ycor() - velocidadeObjeto)
    obstaculo.sety(obstaculo.ycor() - velocidadeObjeto)
    if a.ycor() <= -1197:
        a.sety(1197)
        score += 10
        placar.clear()
        placar.write(score, font=('Times', 22, 'bold'))
        gasolina -= 3
        combustivel.clear()
        combustivel.write(f'Fuel:\n {gasolina}', font=('Italic', 20, 'bold'))
    if b.ycor() <= -1197:
        score += 10
        placar.clear()
        placar.write(score, font=('Times', 22, 'bold'))
        b.sety(1197)
        gasolina -= 3
        combustivel.clear()
        combustivel.write(f'Fuel:\n {gasolina}', font=('Italic', 20, 'bold'))
    if gasolina <= 0:
        perder()


def stop():
    global velocidadeImagem, velocidadeObjeto
    velocidadeObjeto = 0
    velocidadeImagem = 0
    mensagem.write('Aperte espaço para continuar', font=('Times', 23, 'bold'))


def voltar_ao_jogo():
    global velocidadeImagem, velocidadeObjeto
    velocidadeObjeto = 0.4
    velocidadeImagem = 0.7
    mensagem.clear()


def perder():
    janela.clear()
    janela.bgpic('perder.gif')


# Leitura teclas do teclado
janela.listen()
janela.onkeypress(move_to_left, 'Left')
janela.onkeypress(move_to_right, 'Right')
janela.onkeypress(voltar_ao_jogo, 'space')

# Loop do Jogo
while True:
    colisao_obstaculo()
    colisao_borda()
    colisao_comida()
    animacoes_do_jogo(imagem, imagem2)
    janela.update()
