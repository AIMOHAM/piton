x = 0
y = 0
q = 0
w = 0
e = 0
r = 0
def setup():
    size(1000,500)
    frameRate(60)
    strokeWeight(100)    


def draw():
    global x, y, q, w, e, r
    #   красный цвет
    stroke(x,0,0)
    point(50,50)
     
     #  зеленый цвет
    stroke(0,y,0)
    point(150,50)
    
    #  синий цвет
    stroke(0,0,q)
    point(250,50)
    
    #  желтый цвет
    stroke(w,w,0)
    point(350,50)
    
    #  голубой цвет
    stroke(0,e,e)
    point(450,50)
    
    #  фиолетовый цвет
    stroke(r,0,r)
    point(550,50)
    
    x+=0.1
    y+=0.5
    q+=0.2
    w+=0.3
    e+=0.6
    r+=0.8
    
    if x > 255*60:
        if y > 255*60:
            if q > 255*60:
                if w > 255*60:
                    if e > 255*60:
                        if r > 255*60:
                            noLoop()
