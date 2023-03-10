zxc = 500 #переменная кординат
cxz = 500
def setup():
    size(1000,1000)
    strokeWeight(150)
    stroke(0)
def draw():
    global zxc, cxz
    background(255)
    point(zxc,zxc)
    point(zxc,cxz)
    point(cxz,cxz)
    point(cxz,zxc)
    zxc-=1
    cxz+=1
