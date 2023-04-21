x=0
y=0

def setup():
    size(1000,1000)
    frameRate(60)
def draw():
    global x, y
    clear()
    ellipse(x,y,100,50)
    x+=1
    y+=1
    
    if x == 1000:
        x = 0
        y = 0
    
