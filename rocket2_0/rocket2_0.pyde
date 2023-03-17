y = 900
y2 = 860
y3 = 600
y4 = 500
y5 = 700
def setup():
    fullScreen()
    background(255)
    fill(0)
    frameRate(60)

def draw():
    background(255)
    global y, y2, y3, y4, y5
    rect(960,y,40,70)
    rect(900,y,40,70)
    rect(1020,y,40,70)
    rect(900,y2,160,40)
    
    
    noFill()
    strokeWeight(5)
    rect(900,y3,160,300)
    
    triangle(900,y3,1060,y3,980,y4)
    ellipse(980,y5,130,130)
    
    y-=1
    y2-=1
    y3-=1
    y4-=1
    y5-=1    
