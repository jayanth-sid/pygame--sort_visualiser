import random
import time
import pygame
global i
global j
global jp
global ip
def bubble(l):
	global i,j,ip
	j=i
	while i < len(l):
		if ip < i:
			ip+=1
			return l
		while j < len(l):
			try:
				if l[j]<l[j+1]:
					t=l[j+1]
					l[j+1]=l[j]
					l[j]=t
					return l,j
			except:
				None
			j+=1
			if j==len(l):
				break
		i+=1
	return l
def draw(display,l):
	global j
	global i,ip
	global jp
	x=0
	y=720
	b_color=(255,160,20)
	for k in range(len(l)):
		if k==j:
			pygame.draw.rect(display,b_color,(x,y,oneblockspace-2,-1*l[k]))
			time.sleep(0.3)
		if k!=j:
			pygame.draw.rect(display,color,(x,y,oneblockspace-2,-1*l[k]))
		x+=oneblockspace
	time.sleep(delay)
i=0
j=0
ip=-1
jp=-1
wWidth=720
blue=(135,205,235)
orange=(255,160,20)
green=(10,200,10)
color=blue
b_color=orange
count=40
delay=0.3
l=[random.randint(100,wWidth-10) for k in range(count)]
if count<720:
	oneblockspace=720//count
else:
	oneblockspace=count//720
display=pygame.display.set_mode((wWidth,wWidth))
on=True

while on:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			on=False
	display.fill((255,255,255))
	l=bubble(l)
	draw(display,l)
	if i>=len(l):
		time.sleep(0.3)
		color=green
		b_color=green
	pygame.display.flip()