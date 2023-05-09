x = 999999
y = 999999
def setup():
    fullScreen()
    background(209)
    frameRate(999)
def draw():
    global x, y
    point(x,y)
    strokeWeight(5)
    if mousePressed:
        x = mouseX
        y = mouseY
        
        
    if keyPressed:
        background(209)
        x = 99999
        y = 99999
