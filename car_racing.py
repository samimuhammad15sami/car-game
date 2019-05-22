#Game developed by Muhammad Sami , Arham Zahid , Mohammad , Syed Armaghan Hashmi , Maaz Ahmed


import pygame
import time
import random 

pygame.init()
display_width = 800
display_height = 600

# were defining color here
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#loading music
car_width = 50
car_height = 100
pygame.mixer.music.load("music.mp3")
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
#loading images
car_img = pygame.image.load("car1.png")
car2_img = pygame.image.load("car2.png")
road_img = pygame.image.load("road.jpg")
crash_img = pygame.image.load("crash.png")
logo = pygame.image.load("logo.png")

# function and logic for menu
def intro():
	intro = True
	menu1_x = 200
	menu1_y = 400
	menu2_x = 500
	menu2_y = 400
	menu_width = 100
	menu_height = 50
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		pygame.display.set_icon(car_img)
		
		pygame.draw.rect(game_display, black, (200, 400, 100, 50))
		pygame.draw.rect(game_display, black, (500, 400, 100, 50))
			
		game_display.fill(white)
		message_display("CAR RACING", 100, display_width/2, display_height/2)
		game_display.blit(logo, ((display_width / 2) - 100, 10))
		pygame.draw.rect(game_display, green, (200, 400, 100, 50))
		pygame.draw.rect(game_display, red, (500, 400, 100, 50))

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		
		if menu1_x < mouse[0] < menu1_x+menu_width and menu1_y < mouse[1] < menu1_y+menu_height:
			pygame.draw.rect(game_display, blue, (200, 400, 100, 50))
			if click[0] == 1:
				intro = False
		if menu2_x < mouse[0] < menu2_x+menu_width and menu2_y < mouse[1] < menu2_y+menu_height:
			pygame.draw.rect(game_display, blue, (500, 400, 100, 50))
			if click[0] == 1:
				pygame.quit()
				quit()
	
		message_display("Go", 40, menu1_x+menu_width/2, menu1_y+menu_height/2)
		message_display("Exit", 40, menu2_x+menu_width/2, menu2_y+menu_height/2)
		
		pygame.display.update()
		clock.tick(50)

def score(counter):
	font = pygame.font.SysFont(None, 20)
	text = font.render("Score : " + str(counter), True, black)
	game_display.blit(text, (0, 0))
	
def enemy_car(enemyx, enemyy, enemy):
	game_display.blit(enemy, (enemyx, enemyy))
	

def car(x, y):
	game_display.blit(car_img, (x, y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()


def message_display(text, size, x, y):
	font = pygame.font.Font("freesansbold.ttf", size)
	text_surface, text_rectangle = text_objects(text, font)
	text_rectangle.center =(x, y)
	game_display.blit(text_surface, text_rectangle)




def crash(x,y):
	game_display.blit(crash_img, (x, y))
	message_display("You Crashed",70,display_width/2,display_height/2)
	pygame.display.update()
	time.sleep(2)
	gameloop() #for restart the game

def gameloop():
	#start by defining the variables for the bg road
	pygame.mixer.music.play(-1)
	bg_x1 = (display_width/2)-(360/2)
	bg_x2 = (display_width/2)-(360/2)
	bg_y1 = 0
	bg_y2 = -600
	bg_speed = 6
	car_x = ((display_width / 2) - (car_width / 2))
	car_y = (display_height - car_height)
	car_x_change = 0
	road_start_x =  (display_width/2)-112
	road_end_x = (display_width/2)+112
	
	enemy_startx = random.randrange(road_start_x,road_end_x-car_width)
	enemy_starty = -600
	enemy_width = 50
	enemy_height = 100
	enemy_speed = 3
	count = 0
	gameExit = False
	
	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					car_x_change = -5
				elif event.key == pygame.K_RIGHT:
					car_x_change = 5
				
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					car_x_change = 0
			
			
		car_x+=car_x_change
		
		if car_x > road_end_x-car_width:
			crash(car_x, car_y)
		if car_x < road_start_x:
			crash(car_x-car_width, car_y)
		
		
		if car_y < enemy_starty + enemy_height:
			if car_x >= enemy_startx and car_x <= enemy_startx+enemy_width:
				crash(car_x-25, car_y-car_height/2)
			if car_x+car_width >= enemy_startx and car_x+car_width <= enemy_startx+enemy_width:
				crash(car_x, car_y-car_height/2)
		
		game_display.fill(white) #display white background

		# displaying and refreshing the bg road
		game_display.blit(road_img, (bg_x1, bg_y1))
		game_display.blit(road_img, (bg_x2, bg_y2))
		game_display.blit(logo, (10, (display_height / 2) - 100))
		game_display.blit(logo, (display_width - 200 - 10, (display_height / 2) - 100))
		car(car_x,car_y) #display car
		enemy_car(enemy_startx, enemy_starty, car2_img)
		score(count)
		count += 1
		enemy_starty += enemy_speed
		
		if enemy_starty > display_height:
			enemy_startx = random.randrange(road_start_x, road_end_x-car_width)
			enemy_starty = -200

		if count > 200:
			enemy_speed += 0.001


		bg_y1 += bg_speed
		bg_y2 += bg_speed
		
		if bg_y1 >= display_height:
			bg_y1 = -600
			
		if bg_y2 >= display_height:
			bg_y2 = -600
			
		
		
		pygame.display.update() # update the screen
		clock.tick(60) # frame per sec
intro()
gameloop()	
