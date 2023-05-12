import pygame as py
import os
import sys
import time
from pygame import mixer

py.init()
def get_highscore():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    high_score_file = os.path.join(script_dir, "HISCORE.txt")
    try:
        with open(high_score_file, "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        print("High score file not found.")
    except ValueError:
        print("Invalid high score format.")

    return high_score


def update_high_score(score):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    high_score_file = os.path.join(script_dir, "HISCORE.txt")
    high_score = get_highscore()
    if score > high_score:
        with open(high_score_file, "w") as file:
            file.write(str(score))
            


W=py.display.set_mode((400,700))
py.display.set_caption("THINKING!!")
py.font.init()

BLUE=(173,216,230)
RED=(255,60,59)
BLACK=(0,0,0)
FRAMES=60
RADIUS=32.5
FONT_LOCATION="PYgame/Assets/BabyDoll.ttf"

Start=py.font.Font(FONT_LOCATION,25)
Best=py.font.Font(FONT_LOCATION,23)
Score=py.font.Font(FONT_LOCATION,30)
TITLE=py.font.Font(FONT_LOCATION,43)
score_update=py.font.Font(FONT_LOCATION,35)
background=py.image.load('PYgame/Assets/Back.jpg')
BALL=py.image.load("PYgame/Assets/basketball.png")
B=py.transform.rotate(py.transform.scale(BALL,(40,40)),210)
HOOP=py.image.load("PYgame/Assets/HOOP.png")
H=py.transform.scale(HOOP,(100,100))



def welcome() : 
    mixer.music.load('PYgame/Assets/MUSIC/main.mp3')
    mixer.music.play(-1)
    time=py.time.Clock()
    game=True
    while game:
        time.tick(FRAMES)
        for event in py.event.get():
            if event.type == py.QUIT:
                game=False
            if event.type == py.KEYDOWN and event.type != py.K_ESCAPE:
                button_sound=mixer.Sound('PYgame/Assets/MUSIC/Button.mp3')
                button_sound.play()
                main()
        objects1()


def balls() : 
    W.blit(B,(10,10))
    W.blit(B,(100,100))
    W.blit(B,(300,50))
    W.blit(B,(60,550))
    W.blit(B,(140,250))
    W.blit(B,(250,400))
    W.blit(B,(310,610))
    #py.display.update()





def objects1() :
    ls=[(10,10),(100,200),(20,50),(30,100)]
    W.blit(background,(0,0))
    balls()
    Start_text=Start.render("Press Any Key To Start ",True,BLACK)
    Best_text = Best.render("Best : " + str(get_highscore()), True, py.Color("black"))
    #Best_text=Best.render("Best : X ",True,BLACK)
    Title_text=TITLE.render("PASS THE BALL ",True,BLACK)
    W.blit(Start_text,(65,500))
    W.blit(Best_text,(145,440))
    W.blit(Title_text,(55,200))
    py.display.update()


def objects2(b,h,score) :
    W.blit(background,(0,0))
    score_text = score_update.render("Score: " + str(score), True, py.Color("black"))
    W.blit(score_text, (20, 20))
    '''Score_text=Score.render("Score :  ",True,BLACK)   
    W.blit(Score_text,(20,20))'''
    W.blit(H,(h.x,h.y))
    W.blit(B,(b.x,b.y))
    py.display.update()

def restart_game():
    global SPEED, GRAVITY, score
    SPEED = 0
    GRAVITY = 0.1
    score = 0
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_y:
                    main()  # restart the game
                elif event.key == py.K_n:
                    #print(get_highscore())
                    py.quit()  # quit the game
                    sys.exit()

        W.blit(background, (0, 0))
        restart_text = Start.render("Do you want to play again? (Y/N)", True, BLACK)
        GAME_OVER_text=TITLE.render("GAME OVER !!",True,RED)
        W.blit(GAME_OVER_text ,(70,300))
        W.blit(restart_text, (10, 380))
        py.display.update()
        py.time.wait(100)


    
def main() :
    SPEED=0
    GRAVITY =0.1
    score =0
    VEL=3
    FALLING = False
    b=py.Rect(165,100,60,60)
    h=py.Rect(120,450,100,100)
    time=py.time.Clock()
    game=True
    while game:
        


        time.tick(FRAMES)
        for event in py.event.get():
            if event.type == py.QUIT:
                game=False
            #print(event)

        key_pressed=py.key.get_pressed()
        if key_pressed[py.K_ESCAPE] :
            welcome()
            break
        if key_pressed[py.K_SPACE] :
            if not FALLING:
                FALLING=True        
        if b.y + RADIUS*2 > 700 :
            gameover_sound=mixer.Sound('PYgame/Assets/MUSIC/gameover.mp3')
            gameover_sound.play()
            score=0           
            SPEED=0
            GRAVITY=0
            
            
            py.display.update()
            py.time.wait(300)
            #if key_pressed[py.K_SPACE] :
            restart_game()

        
        '''if (((b.x - h.x)**2 + (b.y - h.y)**2 )**0.5 )< 50 :
            score=score +1'''
        if b.x > h.x+15 and b.x < h.x + 50 and b.y > h.y:
            score_sound=mixer.Sound('PYgame/Assets/MUSIC/score 2.mp3')
            score_sound.play()
            score += 1
            b.x,b.y = [165,100]
            FALLING = False  # Reset the falling flag
            SPEED = 0
            GRAVITY = 0.1
            update_high_score(score)

        
            #update_score(score)
            '''W.blit(GAME_OVER_text,(70,300))
            py.display.update()
            
            py.time.wait(3000)
            main()'''
        
        h.x+=VEL
        if(h.x + 100 > 400) : 
            VEL=-VEL
        if(h.x < 0) : 
            VEL=-VEL
        if FALLING:
            SPEED+=GRAVITY
        b.y += SPEED
        objects2(b,h,score)
    py.quit()


welcome()
