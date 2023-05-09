zxc = 0
def setup():
     size(600,700)
     background(0)
     textSize(60)
     
def draw():
    global zxc
    background(0)
    
    textSize(60)
        
    text('heads or tails',120,100)
    if zxc == 1:
        text("heads",120,300)        

    if zxc == 2:
        text('tails',120,300)    
            
    
    if keyPressed:
        zxc=int(random(1,3))
    
    
