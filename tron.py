#encoding : utf-8
import tkinter as tk
from PIL import ImageTk,Image

# This simple project was an introduction to python GUI through the tkinter module.
# This tron game is pretty straightforward : it is the equivalent of a player vs player snake game
# where each player's avatar leaves a colored trail behind them as they move, just like in the tron movie.
# the goal is to make the other player run into either their own trail or the opponent's.
# Each player controls their avatar on the same keyboard, one with WASD and the other with the arrow keys.


# First, you need to create the main window tk.Tk() that will receive the menu and its child windows, Toplevel(),
# that will contain the game itself and the other options.
fentk = tk.Tk() 
fentk.title("MENU")
w1 = tk.Toplevel()
w1.title("TRON")
w1.withdraw()
w2 = tk.Toplevel()
w2.title("CREDITS")
w2.withdraw()
w3 = tk.Toplevel()
w3.title("CONFIRM")
w3.withdraw()

#Then we initialize the parameters
width= 1920
height = 1080
play_y = height/2
settings_y = play_y + 100
quit_y = settings_y + 100
#the arbitrary variables for the menu
l=0
k=0
q=0
#the initial movement of each player
dx,dx2=0,0
dy,dy2=0,0
#the inital countdown
z=6
#the intial spawn coordinates for each player
balle1Spawn = 325, 200, 325, 200
balle2Spawn = 75, 200, 75, 200
#
stop = False


#We then create each canvas within their respective windows, that will contain the visualisation of tkinter objects.
canvas = tk.Canvas(fentk, width=width, height=height, bg="black")
canvas.pack(padx=0, pady=0)

canvas1 = tk.Canvas(w2, width=width, height=height, bg="black")
canvas1.pack(padx=0, pady=0)

canvas2 = tk.Canvas(w3, width=width, height=height, bg="black")
canvas2.pack(padx=0, pady=0)

canvas3 = tk.Canvas(w1, width=400, height=400, bg="white")
canvas3.grid(row=2,column=0)

#We create the tkinter image associated to the .gif file
path = "bgimage.gif"
img = Image.open(path)
img = ImageTk.PhotoImage(img)
#img = tk.PhotoImage(file="bgimage.gif")
#and then place the image on the canvas itself
canvas.create_image(0,0, anchor=tk.NW, image=img)
canvas1.create_image(0,0, anchor=tk.NW, image=img)
canvas2.create_image(0,0, anchor=tk.NW, image=img)

#Then we create each text displayed on the main window : fentk
tron = canvas.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="black", font=("Hobo Std", 102, "bold"))
tron = canvas.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="#26b4ca", font=("Hobo Std", 100, "bold"))

play = canvas.create_text(width/2, play_y, anchor=tk.N, text="Jouer", fill="black", font=("Arial", 26, "bold"))
play1 = canvas.create_text(width/2, play_y, anchor=tk.N, text="Jouer", fill="#26b4ca", font=("Arial", 25, "bold"))
#second text to display a shadow
bbox3 = canvas.bbox(play) #To get the coordinates of the upper left and lower right of the rectangle envelopping the text
x1,y1,x2,y2 = bbox3
canvas.create_polygon(x1, y1, x2, y1, x2, y2, x1, y2,  fill="", width=2, activeoutline="#26b4ca")
#To show a rectangle surrounding the text whenever the cursor passes over the text


settings = canvas.create_text(width/2, settings_y, anchor=tk.N, text="Credits", fill="black", font=("Arial", 21, "bold"))
settings1 = canvas.create_text(width/2, settings_y, anchor=tk.N, text="Credits", fill="#26b4ca", font=("Arial", 20, "bold"))
bbox4 = canvas.bbox(settings)
x3,y3,x4,y4 = bbox4
canvas.create_polygon(x3, y3, x4, y3, x4, y4, x3, y4, fill="",width=2, activeoutline="#26b4ca")


quit = canvas.create_text(width/2, quit_y+1, anchor=tk.N, text="Quitter", fill="black", font=("Arial", 21, "bold"))
quit1 = canvas.create_text(width/2, quit_y, anchor=tk.N, text="Quitter", fill="#26b4ca", font=("Arial", 20, "bold"))
bbox5 = canvas.bbox(quit)
x5,y5,x6,y6 = bbox5
canvas.create_polygon(x5, y5, x6, y5, x6, y6, x5, y6, fill="", width=2, activeoutline="#26b4ca")



#we then put what the parameter/credits window will display
tron = canvas1.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="black", font=("Hobo Std", 102, "bold"))
tron = canvas1.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="#26b4ca", font=("Hobo Std", 100, "bold"))

Nom1 = canvas1.create_text(width/2, play_y, anchor=tk.N, text="Name1", fill="black", tag="tag_nom1", font=("Arial", 26, "bold"))
Nom11 = canvas1.create_text(width/2, play_y, anchor=tk.N, text="Name1", fill="#26b4ca", tag="tag_nom11", font=("Arial", 25, "bold"))

