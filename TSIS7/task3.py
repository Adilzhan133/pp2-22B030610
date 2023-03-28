"""
Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. 
The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 50
y = 50

clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20

        if x < 25: x = 25
        if x >= 375: x = 375
        if y < 25: y = 25
        if y >= 275: y = 275

        pygame.draw.circle(screen, (255, 0, 0) , (x, y), 25)
        pygame.display.flip()
        clock.tick(60)