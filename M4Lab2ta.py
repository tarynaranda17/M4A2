import pygame
import random
 
pygame.init()
 

width, height = 600, 600
size = (width, height)
 
screen = pygame.display.set_mode(size)

 
pygame.display.set_caption("Click and drag to draw")

 

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
colors = [red, green, blue]
 
 
keep_going = True

 

radius = 10
 

pen_size = 5  
 
mousedown = False   
keep_going = True   
 

while keep_going:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
             
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
     
    if mousedown: # start drawing
        spot = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            button_color = colors[0]
  
        elif pygame.mouse.get_pressed()[1]:
            button_color = colors[1]
 
        elif pygame.mouse.get_pressed()[2]:
            button_color = colors[2]
 
        pygame.draw.circle(screen, button_color, spot, radius)
 
    pygame.display.update()
 
pygame.quit()
