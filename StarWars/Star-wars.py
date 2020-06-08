import pygame
import time
import random
from random import randint
from pygame import mixer

pygame.init()
score = 0
high_score = 100
wt,ht = 500,600

screen = pygame.display.set_mode((wt,ht))
pygame.display.set_caption("Star Wars")

mixer.music.load("star_wars.mp3")
mixer.music.play(-1)

font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10


def show_score():
	scoreText = font.render("Score: " + str(score),True,(200,200,200))
	screen.blit(scoreText,(textX,textY))

icon = pygame.image.load("icon.png")
bg = pygame.image.load('bg.jpg')
pygame.display.set_icon(icon)
falcon = pygame.image.load("falcons.png")
xshot = pygame.image.load("xshot45.png")
sd = pygame.image.load("sd120.png")
bullet = pygame.image.load("bbullet.png")


playerX = (wt -64)//2
playerY = ht - 93

enemyX = []
enemyY = []


def new_xshot():
	return randint(0,wt-46),randint(30,ht-300)


for i in range(10):
	x,y = new_xshot()
	enemyX.append(x)
	enemyY.append(y)

dx = 0
dy = 0

ex = list(randint(5,30)/100 * random.choice([-1,1]) for i in range(10))
ey = 0.1

bulletY = []
bulletX = []
shoot = False

ty = -130

def dist(i,j,k,l):
	return ((i-k)**2+(j-l)**2)

def draw_ship(x,y,z):
	screen.blit(z,(int(x),int(y)))


running =True
while running:
	screen.fill((20,20,20))
	screen.blit(bg,(0,0))



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bulletX.append(playerX + 25)
				bulletY.append(ht - 100)
			if event.key == pygame.K_LEFT:
				dx = -0.5
			if event.key == pygame.K_RIGHT:
				dx = 0.5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				dx = 0
	if ty <3:
		ty += 0.04
	draw_ship(190,ty,sd)
	
	if playerX>wt-64:
		playerX = wt-64
	elif playerX<0:
		playerX = 0

	
	

	for i in range(10):
		enemyX[i] = enemyX[i] + ex[i]
		enemyY[i] += ey
		draw_ship(enemyX[i],enemyY[i],xshot)
		if enemyX[i] < 0:
			ex[i] = -1 * ex[i]
		if enemyX[i] > wt-46:
			ex[i] = -1 * ex[i]


	for i in range(len(bulletX)):
		bulletY[i] -= 0.4
		draw_ship(bulletX[i],bulletY[i],bullet)
		# bullet_sound = mixer.Sound("bullet.mp3 ")
		# bullet_sound.play()

	no = len(bulletX)
	for i in range(no):	
		try:
			if bulletY[i]<0:
				del bulletY[i]
				del bulletX[i]
				no -= 1
			for j in range(10):
				if dist(bulletX[i]+2,bulletY[i]+2,enemyX[j]+32,enemyY[j]+32) < 500:
					enemyX[j],enemyY[j] = randint(0,wt-46),randint(30,ht-300)
					ex[i] = randint(5,30)/100
					score += 1
					del bulletX[i]
					del bulletY[i]

		except:
			pass

	draw_ship(playerX,playerY,falcon)
	show_score()

	playerX += dx
	playerY += dy
	pygame.display.update()