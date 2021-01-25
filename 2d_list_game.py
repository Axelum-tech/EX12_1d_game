from os import system
hp=2
over=False
robo_r=0
robo_c=0
gmap = [
    ['x',' ',' ','⚠',' '],  # 0
    ['⚠',' ',' ',' ',' '],  # 1
    [' ',' ',' ',' ',' '],  # 2
    [' ',' ',' ','⚠',' '],  # 3
    [' ',' ',' ',' ',' ']   # 4
    # 0,  1 , 2 , 3 , 4
]
option=''
control="\nCONTROLS:\na-left\nd-right\nx-exit\ns-down\nw-up\n"

while option!='x':
    system('cls')   
    #######################PRINT THE MAP###################
    print("-"*12)

    for r in range(5):
        print("|",end="")
        for c in range(5):
            print(gmap[r][c],end=" ")
        print("|")

    print("-"*12,end=control)

  

    if over:
        print("YOU FAILED, TRY AGAIN")
        break


    #######################CONTROL OPTION######################
    print("You have",hp,"more lives")
    option=input(">>>>")

    #######################MOVEMENT############################
  
    if option=='d' and robo_c<4:
        gmap[robo_r][robo_c]=' '
        robo_c+=1
        if gmap[robo_r][robo_c]=='⚠':
           gmap[robo_r][robo_c]='☠'
           hp-=1
           if hp==0:
               over=True
        else:
            gmap[robo_r][robo_c]='x'
        
    elif option=='s' and robo_r<4:
        gmap[robo_r][robo_c]=' '
        robo_r+=1
        if gmap[robo_r][robo_c]=='⚠':
            gmap[robo_r][robo_c]='☠'
            hp-=1
            if hp==0:
               over=True
        else:
            gmap[robo_r][robo_c]='x'
    
    elif option=='a' and robo_c>0:
        gmap[robo_r][robo_c]=' '
        robo_c-=1
        if gmap[robo_r][robo_c]=='⚠':
            gmap[robo_r][robo_c]='☠'
            hp-=1
            if hp==0:
               over=True
        else:
            gmap[robo_r][robo_c]='x'

    elif option=='w' and robo_r>0:
        gmap[robo_r][robo_c]=' '
        robo_r-=1
        if gmap[robo_r][robo_c]=='⚠':
            gmap[robo_r][robo_c]='☠'
            hp-=1
            if hp==0:
                over=True
        else:
            gmap[robo_r][robo_c]='x'

    elif option=="x":
        print("GAME OVER")


  


