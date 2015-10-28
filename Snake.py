import pygame
import random

#Location of resources locally
game_path = 'C:/Users/Nobody/Desktop/SnakeWithPython/'

pygame.init()

#color scheme
black = (0, 0, 0)
ltGreen = (50, 255, 100)
white = (255, 255, 255)
red = ( 200, 50, 50)

resX = 20; resY = 20
boxW = 20

gameDisplay = pygame.display.set_mode((resX*boxW,resY*boxW))
pygame.display.set_caption('Slither')

i_head = pygame.image.load(game_path + 'Head.png')

FPS = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def disp_message(msg,color):
	text = font.render(msg, True, color)
	gameDisplay.blit(text, [resX/2, resY/2])
	pygame.display.update()

def snakeDraw( snake, boxW ):

	gameDisplay.blit(i_head, (boxW*snake[-1][0], boxW*snake[-1][1]))

	for xy in snake[:-1]:
		specs = [ boxW*xy[0], boxW*xy[1], boxW, boxW]
		pygame.draw.rect(gameDisplay, ltGreen, specs)


def gameLoop():
	gameExit = False; gameOver = False
	x_head = resX/2; y_head = resY/2;

	foodX = random.randrange(0, resX-1)
	foodY = random.randrange(0, resY-1)

	snake = [[x_head, y_head]]
	snakeLength = 10

	go = 'R'

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(black)
			disp_message("Game Over", white)
			disp_message("q: Quit", white)
			disp_message("c: Restart", white)
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
						#gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					go = 'L'
				if event.key == pygame.K_RIGHT:
					go = 'R'
				if event.key == pygame.K_UP:
					go = 'U'
				if event.key == pygame.K_DOWN:
					go = 'D'

		dir_dx = {'L':-1,'R':1,'D':0,'U':0}		
		dir_dy = {'L':0,'R':0,'D':1,'U':-1}		

		x_head += dir_dx[go]
		y_head += dir_dy[go]

		if x_head == foodX and y_head == foodY:
			snakeLength += 1
			foodX = random.randrange(0, resX-1)
			foodY = random.randrange(0, resY-1)

		if x_head+1>resX or x_head<0 or y_head+1>resY or y_head<0:
			gameOver = True

		gameDisplay.fill((30, 60, 200))
		pygame.draw.rect(gameDisplay, red, [ foodX*boxW, foodY*boxW, boxW, boxW])
		snakeDraw( snake, boxW )
		
		if len(snake) > snakeLength:
			del snake[0]
		snake.append( [x_head, y_head] )
		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()

