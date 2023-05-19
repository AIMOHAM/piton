zxc = 0
xxx = 0
plus = 100
minus = 100
division = 100
multiplication = 100
def setup():
    size(400,700)
    frameRate(60)
def draw():
    global zxc, plus, minus, division, multiplication
    background(0)
    fill(100)
    rect(0,300,100,100)     #7
    rect(100,300,100,100)   #8
    rect(200,300,100,100)   #9
    rect(0,400,100,100)     #4
    rect(100,400,100,100)   #5
    rect(200,400,100,100)   #6      
    rect(0,500,100,100)     #1
    rect(100,500,100,100)   #2
    rect(200,500,100,100)   #3
    fill(multiplication)
    rect(0,600,150,100)     #*
    fill(division)
    rect(150,600,150,100)   #:
    fill(minus)
    rect(300,400,100,100)   #-
    fill(plus)    
    rect(300,300,100,100)   #+
    
    fill(255,80,0)
    rect(0,200,400,100)     #clear
    fill(255,80,0)
    rect(300,500,100,200)   #= 
    
    fill(255)
    text(zxc,180,190)
################################
#            цифры             #
################################
    textSize(100)
    text("CLEAR",50,285)
    text("1",25,580)
    text("2",125,580)
    text("3",225,580)
    text("4",25,480)
    text("5",125,480)
    text("6",225,480)
    text("7",25,380)
    text("8",125,380)
    text("9",225,380)
    text("+",325,380)
    text("-",335,480)
    
    textSize(150)
    text("*",45,735)
    text(":",200,685)
    textSize(100)
################################
################################
def mouseClicked():
    global zxc, xxx, plus, minus, division, multiplication
###################################
###################################    сложение
###################################
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 1:
                        zxc += 7
                         

    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 1:
                        zxc += 8
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 1:
                        zxc += 9
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 1:
                        zxc += 4
                    
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 1:
                        zxc += 5
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 1:
                        zxc += 6
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 1:
                        zxc += 1                    
                        
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 1:
                        zxc += 2
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 1:
                        zxc += 3
                    
                    
                    
                    
                    
                    
##################################
##################################         умножение, деление, вычитание, сложение                
                    
                    
    if mouseX > 300:
        if mouseX < 400:
            if mouseY > 400:
                if mouseY < 500:
                    xxx = 2
                    
                    
    if mouseX > 300:
        if mouseX < 400:
            if mouseY > 300:
                if mouseY < 400:
                    xxx = 1
    
    if mouseX > 0:
        if mouseX < 150:
            if mouseY > 600:
                if mouseY < 700:
                    xxx = 3
                    
    if mouseX > 150:
        if mouseX < 300:
            if mouseY > 600:
                if mouseY < 700:
                    xxx = 4
    
    if mouseX > 0:
        if mouseX < 400:
            if mouseY > 200:
                if mouseY < 300:
                    zxc = 0
                    
                    
##############################
##############################        вычитание
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 2:
                        zxc -= 7
                         

    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 2:
                        zxc -= 8
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 2:
                        zxc -= 9
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 2:
                        zxc -= 4
                    
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 2:
                        zxc -= 5
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 2:
                        zxc -= 6
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 2:
                        zxc -= 1                    
                        
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 2:
                        zxc -= 2
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 2:
                        zxc -= 3
#################################
################################# умножение
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 3:
                        zxc *= 7
                         

    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 3:
                        zxc *= 8
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 3:
                        zxc *= 9
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 3:
                        zxc *= 4
                    
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 3:
                        zxc *= 5
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 3:
                        zxc *= 6
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 3:
                        zxc *= 1                    
                        
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 3:
                        zxc *= 2
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 3:
                        zxc *= 3
################################
################################    деление
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 4:
                        zxc /= 7
                         

    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 4:
                        zxc /= 8
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 300:
                if mouseY < 400:
                    if xxx == 4:
                        zxc /= 9
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 4:
                        zxc /= 4
                    
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 4:
                        zxc += 5
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 400:
                if mouseY < 500:
                    if xxx == 4:
                        zxc /= 6
                    
    if mouseX > 0:
        if mouseX < 100:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 4:
                        zxc /= 1                    
                        
    if mouseX > 100:
        if mouseX < 200:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 4:
                        zxc /= 2
                    
    if mouseX > 200:
        if mouseX < 300:
            if mouseY > 500:
                if mouseY < 600:
                    if xxx == 4:
                        zxc /= 3
################################                        
    if xxx == 1:
        plus = 0
        
    if xxx != 1:
        plus = 100
        
    if xxx == 2:
        minus = 0
    
    if xxx != 2:
        minus = 100
        
    if xxx == 3:
        multiplication = 0    
        
    if xxx != 3:
        multiplication = 100
           
    if xxx == 4:
        division = 0
        
    if xxx != 4:
        division = 100
