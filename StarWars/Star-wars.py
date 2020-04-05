import pygame
import time
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
pygame.display.set_icon(icon)
falcon = pygame.image.load("falcons.png")
xshot = pygame.image.load("xshot45.png")
sd = pygame.image.load("sd100.png")
bullet = pygame.image.load("bbullet.png")


playerX = (wt -64)//2
playerY = ht - 93

enemyX = []
enemyY = []


def new_xshot():
	return randint(0,wt-46),randint(30,ht-105)


for i in range(10):
	x,y = new_xshot()
	enemyX.append(x)
	enemyY.append(y)

dx = 0
dy = 0

ex = 0.1
ey = 0 

bY = []
bX = []
shoot = False

ty = -130

def dist(i,j,k,l):
	return ((i-k)**2+(j-l)**2)

def draw_ship(x,y,z):
	screen.blit(z,(int(x),int(y)))

ex = list(randint(5,30)/100 for i in range(10))
running =True
while running:
	screen.fill((20,20,20))



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				dx = -0.5
			if event.key == pygame.K_RIGHT:
				dx = 0.5
			if event.key == pygame.K_SPACE:
				bX.append(playerX + 25)
				bY.append(ht - 100)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				dx = 0
	if ty <3:
		ty += 0.04
	draw_ship(200,ty,sd)
	
	if playerX>wt-64:
		playerX = wt-64
	elif playerX<0:
		playerX = 0

	
	

	for i in range(10):
		enemyX[i] += ex[i]
		draw_ship(enemyX[i],enemyY[i],xshot)
		if enemyX[i] < 0:
			ex[i] = -ex[i]
		if enemyX[i] > wt-46:
			ex[i] = -ex[i]


	for i in range(len(bX)):
		bY[i] -= 0.4
		draw_ship(bX[i],bY[i],bullet)
		# bullet_sound = mixer.Sound("bullet.mp3 ")
		# bullet_sound.play()

	no = len(bX)
	for i in range(no):	
		try:
			if bY[i]<0:
				del bY[i]
				del bX[i]
				no -= 1
			for j in range(10):
				if dist(bX[i]+2,bY[i]+2,enemyX[j]+32,enemyY[j]+32) < 500:
					enemyX[j],enemyY[j] = randint(0,wt-46),randint(30,ht-105)
					ex[i] = randint(5,30)/100
					score += 1
					del bX[i]
					del bY[i]

		except:
			pass

	draw_ship(playerX,playerY,falcon)
	show_score()

	playerX += dx
	playerY += dy
	pygame.display.update()