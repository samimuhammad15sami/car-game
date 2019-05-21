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
