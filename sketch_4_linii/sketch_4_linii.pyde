zxc = 500 #переменная кординат
cxz = 500
def setup():
    size(1000,1000)
    strokeWeight(15)
    stroke(0)
def draw():
    global zxc, cxz
    background(255)
    line(500,500,zxc,zxc)
    line(500,500,zxc,cxz)
    line(500,500,cxz,zxc)
    line(500,500,cxz,cxz)
    zxc-=1
    cxz+=1
