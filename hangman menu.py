#IMPORTING PRE-DEFINED MODULES
import mysql.connector as ms
from tkinter import *
import os

SQLpassword="Enter Your MySQL Password"

#FOR CONNECTING WITH SQL SERVER AND CREATING A DATABASE IF NOT AVAILABLE
con=ms.connect(host="localhost",user="root",passwd=SQLpassword) 
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS Hangman")
cur.execute("USE HANGMAN")
cur.execute("CREATE TABLE IF NOT EXISTS Leaderboard(Player varchar(20) PRIMARY KEY,Points int DEFAULT 0,Games int DEFAULT 0,Signup_Date datetime)")
cur.execute("CREATE TABLE IF NOT EXISTS Password(Player varchar(20) PRIMARY KEY,passwd varchar(15))")
cur.execute("INSERT IGNORE INTO LEADERBOARD (PLAYER,Signup_Date) VALUES('Guest',sysdate())")
cur.execute("INSERT IGNORE INTO PASSWORD (PLAYER,PASSWD) VALUES('Guest','Guest')")
con.commit()

#EXIT BUTTON FUNCTION
def eradicate():
    con=ms.connect(host="localhost",user="root",passwd=SQLpassword) 
    cur=con.cursor()
    cur.execute("USE HANGMAN")
    cur.execute("DELETE FROM Leaderboard WHERE Player = 'Guest'")
    cur.execute("DELETE FROM Password WHERE Player = 'Guest'")
    con.commit()
    os._exit(0)

def nothing():
    pass

#FOR CLOSING MESSAGE BOXES
def close(num3):
    playerdetail.grab_release()
    if num3==0:
        msg.destroy()
    if num3==1:
        msg.destroy()
        win.destroy()
        con=ms.connect(host="localhost",user="root",passwd=SQLpassword) 
        cur=con.cursor()
        cur.execute("USE HANGMAN")
        cur.execute("DELETE FROM Leaderboard WHERE Player = 'Guest'")
        cur.execute("DELETE FROM Password WHERE Player = 'Guest'")
        con.commit()
        import hangman  #IMPORTING USER DEFINED MODULE (hangman.py)

#FOR UNIVERSAL MESSAGE BOXES
def msgbox(num1,num2):
    global msg
    msg=Tk()
    msg.protocol("WM_DELETE_WINDOW",nothing)
    msg.resizable(0,0)
    msg.geometry("300x100")
    playerdetail.grab_set()
    if num1==0:
        msg.title("Whoops!")
        ok=Button(msg, text="OK",command=lambda: close(0))
        ok.grid(column=2,row=5)
        if num2==0:
            desc=Label(msg, text="Credentials not within range")
            desc.grid(column=0,row=0)
        elif num2==1:
            desc=Label(msg, text="Username already exists!")
            desc.grid(column=0,row=0)
        elif num2==2:
            desc=Label(msg, text="Incorrect Password!")
            desc.grid(column=0,row=0)
        else:
            desc=Label(msg, text="Username does not exist!")
            desc.grid(column=0,row=0)
    if num1==1:
        msg.title("Success!")
        ok=Button(msg, text="OK",command=lambda: close(1))
        ok.grid(column=2,row=5)
        if num2==0:
            desc=Label(msg, text="Signed up successfully!")
            desc.grid(column=0,row=0)
        else:
            desc=Label(msg, text="Signed in successfully!")
            desc.grid(column=0,row=0)
    

    
#FOR LOGIN WINDOW
win=Tk()
win.resizable(0,0)
win.geometry("800x350")
win.title("Welcome to Hangman Game Login Screen")

bg=PhotoImage(file='source/hangman.png')
bgI=Label(win, image=bg)
bgI.place(x=0, y=0, relwidth=1, relheight=1)

win.columnconfigure(0,weight=1)
win.columnconfigure(1,weight=1)

playerdetail=Label(win, text="New Player or Existing Player:", bg="#C1CDCD", font=("Times New Roman",14))
playerdetail.grid(column=0,row=2)

PD=IntVar()

signup=Radiobutton(win, text="Sign Up",variable=PD,value=0, font=("Times New Roman",14))
signup.grid(column=1,row=2,padx=(0,100))

signin=Radiobutton(win, text="Sign In",variable=PD,value=1, font=("Times New Roman",14))
signin.grid(column=1,row=2,padx=(100,0))

username=Label(win, text="Name:", bg="#C1CDCD", font=("Times New Roman",14))
username.grid(column=0,row=3,pady=(10,0))

Uname=Entry(win,width=70)
Uname.grid(column=1,row=3,pady=(10,0))

password=Label(win, text="Password:", bg="#C1CDCD", font=("Times New Roman",14))
password.grid(column=0,row=4)

Pword=Entry(win,width=70,show="*")
Pword.grid(column=1,row=4)
Pword.bind("<Key>", lambda e: nothing())

exitwin=Button(win, text="EXIT", command=eradicate, font=("Times New Roman",14))
exitwin.grid(column=1,row=10,pady=(10,0))

guestwin=Button(win, text="Play as Guest", command=lambda: run(1), font=("Times New Roman",14))
guestwin.grid(column=0,row=10,pady=(10,0))

submit=Button(win, text="SUBMIT", command=lambda: run(0), font=("Times New Roman",14))
submit.grid(column=1,row=5,pady=(10,0))

win.protocol("WM_DELETE_WINDOW",nothing)

note="Note:\nCredentials cannot be empty\nUsername should be 5 to 20 characters\nUsername\
 cannot be Guest\nPassword should be 5 to 15 characters\nScores playing as Guest is temporary"

