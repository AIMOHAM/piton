x=0
def setup():
    size(700,700)
    background(255)
def draw():
    global x
    strokeWeight(x)
    noFill
    ellipse(350,350,500,500)
    line(350,100,450,580)
    
    line(350,100,250,580)
    
    line(250,580,580,250)
    
    line(580,250,120,250)
    
    line(120,250,450,580)
    
    x+=1
