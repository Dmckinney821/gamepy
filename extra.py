for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    guy.shoot()
 if event.type == pygame.KEYDOWN:
                if event.key == pygame.SPACE:
                    shootBullets
        
def shootBullets():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_SPACE:
            bulletY += -5
            screen.blit(bulletImg,(247,bulletY)) 