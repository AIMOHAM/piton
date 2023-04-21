y = 0
def setup():
    size(1000,1000)

def draw():
    global y
    clear()
    stroke(255)
    strokeWeight(y)
    point(500,500)
    
    y +=1
    
    if y == 500:
        y=0
