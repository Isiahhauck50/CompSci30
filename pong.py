import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 400
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_RADIUS = 10
PADDLE_SPEED = 5
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = PADDLE_SPEED

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += self.speed
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Ball(Paddle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Collision with walls
        if self.y <= 0 or self.y >= HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)


# Create paddles and ball
paddle1 = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle2 = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move_up()
    if keys[pygame.K_s]:
        paddle1.move_down()
    if keys[pygame.K_UP]:
        paddle2.move_up()
    if keys[pygame.K_DOWN]:
        paddle2.move_down()

    # Update ball
    ball.update()

    # Collision with paddles
    if ball.x <= paddle1.x + paddle1.width and paddle1.y <= ball.y <= paddle1.y + paddle1.height:
        ball.speed_x *= -1
    if ball.x >= paddle2.x - ball.radius and paddle2.y <= ball.y <= paddle2.y + paddle2.height:
        ball.speed_x *= -1

    # Draw objects
    window.fill((0, 0, 0))
    paddle1.draw()
    paddle2.draw()
    ball.draw()
    pygame.display.update()

    clock.tick(60)

# Quit the game
pygame.quit()



#Difference between OOP and Procedural Coding:
#OOP: Code is organized around objects that have both data and behavior. Objects represent things from the real world, and we can reuse and modify them easily.
#Procedural Coding: Code is organized around procedures or functions that operate on data. It follows a step-by-step approach, focusing on how to perform tasks.

#Differences in Procedural Coding:
#If the Pong game were made using procedural coding, it would have functions for moving paddles, updating the ball, handling collisions, and drawing game elements. Data would be stored in global variables accessible by different functions.

#Benefits of OOP:
#Modularity and Reusability: OOP helps organize code into reusable and independent pieces, making it easier to understand, maintain, and reuse.
#Encapsulation: OOP hides internal details of objects and provides a clear interface to work with them, making code easier to maintain and reducing dependencies.
#Inheritance and Polymorphism: OOP allows classes to inherit properties and behaviors from other classes, promoting code reuse. Polymorphism allows different objects to be treated interchangeably, adding flexibility.

#Drawbacks of OOP:
#Learning Curve: OOP concepts can be more challenging to learn, especially for those used to procedural coding.
#Abstraction Overuse: Overusing abstraction in OOP can make code more complex and harder to understand.
#Performance Overhead: OOP features can introduce some performance overhead compared to procedural code.
#Increased File and Code Size: OOP can result in larger files and more code, which can take more time to develop and compile.
