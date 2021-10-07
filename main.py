import turtle
import math
import random

# Layar
wn = turtle.Screen()
wn.bgcolor("Black")
wn.bgpic(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\bckground.gif")
wn.title("Space Invader")
wn.tracer(0)

# Custom Shape
wn.register_shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\plane.gif")
wn.register_shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\invader.gif")
wn.register_shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\bullet.gif")

# Batas Layar
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.setpos(-250, -250)
pen.pendown()
pen.pensize(2)
pen.pencolor("white")
for sisi in range(4) :
    pen.forward(500)
    pen.left(90)

# Pemain
pemain = turtle.Turtle()
pemain.speed(0)
pemain.shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\plane.gif")
pemain.color("red")
pemain.penup()
pemain.setpos(0, - 230)
pemain.setheading(90)
pemain.kecepatan = 0

# Peluru
peluru = turtle.Turtle()
peluru.speed(0)
peluru.color("yellow")
peluru.shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\bullet.gif")
peluru.penup()
peluru.setheading(90)
peluru.shapesize(0.5, 0.5)
peluru.kecepatan = 4
peluru.hideturtle()

# Keadaan peluru
# Siap - Dalam posisi hide
# Menembak - Dalam posisi terlihat
keadaanpeluru = "siap"

# Musuh
musuhs = []
banyak_musuh = 30
start_x = -205
start_y = 220
musuh_dalam_garis = 0

for _ in range(banyak_musuh) :
    musuh = turtle.Turtle()
    musuh.speed(0)
    musuh.shape(r"D:\Kuliah\Coding\Python\Python Tutorial\00\src\Advance\turtle\Space Invader\res\invader.gif")
    musuh.color("Blue")
    musuh.penup()
    musuh.kecepatan = 0.3
    musuhs.append(musuh)

    x = start_x + (45 * musuh_dalam_garis )
    y = start_y
    musuh.setposition(x, y)
    musuh_dalam_garis += 1

    if musuh_dalam_garis == 10 :
        musuh_dalam_garis = 0
        start_y -= 45

# Skor
skor = 0

pen_skor = turtle.Turtle()
pen_skor.speed(0)
pen_skor.penup()
pen_skor.hideturtle()
pen_skor.color("White")
pen_skor.setposition(-250, 255)
pen_skor.write("Scores : {} ".format(skor), align="left", font=("Arial", 13, "normal"))

# Function
def kiri() :
    pemain.kecepatan = -3

def kanan() :
    pemain.kecepatan = 3

def bergerak() :
    x = pemain.xcor()
    x += pemain.kecepatan
    if x > 230 :
        x = 230
    elif x < -230 :
        x = -230
    pemain.setx(x)
    
def menembak() :
    global keadaanpeluru
    if keadaanpeluru == "siap" :
        keadaanpeluru = "tembak"
        # Memindahkan posisi peluru
        x = pemain.xcor()
        y = pemain.ycor() + 7
        peluru.setposition(x,y)
        peluru.showturtle()

def tabrakan(a1,a2) :
    jarak = math.sqrt(math.pow(a1.xcor()-a2.xcor(),2) + math.pow(a1.ycor()-a2.ycor(),2))
    if jarak < 15 :
        return True
    else :
        return False

# Keyboard Binding
wn.listen()
wn.onkeypress(kiri, "Left")
wn.onkeypress(kanan, "Right")
wn.onkeypress(menembak, "Up")

# Loop
while True :

    wn.update()
    
    # Pemain bergerak
    bergerak()

    # Musuh Bergerak
    for musuh in musuhs :
        x = musuh.xcor()
        x += musuh.kecepatan
        musuh.setx(x)

        if musuh.xcor() < -230 or musuh.xcor() > 230 :
            for e in musuhs :
                e.kecepatan *= -1
                y = e.ycor()
                y -= 5
                e.sety(y)
                
        # Tertembak Cek
        if tabrakan(peluru, musuh): 
            peluru.hideturtle()
            keadaanpeluru = "siap"
            musuh.setposition(0, 10000)
            # musuh.setposition(random.randint(-230,230),random.randint(0,230))
            pen_skor.clear()
            skor += 10
            pen_skor.write("Scores : {} ".format(skor), align="left", font=("Arial", 13, "normal"))


        # Tertabrak Cek
        if tabrakan(pemain, musuh):
            pemain.hideturtle()
            musuh.hideturtle()
            print("Game Over")
            break

    # Peluru bergerak
    if keadaanpeluru == "tembak" :
        y = peluru.ycor()
        y += peluru.kecepatan
        peluru.sety(y)

    if peluru.ycor() > 240 :
        peluru.hideturtle()
        keadaanpeluru = "siap"


wn.mainloop()