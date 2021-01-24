

from os import system

robo_x = 4
hp     =int(input("how many lives do you want to have?"))
over   = False
gmap   = [' ','⚠',' ',' ','●',' ','⚠',' ','☠',' ']
option=''

   
while option!='x':
#######################PRINT THE MAP###################
    system('cls')    
    
    print("-"*20)

    for i in range(len(gmap)):
        print(gmap[i],end=" ")

    print()
    print("-"*20)

    for i in range(len(gmap)):
        print(i,end=" ")
    print("\n\nCONTROLS:\na-left\nd-right\nx-exit")
    print("\nLives",hp)
    

    
    #######################PRINT THE MAP###################


    #######################CONTROLS########################
    
    if over:
        print("You failed!!!")
        print("To start a new game press enter")
        break   
    option=input(">>> ")
     
    if option=='a' and robo_x>0:        
        gmap[robo_x]=' '
        robo_x -= 1
        if gmap[robo_x]=='⚠':
            gmap[robo_x]='☠'
            hp-=1
            if hp==0:
                over =True  
        else:
            gmap[robo_x]='●'

    elif option=='d' and robo_x<9:
        gmap[robo_x]=' ' #remove current position
        robo_x+=1
        if gmap[robo_x]=='⚠':
            gmap[robo_x]='☠'
            hp-=1
            if hp==0:
                over =True
        else:
            gmap[robo_x]='●' #place it in the new position
            
           
    elif option=="x":
        print("Game over")
        
  
#######################CONTROLS########################



