x = 0
def setup():
    size(500,500)
    
def draw():
    global x
    strokeWeight(100)
    stroke(x)
    point(250,250)
    
    x+=1
    
    if x == 255:
        x=0
