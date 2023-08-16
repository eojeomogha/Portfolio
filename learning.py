# import pygame
# # from sys import exit. This is needed to close pygame without any errors when you quit it

# # Initialize pygame
# pygame.init()

# # Set up display dimensions
# # screen = pygame.display.set_mode((a, b)) where a = width & b = height
# # pygame.display.set_caption("Another Day Another Bully") this is how you title your game
# # clock = pygame.time.Clock() this is used to set framerate so whether it's a potato or high end PC, game runs consistently 
# # test_font = pygame.font.Font(None, 50) where this is used to have any font you want. Takes 2 args, font type + size

# # test_surface = pygame.Surface(a, b) where a's height & b's width
# # test_surface.fill('deeppink') which is used to color our surface cus currently screen.blit has no color
# # test_surface = pygame.image.load() where if I have images already, I can import them here instead of using colors
# # text_surface = test_font.render('Another Day Another Bully', True, 'Red') takes 3 args, name of game, AA i.e. text smoothing which is true/false and a color arg


# # while True:
#   # for event in pygame.event.get(): where "pygame.event.get" gets all the events, and "for event in" loops through them all
#     # if event.type == pygame.QUIT:
#       # pygame.quit() pygame.quit is the opposite of pygame.init so if you run it in isolation.
#       # exit

#       # screen.blit(test_surface, (0,0)) where blit = block image transfer i.e. stacking one surface on another surface. 
#       # 2 args passed which are surface you wanna place & position
#       # screen.blit(text_surface, (300,50))
  
#   #draw all elements
#   #update everything
  
#   # pygame.display.update()
#   # clock.tick(60) basically saying don't run faster than 60fps per second

  
# display_width = 800
# display_height = 600
# game_display = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption("Another Day Another Bully")

# # Define grid size and player position
# grid_size = 50
# player_x = 0
# player_y = 0

# # Define obstacle positions
# obstacles = [(100, 100), (200, 300), (300, 200)]  # Example positions

# # Load player and obstacle images
# player_image = pygame.Surface((grid_size, grid_size))
# player_image.fill((255, 0, 0))  # Red square

# obstacle_image = pygame.Surface((grid_size, grid_size))
# obstacle_image.fill((0, 0, 255))  # Blue square

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Handle player movement
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player_x -= grid_size
#     if keys[pygame.K_RIGHT]:
#         player_x += grid_size
#     if keys[pygame.K_UP]:
#         player_y -= grid_size
#     if keys[pygame.K_DOWN]:
#         player_y += grid_size

#     # Create player and obstacle rectangles for collision detection
#     player_rect = pygame.Rect(player_x, player_y, grid_size, grid_size)

#     # Clear the screen
#     game_display.fill((0, 0, 0))  # Fills the screen with black

#     # Draw game elements
#     game_display.blit(player_image, (player_x, player_y))
#     for obstacle in obstacles:
#         game_display.blit(obstacle_image, obstacle)

#     pygame.display.update()

# # Quit pygame
# pygame.quit()
# quit()
