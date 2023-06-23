#=====================
# Comp Sci 30
# Final Project
# Isiah Hauck
#=====================

import pygame
import random

# Score
score = 0
high_score = 0


# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_lives():
    font = pygame.font.SysFont(None, 30)
    text = font.render("Lives: " + str(player.lives), True, WHITE)
    win.blit(text, (10, 40))

def reset_score():
    global score
    score = 0

# Load the current high score
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score_data = file.readline().strip().split(":")
            return high_score_data[0], int(high_score_data[1]), int(high_score_data[2])
    except FileNotFoundError:
        return "", 0, 0


# Load initial high score and top high score
high_score_name, high_score, top_high_score = load_high_score()

# Define top high score
top_high_score = high_score

def update_top_high_score():
    global top_high_score
    if high_score > top_high_score:
        top_high_score = high_score
        

def save_top_high_score():
    with open("high_score.txt", "w") as file:
        file.write(high_score_name + ":" + str(high_score) + ":" + str(top_high_score))

def display_leaderboard():
    win.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 60)
    text1 = font.render("Leaderboard", True, WHITE)
    text2 = font.render("Top High Score: " + str(top_high_score), True, WHITE)
    win.blit(text1, (WIDTH // 2 - text1.get_width() // 2, 100))
    win.blit(text2, (WIDTH // 2 - text2.get_width() // 2, 200))

    pygame.display.update()

# Player class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.lives = 3
        self.shoot_delay = 0
        self.shoot_cooldown = 10

    def draw(self):
        pygame.draw.rect(win, GREEN, (self.x, self.y, self.width, self.height))

    def move_left(self):
        if self.x > 0:
            self.x -= self.vel

    def move_right(self):
        if self.x < WIDTH - self.width:
            self.x += self.vel

    def shoot(self):
        if self.shoot_delay == 0:
            bullets.append(Bullet(self.x + self.width // 2, self.y))
            self.shoot_delay = self.shoot_cooldown

    def hit(self):
        self.lives -= 1
        if self.lives == 0:
            global game_over
            game_over = True

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.vel = 10

    def draw(self):
        pygame.draw.circle(win, RED, (self.x, self.y), self.radius)

    def move(self):
        self.y -= self.vel

    def collision(self, target):
        if target.x <= self.x <= target.x + target.width and target.y <= self.y <= target.y + target.height:
            return True
        return False

# Target class
class Target:
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def draw(self):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.vel

# Create instances of the classes
player = Player(400, 500, 50, 50)
bullets = []
targets = []
clock = pygame.time.Clock()
game_over = False
start_screen = True

def redraw_window():
    win.fill((0, 0, 0))
    
    # Display score and high score
    font = pygame.font.SysFont(None, 30)
    text_score = font.render("Score: " + str(score), True, WHITE)
    text_top_high_score = font.render("Top High Score: " + str(top_high_score), True, WHITE)
    win.blit(text_score, (WIDTH - text_score.get_width() - 10, 10))
    win.blit(text_top_high_score, (10, 10))
    
    # Call the draw_lives() function
    draw_lives()

    if start_screen:
        # Draw start screen elements
        font = pygame.font.SysFont(None, 60)
        text1 = font.render("Target Shooter", True, WHITE)
        text2 = font.render("Use A and D to move and W to shoot", True, WHITE)
        text3 = font.render("You have 3 lives", True, WHITE)
        text4 = font.render("Press X to start", True, WHITE)
        win.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 200))
        win.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 - 100))
        win.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2))
        win.blit(text4, (WIDTH // 2 - text4.get_width() // 2, HEIGHT // 2 + 100))
    elif not game_over:
        # Draw gameplay elements
        player.draw()
        for bullet in bullets:
            bullet.draw()
        for target in targets:
            target.draw()
    else:
        font = pygame.font.SysFont(None, 60)
        text1 = font.render("Game Over", True, WHITE)
        text2 = font.render("Press R to Restart, X to Quit", True, WHITE)

        # Display game over text
        win.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - text1.get_height() // 2))
        win.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + text2.get_height()))


        # Save top high score to the file
        save_top_high_score()
        
        # Update top high score
        update_top_high_score()
        
    pygame.display.update()

# Game loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if start_screen:
        if keys[pygame.K_x]:
            start_screen = False
    elif not game_over:
        if keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_d]:
            player.move_right()
        if keys[pygame.K_w]:
            player.shoot()

        if player.shoot_delay > 0:
            player.shoot_delay -= 1

        for bullet in bullets:
            bullet.move()
            if bullet.y < 0:
                bullets.remove(bullet)

            for target in targets:
                if bullet.collision(target):
                    bullets.remove(bullet)
                    targets.remove(target)
                    score += 1
                    # Update high score if necessary
                    if score > high_score:
                        high_score = score
                        
        if len(targets) < 5 and random.randint(0, 100) < 3:
            targets.append(Target(random.randint(0, WIDTH - 50), 0, 50, 50, random.randint(1, 2)))

        for target in targets:
            target.move()
            if target.y + target.height > HEIGHT:
                targets.remove(target)
                player.hit()
                if player.lives == 0:
                    game_over = True

    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Restart the game
            reset_score()
            player.lives = 3
            bullets = []
            targets = []
            game_over = False
        elif keys[pygame.K_x]:
            run = False


    redraw_window()

# Save top high score before exiting
save_top_high_score()

pygame.quit()
