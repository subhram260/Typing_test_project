import random
import sys

import pygame
import time
import difflib
###############################
pygame.init()
screen = pygame.display.set_mode((800,600))
################################

#color
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

#text
start="START"

textX = 225
textY = 150
#######################################
#title
pygame.display.set_caption("Typing Test")
#logo
#icon = pygame.image.load('#png')
#pygame.display.set_icon(icon)
#########################################

class button:
    def __init__(self,color,x,y,width,height,text):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
    def draw(self,win,btntext,fontsize,outline=None):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        pygame.draw.rect(win,(0,0,0),(self.x,self.y,self.width,self.height),outline)
        text(self.x+45,self.y,btntext,fontsize,"BabaPro-Bold.ttf")
    def isOver(self,pos):
        if pos[0]>self.x and pos[0]<self.x+self.width and pos[1]>self.y and pos[1]<self.y+self.height:
            return True
        return False

########################################################
#Display text
def text(x,y,text,size,font):
    font = pygame.font.Font(font, size)
    score = font.render(text, True, (0, 0, 0))
    screen.blit(score, (x, y))
def drawtext(x,y,text,size,font):
    font = pygame.font.Font(font, size)
    score = font.render(text, True, "#352727")
    #length_text=len(text)
    #screen.blit(score,score.get_rect(center =screen.get_rect().center))
    w=score.get_rect(center =(800/2,y))

    #'''
#text_rect = text.get_rect(center=(w / 2, y))
    screen.blit(score,w)#(x,y))


#def isOver(pos):
 #   if pos[0]>280 and pos[0]<250:
  #      if pos[1]>370 and pos[1]<70:
  #          return True
   # return False
############################################

##################################################################################
def play_loop():
    user_text = ''
    Atext=get_sentence()
    t1=0
    typo=False
    end=False
    resultsprint=''

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                sys.exit()
                # background

            screen.fill('#8B9CA0')
            pygame.draw.rect(screen, '#D3D3D3', (27, 27, 746, 546))
            pygame.draw.rect(screen, '#D3D3D3', (27, 27, 746, 546))
            #pygame.draw.rect(screen,(0,0,0),(80,350,650,50),3)
            #pygame.draw.rect(screen,'#ffffff',(80,350,650,50))
            pygame.draw.rect(screen,'#8B9CA0', (27, 27, 746, 140))
            pygame.draw.polygon(screen,'#8B9CA0',[[350,120],[480,120],[415,190]])
            #pygame.draw.polygon(screen,'#8B9CA0',[[398,180],[432,180],[415,200]])
            pygame.draw.line(screen, "#4D3A3A",start_pos=(27,165),end_pos=(390,165),width=2)
            pygame.draw.line(screen, "#4D3A3A",start_pos=(438,165),end_pos=(773,165),width=2)
            pygame.draw.line(screen, "#4D3A3A",start_pos=(27,165),end_pos=(27,572),width=2)
            pygame.draw.line(screen, "#4D3A3A",start_pos=(773,165),end_pos=(773,572),width=2)
            pygame.draw.line(screen, "#4D3A3A",start_pos=(27,571),end_pos=(252,571),width=2)
            pygame.draw.line(screen, "#4D3A3A",start_pos=(500,571),end_pos=(773,571),width=2)

            text(60,50,'Test your typing skill',64, "aAkarRumput.ttf")
            pose = pygame.mouse.get_pos()
