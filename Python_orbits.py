import pygame,sys
from pygame.locals import *
from math import *
from numpy import *
import os

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Orbits')

objs = 0
pos = []
vel = []
mas = []
rad = []

frame = 0

def new_object (x,y,radius,dx,dy,mass):
    pos.append([x,y])
    vel.append([dx,dy])
    rad.append(radius)
    mas.append(mass)

#in order to create the objects, use the new_objects function above
#and set objs to increase by the total number of objects to be made.

new_object(0,0,5000,0,0,1000000000000000000)
new_object(0,100000,1000,30,0,10000000000)
new_object(0,102500,1000,31.2,0,1)
new_object(0,150000,1000,15.2,0,10000000000)
new_object(0,160000,1000,20.2,0,1)
objs += 4

go = True

DISPLAYSURF.fill((255,255,255))

while go:
    for event in pygame.event.get():
        if event.type == QUIT:
            go = False
    for n in range(250):
        for i in range(objs):
            pos[i][0] += vel[i][0]
            pos[i][1] += vel[i][1]
            for j in range(objs):
                if i != j:
                    dist = ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)**0.5
                    g = 6.673e-11
                    dist -= rad[i] + rad[j]
                    if dist < 0:
                        if mas[i] < mas[j]:
                            mas[j] += mas[i]
                            mas.pop(i)
                            vel.pop(i)
                            pos.pop(i)
                            rad.pop(i)
                            objs -= 1
                        else:
                            mas[i] += mas[j]
                            mas.pop(j)
                            vel.pop(j)
                            pos.pop(j)
                            rad.pop(j)
                            objs -= 1
                    else:
                        theta = arcsin((pos[i][0]-pos[j][0])/(dist+rad[i]+rad[j]))
                        force = g * (mas[i]*mas[j])/dist**2
                        force /= mas[i]
                        xv = force*sin(theta)
                        yv = force*cos(theta)
                        if pos[i][1] > pos[j][1]:
                            vel[i][1] -= yv
                        else:
                            vel[i][1] += yv
                        vel[i][0] -= xv
                        #print(pos[i])
    DISPLAYSURF.fill((255,255,255))
    for i in range(objs):
        pygame.draw.circle(DISPLAYSURF,(i*200,(i*200**2%256),((i*200**3)%256)),(int(pos[i][0]/1000)+250,int(pos[i][1]/1000)+250),int(rad[i]/1000)+3,0)
    pygame.display.update()
