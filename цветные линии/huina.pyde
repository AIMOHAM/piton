z = 1
zxc=0
c=0
x=0
def setup():
    background(0)
    size(1000,500)
    strokeWeight(5)
def draw():
    global z, x, c, zxc
    translate(500,250)
    rotate(radians(z))
    line(0,0,100,500)
    stroke(zxc,c,x)
    
    
    
    
    
    x=random(255)
    c=random(255)
    zxc=random(255)
    z+=1



    if mousePressed:
        background(0)
