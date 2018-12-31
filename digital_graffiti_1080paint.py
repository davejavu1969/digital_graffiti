# Digital Graffiti - David Pride 2018. CC-BY License. Please feel free to distribute - but do give credit!


import cwiid
import time
import os
import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.mouse.set_visible(0)


cursor_surface = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)

draw_surface = cursor_surface.copy()

cursor_surface.fill((34,34,34))
pygame.display.update()
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.mouse.set_visible(0)


cursor_surface.fill((34,34,34))
pygame.display.update()
digi = pygame.image.load('digital.jpeg')
cursor_surface.blit(digi, (475,400))
pygame.display.update()
time.sleep(1)

cursor_surface.fill((34,34,34))
pygame.display.update()
digi = pygame.image.load('connect.jpeg')
cursor_surface.blit(digi, (400,220))
pygame.display.update()
time.sleep(5)

wm = None

mainloop = True

i=1
img = 1
while not wm:
        for x in range(0,6):
                try:
                        time.sleep(0.5)
                        print ("Bluetooth pairing attempt " + str(i))
                        wm = cwiid.Wiimote("Enter WiiMote MAC address here")
                        wm.led = 1
                        if wm:
                                break

                        
                except RuntimeError:
                        if (i>=5):
                                print("cannot create connection")
                                quit()
                        print ("Error opening wiimote connection")
                        i +=1

print ("Remote #1 Connected")

time.sleep(1)

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
dark_green=(0,102,0)
bright_green=(128,255,0)
blue=(0,0,255)
b_blue=(102,102,255)
pink=(255,0,255)
dark_pink=(153,0,76)
yellow=(255,255,51)
p_yellow=(204,255,153)
purple=(127,0,255)
brown=(102,51,0)
grey=(192,192,192)
taupe=(0,102,102)
black=(0,0,0)

cursor_surface.fill((255,255,255))
draw_surface.fill(white)
pygame.display.update()

font = pygame.font.SysFont('Courier', 24)

#set wiimote to report button presses and accelerometer state - and IR now too! 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_IR

buttons = wm.state['buttons']

acc = wm.state

colour_list = [red,green,dark_green,bright_green,blue,b_blue,pink,dark_pink,taupe, p_yellow, yellow,purple,brown,grey,black,white]

c = 0
size = 10
brush = 0

x1 = 0
y1 = 0

colour = colour_list[c]
                
draw_surface.fill(white)

while mainloop:
        pressed = False
        buttons = wm.state['buttons']
        acc = wm.state
        pos1 = acc['acc']
        but1 = acc['buttons']
        sens = acc['ir_src']
        # Uncomment to print out IR sensor readings
        #print sens
       
        if sens[0] != None and sens [1] != None:
                if x1 > 1920:
                        x1 = 1920 - size

                else:
                        x1 = 1920 - ((sens[0].get('pos')[0]) + (sens[1].get('pos')[0]))
                        
        if sens[0] != None and sens[1] == None:
                if x1 > 1920-size :
                        x1 = 1920-size
                else:
                                x1 = (1920 - size - int(sens[0].get('pos')[0])) - 1015
                        
        if sens[0] == None and sens[1] != None:
                if x1 > 1920-(size):
                        x1 = 1920 - (size)
                else:
                        x1 = 1920 - (size)- (int(sens[1].get('pos')[0]))  

        if x1 <0+size:
                x1 = 0 + size
        if x1 > 1920:
                x1 = 1920 - size

        if sens[0] != None and sens [1] != None:
                if y1 > 999-size:
                        y1 = 999-size

                else:
                        y1 = 999 - size - int(sens[0].get('pos')[1] + int(sens[1].get('pos')[1]))

        if sens[0] != None and sens[1] == None:
                if y1 > 999-size:
                        y1 = 999-size
                else:
                        y1 = 999 - size - (int(sens[0].get('pos')[1]) * 2)

                        
        if sens[0] == None and sens[1] != None:
                if y1 > 999 - size:
                        y1 = 999 - size
                else:
                        y1 = 999 - size - (int(sens[1].get('pos')[1]) *2)

        if y1 < 0 + size:
                y1 = 0 + size
        if y1 > 999-size:
                y1 = 999-size

        pygame.display.update()
        #Read button input here

        if but1 == 8 and not pressed:
                x1 = 960
                y1 = 540
                pressed = True

        if but1 == 256 and not pressed:
                if c == 15:
                        c = 0
                else:
                        c += 1
                colour = colour_list[c]
                pressed = True
                time.sleep(0.1)

        if but1 == 512 and not pressed:
                if c == 0:
                        c = 15
                else:
                        c -= 1
                colour = colour_list[c]
                pressed = True
                time.sleep(0.1)

        if but1 == 4112:
                pygame.quit()

        if but1 == 1 and not pressed:
                
                image = pygame.Rect(0,0,1920,1000)
                sub = draw_surface.subsurface(image)
                filename = "image%d.jpg" % img
                pygame.image.save(sub, filename)
                img += 1
                #print("Saved image%img.jpeg" % img)
                
        if but1 == 2048 and not pressed:
                if size == 30:
                        size = 30
                else:
                        size += 1
                pressed = True
                
        if but1 == 1024 and not pressed:
                if size == 2:
                        size = 2
                else:
                        size -= 1
                pressed = True
                
        if but1 == 16 and not pressed:
                pygame.draw.rect(draw_surface, white, (5,1005,65,65))
                pygame.display.update()
                if brush == 0:
                        brush = 1
                else:
                        brush = 0
                pressed = True
                time.sleep(0.1)

        if but1 == 2 and not pressed:
                draw_surface.fill((255,255,255))
                pygame.display.update()
                time.sleep(0.5)
                
        if but1 == 4 and brush == 0:
                pygame.draw.circle(draw_surface, colour, (x1,y1), size)
                
        if but1 == 4 and brush == 1:
                pygame.draw.rect(draw_surface, colour, (x1,y1,size,size))
                
        pygame.draw.lines(draw_surface, black, True, [(0,1000), (1917,1000), (1917,1077), (0,1077)], 3)
        
        if brush == 0 and colour != white:
                pygame.draw.circle(draw_surface, white, (35,1040), (size+1))
                pygame.draw.circle(draw_surface, colour, (35,1040), size)
        if brush == 0 and colour == white:
                pygame.draw.circle(draw_surface, white, (35,1040), (size+1))
                pygame.draw.circle(draw_surface, black, (35,1040), size)
                pygame.draw.circle(draw_surface, white, (35,1040), (size-1))
                

        if brush == 1:
                pygame.draw.rect(draw_surface, white, (16,1025,size+1,size+1))              
                pygame.draw.rect(draw_surface, colour, (16,1025,size,size))

        cursor_surface.fill(white)
        cursor_surface.blit(draw_surface, (0, 0))
        if brush == 0:
                pygame.draw.circle(cursor_surface, colour, (x1,y1), size)
        if brush == 1:
                pygame.draw.rect(cursor_surface, colour, (x1,y1,size,size))
        pygame.display.update()                       

        pygame.display.update()

pygame.quit()

        
        
        