Nom2 = canvas1.create_text(width/2, play_y+50, anchor=tk.N, text="Name2", fill="black", tag="tag_nom2", font=("Arial", 26, "bold"))
Nom21 = canvas1.create_text(width/2, play_y+50, anchor=tk.N, text="Name2", fill="#26b4ca", tag="tag_nom21",font=("Arial", 25, "bold"))

Nom3 = canvas1.create_text(width/2, play_y+100, anchor=tk.N, text="Name3", fill="black", tag="tag_nom3", font=("Arial", 26, "bold"))
Nom31 = canvas1.create_text(width/2, play_y+100, anchor=tk.N, text="Name3", fill="#26b4ca", tag="tag_nom31", font=("Arial", 25, "bold"))

Retour = canvas1.create_text(width/2, quit_y+1, anchor=tk.N, text="Return to menu", fill="black", tag="tag_retour", font=("Arial", 21, "bold"))
Retour1 = canvas1.create_text(width/2, quit_y, anchor=tk.N, text="Return to menu", fill="#26b4ca", tag="tag_retour1",font=("Arial", 20, "bold"))
x7,y7,x8,y8 = bbox6 = canvas1.bbox(Retour1)
canvas1.create_polygon(x7, y7, x8, y7, x8, y8, x7, y8,  fill="", width=2, tag="tag_outline6", activeoutline="#26b4ca")

#we then put what the quitting window will display
tron = canvas2.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="black", font=("Hobo Std", 102, "bold"))
tron = canvas2.create_text(width/2,height/7, anchor=tk.N, text="TRON", fill="#26b4ca", font=("Hobo Std", 100, "bold"))

verification = canvas2.create_text(width/2, play_y+1, text="Confirm", fill="black", tag="tag_verif", font=("Arial", 26, "bold"))
verification1 = canvas2.create_text(width/2, play_y, text="Confirm",  fill="#26b4ca", tag="tag_verif1", font=("Arial", 25, "bold"))

verif_oui = canvas2.create_text(width*(1/3), quit_y+1, anchor=tk.W, text="Yes", fill="black", tag="tag_oui", font=("Arial", 21, "bold"))
verif_oui1 = canvas2.create_text(width*(1/3), quit_y, anchor=tk.W, text="Yes", fill="#26b4ca", tag="tag_oui1", font=("Arial", 20, "bold"))
x9,y9,x10,y10 = bbox7 = canvas2.bbox(verif_oui)
canvas2.create_polygon(x9, y9, x10, y9, x10, y10, x9, y10, fill="", width=2, tag="tag_outline7", activeoutline="#26b4ca")

verif_non = canvas2.create_text(width*(2/3), quit_y+1, anchor=tk.E, text="No", fill="black", tag="tag_non", font=("Arial", 21, "bold"))
verif_non1 = canvas2.create_text(width*(2/3), quit_y, anchor=tk.E, text="No", fill="#26b4ca", tag="tag_non1", font=("Arial", 20, "bold"))
x11,y11,x12,y12 = bbox8 = canvas2.bbox(verif_non)
canvas2.create_polygon(x11, y11, x12, y11, x12, y12, x11, y12, fill="", width=2, tag="tag_outline8", activeoutline="#26b4ca")

#on mets ce que les boutons vont faire
def click_souris(event):
    global e1, e2, x1, x2, y1, y2, x3 ,x4, y3, y4, x5, x6, y5, y6, l, k, q
    x=event.x
    y=event.y
    if l==0:
        if k==0:
            if x in range(x1,x2):
                if y in range(y1,y2):
                    q=q+1
            if x in range(x3,x4):
                if y in range(y3,y4):
                    l=l+1

            if x in range(x5, x6):
                if y in range(y5, y6):
                    k=k+1

        if k==1:
            fentk.withdraw()
            w3.deiconify()

            if x in range(x9,x10):
                if y in range(y9, y10):
                    w3.destroy()

            if x in range(x11,x12):
                if y in range(y11,y12):
                    w3.withdraw()
                    fentk.deiconify()
                    k=k-1
    if q==1:
        fentk.withdraw()
        w1.deiconify()


    if l==1:
        fentk.withdraw()
        w2.deiconify()

        if x in range(x7, x8):
            if y in range(y7, y8):

                w2.withdraw()
                fentk.deiconify()
                l=l-1
#we associate the mouse's left click to the previous function on each window
fentk.bind("<Button 1>", click_souris)
w2.bind("<Button 1>", click_souris)
w3.bind("<Button 1>", click_souris)

#we create a function that displays a countdown
def go():
    global z,dx,dy,dx2,dy2
    z+=1
    if z==1:
        canvas3.create_text(200,200,text="3",fill="#26b4ca",font=("Arial","100","bold"))
    elif z==2:
        canvas3.delete('all')
        canvas3.create_text(200,200,text="2",fill="#26b4ca",font=("Arial","100","bold"))
    elif z==3:
        canvas3.delete('all')
        canvas3.create_text(200,200,text="1",fill="#26b4ca",font=("Arial","100","bold"))
    elif z==4:
        canvas3.delete('all')
        canvas3.create_text(200,200,text="GO !",fill="#26b4ca",font=("Arial","100","bold"))
    elif z==5:
        canvas3.delete('all')
        replay()
        deplacement()
        deplacement2()
    else:
        pass

