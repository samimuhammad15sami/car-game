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
