zxc = 0
def setup():
    size(600,700)
    background(0)
def draw():
    global zxc,img
    img = loadImage("xxx.jpg")
    image(img,0,0)
    
###########################    
###########################
    if zxc > 0:
        background(random(255),random(255),random(255))    
    
    
    
    
    
    
    
    textSize(100)
    text(zxc,270,350)
    

    
    if keyPressed:
        zxc = int(random(1,100))
    
    
