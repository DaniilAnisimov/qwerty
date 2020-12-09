import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, SIZE_OF_WINDOW, image):
        super().__init__()
        self.height, self.width = 40, 30
        # self.image = pygame.Surface((self.width, self.height))
        # self.image.fill(pygame.Color("white"))

        self.image = image
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect(center=(10, 10))
        self.rect.x = SIZE_OF_WINDOW[0] // 2
        self.rect.y = SIZE_OF_WINDOW[1] - self.height
        self.speed = 0
        self.jump_dt = 1

        self.jumpCount = 10
        self.isJump = False

    def update(self, *args):
        if 0 <= self.rect.x + self.speed <= args[0] - self.width:
            self.rect.x += self.speed
        self.jump()

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                k = -1 if self.jumpCount <= 0 else 1
                self.rect.y -= self.jumpCount ** 2 * k
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
