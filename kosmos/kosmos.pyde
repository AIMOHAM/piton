
def setup():
    fullScreen()
    background(0)
    frameRate(60)
    ellipseMode(CENTER)
def draw():
    stroke(random(55)+200)
    strokeWeight(random(4)+1)
    point(random(1900),random(1000))
