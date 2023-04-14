img = 0
negr = 0
xuilo = 0
def setup():
    global img, negr, xuilo
    img = loadImage('xxx.jpg')
    negr = loadImage('negr.jpg')
    size(500,500)
    
    image(img, 0,0)
    image(negr,100,300,100,100)
########################################

    rect(100,200,300,300)
    triangle(100,200,250,0,400,200)
    
    noFill()
    rect(300,300,100,200)
    rect(100,300,100,100)
    rect(200,300,100,100)
         
    
def draw():
    
    if keyPressed:
        clear()
        
    global img, negr, xuilo
    negr = loadImage('negr.jpg')
    image(negr,100,300,100,100)
    xuilo = loadImage("xuilo.jpg")
    image(xuilo,200,300,100,100)
