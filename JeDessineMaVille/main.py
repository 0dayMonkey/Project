import turtle as t
from random import randint
import math as m


def couleur_aleatoire():
  t.colormode(255)
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)


t.speed(500)
t.title("Je dessine ma ville")
t.setup(1080,900)

def sol(y):
  t.penup()
  t.setpos(0-(y/2),0)
  t.pendown()
  t.forward(y)
  t.penup()
  t.setpos(0-((y/2)),-1)
  t.pendown()
  t.fillcolor("grey")
  t.begin_fill()
  t.forward(y)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(y)
  t.right(90)
  t.forward(50)
  t.end_fill()
  t.backward(15)
  for i in range(round(y/100)):
    t.pendown()
    t.setheading(0)
    t.fillcolor("white")
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)
    t.forward(100)

# t.setpos(0,0)
    


def ciel(y):
  t.penup()
  t.setpos(0-(y/2),0)
  t.pendown()
  t.fillcolor("lightblue")
  t.begin_fill()
  t.setheading(0)
  t.left(90)
  t.forward(1000)
  t.right(90)
  t.forward(y)
  t.right(90)
  t.forward(1000)
  t.end_fill()


def mur(x, y, w, h):
  if w==h:
    raise ValueError("La largeur ne peut pas etre pareil que la longueur car nous voulons un rectangle")
  else:
    t.setheading(0)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.fillcolor(couleur_aleatoire())
    t.begin_fill()
    t.left(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.end_fill()
    t.penup()

      

    
def fenetre(x, y, w, h):
  t.setheading(0)
  t.penup()
  t.setpos(x+20,y+20)
  t.pendown()
  t.fillcolor("white")
  t.begin_fill()
  t.left(90)
  t.forward(20)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(20)
  t.end_fill()
  t.penup()

def toit(x, y, w, h):
  t.setheading(0)
  t.penup()
  a = randint(1,2)
  if a==1:
    t.setpos(x,y+h)
    t.pendown()
    t.fillcolor(couleur_aleatoire())
    t.begin_fill()
    t.left(45)
    t.forward(m.sqrt(2)/2*w)
    t.right(90)
    t.forward(m.sqrt(2)/2*w)
    t.end_fill()
    t.penup()
  else:
    t.setpos(x+w,y+h)
    t.fillcolor(couleur_aleatoire())
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.circle(w/2,180)
    t.end_fill()

def porte(x, y, w, h):
  t.setheading(0)
  t.penup()
  t.setpos(x+((w/3)*2.5),y)
  t.pendown()
  a = randint(1,2)
  if a == 1:
    t.fillcolor(couleur_aleatoire())
    t.begin_fill()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.backward(20)
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.penup()
  else:
    t.fillcolor(couleur_aleatoire())
    t.begin_fill()
    t.left(90)
    t.forward(30)
    t.circle(10,180)
    t.forward(30)
    t.end_fill()

def cercle_plein(rayon, couleur):
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()

def nuage(rayon, couleur="white"):
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.forward(rayon)
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.right(90)
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.right(90)
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.right(90)
    t.color(couleur)
    t.begin_fill()
    t.circle(rayon)
    t.end_fill()
    t.right(90)




def immeuble(x,y,w,h):
  e = 0
  print(x,y,w,h)
  t.pendown()
  mur(x,y,w,h)
  toit(x,y,w,h)
  ht = y
  if ht+35 < h:
    while ht+50 < h:
      fenetre(x,ht,w,h)
      ht += 30
      e += 1
  porte(x,y,w,h)
  if e > 1:
    t.penup()
    t.setpos(x,y+43)
    a = y+43
    for i in range(e-1):
      t.setheading(0)
      t.penup()
      t.setpos(x,a)
      t.pendown()
      t.forward(w)
      a += 30
      
  t.penup()
  t.setheading(0)
  t.setpos(0,0)


def ville(n=5):
  t.Screen().bgcolor("lightgreen")
  x=-100
  sol(n*500)
  ciel(n*500)
  xbis = 0-(n*500/2)
  ybis = 250
  for i in range(2):
    for i in range(n*5):
      t.penup()
      t.setpos(xbis,ybis)
      c = randint(1,2)
      if c == 1:
        nuage(randint(10,19),"white")
      else:
        nuage(randint(10,19),"lightgrey")
      xbis += randint(50,150)
    xbis = 0-(n*500/2)
    ybis -= 90
  for i in range(n):
    immeuble(x-(n*150)/2,y=0,w = randint(100,200),h=randint(60,200))
    x += randint(200,250)
    t.penup()
    t.setheading(0)
    t.forward(randint(190,350))
    t.pendown()

ville(5)