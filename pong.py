import pygame
import random

class Paddle:
	SPEED = 10
	def __init__(self, screen, x, y, width, height):
		self.screen = screen
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dir = 0 # -1, 0, 1
		self.score = 0
	def draw(self):
		pygame.draw.rect(self.screen, white, [self.x,self.y,self.width,self.height])

	def move(self, direction):
		_, height = self.screen.get_size()
		if self.y + self.height/2 < height and direction == "down":
			self.y = self.y + self.SPEED
			# self.dir = 1
		elif self.y + self.height/2 > 0 and direction == "up":
			self.y = self.y - self.SPEED
			# self.dir = -1

class Ball:
	SPEED = 15
	def __init__ (self, screen, x, y, size):
		self.screen = screen
		self.x = x
		self.y = y
		self.size = size
		self.xVel = self.SPEED
		self.yVel = random.randint(-10, 10)

	def draw(self):
		self.x = self.x + self.xVel
		self.y = self.y + self.yVel
		pygame.draw.rect(self.screen, white, [self.x,self.y,self.size,self.size])

	def collides(self, paddle1, paddle2):
		if (self.x < paddle1.x + paddle1.width and 
			self.x + self.size > paddle1.x and
			self.y < paddle1.y + paddle1.height and 
			self.y + self.size > paddle1.y):

			self.xVel = -self.xVel

		if (self.x < paddle2.x + paddle2.width and 
			self.x + self.size > paddle2.x and
			self.y < paddle2.y + paddle2.height and 
			self.y + self.size > paddle2.y):

			self.xVel = -self.xVel
			
		width, height = self.screen.get_size()
		if self.y < 0 or self.y + self.size > height:
			self.yVel = -self.yVel

		if self.x < 0:
			paddle2.score += 1
			self.x = width/2
			self.y = height/2
			self.yVel = random.randint(-10, 10)
		if self.x + self.size > width:
			paddle1.score += 1
			self.x = width/2
			self.y = height/2
			self.yVel = random.randint(-10, 10)





pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("pong")

player1 = Paddle(gameDisplay, 10, 400, 20, 120)
player2 = Paddle(gameDisplay, 770, 200, 20, 120)
ball1 = Ball(gameDisplay, 400,300, 10)
ball2 = Ball(gameDisplay, 400,300, 10)
ball3 = Ball(gameDisplay, 400,300, 10)

white = (255,255,255)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pink = (255,114,187)
blue = (79,151,221)
gameExit = False

def write_score(score1, score2):
	display_width, display_height = gameDisplay.get_size()
	font = pygame.font.SysFont(None, 60)
	screen_text = font.render(str(score1) + "|" + str(score2), True, white)
	gameDisplay.blit(screen_text, [display_width/2-25,5])

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	keys = pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		player2.move("down")
	if keys[pygame.K_UP]:
		player2.move("up")
	if keys[pygame.K_w]:
		player1.move("up")
	if keys[pygame.K_s]:
		player1.move("down")
	gameDisplay.fill(black)
	player1.draw()
	player2.draw()
	ball1.draw()
	ball1.collides(player1, player2)
	ball2.draw()
	ball2.collides(player1, player2)
	ball3.draw()
	ball3.collides(player1, player2)
	write_score(player1.score, player2.score)
	pygame.display.flip()	
	pygame.time.wait(40)	

pygame.quit()
quit()
