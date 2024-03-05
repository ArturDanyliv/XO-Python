# https://www.youtube.com/watch?v=zwh4-lb-t5M
import turtle 
import random
import time

window  = turtle.Screen()

BOK = 600
X =300
Y = 300

window.setup(BOK,BOK)
window.title("Kółko i krzyzyk") 
window.bgcolor('black')

xo = turtle.Turtle()
xo.color("white")
xo.pensize(7)
xo.speed(0)
xo.hideturtle()

tablica = [[None,None,None],
            [None,None,None],
            [None,None,None]]

 # tablica [wiersz] [kolumna]

kolej = random.choice(['x','o'])

#siatka

ODSTEP = int(BOK/3)

for a in [1,2]:
    xo.penup()
    xo.goto(X + a * ODSTEP,Y)
    xo.pendown()
    xo.goto(X + a*ODSTEP,-Y)

    xo.penup()
    xo.goto(X,Y - a*ODSTEP )
    xo.pendown()
    xo.goto(-X,Y -a*ODSTEP)


def sprawdz():
    
    # po skosie
    if tablica[0][0] == tablica [1][1] == tablica[2][2]:return tablica[2][2]
    if tablica[0][2] == tablica [1][1] == tablica[2][0]:return tablica[2][0]

    # w wierszu
    for w in range(2):
        if tablica[w][0] == tablica[w][1] == tablica[w][2]:return tablica [w][2]

    # w kolumnie 
    for k in range(2):
        if tablica[0][k] == tablica[1][k] == tablica[2][k]:return tablica [2][k]


def click(x,y):
    
    global kolej

    # ktore pole
    kolumna = 0
    wiersz=0

    if x < X + ODSTEP : kolumna = 0
    elif x > X + 2*ODSTEP : kolumna = 2
    else: kolumna =1

    if y < Y -2 * ODSTEP: wiersz=2
    elif y > Y -ODSTEP: wiersz=0
    else: wiersz = 1

    # pole jest puste
    if tablica[wiersz][kolumna] != None : return


    #narywsowac 
    
    kolumna_srodek = (kolumna * ODSTEP / 2) - BOK / 2
    wiersz_srodek = (-wiersz*ODSTEP - ODSTEP / 2) + BOK / 2

    xo.penup()
    xo.geto(kolumna_srodek -25,wiersz_srodek-25)
    if kolej == 'x' : xo.write('X',font = ('Arial',50) )
    else:xo.write('O',font=('Arial',50))
    

    #dodac do tablicy

    tablica[wiersz][kolumna] = kolej

    if kolej == 'o': kolej = 'x'
    else: kolej = 'o'  
    
    #sprawdz 

    if sprawdz() !=None:
        xo.penup()
        xo.goto(-150,0)
        time.sleep(1)
        xo.clear()
        xo.write("Wygralu"+ sprawdz(),font=("Arial",50))

window.onckick(click)

window.listen()
window.mainloop()