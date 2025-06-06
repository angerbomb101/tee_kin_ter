from tkinter import *
import time
tk = Tk()
    # !No code above this line!



    # To-Do
        # 1. Make a start screen
        # 2. Rposition the butons   DONE    May,15
        # 3. Make the x/y axis speed buttons do stuff   DONE    May,19
        # 4. make all the labbles for button costs
        # 5. Get the exponetl cost working Done     May,28
        # 6. Make the "increse radous" button working
        # 7. Make the "Corner multiplyer" button work
        # 8. Fix the glitch that makes the y-axis dispay cost
        # 9. Make the bg of the labbles and the buttons change with the win1, win2, win3, ext (on the x and y axis) (and stay thst way)
        # 10. Make the rebirth, it costs $1000000 x 1.25 (add 1 ball evry pirstige)

    # THing I can do
    # 1. Make the button for prestinging and the cost labble
    # 2. Get the exponetal cost working for the prestige



    # Designing the tkinter window "Game"
win = Tk() # assigning window (win) to be Tk
win.title("Game") # title of the PyCharm window
win.config(bg="white") #setting the color of the widow
win.geometry("425x425+1050-600") #window geometry



    # Making canvas
canvas = Canvas(tk, bg="white",width=(750),height=(750))
canvas.pack()



    #Making all the global
global YaxisSpeed, ball, totalMoney
global XaxisSpeed
global speedList
global coolDownX
global coolDownY

totalMoney = 0
speedList = [[2,2],[2,2]]


radiusCost = 75

    # Making the x and y speed increese buttons have a 0.25 second cooldown on
coolDownY = False
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
# Making the cost label and placing it
    global IncreaseRadiuscost, radiusCost, ball
    if money >= radiusCost:
        IncreaseRadiuscost = Label(win, text="75", bg="white", font=("Arial", 20))
        radiusCost = radiusCost * 1.25
        XaxisCost.place(x=105, y=200)



def stopSpammingX():
    global coolDownX
    coolDownX= False
    # Increase the balls y-axis speed by 1      75$     15% more expensive (exponential) 75x1.15^x
def XaxisSpeed():
    global speedList, coolDownX, money, xspeedcost, XaxisCost
    if coolDownX == False and money >= xspeedcost:  # If the cool down is false don't let the user buy X-axis speed
        money -= xspeedcost
        money = int(money)
        xspeedcost += xspeedcost*0.2
        XaxisCost.config(text=int(xspeedcost))
        print(xspeedcost)
        coolDownX = True    # If the cool down is true then let them buy X-axis speed and start a 0.2 second time till you can buy another X-axis speed
        for speed in speedList:
            speed[0] += ((speed[0])/abs(speed[0])) * 5             # Adding 1 X-axis speed the already existing X-axis speed
        win.after(250, stopSpammingX)   # 0.25 second wait to stop spamming the X-axis speed button
B = Button(win, text ="Increase X-axis speed", bg="white" , command = XaxisSpeed)
B.place(x=25,y=50)
    # Making the cost labble and placing it
global XaxisCost
XaxisCost = Label(win, text="5",bg="white", font=("Arial", 20))
global xspeedcost
    # Changing the base cost of the x-axis speed increse
xspeedcost = 5
XaxisCost.place(x=105, y=77.5)


def stopSpammingY():
    global coolDownY
    coolDownY= False
    # Increase the balls y-axis speed by 1      75$     15% more expensive (exponential) 75x1.15^x
def YaxisSpeed():
    global speedList, coolDownX, money, yspeedcost, YaxisCost
    if coolDownX == False and money >= yspeedcost:  # If the cool down is false don't let the user buy X-axis speed
        money -= yspeedcost
        money = int(money)
        yspeedcost += yspeedcost*0.2
        YaxisCost.config(text=int(yspeedcost))
        print(yspeedcost)
        coolDownY = True    # If the cool down is true then let them buy X-axis speed and start a 0.2 second time till you can buy another X-axis speed
        for speed in speedList:
            speed[1] += ((speed[1])/abs(speed[1])) * 5             # Adding 1 X-axis speed the already existing X-axis speed
        win.after(250, stopSpammingY)   # 0.25 second wait to stop spamming the X-axis speed button
