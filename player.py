import pygame
from projectile import ProjectileList
from time import time


class Player:

    def __init__(self, screen, pressed):
        self.health = 500
        self.max_health = 100
        self.attack = 10
        self.velocity = 16
        self.image = pygame.image.load("data game/spaceship_01.png")
        self.image2 = pygame.image.load("data game/spaceship_01 hit.png")
        self.explosion_picture = pygame.image.load("data game/explosion.png")
        self.explosion_picture = pygame.transform.scale(self.explosion_picture, (150, 160))
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image2 = pygame.transform.scale(self.image2, (150, 150))
        self.rect = self.image.get_rect().move(50, 250)
        self.screen = screen
        self.pressed = pressed
        self.projectile_list = ProjectileList(screen)
        self.margin_error = 40
        self.last_hit_time = 0
        self.hit_latency = 0.25

    def move(self):
        if self.pressed.get(pygame.K_w) and self.rect.top > -self.margin_error:
            self.rect.move_ip(0, -self.velocity)

        if self.pressed.get(pygame.K_s) and self.rect.bottom - self.margin_error < self.screen.get_height():
            self.rect.move_ip(0, self.velocity)

        if self.pressed.get(pygame.K_d) and self.rect.right < self.screen.get_width():
            self.rect.move_ip(self.velocity, 0)

        if self.pressed.get(pygame.K_a) and self.rect.left > 0:
            self.rect.move_ip(-self.velocity, 0)

    def shoot(self):
        self.projectile_list.spawn_projectile(self.rect.right - self.margin_error, self.rect.y + self.rect.height/2)

    def spawn(self):
        if self.health > 0:
            self.screen.blit(self.image, self.rect)

    def blink(self):
        time_now = time()
        time_diff = time_now - self.last_hit_time
        if time_diff > self.hit_latency:
            self.screen.blit(self.image2, self.rect)
            pygame.mixer.music.load("data game/damage.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(1)
            self.last_hit_time = time()

    def crash(self):
        if self.health <= 0:
            self.screen.blit(self.explosion_picture, self.rect)
            pygame.mixer.music.load("data game/blast.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(1)
