zxc = 0 #переменная кординат
def setup():
    size(1000,1000)
    strokeWeight(150)
    stroke(0)
def draw():
    global zxc
    background(255)
    point(zxc,zxc)
    zxc+=1
