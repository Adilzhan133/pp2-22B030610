"""
Create music player with keyboard controller. 
You have to be able to press keyboard: play, stop, next and previous as some keys. 
Player has to react to the given command appropriately.
"""
import pygame
Background_color = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((800, 300))
screen.fill( Background_color)
done = False
order = 0
songs = ['tsis7/I tried so hard.mp3', 'tsis7/Iphone.mp3']

pygame.mixer.music.load(songs[order])
pygame.mixer.music.play()

font = pygame.font.SysFont("comicsansms", 24)
text1 = font.render("Space - pause music", True, (0, 128, 0))
text2 = font.render("W - unpause music", True, (0, 128, 0))
text3 = font.render("D - next song", True, (0, 128, 0))
text4 = font.render("A - previous song", True, (0, 128, 0))
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
               text = font.render("Current song: " + songs[order], False, (0, 0, 0))
               screen.blit(text, (20, 20))
               pygame.mixer.music.stop()
               order = (order - 1) % len(songs)
               pygame.mixer.music.load(songs[order])
               pygame.mixer.music.play()
        if pressed[pygame.K_d]:
               text = font.render("Current song: " + songs[order], False, (0, 0, 0))
               screen.blit(text, (20, 20))
               pygame.mixer.music.stop()
               order = (order + 1) % len(songs)
               pygame.mixer.music.load(songs[order])
               pygame.mixer.music.play()
        if pressed[pygame.K_w]:  pygame.mixer.music.unpause()
        if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()

        text = font.render("Current song: " + songs[order], True, (128, 0, 0))
        pygame.display.update()
        screen.blit(text, (20, 20))
        screen.blit(text1, (20, 60))
        screen.blit(text2, (20, 100))
        screen.blit(text3, (20, 140))
        screen.blit(text4, (20, 180))

        pygame.event.wait()
        pygame.display.flip()
        clock.tick(30)