###############################################################################
#            if event.type == pygame.MOUSEBUTTONDOWN:
 #               x, y = pygame.mouse.get_pos()
  #              # position of input box
   #             if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
    #                user_text = ''
     #               t1 = time.time()
      #              # position of reset box
       #        # if (x >= 310 and x <= 510 and y >= 390 and self.end):
        #            #self.reset_game()
         #       #    x, y = pygame.mouse.get_pos()
 ###############################################################################################
            if event.type == pygame.MOUSEBUTTONUP:
                    if (pose[0] > 70 and pose[0] < 730 and pose[1] > 350 and pose[1] < 400):
                         t1 = time.time()
                         typo=True
                         print("Mt1=",t1)
                    else:
                        typo=False

            if event.type == pygame.KEYDOWN:
                if end==False:
                    if event.key == pygame.K_BACKSPACE:
                         user_text =user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        #enter
                        #user_text ='daxgcjabshx'
                        resultsprint=result(t1,user_text,Atext)
                        #drawtext(screen,10, 10, resultsprint, 20, "Century Schoolbook 400.ttf")
                        if user_text=='':
                            resultsprint[0]=0
                        results = 'Time:' + str(round(resultsprint[0])) + " secs   Accuracy:" + str(
                            resultsprint[1]) + "%" + '   Wpm: ' + str(round(resultsprint[2]))
                        end=True
                        #print(results)
                    elif typo:
                        user_text += event.unicode
            if typo == True:
                pygame.draw.rect(screen, '#e9e9e9', (80, 350, 650, 50))
            pygame.draw.rect(screen, (0, 0, 0), (80, 350, 650, 50), 3)
            length_text = (len(Atext)//2)*9
            text(400-length_text, 255, Atext, 20, "Century Schoolbook 400.ttf")
            drawtext(100, 373, user_text, 20,"Century Schoolbook 400.ttf")
            if end==True:
                text(210, 470, results, 20, "Century Schoolbook 400.ttf")
            resetbtn=button(green,400,542,155,30,"reset")
            resetbtn.draw(screen,"reset",20,2)

            backbtn=button(red,250,542,155,30,"back")
            backbtn.draw(screen,"back",20,2)

            if event.type==pygame.MOUSEBUTTONDOWN:
                if resetbtn.isOver(pose):
                    end=False
                    user_text=''
                   # resultsprint[0]=0
                    Atext=get_sentence()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if backbtn.isOver(pose):
                    mainloop()




#################################################################################################




       # text_surface=pygame.render(user_text,True,(0,0,0))
       # text(screen,input_text, 274, 26, (250, 250, 250))

#######################################################
        pygame.display.update()
#######################################################
def get_sentence():
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence
######################################################
def accuracy(text1,text2):
    sequence=difflib.SequenceMatcher(isjunk=None,a=text1,b=text2)
    difference=sequence.ratio()*100
    difference=round(difference,1)
    return difference
####################################
def result(t1,usertxt,word):
    #time
    print("rt1=",t1)
    t2=time.time()
    print("rt2=",t2)
    totaltime=int(time.time()-t1)
   # text(300,200,str(totaltime),20,None)

    #accuracy1
    accuracy1=accuracy(word, usertxt)
    # Calculate words per minute
    try:
        wpm = len(usertxt) * 60 / (5 * totaltime)
    except:
        wpm =0

    print(totaltime)
    if totaltime>1613052610:
        totaltime=0
    #results = 'Time:' + str(round(totaltime)) + " secs   Accuracy:" + str(accuracy(word,usertxt)) + "%" + '   Wpm: '+ str(round(wpm))
   # text(10, 10, results, 20, "Century Schoolbook 400.ttf")
    #print(results)
    return  [totaltime,accuracy1,wpm]
#Wpm
#########################################
begin=True





def mainloop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                sys.exit()
             #background

            screen.fill((139, 156, 160))
            pygame.draw.rect(screen, '#D3D3D3', (27, 27, 746, 546))
            #typing text
            text(textX,textY,"Typing test",70,'aAmbangResesi.ttf')

              # mouse
            pos = pygame.mouse.get_pos()

              #text border
            pygame.draw.rect(screen, (255, 192, 25), (155, 130, 500, 100), 8)

            #button
            greenbutton=button(red,280,400,250,70,"")
            greenbutton.draw(screen,start,50,3)

##################################################
#MOUSE OVER BUTTON
            if event.type == pygame.MOUSEBUTTONDOWN:
                if greenbutton.isOver(pos):
                    greenbutton.color = green
                    greenbutton.draw(screen,start,50, 6)
                    running = False
                    play_loop()



            if event.type == pygame.MOUSEMOTION:
                if greenbutton.isOver(pos):
                    greenbutton.color=green
                    greenbutton.draw(screen,start,50, 3)
            if event.type == pygame.MOUSEBUTTONUP:
                if greenbutton.isOver(pos):
                    greenbutton.color = red
                    greenbutton.draw(screen,start,50, 3)





#######################################
        pygame.display.update()
#######################################
mainloop()
#while begin:
 #   for event in pygame.event.get():
  #     if event.type == pygame.QUIT:
   #        begin=False
    #       sys.exit()
     #  else:
      #     mainloop()
   # pygame.display.update()