import pygame
from sys import exit
import math
from settings import *
# from astar import a_star, heuristic

# All player related functionalities in here from looks, positioning, collision, shooting, and movement
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # For setting player image + size
        self.image = pygame.transform.rotozoom(pygame.image.load("characters/pink.png").convert_alpha(), 0, size)
        print(self.image)

        # This is to store the unrotated version of the image so when the mouse is moved, the image looks the same and rotates with me.
        self.base_player_image = self.image

        # Vector's a class for handling position & movement
        self.pos = pygame.math.Vector2(x_beginning, y_beginning)
        # Could also be rewritten as:
        # self.x_pos = x_beginning 
        # self.y_pos = y_beginning
        
        # Create a hitbox rectangle for collision detection
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        
        # Create a rect for positioning and collision detection
        self.rect = self.hitbox_rect.copy()
        
        self.speed = M_speed
        self.shoot = False
        self.gunshot_cd = 0

        # this is to see where the bullet spawns from, relative to the gun. Without this, bullet flies from player's head.
        # self.gun_barrel_offset = pygame.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)

    def player_rotation(self):
        # Get the current mouse coordinates
        self.mouse_coords = pygame.mouse.get_pos()
        
        #  # Calculate the change in x and y between the player's position and the mouse position
        self.x_mouse_coords = (self.mouse_coords[0] - width // 2)
        self.y_mouse_coords = (self.mouse_coords[1] - length // 2)
        
         # Calculate the angle between the player's position and the mouse position in radians
        angle_radians = math.atan2(self.y_mouse_coords, self.x_mouse_coords)

        # Convert the angle from radians to degrees
        self.angle = math.degrees(angle_radians)
    
        # Rotate the player's image based on the calculated angle
        self.image = pygame.transform.rotate(self.base_player_image, self.angle)

        # Update the rect of the rotated image to maintain its position
        self.rect = self.image.get_rect(center=self.hitbox_rect.center)

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        
        # This handles diagonal movement
        if self.velocity_x != 0 and self.velocity_y != 0: 
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        if pygame.mouse.get_pressed() == (1, 0, 0) or keys[pygame.K_SPACE]:
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    def is_shooting(self):
        if self.gunshot_cd == 0:
            self.gunshot_cd = G_cooldown
    
    # Calculate the position for bullet spawn based on aiming line
        aim_vector = pygame.math.Vector2(self.mouse_coords) - pygame.math.Vector2(self.hitbox_rect.center)
    
    # Calculate the offset based on a fraction of the player's image width
        offset = pygame.math.Vector2(self.image.get_width() * 0.5, 0).rotate(-self.angle)
        spawn_bullet_pos = self.hitbox_rect.center + offset

    # Create a new bullet instance
        self.bullet = Bullet(spawn_bullet_pos.x, spawn_bullet_pos.y, self.angle)
    
    # Add the bullet to sprite groups
        bullet_group.add(self.bullet)
        all_sprites_group.add(self.bullet)

    def draw_aiming_line(self, screen):
        pygame.draw.line(screen, (255, 0, 0), self.hitbox_rect.center, self.mouse_coords, 2)

    def move(self):
        # this ensures player doesn't clip OOB
        new_pos = self.pos + pygame.math.Vector2(self.velocity_x, self.velocity_y)
        if 0 <= new_pos.x <= width and 0 <= new_pos.y <= length:
            self.pos = new_pos
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()
        if hasattr(self, 'bullet'):
            self.bullet.update()

 # Calculate the end point of the aiming line based on the mouse position
        self.aiming_line_end = pygame.math.Vector2(self.mouse_coords[0] - width // 2, self.mouse_coords[1] - length // 2)

        if self.gunshot_cd > 0:
            self.gunshot_cd -= 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(enemy_group, all_sprites_group)
        self.image = pygame.transform.rotozoom(pygame.image.load("characters/black.png").convert_alpha(), 0, size)
        self.pos = pygame.math.Vector2(position)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = E_speed

        # new code to test movement
        self.vertical_movement_range = 100  # Adjust this value as needed
        self.is_moving_up = True

    def hunt_player(self):
        player_vector = pygame.math.Vector2(player.hitbox_rect.center)
        enemy_vector = pygame.math.Vector2(self.rect.center)
        distance = self.get_vector_distance(player_vector, enemy_vector)

        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = pygame.math.Vector2()

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        # Alternate between moving up and down within the specified range
        if self.is_moving_up:
            self.velocity = pygame.math.Vector2(0, -self.speed)
            self.position += self.velocity
        else:
            self.velocity = pygame.math.Vector2(0, self.speed)
            self.position += self.velocity

        # Check if the enemy has reached the upper or lower boundary of the movement range
        if self.position.y <= self.rect.centery - self.vertical_movement_range:
            self.is_moving_up = False
        elif self.position.y >= self.rect.centery + self.vertical_movement_range:
            self.is_moving_up = True

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def get_vector_distance(self, vector_1, vector_2):
        return (vector_1 - vector_2).magnitude()
    
    def update(self):
        self.hunt_player()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("bullet/0.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, B_size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = B_speed
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_time = B_time
        self.spawn_time = pygame.time.get_ticks() # gets the specific time that the bullet was created

    def bullet_movement(self):  
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        screen.blit(self.image, self.rect)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_time:
            self.kill() 
            

    def update(self):
        self.bullet_movement()

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0, 0))

    def custom_draw(self):
        self.offset.x = player.rect.centerx - width // 2
        self.offset.y = player.rect.centery - length // 2

        # draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset_pos)

        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

# Initialize pygame
pygame.init()

# Set up display dimensions
screen = pygame.display.set_mode((width, length))

# Game title
pygame.display.set_caption("Mickey with the Blicky")

# Sets up game FPS. Generlly 60 FPS is fine, but 30 if your PC is a potato.
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background/background.jpg").convert(), (width, length))

all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

camera = Camera()
player = Player()



all_sprites_group.add(player)
enemy = Enemy((200,450))

print(enemy.pos)
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    
    
    
    player.update()

    # player.draw_aiming_line(screen)
    
    # checking for collisions
    # pygame.draw.rect(screen, "red", player.hitbox_rect, width=2)
    # pygame.draw.rect(screen, "yellow", player.rect, width=2)

    pygame.display.update()
    clock.tick(FPS)