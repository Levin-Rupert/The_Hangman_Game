#USER DEFINED MODULE (hangman.py)

#IMPORTING PRE-DEFINED MODULES
import random
from tkinter import *
from tkinter import messagebox

#INITIALISING MAX AVAILABLE POINTS
pointL=[]
points = 100
run = True

def nothing():
    pass

#GAME LOOP
while run:
    root = Tk()
    root.geometry('1920x1080')
    root.protocol("WM_DELETE_WINDOW",nothing)
    root.attributes('-fullscreen',True)
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0 #WRONG GUESSES
    win_count = 0 
    score=Label(root, text="Available Points:{}".format(points,), bg="#FFFF00", font=("Times New Roman",40))
    score.grid(column=0,row=1)

    #CHOOSING WORDS
    file = open('source/words.txt','r')
    l = file.read().split("\n")
    selected_word =random.choice(l)
    
    #CREATING FILLING SPOTS
    x = 540
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #DEFINING LETTER ICONS
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="source/{}.png")'.format(let,let))
        
    #DEFINING HANGMAN IMAGES
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="source/{}.png")'.format(hangman,hangman))
        
    #PLACING LETTERS ICONS
    button = [['b1','a',0,595],['b2','b',117,595],['b3','c',234,595],['b4','d',351,595],['b5','e',468,595],['b6','f',585,595],['b7','g',702,595],['b8','h',819,595],['b9','i',936,595],['b10','j',1053,595],['b11','k',1170,595],['b12','l',1287,595],['b13','m',1404,595],['b14','n',0,712],['b15','o',117,712],['b16','p',234,712],['b17','q',351,712],['b18','r',468,712],['b19','s',585,712],['b20','t',702,712],['b21','u',819,712],['b22','v',936,712],['b23','w',1053,712],['b24','x',1170,712],['b25','y',1287,712],['b26','z',1404,712]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #PLACING HANGMAN IMAGES
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))

    c1.place(x = 550,y =- 50)
    
    #EXIT FUNCTION
    def closegame():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            points=0
            pointL.append(points)
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'source/exit.png')
    ex = Button(root,bd = 0,command = closegame,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=1395,y=10)

    #EVALUATION FUNCTION
    def check(letter,button):
        global count,win_count,run,points
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                pointL.append(points)
                if answer == True:
                    points=100
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            points-=15
            score.destroy()
            scorec=Label(root, text="Available Points:{}".format(points,), bg="#FFFF00", font=("Times New Roman",40))
            scorec.grid(column=0,row=1)
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,550,-50))
            if count == 6:
                points=0
                scorec.destroy()
                scoref=Label(root, text="Available Points:  {}".format(points,), bg="#FFFF00", font=("Times New Roman",40))
                scoref.grid(column=0,row=1)
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?\nTHE ANSWER IS "{}"'.format(selected_word.upper()))
                pointL.append(points)
                if answer == True:
                    run = True
                    points = 100
                    root.destroy()
                else:
                    run = False
                    root.destroy()
            
    root.mainloop()

#COLLECTING PLAYER DATA FOR MAIN PROGRAM
def gamestatus():
    global totalpoints, pointL
    totalpoints=0
    for i in pointL:
        totalpoints+=i
    return totalpoints,len(pointL)