conditions=Label(win, text=note, justify="left", bg="#C1CDCD", font=("Times New Roman",14))
conditions.grid(column=0,row=8)

#USER CREDENTIAL VALIDATION FUNCTION
def run(z):
    global name
    players=[]
    name=Uname.get()
    PlayerD=PD.get()
    PW=Pword.get()
    if z==1:
        name="Guest"
        PW="Guest"
        PlayerD=1

    if len(PW)<5 or len(name)<5 or len(PW)>15 or len(name)>20 or Uname.get()=="Guest":
        msgbox(0,0)
    else:
        con=ms.connect(host="localhost",user="root",passwd=SQLpassword,database="Hangman")
        cur=con.cursor()
        cur.execute("SELECT PLAYER FROM LEADERBOARD")
        data=cur.fetchall()

        for rec in data:
            players.append(rec[0])
        if PlayerD==0:
            if name not in players:
                cur.execute("INSERT INTO LEADERBOARD(PLAYER,SIGNUP_DATE) VALUES('{}',sysdate())".format(name,))
                cur.execute("INSERT INTO PASSWORD VALUES('{}','{}')".format(name,PW))
                con.commit()
                msgbox(1,0)
            else:
                msgbox(0,1)
                
        elif PlayerD==1:
            if name in players:
                cur.execute("SELECT * FROM PASSWORD")
                pdata=cur.fetchall()
                if (name,PW)==("Guest","Guest"):   #TO SKIP MESSAGE BOX IF PLAYING AS GUEST
                    win.destroy()
                    import hangman
                elif (name,PW) in pdata:
                    msgbox(1,1)
                else:
                    msgbox(0,2)
            else:
                msgbox(0,3)
        
win.mainloop()

#COLLECTING PLAYER DATA FROM HANGMAN
from hangman import gamestatus
totalpoints,totalgames=gamestatus()

con=ms.connect(host="localhost",user="root",passwd=SQLpassword)
cur=con.cursor()

#UPDATING LEADERBOARD IN SQL
cur.execute("USE Hangman")
cur.execute("UPDATE LEADERBOARD SET POINTS=POINTS+{}, GAMES=GAMES+{} WHERE PLAYER='{}'".format(totalpoints,totalgames,name))
cur.execute("SELECT PLAYER,POINTS,GAMES,(POINTS/GAMES) AS AVERAGE, SIGNUP_DATE FROM LEADERBOARD ORDER BY POINTS DESC")
DATUM=cur.fetchall()

#DISPLAYING LEADERBOARD

LB=Tk()
LB.resizable(0,0)
LB.protocol("WM_DELETE_WINDOW",nothing)
LB.geometry("1920x1080")
LB.attributes('-fullscreen',True)
LB.title("Leaderboard")

LBG=PhotoImage(file="source/LeaderboardBG.png")
LBGI=Label(LB, image=LBG)
LBGI.place(x=0)

LB.columnconfigure(0,weight=1)
LB.columnconfigure(1,weight=1)
LB.columnconfigure(2,weight=1)
LB.columnconfigure(3,weight=1)
LB.columnconfigure(4,weight=1)
LB.columnconfigure(5,weight=1)

exitLB=Button(LB, text="EXIT", font=("Times New Roman",14), command=eradicate)
exitLB.grid(column=5,row=0,pady=5)

LB.option_add("*Background", "#00FFFF")
head=Label(LB, text="LEADERBOARD", font=("Times New Roman",14))
head.place(x=700,y=3)

rank=Label(LB, text="RANK", font=("Times New Roman",14))
rank.grid(column=0,row=1,pady=5)

name=Label(LB, text="NAME", font=("Times New Roman",14))
name.grid(column=1,row=1,pady=5)

score=Label(LB, text="SCORE", font=("Times New Roman",14))
score.grid(column=2,row=1,pady=5)

games=Label(LB, text="GAMES", font=("Times New Roman",14))
games.grid(column=3,row=1,pady=5)

average=Label(LB, text="AVERAGE", font=("Times New Roman",14))
average.grid(column=4,row=1,pady=5)

signupdate=Label(LB, text="SIGNUP DATE", font=("Times New Roman",14))
signupdate.grid(column=5,row=1,pady=5)


LB.option_add("*Background", "#FFC90E")
R="1"
row=2
for i in DATUM:
    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L1"+R,R))
    exec('{}.grid(column=0,row={},pady=5)'.format("L1"+R,row))

    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L2"+R,i[0]))
    exec('{}.grid(column=1,row={},pady=5)'.format("L2"+R,row))

    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L3"+R,i[1]))
    exec('{}.grid(column=2,row={},pady=5)'.format("L3"+R,row))

    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L4"+R,i[2]))
    exec('{}.grid(column=3,row={},pady=5)'.format("L4"+R,row))

    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L5"+R,i[3]))
    exec('{}.grid(column=4,row={},pady=5)'.format("L5"+R,row))

    exec('{}=Label(LB, text="{}", font=("Times New Roman",13))'.format("L6"+R,i[4]))
    exec('{}.grid(column=5,row={},pady=5)'.format("L6"+R,row))

    row+=1
    if row==3:
        LB.option_add("*Background","#C3C3C3")
    if row==4:
        LB.option_add("*Background","#FF9E3E")
    if row>4 and row%2!=0:
        LB.option_add("*Background","#FFFFFF")
    if row>4 and row%2==0:
        LB.option_add("*Background","#E3E3E3")
    R=str(int(R)+1)
    
con.commit()

#DISCONNECTION FROM SQL 
con.close()

input()

