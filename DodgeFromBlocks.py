from Player import *
from Obstacle import *

pygame.init()


def does_collide(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x \
       and rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y:
        return True
    return False


WIDTH, HEIGHT = 500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

drop = []

pl = pygame.image.load('img/kot.png').convert()
bg = pygame.image.load('img/bg.jpg').convert()
ob = pygame.image.load('img/50x50.png').convert()

all_sprites = pygame.sprite.Group()
obstacle_sprites = pygame.sprite.Group()

player = Player((WIDTH, HEIGHT), pl)
all_sprites.add(player)

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.speed = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed = 0

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.speed = -400 * dt

    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.speed = 400 * dt

    if keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.isJump = True
        player.jump_dt = int(100 * dt)

    if Obstacle.drop:
        r = Obstacle((WIDTH, HEIGHT), ob)
        all_sprites.add(r)
        for elem in obstacle_sprites:
            print(r.rect)
            print(elem.rect)
            if does_collide(r.rect, elem.rect):
                print('collide')
                r.speed = 0
                r.rect.y = 400
        obstacle_sprites.add(r)

    # for elem in obstacle_sprites:
    #     if does_collide(elem.rect, player.rect):
    #         print('collide')

    # Обновление
    all_sprites.update(WIDTH, HEIGHT)
    # Отрисовка
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)

    screen.blit(player.image, player.rect)
    pygame.display.update()
