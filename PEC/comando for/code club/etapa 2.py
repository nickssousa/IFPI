from turtle import *

#uma função para desenhar uma estrela de um tamanho especifíco
def drawStar(starSize, starColor):
    color(starColor)
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(starSize)
    end_fill()
    penup()

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#use a função para desenhar estrelas de tamanhos  diferentes!
drawStar(50, "Red")
forward(100)
drawStar(30, "White")
left(120)
forward(150)
drawStar(70,"Green")

hideturtle()
done()
