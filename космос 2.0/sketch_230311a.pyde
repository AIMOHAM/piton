zxc = random(255)
def setup():
    fullScreen()
    background(0)
    frameRate(60)
def draw():
    stroke(zxc)
    fill(zxc)
    strokeWeight(random(4)+1)
    point(random(1366),random(768))
    if keyPressed:
        if key == ' ':
            background(0)
