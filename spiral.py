#!/usr/bin/python3

import pygame
from math import pi,sin,cos
from time import sleep
class spiralAnimation:
    def __init__(self):
        pygame.init()
        self.width=1024
        self.height=768
       
        self.size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.size)
        self.centreX = self.width/2
        self.centreY = self.height/2
        self.col = 0
        self.ang = 4.8

        pygame.display.set_caption("Spiral Animation")
        done = False
        self.clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    done=True 
            self.screen.fill((0,0,0))
            self.drawAnim()
        pygame.quit()
    def sinwv(self,t,frequency,offset,amp):
        return sin(frequency*t+offset)*(amp-1)+amp;
       
    def drawAnim(self):        
        self.screen.fill((0,0,0))
        
        #for (let x =250; x >= 0; x--):
        
        for x in range(250, -1, -1):
            colour = (
            self.sinwv(self.col+x/2,0.05,3,128),
            self.sinwv(self.col+x/2,0.05,1,128),
            self.sinwv(self.col+x/2,0.05,0,128)
            )
            t=self.sinwv(self.ang,1,0,100)/100
            self.col=self.col+0.0021
            self.spiral(t,self.centreX,self.centreY,colour,x,x+16)
            self.ang=self.ang+0.000001
        pygame.display.flip()

    def spiral(self,ang, centreX,centreY,colour,start,stop):
        #for (g = start; g <= stop; g++)
        cords = []
        for g in range(start, stop, 1):
             angle = -ang   * g
             x = round(centreX + (angle * cos(angle)/1))
             y = round(centreY + (angle * sin(angle)/1))
             
             cords.append([x,y])
        
        
        pygame.draw.lines(self.screen, colour, False, cords, 1)
 
      
tmp =  spiralAnimation()
