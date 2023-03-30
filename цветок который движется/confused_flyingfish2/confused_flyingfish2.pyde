x = 250
o = 0
def setup():
    size(1000,500)
def draw():
    global x, o
    background(0)
    
    strokeWeight(15)
    stroke(0,125,38)
    line(500,500,500,x)     # стебель
    
    
    
    translate(0,o)
    strokeWeight(100)
    stroke(255)
    point(500,250)            # пыльца
    o-=1
    x-=1
