x=0
y=0
def setup():
    fullScreen()
    background(255)
    
def draw():
    global x, y
    fill(y)
    rect(900,500,100,100)
    rect(700,500,100,100)
    if mouseX > 900:
        if mouseX < 1000:
            if mouseY > 500:
                if mouseY < 600:
                    if x == 0:
                        if mousePressed:
                            background(0)
                            x = 1
                            y = 255
                            
                            
    if mouseX > 700:
        if mouseX < 800:
            if mouseY > 500:
                if mouseY < 600:
                    if x == 1:
                        if mousePressed:
                            background(255)
                            x = 0
                            y = 0
                            
                            
