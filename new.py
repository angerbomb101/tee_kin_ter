from tkinter import *
import time
import math as m
import random as r
w = Tk()
w.title("Ball Game")
w.geometry("600x400")
def game():
    global win,tk, totalMoneyL
    tk = Toplevel(w)
        # !No code above this line!



        # To-Do
            # 1. Make a start screen DONE
            # 2. Rposition the butons   DONE    May,15
            # 3. Make the x/y axis speed buttons do stuff   DONE    May,19
            # 4. make all the labbles for button costs DONE
            # 5. Get the exponetl cost working Done     May,28
            # 6. Make the "increse radous" button working DONE
            # 7. Make the "Corner multiplyer" button work DONE
            # 8. Fix the glitch that makes the y-axis dispay cost ???
            # 9. Make the bg of the labbles and the buttons change with the win1, win2, win3, ext (on the x and y axis) (and stay thst way) DONE
            # 10. Make the rebirth, it costs $1000000 x 1.25 (add 1 ball evry pirstige) DONE

        # THing I can do
        # 1. Make the button for prestinging and the cost labble
        # 2. Get the exponetal cost working for the prestige



        # Designing the tkinter window "Game"
    win = Toplevel(w) # assigning window (win) to be toplevel
    win.title("Game") # title of the PyCharm window
    win.config(bg="white") #setting the color of the widow
    win.geometry("425x425+1050-600") #window geometry



        # Making canvas
    canvas = Canvas(tk, bg="white",width=(750),height=(750))
    canvas.pack()



        #Making all the global
    global YaxisSpeed, ball, totalMoney, money, moneyL,speedList,radiusCost, radius, Gamerball
    global XaxisSpeed
    global speedList
    global coolDownX
    global coolDownY
    Gamerball = False

    global cornerMult
    cornerMult = 1

    totalMoney = 0
    speedList = [[2,2]]


    radiusCost = 75
    radius = 20

        # Making the x and y speed increese buttons have a 0.25 second cooldown on
    coolDownY = False
    coolDownX = False



        #seting thr money to 0 at the start of the game
    money = 0
        # Making the "Your balance" labble
    moneyL = Label(win, text="Your balance = 0", font=("Arial", 20))
        # Making the money dispaly on the 425x425 window
    def moneyyyy():
        global money, moneyL, totalMoneyL, totalMoney

        moneyL.config(text=f"Your balance = {money}")
        moneyL.place(x=140, y=12.5)
        totalMoneyL.config(text=f"Total Money: {totalMoney}")



    global IncreaseRadiuscost
        # Increase the balls radius by 2.5          100$     25% more expensive (exponential) 100x1.25^x
    def radiusIncrease():
    # Making the cost label and placing it
        global IncreaseRadiuscost, radiusCost, ball,radius, ballsList

        if money >= radiusCost:
            radius+=10
            radiusCost = m.floor(radiusCost * 1.25)
            IncreaseRadiuscost.config(text=radiusCost)
            temp = len(ballsList)
            for i in ballsList:
                canvas.delete(i)
            ballsList = []
            for i in range(temp):
                rand  = r.randrange(10,300)
                rand2  = r.randrange(10,300)
                ballsList.append(canvas.create_oval(rand,rand2,rand+2*radius,rand2+2*radius))

        
    radiusB = Button(win, text ="Increase Radius", command = radiusIncrease)
    radiusB.place(x=20,y=125)
    IncreaseRadiuscost = Label(win, text=radiusCost, bg="white", font=("Arial", 20))
    IncreaseRadiuscost.place(x=20, y=150)



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
    xspeedB = Button(win, text ="Increase X-axis speed", bg="white" , command = XaxisSpeed)
    xspeedB.place(x=25,y=50)
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
    yspeedB = Button(win, text ="Increase Y-axis speed", command = YaxisSpeed)
    yspeedB.place(x=225,y=50)
        # Making the cost labble and placing it
    global YaxisCost
    YaxisCost = Label(win, bg="white", text="5", font=("Arial", 20))
    global yspeedcost
        # Changing the base cost of the 7-axis speed increse
    yspeedcost = 5
    YaxisCost.place(x=300, y=77.5)





    global cornerCost, cornerCostL
    cornerCost =100

    cornerCostL = Label(win, bg="white",text=cornerCost,font=('Arial',20))
    cornerCostL.place(x=275,y=155)
        # Multiply the points by 3 if it hits a corner    100$    25% more expensive (exponential)
    def cornerMultiplier():
        global cornerMult, cornerB, cornerCost, money, cornerCostL
        if money >= cornerCost:
            money -= cornerCost
            cornerCost = m.floor(cornerCost * 1.25)
            cornerMult += 2
            cornerCostL.config(text=cornerCost)
    cornerB = Button(win, text ="corner multiplier", command = cornerMultiplier)
    cornerB.place(x=275,y=125)




    global prestigecost, prestigecostlable    
    prestigecost = 1000000
    prestigecostlable = Label(win, bg="white", text=prestigecost, font=("Arial", 20))
    prestigecostlable.place(x=180, y=277.5)
    # Making the prestige button
    def prestige():
        global prestigecost, ballsList, speedList,money, prestigecostlable, radius
        if money >= prestigecost:
            money -= prestigecost
            prestigecost = m.floor(prestigecost * 2.5)      # Exponetal
            prestigecostlable.config(text=prestigecost)
            prestigecostlable.place(x=180, y=277.5)
            ballsList.append(canvas.create_oval(10,10,10+radius*2,10+radius*2))
            speedList.append([speedList[0][0],speedList[0][1]])
    prestigeB = Button(win, text="prestige", command=prestige)
    prestigeB.place(x=177.5, y=250)

    






    ''' NOT WORKING
    def Gamer_ball():
        global Gamerball
        Gamerball = True
        # RGB ball (cycling through red, green, blue)
    gamerB = Button(win, text ="GAMER ball", command = Gamer_ball)
    gamerB.place(x=163,y=125)
        # Changes the color evrey 2 seconds'''
    



        # Seting the x axis speed amd the y axis speed, also creating the ball
    def ballvar():
        global money, moneyL, win, totalMoney, ballsList, speedList, YaxisCost, XaxisCost, Button
        moneyL = Label(win, text=f"Your balance = 0", font=("Arial", 20))


        ballsList = [canvas.create_oval(10,20,50,60)]
        
        while True:
            for i in range(len(ballsList)):
                ball = ballsList[i]
                canvas.move(ball, speedList[i][0], speedList[i][1])
                pos = canvas.coords(ball)
                # Making the ball bounce agesnst the walls (set to a little below canvas size)
                if pos[2] >=758 or pos[0] <0:
                    speedList[i][0] = -speedList[i][0]
                    if pos[3] >=758 or pos[1]<0:
                        money += cornerMult
                        totalMoney += cornerMult
                    else:
                        money +=1   # Adding money on if the ball hits a wall on the x-axis
                        totalMoney += 1


                        

                    if totalMoney >= 100000:  # Win6
                        win.config(bg="purple")
                        YaxisCost.config(bg="purple")
                        XaxisCost.config(bg="purple")
                        xspeedB.config(highlightbackground="purple")
                        yspeedB.config(highlightbackground="purple")
                        yspeedB.config(highlightbackground="purple")
                        radiusB.config(highlightbackground="purple")
                        cornerB.config(highlightbackground="purple")
                        cornerCostL.config(bg="purple")
                        prestigeB.config(highlightbackground="purple")
                        prestigecostlable.config(bg="purple")
                        moneyL.config(bg="purple")
                        totalMoneyL.config(bg="purple")
                        IncreaseRadiuscost.config(bg="purple")
                    elif totalMoney >= 10000:   # Win5
                        win.config(bg="pink")
                        YaxisCost.config(bg="pink")
                        XaxisCost.config(bg="pink")
                        xspeedB.config(highlightbackground="pink")
                        yspeedB.config(highlightbackground="pink")
                        yspeedB.config(highlightbackground="pink")
                        radiusB.config(highlightbackground="pink")
                        cornerB.config(highlightbackground="pink")
                        cornerCostL.config(bg="pink")
                        prestigeB.config(highlightbackground="pink")
                        prestigecostlable.config(bg="pink")
                        moneyL.config(bg="pink")
                        totalMoneyL.config(bg="pink")
                        IncreaseRadiuscost.config(bg="pink")
                    elif totalMoney >= 1000:   # Win4
                        win.config(bg="orange")
                        YaxisCost.config(bg="orange")
                        XaxisCost.config(bg="orange")
                        xspeedB.config(highlightbackground="orange")
                        yspeedB.config(highlightbackground="orange")
                        yspeedB.config(highlightbackground="orange")
                        radiusB.config(highlightbackground="orange")
                        cornerB.config(highlightbackground="orange")
                        cornerCostL.config(bg="orange")
                        prestigeB.config(highlightbackground="orange")
                        prestigecostlable.config(bg="orange")
                        moneyL.config(bg="orange")
                        totalMoneyL.config(bg="orange")
                        IncreaseRadiuscost.config(bg="orange")
                    elif totalMoney >= 100:  # Win3
                        win.config(bg="green")
                        YaxisCost.config(bg="green")
                        XaxisCost.config(bg="green")
                        xspeedB.config(highlightbackground="green")
                        yspeedB.config(highlightbackground="green")
                        yspeedB.config(highlightbackground="green")
                        radiusB.config(highlightbackground="green")
                        cornerB.config(highlightbackground="green")
                        cornerCostL.config(bg="green")
                        prestigeB.config(highlightbackground="green")
                        prestigecostlable.config(bg="green")
                        moneyL.config(bg="green")
                        totalMoneyL.config(bg="green")
                        IncreaseRadiuscost.config(bg="green")
                    elif totalMoney >= 50:  # Win2
                        win.config(bg="red")
                        YaxisCost.config(bg="red")
                        XaxisCost.config(bg="red")
                        xspeedB.config(highlightbackground="red")
                        yspeedB.config(highlightbackground="red")
                        yspeedB.config(highlightbackground="red")
                        radiusB.config(highlightbackground="red")
                        cornerB.config(highlightbackground="red")
                        cornerCostL.config(bg="red")
                        prestigeB.config(highlightbackground="red")
                        prestigecostlable.config(bg="red")
                        moneyL.config(bg="red")
                        totalMoneyL.config(bg="red")
                        IncreaseRadiuscost.config(bg="red")
                    elif totalMoney >= 10:  # Win1
                        win.config(bg="blue")
                        YaxisCost.config(bg="blue")
                        XaxisCost.config(bg="blue")
                        xspeedB.config(highlightbackground="blue")
                        yspeedB.config(highlightbackground="blue")
                        yspeedB.config(highlightbackground="blue")
                        radiusB.config(highlightbackground="blue")
                        cornerB.config(highlightbackground="blue")
                        cornerCostL.config(bg="blue")
                        prestigeB.config(highlightbackground="blue")
                        prestigecostlable.config(bg="blue")
                        moneyL.config(bg="blue")
                        totalMoneyL.config(bg="blue")
                        IncreaseRadiuscost.config(bg="blue")
                        

                    moneyyyy()
                if pos[3] >=758 or pos[1]<0:
                    speedList[i][1] = -speedList[i][1]
                    if pos[2] >=758 or pos[0]<0:
                        money += cornerMult
                        totalMoney += cornerMult
                    else:
                        money +=1   # Adding money on if the ball hits a wall on the y-axis
                        totalMoney += 1
                



                    
                    if totalMoney >= 100000:  # Win6
                        win.config(bg="purple")
                        YaxisCost.config(bg="purple")
                        XaxisCost.config(bg="purple")
                        xspeedB.config(highlightbackground="purple")
                        yspeedB.config(highlightbackground="purple")
                        yspeedB.config(highlightbackground="purple")
                        radiusB.config(highlightbackground="purple")
                        cornerB.config(highlightbackground="purple")
                        cornerCostL.config(bg="purple")
                        prestigeB.config(highlightbackground="purple")
                        prestigecostlable.config(bg="purple")
                        moneyL.config(bg="purple")
                        totalMoneyL.config(bg="purple")
                        IncreaseRadiuscost.config(bg="purple")
                    elif totalMoney >= 10000:   # Win5
                        win.config(bg="pink")
                        YaxisCost.config(bg="pink")
                        XaxisCost.config(bg="pink")
                        xspeedB.config(highlightbackground="pink")
                        yspeedB.config(highlightbackground="pink")
                        yspeedB.config(highlightbackground="pink")
                        radiusB.config(highlightbackground="pink")
                        cornerB.config(highlightbackground="pink")
                        cornerCostL.config(bg="pink")
                        prestigeB.config(highlightbackground="pink")
                        prestigecostlable.config(bg="pink")
                        moneyL.config(bg="pink")
                        totalMoneyL.config(bg="pink")
                        IncreaseRadiuscost.config(bg="pink")
                    elif totalMoney >= 1000:   # Win4
                        win.config(bg="orange")
                        YaxisCost.config(bg="orange")
                        XaxisCost.config(bg="orange")
                        xspeedB.config(highlightbackground="orange")
                        yspeedB.config(highlightbackground="orange")
                        yspeedB.config(highlightbackground="orange")
                        radiusB.config(highlightbackground="orange")
                        cornerB.config(highlightbackground="orange")
                        cornerCostL.config(bg="orange")
                        prestigeB.config(highlightbackground="orange")
                        prestigecostlable.config(bg="orange")
                        moneyL.config(bg="orange")
                        totalMoneyL.config(bg="orange")
                        IncreaseRadiuscost.config(bg="orange")
                    elif totalMoney >= 100:  # Win3
                        win.config(bg="green")
                        YaxisCost.config(bg="green")
                        XaxisCost.config(bg="green")
                        xspeedB.config(highlightbackground="green")
                        yspeedB.config(highlightbackground="green")
                        yspeedB.config(highlightbackground="green")
                        radiusB.config(highlightbackground="green")
                        cornerB.config(highlightbackground="green")
                        cornerCostL.config(bg="green")
                        prestigeB.config(highlightbackground="green")
                        prestigecostlable.config(bg="green")
                        moneyL.config(bg="green")
                        totalMoneyL.config(bg="green")
                        IncreaseRadiuscost.config(bg="green")
                    elif totalMoney >= 50:  # Win2
                        win.config(bg="red")
                        YaxisCost.config(bg="red")
                        XaxisCost.config(bg="red")
                        xspeedB.config(highlightbackground="red")
                        yspeedB.config(highlightbackground="red")
                        yspeedB.config(highlightbackground="red")
                        radiusB.config(highlightbackground="red")
                        cornerB.config(highlightbackground="red")
                        cornerCostL.config(bg="red")
                        prestigeB.config(highlightbackground="red")
                        prestigecostlable.config(bg="red")
                        moneyL.config(bg="red")
                        totalMoneyL.config(bg="red")
                        IncreaseRadiuscost.config(bg="red")
                    elif totalMoney >= 10:  # Win1
                        win.config(bg="blue")
                        YaxisCost.config(bg="blue")
                        XaxisCost.config(bg="blue")
                        xspeedB.config(highlightbackground="blue")
                        yspeedB.config(highlightbackground="blue")
                        yspeedB.config(highlightbackground="blue")
                        radiusB.config(highlightbackground="blue")
                        cornerB.config(highlightbackground="blue")
                        cornerCostL.config(bg="blue")
                        prestigeB.config(highlightbackground="blue")
                        prestigecostlable.config(bg="blue")
                        moneyL.config(bg="blue")
                        totalMoneyL.config(bg="blue")
                        IncreaseRadiuscost.config(bg="blue")
                        

                    moneyyyy()
            tk.update()
                # Adusts hoow maay timees thhe balll updattes peeer seec (curently onethousond timess peeer secondd(buttter( \_(-_-)_/ absolte cinima)))
            time.sleep(0.001)



    # !No code below this line!
    #placing the "your balence"
    totalMoneyL = Label(win, text=f"Total Money: 0", font=("Arial", 20))
    totalMoneyL.place(x=140,y=380)
    moneyL.place(x=140, y=12.5)
    ballvar()
    win.mainloop()
title = Label(w,text="BALL GAME", font=("Arial", 50))
title.place(x=300,y=100,anchor="center")
start = Button(w, text ="Start", command = game)
start.place(x=300,y=200, anchor="center")
w.mainloop()
