zxc = 0
img = 0
xxx = 0
zzz = 0
def setup():
    global img, xxx
    size(500,700)
    background(0)
    xxx = loadImage("xxx.jpg")
    img = loadImage("zzz.jpg")
def draw():
    global zxc,img
    background(0)
    textSize(40)
    
    
    if zxc < 50:
        image(xxx,0,0,500,700)
    if zxc > 49:
        image(img,0,0,500,700)
        
        
    text("randomizer 1-100",60,100)
    textSize(100)
    text(zxc,215,400)
    if keyPressed:
        zxc = int(random(100))
        
        
    
