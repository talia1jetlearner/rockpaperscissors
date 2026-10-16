from tkinter import*
import tkinter as tk
import random
cscore=0
pscore=0
options= [("rock",0),("paper",1),("scissors",2)]
def computer_wins():
    global cscore,pscore
    cscore+=1
    result.configure(text="Computer Wins!")
    c_score.configure(text="Computer Score: "+str(cscore))
    p_score.configure(text="Player Score: "+str(pscore))
def player_wins():
    global cscore,pscore
    pscore+=1
    result.configure(text="Player Wins!")
    c_score.configure(text="Computer Score: "+str(cscore))
    p_score.configure(text="Player Score: "+str(pscore))
def tie():
    global cscore,pscore
    result.configure(text="Its a TIE!!")
    c_score.configure(text="Computer Score: "+str(cscore))
    p_score.configure(text="Player Score: "+str(pscore))
def c_choice():
    return random.choice(options)
def p_choice(player_inpt):
    global cscore,pscore
    print(player_inpt)
    c_inpt= c_choice()
    print(c_inpt)
    p_select.configure(text="You Selected: "+player_inpt[0])
    c_select.configure(text="Computer Selected: "+c_inpt[0])
    if player_inpt== c_inpt:
        tie()
    if player_inpt[1]==0:
        if c_inpt[1]==1:
            computer_wins()
        elif c_inpt[1]==2:
            player_wins()
    if player_inpt[1]==1:
        if c_inpt[1]==0:
            player_wins()
        elif c_inpt[1]==2:
            computer_wins()
    if player_inpt[1]==2:
        if c_inpt[1]==0:
            computer_wins()
        elif c_inpt[1]==1:
            player_wins()

window= Tk() 
window.title("Rock, paper, scissors")
window.geometry("600x300")
window.configure(bg="light pink")
title= Label(window,text="Rock, Paper, Scissors",fg="purple",bg="light pink",font="Arial 20" )
title.place(x=160,y=10)
result= Label(window,text=" ",bg="light pink",font="Arial 10")
result.place(x=270,y=70)
label= Label(window,text="Your Options: ",fg="purple",bg="light pink",font="Arial 15" )
label.place(x=30,y=100)
rock= Button(window,text="Rock",command= lambda: p_choice(options[0]))
rock.place(x=170,y=100)
paper= Button(window,text="Paper",command= lambda:p_choice(options[1]))
paper.place(x=240,y=100)
scissors= Button(window,text="Scissors",command=lambda: p_choice(options[2]))
scissors.place(x=310,y=100)
score_txt=Label(window,text="Score: ",font="Arial 15",fg="purple",bg="light pink")
score_txt.place(x=30,y=140)
p_select= Label(window,text="You selected: ",fg="purple",bg="light pink",font="Arial 12")
p_select.place(x=100,y=180)
c_select= Label(window,text="Computer selected: ",fg="white",bg="light pink",font="Arial 12")
c_select.place(x=100,y=200)
p_score= Label(window,text="Player Score: ",fg="purple",bg="light pink",font="Arial 12")
p_score.place(x=300,y=180)
c_score= Label(window,text="Computer Score: ",fg="white",bg="light pink",font="Arial 12")
c_score.place(x=300,y=200)
window.mainloop()
