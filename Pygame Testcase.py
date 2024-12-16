import pygame
pygame.init()
screenWidth,screenHeight = (500,500)
window = pygame.display.set_mode((screenWidth,screenHeight))

x,y = (50,50)
width,height = (40,40)
vel = 5

isjump = False
jumpcount = 10
pygame.display.set_caption("First Game")
run = True
while run :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel:
        x-= vel
    if keys[pygame.K_d] and x < screenWidth - width:
        x += vel
    if not(isjump):    
        if keys[pygame.K_w] and y > vel:
            y -= vel
        if keys[pygame.K_s] and y < screenHeight - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= neg * (jumpcount ** 2) * 0.5
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10
    window.fill((0,0,0))
    pygame.draw.rect(window, (0,255,0), (x,y,width,height))
    pygame.display.update() 


    
pygame.quit()
