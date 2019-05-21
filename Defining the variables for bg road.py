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
