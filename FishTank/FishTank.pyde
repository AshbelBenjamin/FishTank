def setup():
    size(600, 400)
    background(0,100,255)
    
    global x, speedX, y, speedY
    x = 100
    speedX = 5
    
def draw():
    global x, speedX, y, speedY
    
    background(0,100,255)
    drawFish(x+5,50,random(255),random(255),random(255))
    delay(100)
    drawFish(x-10,100,255,75,65)
    drawRedFish(x+35,150)
    drawCastle()
    
    for i in range (7):
        drawFish(x+random(200),i + random(200) + 25, random(255),random(255),random(255))
        drawRedFish(x+random(200),i + random(200))
    
    if (x < 25 or x > 550):
        speedX = speedX * -1
 
    # Update position 
    x = x + speedX
 
def drawFish(x,y,fishRed, fishGreen, fishBlue):
    # Code to draw a fish.
    # Don't forget to use parameters to make it customizable.
    fill(fishRed,fishGreen,fishBlue)
    ellipse(x,y,50,30)
    triangle(x+25, y, x+50, y+25, x+50, y-25)
 
 
def drawRedFish(x,y):
    fill(255,0,0)
    ellipse(x,y,30,20)
    triangle(x+15, y, x+25, y+15, x+25, y-15)
    
def drawRedFish(x,y):
    fill(255,0,0)
    ellipse(x,y,30,20)
    triangle(x+15, y, x+25, y+15, x+25, y-15)
    
    
    
def drawCastle():
    fill(237, 201, 175)#Sand Color
    rect(500,300,50,100)#Tower
    triangle(575,300,475,300,525,250)#Tower
    fill(0)#window color
    ellipse(525,325,10,15)#window
    
    fill(237, 201, 175)#Sand Color
    rect(350,375,150,50)#Building
    circle(425, 375, 150)#Dome
    
    fill(237, 201, 175)#Sand Color
    rect(300,300,50,100)#Tower
    triangle(375,300,275,300,325,250)#Tower
    fill(0)#window color
    ellipse(325,325,10,15)#window
