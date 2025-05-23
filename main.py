from tkinter import *
import time
tk = Tk()
# !No code above this line!



# To-Do
    # 1. Make a start screen
    # 2. Rposition the butons   DONE    May,15
    # 3. Make the x/y axis speed buttons do stuff   DONE    May,19
    # 4. make all the labbles for button costs
    # 5. Get the exponetl cost working



    # Designing the tkinter window "Game"
win = Tk() # assigning window (win) to be Tk
win.title("Game") # title of the PyCharm window
win.config(bg="pink") #setting the color of the widow
win.geometry("425x425+1050-600") #window geometry



    # Making canvas
canvas = Canvas(tk, bg="white",width=(1000 ),height=(750))
canvas.pack()



    #Making all the global
global YaxisSpeed
global XaxisSpeed
global yspeed
global xspeed



xspeed = 2
yspeed = 2



    # Making the x and y speed increese buttons have a 0.25 second cooldown on
global coolDownY
coolDownY = False
global coolDownX
coolDownX = False



    #seting thr money to 0 at the start of the game
money = 0
    # Making the "Your balance" labble
moneyL = Label(win, text="Your balance = 0", font=("Arial", 20))
    # Making the money dispaly on the 425x425 window
def moneyyyy():
    global money, moneyL

    moneyL.destroy()
    moneyL = Label(win, text=f"Your balance = {money}", font=("Arial", 20))
    moneyL.place(x=140, y=12.5)



B = Button(win, text ="Increase Radius", command = "radiusIncrease")
B.place(x=20,y=125)
    # Increase the balls radius by 2.5          100$     25% more expensive (exponential) 100x1.25^x
def radiusIncrease():
    pass



def stopSpammingX():
    global coolDownX
    coolDownX= False
    # Increase the balls y-axis speed by 1      75$     15% more expensive (exponential) 75x1.15^x
def XaxisSpeed():
    global xspeed, coolDownX, money, xspeedcost, XaxisCost
    if coolDownX == False and money >= xspeedcost:  # If the cool down is false don't let the user buy X-axis speed
        money -= xspeedcost
        money = int(money)
        xspeedcost += xspeedcost*0.2
        XaxisCost.config(text=int(xspeedcost))
        print(xspeedcost)
        coolDownX = True    # If the cool down is true then let them buy X-axis speed and start a 0.2 second time till you can buy another X-axis speed
        xspeed += ((xspeed)/abs(xspeed)) * 5             # Adding 1 X-axis speed the already existing X-axis speed
        win.after(250, stopSpammingX)   # 0.25 second wait to stop spamming the X-axis speed button
B = Button(win, text ="Increase X-axis speed", command = XaxisSpeed)
B.place(x=25,y=50)
    # Making the cost labble and placing it
global XaxisCost
XaxisCost = Label(win, text="75", font=("Arial", 20))
global xspeedcost
xspeedcost = 75
XaxisCost.place(x=105, y=77.5)













def stopSpammingY():
    global coolDownY
    coolDownY= False
    # Increase the balls y-axis speed by 1      75$     15% more expensive (exponential) 75x1.15^x
def YaxisSpeed():
    global yspeed, coolDownX, money, yspeedcost, YaxisCost
    if coolDownX == False and money >= yspeedcost:  # If the cool down is false don't let the user buy X-axis speed
        money -= yspeedcost
        money = int(money)
        yspeedcost += yspeedcost*0.2
        YaxisCost.config(text=int(yspeedcost))
        print(yspeedcost)
        coolDownY = True    # If the cool down is true then let them buy X-axis speed and start a 0.2 second time till you can buy another X-axis speed
        yspeed += ((yspeed)/abs(xspeed)) * 5             # Adding 1 X-axis speed the already existing X-axis speed
        win.after(250, stopSpammingX)   # 0.25 second wait to stop spamming the X-axis speed button
B = Button(win, text ="Increase Y-axis speed", command = XaxisSpeed)
B.place(x=25,y=50)
    # Making the cost labble and placing it
global YaxisCost
YaxisCost = Label(win, text="75", font=("Arial", 20))
global yspeedcost
yspeedcost = 75
XaxisCost.place(x=300, y=77.5)
















B = Button(win, text ="corner multiplier", command = "cornerMultiplier")
B.place(x=275,y=125)
    # Multiply the points by 0.5 if it hits a corner    100$    25% more expensive (exponential)
def cornerMultiplier():
    pass



    # RGB ball (cycling through red, green, blue
B = Button(win, text ="GAMER ball", command = "Gamer_ball")
B.place(x=163,y=125)
    # Changes the color evray 2 seconds
def Gamer_ball():
    ball.config(fill = "red")

    ["red", "blue", "green", "yellow", "orange", "purple", "pink"]



    # Ball speed on the x and y-axis
    BallSpeedX = 2  # Balls speed on the x-axis
    BallSpeedY = 2  # Balls speed on the y-axis



    # Seting the x axis speed amd the y axis speed, also creating the ball
def ball():
    global money, moneyL
    global yspeed
    global xspeed
    moneyL = Label(win, text=f"Your balance = 0", font=("Arial", 20))



    ball = canvas.create_oval(430,10,470,50)
    while True:
        canvas.move(ball, xspeed, yspeed)
        pos = canvas.coords(ball)
        # Making the ball bounce agesnst the walls (set to a little below canvas size)
        if pos[2] >=1000 or pos[0] <0:
            xspeed = -xspeed
            money += 1
            moneyyyy()
        if pos[3] >=750 or pos[3]<46:
            yspeed = -yspeed
            money +=1
            moneyyyy()
        tk.update()
            # Adusts how may times the ball updates per sec (curently 1000 times per second(butter( \_(-_-)_/ absolte cinima)))
        time.sleep(0.001)



# !No code below this line!
#placing the "your balence"
moneyL.place(x=140, y=12.5)
ball()
win.mainloop()