B = Button(win, text ="Increase Y-axis speed", command = YaxisSpeed)
B.place(x=225,y=50)
    # Making the cost labble and placing it
global YaxisCost
YaxisCost = Label(win, bg="white", text="5", font=("Arial", 20))
global yspeedcost
    # Changing the base cost of the 7-axis speed increse
yspeedcost = 5
YaxisCost.place(x=300, y=77.5)





B = Button(win, text ="corner multiplier", command = "cornerMultiplier")
B.place(x=275,y=125)
    # Multiply the points by 1.5 if it hits a corner    100$    25% more expensive (exponential)
def cornerMultiplier():
    pass





    prestigecost == 10
    # Making the prestige button
B = Button(win, text="prestige", command="prestige")
B.place(x=177.5, y=250)
def prestige():
    global prestigecost
    prestigecost * 2.5      # Exponetal
    prestigecost = prestigecostlable
prestigecostlable = Label(win, bg="white", text="1000000", font=("Arial", 20))
prestigecostlable.place(x=180, y=277.5)








    # RGB ball (cycling through red, green, blue)
B = Button(win, text ="GAMER ball", command = "Gamer_ball")
B.place(x=163,y=125)
    # Changes the color evrey 2 seconds
def Gamer_ball():
    ball.config(fill = "red")

    ["red", "blue", "green", "yellow", "orange", "purple"]



    # Ball speed on the x and y-axis
    BallSpeedX = 2  # Balls speed on the x-axis
    BallSpeedY = 2  # Balls speed on the y-axis



    # Seting the x axis speed amd the y axis speed, also creating the ball
def ballvar():
    global money, moneyL, win, totalMoney, ballsList, speedList, YaxisCost, XaxisCost, Button
    moneyL = Label(win, text=f"Your balance = 0", font=("Arial", 20))


    ballsList = []
    ball = canvas.create_oval(430,10,470,50)
    ball2 = canvas.create_oval(450,50,490,90)
    ballsList.append(ball)
    ballsList.append(ball2)
    while True:
        for i in range(len(ballsList)):
            ball = ballsList[i]
            canvas.move(ball, speedList[i][0], speedList[i][1])
            pos = canvas.coords(ball)
            # Making the ball bounce agesnst the walls (set to a little below canvas size)
            if pos[2] >=758 or pos[0] <0:
                speedList[i][0] = -speedList[i][0]
                money +=1   # Adding money on if the ball hits a wall on the x-axis
                totalMoney += 1

                if totalMoney == 10000:  # Win6
                    win.config(bg="purple")
                if totalMoney == 1000:   # Win5
                    win.config(bg="pink")
                if totalMoney == 100:   # Win4
                    win.config(bg="orange")
                if totalMoney == 10:  # Win3
                    win.config(bg="green")
                if totalMoney == 5:  # Win2
                    win.config(bg="red")
                if totalMoney == 1:  # Win1
                    win.config(bg="blue")
                    XaxisCost.bg = "blue"
                    YaxisCost.config(bg="blue")
                    XaxisCost.config(bg="blue")
                    B = Button(bg="blue")
                    Label(win, bg="white", text="1000000", font=("Arial", 20))

                moneyyyy()
            if pos[3] >=758 or pos[3]<46:
                speedList[i][1] = -speedList[i][1]
                money +=1   # Adding money on if the ball hits a wall on the y-axis
                totalMoney += 1

                if totalMoney == 10000:  # Win6
                    win.config(bg="purple")
                if totalMoney == 1000:  # Win5
                    win.config(bg="pink")
                if totalMoney == 100:  # Win4
                    win.config(bg="orange")
                if totalMoney == 10:  # Win3
                    win.config(bg="green")
                if totalMoney == 5:   # Win2
                    win.config(bg="red")
                if totalMoney == 1:   # Win1
                    win.config(bg="blue")

                moneyyyy()
        tk.update()
            # Adusts hoow maay timees thhe balll updattes peeer seec (curently onethousond timess peeer secondd(buttter( \_(-_-)_/ absolte cinima)))
        time.sleep(0.001)



# !No code below this line!
#placing the "your balence"
moneyL.place(x=140, y=12.5)
ballvar()
win.mainloop()
