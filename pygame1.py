import pygame

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.speed = 5
        self.direction = [1, 1]
        
    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        
        if self.x - self.radius <= 0 or self.x + self.radius >= 600:
            self.direction[0] *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= 400:
            self.direction[1] *= -1
            
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

def main():
    pygame.init()
    
    # set up the window
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Bouncing Ball")
    
    # create a Ball object
    ball = Ball(100, 100, (255, 0, 0))
    
    # game loop
    running = True
    while running:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # update the ball
        ball.move()
        
        # draw the ball
        screen.fill((255, 255, 255))
        ball.draw(screen)
        pygame.display.flip()
        
        # set the frame rate
        pygame.time.delay(10)
    
    # quit the game
    pygame.quit()

if __name__ == "__main__":
    main()
