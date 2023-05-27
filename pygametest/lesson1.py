import pygame

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

background = GRAY
screen = pygame.display.set_mode((640, 240))
ball = pygame.image.load("resources\\ball.gif")
rect = ball.get_rect()

speed = [2, 2]
size = 640, 320
width, height = size
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        print(event)
        rect = rect.move(speed)
        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1]
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
        screen.fill(background)
        pygame.draw.rect(screen, RED, rect, 1)
        screen.blit(ball, rect)
        pygame.display.update()
pygame.quit()
