x=200
a=200
z=100
w=100
def setup():
    size(700,700)



def draw():
    global x, z, a, w
    background(255)
    fill(255,255,0)
    rect(0,0,x,x)
    
    fill(0,0,255)
    rect(500,0,a,a)
    fill(0,255,0)
    rect(0,500,z,z)
    fill(255,0,0)
    rect(500,500,w,w)
    w+=0.4
    a-=2
    x-=1
    z+=1
