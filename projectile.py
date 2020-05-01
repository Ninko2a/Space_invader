import pygame
from time import time


class ProjectileList:

    def __init__(self, screen):
        self.projectile_list = []
        self.screen = screen
        self.last_shoot_time = 0
        self.latency = 0.25

    def spawn_projectile(self, x, y):
        time_now = time()
        time_diff = time_now - self.last_shoot_time
        if time_diff > self.latency:
            new_projectile = Projectile(x=x, y=y, screen=self.screen)
            self.projectile_list.append(new_projectile)
            new_projectile.display()
            new_projectile.shoot_sound()
            self.last_shoot_time = time()

    def move_projectiles(self):
        for projectile in self.projectile_list:
            projectile.move()
            projectile.display()

    def projectiles_get_rect(self):
        projectiles_rect = []
        for projectile in self.projectile_list:
            projectiles_rect.append(projectile.rect)
        return projectiles_rect

    def delete_projectile(self):
        for projectile in self.projectile_list:
            if projectile.rect.x > 1280:
                self.projectile_list.remove(projectile)


class Projectile:

    def __init__(self, x, y, screen):
        self.velocity = 60
        self.image = pygame.image.load("data game/green_laser.png")
        self.image = pygame.transform.scale(self.image, (150, 15))
        self.rect = self.image.get_rect().move(x, y)
        self.screen = screen

    def move(self):
        self.rect.left += self.velocity

    def shoot_sound(self):
        pygame.mixer.music.load("data game/laser_sound.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1)

    def display(self):
        self.screen.blit(self.image, self.rect)

