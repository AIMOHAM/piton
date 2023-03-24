x = 0
z =15
def setup():
    size(700,700)
    stroke(255)

def draw():
    global x, z
    strokeWeight(z)
    clear()
    point(x,x)
    x+=1
    z+=3
    
