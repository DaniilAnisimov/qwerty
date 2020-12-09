import pygame
from random import randint

pygame.init()


def does_collide(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x \
       and rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y:
        return True
    return False


class Obstacle(pygame.sprite.Sprite):
    drop = True

    def __init__(self, SIZE_OF_WINDOW, image):
        super().__init__()
        self.height, self.width = 40, 30
        self.image = image
        self.rect = self.image.get_rect(center=(10, 10))
        self.rect.x = randint(0, 9) * 50
        self.rect.y = 0
        self.speed = 5
        self.enabled = True

    def update(self, *args):
        if not self.enabled:
            return
        if self.rect.y + self.height + self.speed <= args[1]:
            self.rect.y += self.speed
            Obstacle.drop = False
        else:
            self.enabled = False
            Obstacle.drop = True

        # r = Obstacle((WIDTH, HEIGHT), ob)
        # all_sprites.add(r)
        # for elem in obstacle_sprites:
        #     print(r.rect)
        #     print(elem.rect)
        #     if does_collide(r.rect, elem.rect):
        #         print('collide')
        #         r.speed = 0
        #         r.rect.y = 400
        # obstacle_sprites.add(r)


