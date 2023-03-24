x=700
def setup():
    size(700,700)
    frameRate(60)
def draw():
    global x
    stroke(random(255),random(255),random(255))
    background(255)
    noFill
    ellipse(350,350,x,x)
    x-=1
