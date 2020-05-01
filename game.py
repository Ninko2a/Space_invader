from player import Player
from enemy import EnemyList
from collisions import Collisions

# create game class
class Game:

    def __init__(self, screen):
        self.pressed = {}
        self.player = Player(screen, self.pressed)
        self.enemyList = EnemyList(screen)
        self.collisions = Collisions(screen, self.player, self.enemyList)
