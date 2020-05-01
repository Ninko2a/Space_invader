import pygame
from game import Game
pygame.init()

clock = pygame.time.Clock()

# create window
pygame.display.set_caption("space invader")
screen = pygame.display.set_mode((1280, 720))

# load background
background = pygame.image.load("data game/background.jpg").convert()
background = pygame.transform.scale(background, (1600, 900))

# load music
# background_music = pygame.mixer.Channel(0).play(pygame.mixer.Sound("data game/eight_beat.wav"))


# load game
game = Game(screen)

running = True

while running:
    clock.tick(60)

    # insert background
    screen.blit(background, (0, 0))

    # insert player
    game.player.spawn()
    # screen.blit(game.player.image, game.player.rect)

    # if player moves
    game.player.move()

    # insert enemies
    game.enemyList.spawn_enemies()
    game.enemyList.move_enemies()

    # if player shoots
    if game.pressed.get(pygame.K_SPACE):
        game.player.shoot()
    game.player.projectile_list.move_projectiles()
    game.player.projectile_list.delete_projectile()

    # destroy enemies
    game.enemyList.delete_enemy()

    # collisions
    game.collisions.playerVSenemies()
    # game.collisions.projectilesVSenemies()

    # if player crash
    # game.player.crash()


    # refresh window
    pygame.display.flip()

    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game over")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
