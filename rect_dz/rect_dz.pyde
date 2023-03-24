zxc=0

def setup():
    size(700,700)
    frameRate(20)
    
def draw():
    global zxc
    rectMode(CENTER)
    rect(350,350,zxc,zxc)
    
    
    zxc+=1