#we associate one player's keypresses to the movement of a player
def keybind(event):
    global dx ,dy
    touche=event.keysym
    if  touche=='Right':
        dx=2
        dy=0

        deplacement()

    if  touche=='Left':
        dx=-2
        dy=0

        deplacement()

    if  touche=='Up':
        dx=0
        dy=-2

        deplacement()

    if  touche=='Down':
        dx=0
        dy=2

        deplacement()

def keybind2(event):
    global dx2 ,dy2
    touche=event.keysym

    if  touche=='d':
        dx2=2
        dy2=0
        deplacement2()

    if  touche=='a':
        dx2=-2
        dy2=0
        deplacement2()

    if  touche=='w':
        dx2=0
        dy2=-2
        deplacement2()

    if  touche=='s':
        dx2=0
        dy2=2
        deplacement2()


def deplacement2():
    global dx2,dy2,stop
    #if the list of the canvas ids of the objects present in the rectangle of the player is superior to 1,
    # meaning that there is another object than the player, then there is a collision
    if len(canvas3.find_overlapping(canvas3.coords(balle2)[0],canvas3.coords(balle2)[1],canvas3.coords(balle2)[2],canvas3.coords(balle2)[3]))>1:
        if len(canvas3.find_overlapping(canvas3.coords(balle1)[0],canvas3.coords(balle1)[1],canvas3.coords(balle1)[2],canvas3.coords(balle1)[3]))==1:
            #if only one of the player is in collision
            finpartie2()
        else:
            #both player are colliding, there is a draw
            egalite()
        stop = True
            
    #if the player is out of bounds, then he loses            
    if stop==False and ((canvas3.coords(balle2)[3]>400) or (canvas3.coords(balle2)[1]<0) or (canvas3.coords(balle2)[0]<0) or (canvas3.coords(balle2)[2]>400)):
        finpartie2()
        stop = True

    #we then must create the player's trail
    canvas3.create_rectangle([canvas3.coords(balle2)], fill = "blue", outline = "blue")

    if not stop:
        canvas3.move(balle2,dx2/3,dy2/3)
        w1.after(30,deplacement2)


def deplacement():
    global dx,dy,stop
    if len(canvas3.find_overlapping(canvas3.coords(balle1)[0],canvas3.coords(balle1)[1],canvas3.coords(balle1)[2],canvas3.coords(balle1)[3]))>1:
        if len(canvas3.find_overlapping(canvas3.coords(balle2)[0],canvas3.coords(balle2)[1],canvas3.coords(balle2)[2],canvas3.coords(balle2)[3]))==1:
            finpartie1()
        else:
            egalite()
        stop = True

    canvas3.create_rectangle([canvas3.coords(balle1)], fill = "red", outline = "red")

    if stop == False and ((canvas3.coords(balle1)[3]>400) or (canvas3.coords(balle1)[1]<0) or (canvas3.coords(balle1)[0]<0) or (canvas3.coords(balle1)[2]>400)):
        finpartie1()
        stop = True

    if not stop:
        canvas3.move(balle1,dx/3,dy/3)
        w1.after(30,deplacement)

def finpartie1():
    Labela['text']='Le Joueur bleu Gagne !'

    boutton.grid(row=19, column=0)
    

def finpartie2():

    Labela['text']='Le Joueur rouge Gagne !'

    boutton.grid(row=19, column=0)

def egalite():

    Labela['text']='Ancun joueur ne gagne , egalité !'

    boutton.grid(row=19, column=0)


def comptearebour():
    global dx,dy,dx2,dy2,z
    dx=-2
    dy=0
    dx2=2
    dy2=0
    z=0
    canvas3.delete("all")
    Labela['text']=' '
    boutton.grid_forget()

def replay():
    global balle1,balle2,stop
    balle1 = canvas3.create_rectangle(balle1Spawn,fill='red')
    balle2 = canvas3.create_rectangle(balle2Spawn,fill='blue')
    stop = False
    
#associate keypress events with their movement functions    
for touchepresse in ['<Right>', '<Left>','<Down>','<Up>']:
        w1.bind(touchepresse,keybind)

for touchepresse in ['<d>', '<s>','<a>','<w>']:
        w1.bind(touchepresse,keybind2)

def timer():
    w1.after(1000,timer)
    go()

timer()
#on mets ce que w1 va afficher
boutton= tk.Button(w1, text="REJOUER", command=comptearebour)
boutton.grid(row=19, column=0)
boutton.grid_forget()

Labela= tk.Label(w1, text=' ')
Labela.grid(row=3, column=0)

Label= tk.Label(w1, text='Jeu Tron:')
Label.grid(row=1, column=0)

quitter= tk.Button(w1, text="QUITTER", command=w1.destroy)
quitter.grid(row=20, column=0)

balle1 = canvas3.create_rectangle(balle1Spawn,fill='red')
balle2 = canvas3.create_rectangle(balle2Spawn,fill='blue')

fentk.mainloop()