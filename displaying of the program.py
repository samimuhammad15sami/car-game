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


