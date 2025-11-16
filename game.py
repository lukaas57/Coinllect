
import pygame
from sys import exit
from utils import resource_path
from const import *
from player import Player
from coin import Coin
from counter import Counter
from spike import Spike
from item import Item


pygame.init()
icon = pygame.image.load(resource_path('assets/coin.png'))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Coinllect')
clock = pygame.time.Clock()
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

lose = False

lost = pygame.font.Font(resource_path('assets/fonts/PressStart2P.ttf'), 40)
lostsurf = lost.render('You lost!', False, 'Red')
lostrect = lostsurf.get_rect(center=(SCREEN_WIDTH/2,150))


gameIsRunning = False

player = None
coin = None
counter = None
spike = []
items = []
invul_bar = None


def startNewGame():
    global player, coin, counter, spikes, items, invul_bar
    player = Player()
    coin = Coin()
    counter = Counter()
    spikes = [Spike()]
    items = []


startNewGame()


def draw():
    player.draw(screen)
    coin.draw(screen)


    for spike in spikes:
        spike.draw(screen)

    for item in items:
        item.draw(screen)

    if lose:
        screen.blit(lostsurf, lostrect)

    if player.invuln_timer > 0:
        invul_bar = pygame.Surface((player.invuln_timer * (SCREEN_WIDTH/180), 20))
        invul_bar.fill('sky blue')
        screen.blit(invul_bar, (0,580))

    counter.draw(screen)

def update():
    global spikes, gameIsRunning, lose, items

    player.update()
    if coin.update(player.get_rect(), counter):
        player.invulnerable = True

        if player.invuln_timer < 180:
            player.invuln_timer += FPS/2
            if player.invuln_timer >= 180:
                player.invuln_timer = 180


    for spike in spikes:
        spike.update()

        if spike.collison(player.get_rect()) and not player.invulnerable:
            gameIsRunning = False
            lose = True
            startNewGame()

    if counter.count % 10 == 0 and counter.count != 0 and counter.count != 10 and len(items) == 0:
        item = Item()
        items.append(item)

    for item in items:
        if item.update(player.get_rect(), player, items):
            player.invulnerable = True
            player.invuln_timer = FPS * 3

    required_spikes = 1 + counter.count // 5
    while len(spikes) < required_spikes:
        spikes.append(Spike())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if gameIsRunning == False:
                gameIsRunning = True
                lose = False

            if event.key == pygame.K_SPACE:
                player.dashing = True

    screen.fill('grey20')
    if gameIsRunning:
        update()
    draw()

    pygame.display.update()
    clock.tick(FPS)
