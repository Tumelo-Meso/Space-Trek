import pygame
import random 
import sound
import utils
#Initializing the game 
pygame.init()
pygame.mixer.init()


WIN = pygame.display.set_mode((utils.SCREEN_WIDTH,utils.SCREEN_HEIGHT))
pygame.display.set_caption("Space Trek")


#Bullets list
bullets = []
#Enemy ships list
enemy_ships = []

#Explosions list 
explosions = []

#Game score
game_score = 0



def drawScreen(player_x,player_y,display_score,timer_text):
    WIN.blit(utils.BG,(0,0))
    WIN.blit(display_score,(10,50))
    WIN.blit(timer_text, (10, 10))
    shipsDrawing()
    bulletsDrawing()
    explosionsDrawing()

    WIN.blit(utils.PLAYER_SHIP,(player_x,player_y))
    
    pygame.display.update()

    
def shipsDrawing():
    for i in range(len(enemy_ships)):
        WIN.blit(utils.ENEMY_SHIP,(enemy_ships[i][0],enemy_ships[i][1]))

def shipsMovement():
    for enemy in enemy_ships[:]:   
        enemy[1] += utils.ENEMY_SHIP_VEL

        if enemy[1]+utils.ENEMY_HEIGHT > utils.SCREEN_HEIGHT:
            enemy_ships.remove(enemy)
            return False
          
    return True

def bulletsDrawing():
    
    for i in range(len(bullets)):
        WIN.blit(utils.BULLET,(bullets[i][0],bullets[i][1]))

def bulletsMovement():
    for bullet in bullets[:]:
        bullet[1] -= utils.BULLET_VEL

        if bullet[1] < -30:
            bullets.remove(bullet)


def checkBulletCollision():
    global game_score

    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], 30, 30)

        for ship in enemy_ships[:]:
            ship_rect = pygame.Rect(ship[0], ship[1],utils.ENEMY_WIDTH, utils.ENEMY_HEIGHT)

            if bullet_rect.colliderect(ship_rect):
                sound.explosion_sound.play()
                explosions.append([ship[0], ship[1], 20]) 
                enemy_ships.remove(ship)
                bullets.remove(bullet)
                game_score+=1
                break


def explosionsDrawing():
    for explosion in explosions[:]:
        WIN.blit(utils.EXPLOSION, (explosion[0], explosion[1]))

        explosion[2] -= 1

        if explosion[2] <= 0:
            explosions.remove(explosion)



def checkGameOver(player_x,player_y):

    global game_score

    
    for ship in enemy_ships[:]:
        ship_rect = pygame.Rect(ship[0], ship[1],utils.ENEMY_WIDTH, utils.ENEMY_HEIGHT)
        player_rect = pygame.Rect(player_x,player_y,utils.PLAYER_WIDTH,utils.PLAYER_HEIGHT)

        if player_rect.colliderect(ship_rect):
            
            enemy_ships.remove(ship)
            return False
    
    return True

def gameOver():
    global game_score
    
    sound.game_over_sound.play()

    while True:
        WIN.fill((0, 0, 0))

        game_over_text =utils.GAME_OVER_FONT.render("YOU LOSE", True, (255, 0, 0))
        score_text = utils.INFO_FONT.render(f"Final Score: {game_score}", True, (255, 255, 255))
        restart_text = utils.INFO_FONT.render("Press R to Restart", True, (255, 255, 0))
        quit_text = utils.INFO_FONT.render("Press ESC to Quit", True, (255, 255, 255))

        WIN.blit(game_over_text, (
            utils.SCREEN_WIDTH//2 - game_over_text.get_width()//2,
            180
        ))

        WIN.blit(score_text, (
            utils.SCREEN_WIDTH//2 - score_text.get_width()//2,
            300
        ))

        WIN.blit(restart_text, (
            utils.SCREEN_WIDTH//2 - restart_text.get_width()//2,
            380
        ))

        WIN.blit(quit_text, (
            utils.SCREEN_WIDTH//2 - quit_text.get_width()//2,
            430
        ))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                if event.key == pygame.K_r:
                    enemy_ships.clear()
                    bullets.clear()
                    game_score = 0
                    utils.ENEMY_SHIP_VEL=0.5
                    main()
                    return



#Main game loop
def main():
    global game_score
    start_time = pygame.time.get_ticks()
    #Player ship coordinates
    player_x = utils.SCREEN_WIDTH//2
    player_y = utils.SCREEN_HEIGHT-utils.PLAYER_HEIGHT
    
    
    sound.engine_sound.play(-1)
    total_counter = 0
    spawn_timer = 0
    timer = 120
    running = True
    while running:
        
        #Updating the pixels
        spawn_timer+=1
        total_counter+=1

        if spawn_timer >= timer:
            enemy_x = random.randint(0,utils.SCREEN_WIDTH-utils.ENEMY_WIDTH-10)
            enemy_ships.append([enemy_x,-20])
            if total_counter>=360:
                if timer>=40:
                    timer-=20
                    total_counter=0
                    utils.ENEMY_SHIP_VEL+=0.2
            spawn_timer = 0
            

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound.laser_sound.play()
                    bullets.append([
                player_x + utils.PLAYER_WIDTH // 2 - 15,
                player_y
            ])
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        timer_text = utils.FONT.render(f"Time: {elapsed_time}", True, (255, 255, 255))
        
        WIN.fill("black")
        #Drawing game objects
        bulletsMovement()
        if not shipsMovement():
            running = False

       
        checkBulletCollision()

        if not checkGameOver(player_x,player_y):
            running = False
        display_score = utils.FONT.render(f"Score: {game_score}", True, (255, 255, 255))
        drawScreen(player_x,player_y,display_score,timer_text)
        
        

        #Player space ship controllers
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and player_x+utils.PLAYER_WIDTH< utils.SCREEN_WIDTH:

            player_x += utils.PLAYER_VEL

        if keys[pygame.K_a] and player_x>0:

            player_x -=utils.PLAYER_VEL

        if keys[pygame.K_w] and player_y>0:
            player_y -=utils.PLAYER_VEL
        
        if keys[pygame.K_s] and player_y+utils.PLAYER_HEIGHT<utils.SCREEN_HEIGHT:
            player_y+= utils.PLAYER_VEL

    

        utils.clock.tick(utils.FPS)

    
    #Ending the game
    gameOver()
    pygame.quit()
    sound.engine_sound.stop()
    
    
    

if __name__ == "__main__":
    main()