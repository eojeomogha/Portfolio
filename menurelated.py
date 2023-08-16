import pygame
from menu import Button

# Initialize pygame
pygame.init()

# Set up display dimensions
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Your Game Title")

# Define grid size and player position
grid_size = 50
player_x = 0
player_y = 0

# Define obstacle positions
obstacles = [(100, 100), (200, 300), (300, 200)]  # Example positions

# Define wall positions
walls = [(200, 100), (400, 300)]  # Example wall positions

# Define goal position
goal_position = (display_width - grid_size, display_height - grid_size)

# Define game state
game_state = "start"  # Can be "start", "game", or "game_over"

# Define wall and goal positions
walls = [(200, 100), (400, 300)]  # Example wall positions
goal_position = (display_width - grid_size, display_height - grid_size)

# A* pathfinding algorithm
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star(start, goal):
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_set.remove(current)

        for neighbor in [(current[0] + grid_size, current[1]),
                         (current[0] - grid_size, current[1]),
                         (current[0], current[1] + grid_size),
                         (current[0], current[1] - grid_size)]:
            if neighbor in walls or neighbor in obstacles:
                continue

            tentative_g_score = g_score[current] + grid_size
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None  # No path found


# Draw UI buttons and text
def draw_ui():
    start_button = pygame.Rect(display_width // 2 - 50, display_height // 2 - 25, 100, 50)
    reset_button = pygame.Rect(display_width // 2 - 50, display_height // 2 + 50, 100, 50)
    quit_button = pygame.Rect(display_width // 2 - 50, display_height // 2 + 125, 100, 50)

    pygame.draw.rect(game_display, (255, 0, 0), start_button)
    pygame.draw.rect(game_display, (255, 0, 0), reset_button)
    pygame.draw.rect(game_display, (255, 0, 0), quit_button)

    font = pygame.font.Font(None, 30)
    start_text = font.render("Start", True, (0, 0, 0))
    reset_text = font.render("Reset", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))

    game_display.blit(start_text, (display_width // 2 - 25, display_height // 2 - 15))
    game_display.blit(reset_text, (display_width // 2 - 25, display_height // 2 + 60))
    game_display.blit(quit_text, (display_width // 2 - 20, display_height // 2 + 135))


# Reset the game state
def reset_game():
    global player_x, player_y, path
    player_x = 0
    player_y = 0
    path = a_star((player_x, player_y), goal_position)

path = []  # Initialize path variable

def main_menu():
    while True:
        # Clear the screen
        game_display.fill((0, 0, 0))
        
        # Blit the main menu background
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "game":
            # Handle player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= grid_size
            if keys[pygame.K_RIGHT]:
                player_x += grid_size
            if keys[pygame.K_UP]:
                player_y -= grid_size
            if keys[pygame.K_DOWN]:
                player_y += grid_size

            # Recalculate path
            path = a_star((player_x, player_y), goal_position)

    # Clear the screen
    game_display.fill((0, 0, 0))

    if game_state == "start":
        main_menu()

    elif game_state == "game":
    # Draw game elements
      pygame.draw.rect(game_display, (0, 255, 0), pygame.Rect(goal_position[0], goal_position[1], grid_size, grid_size))  # Goal
    for wall in walls:
        pygame.draw.rect(game_display, (128, 128, 128), pygame.Rect(wall[0], wall[1], grid_size, grid_size))  # Gray walls
    for obstacle in obstacles:
        pygame.draw.rect(game_display, (0, 0, 255), pygame.Rect(obstacle[0], obstacle[1], grid_size, grid_size))  # Blue obstacles

    # Draw path
    if path:
        for node in path:
            pygame.draw.rect(game_display, (0, 255, 0), pygame.Rect(node[0], node[1], grid_size, grid_size))  # Green path

    # Draw player
    pygame.draw.rect(game_display, (255, 255, 0), pygame.Rect(player_x, player_y, grid_size, grid_size))  # Yellow player

    # Check for reaching the goal
    if (player_x, player_y) == goal_position:
        game_state = "game_over"  # Transition to game over state


    elif game_state == "game_over":
        # Draw game over screen
        game_display.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        game_display.blit(game_over_text, (display_width // 2 - 100, display_height // 2))
        draw_ui()

    pygame.display.update()

# Quit pygame
pygame.quit()
quit()
