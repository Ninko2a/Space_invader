# import pygame
from time import time
from projectile import ProjectileList


class Collisions:

    def __init__(self, screen, player, enemy_list):
        self.player = player
        self.enemy_list = enemy_list
        self.projectile_list = ProjectileList(screen)
        self.last_collision_time = 0
        self.latency = 2

    def playerVSenemies(self):  # todo find colliding enemy
        time_now = time()
        time_diff = time_now - self.last_collision_time
        rect_list = self.enemy_list.enemies_get_rect()
        if self.player.rect.collidelist(rect_list) != -1:
            if time_diff > self.latency:
                self.player.health -= 20
                self.last_collision_time = time()
            self.player.blink()

            # enemy_colliding = self.player.rect.collidelist(rect_list)
            # for enemies in self.enemy_list:
            #     self.enemy_list.remove(enemy_colliding)


    # def projectilesVSenemies(self):
    #     rect_list = self.enemy_list.enemies_get_rect()
    #     projectiles_rect = self.projectile_list.projectiles_get_rect()
    #     print(projectiles_rect)
    #     for projectiles in projectiles_rect:
    #         if projectiles.rect.collidelist(rect_list) != -1:
    #             print("ok")

