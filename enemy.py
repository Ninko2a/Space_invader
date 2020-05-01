import pygame
from random import randrange
from random import choice
from time import time


class EnemyList:

    def __init__(self, screen):
        self.enemy_list = []
        self.last_enemy_time = 0
        self.screen = screen

    def enemies_get_rect(self):
        enemies_rect = []
        for enemy in self.enemy_list:
            enemies_rect.append(enemy.rect)
        return enemies_rect

    def delete_enemy(self):     # todo optimise this destroy enemy in collision
        for enemy in self.enemy_list:
            if enemy.health <= 0:
                self.enemy_list.remove(enemy)

    def move_enemies(self):
        for enemy in self.enemy_list:
            enemy.move()
            enemy.display()

    def spawn_enemies(self):
        time_now = time()
        time_diff = time_now - self.last_enemy_time
        if time_diff > 3:
            new_enemy = Enemy(self.screen)
            self.enemy_list.append(new_enemy)
            self.last_enemy_time = time()


class Enemy(pygame.sprite.Sprite):
    # TODO remove screen from enemy
    def __init__(self, screen):
        super().__init__()
        self.health = 20
        self.x_velocity = -1
        self.y_velocity = 0
        self.image = pygame.image.load("data game/spaceship_04.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect().move(1300, randrange(0, 650))
        self.direction = choice([True, False])
        self.screen = screen
        self.last_enemy_time = 0

    def move(self):
        self.rect.move_ip(self.x_velocity, 0)

        if self.direction:
            self.y_velocity = -2
        else:
            self.y_velocity = 2

        self.rect.move_ip(0, self.y_velocity)

        if self.rect.top <= 0:
            self.direction = False
        if self.rect.bottom >= self.screen.get_height():
            self.direction = True

    def display(self):
        self.screen.blit(self.image, self.rect)
