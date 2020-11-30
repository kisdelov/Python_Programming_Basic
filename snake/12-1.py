# 뱀이 게임판 밖으로 나가면 게임이 끝나도록 해야 한다.
# 지금은 뱀이 180도 방향 전환을 할 수 있다. 한번에 90도씩만 방향을 바꿀 수 있어야 한다.
# 뱀이 계속 길어져서 사과를 더 이상 놓을 곳이 없을 때 게임이 올바르게 종료되도록 해야 한다.
# 사과를 먹으면 게임 속도가 점점 더 빨라지도록 해서 난이도를 높여 보자.
# 사과가 한 번에 여러 개씩 나오면 더 재미있을 것 같다.
# 사과가 놓인 뒤 일정한 시간이 지나면 사과의 색이 점점 흐려지다가 사과가 없어지도록 하자.
# 뱀의 머리 블록에서 꼬리 블록으로 갈 수록 색이 점점 변하게 하자.

import pygame
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("뱀피하기")

RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

from datetime import datetime
from datetime import timedelta
import random

DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east',
}

class Snake:
    """뱀 클래스"""
    color = GREEN  # 뱀의 색

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향

    def draw(self, screen):
        """뱀을 화면에 그린다."""
        for position in self.positions:
            draw_block(screen, self.color, position)
    
    def crawl(self):
        """뱀이 현재 방향으로 한 칸 기어간다."""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        """뱀의 방향을 바꾼다."""
        if self.direction == 'north' and direction == 'south':
            self.direction = 'east'
        elif self.direction == 'south' and direction == 'north':
            self.direction = 'west'
        elif self.direction == 'east' and direction == 'west':
            self.direction = 'north'
        elif self.direction == 'west' and direction == 'east':
            self.direction = 'south'
        else:
            self.direction = direction

    def grow(self):
        """뱀이 한 칸 자라나게 한다."""
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y - 1, x))
        elif self.direction == 'south':
            self.positions.append((y + 1, x))
        elif self.direction == 'west':
            self.positions.append((y, x - 1))
        elif self.direction == 'east':
            self.positions.append((y, x + 1))

class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass

class Apple:
    """사과 클래스"""
    color = RED

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.position)

class GameBoard:
    """게임판 클래스"""
    width = 20
    height = 20
    x = range(0, width)
    y = range(0, height)
    # box = [(x[i], y[j]) for i in y for j in x]
    box = []
    
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        for i in self.y:
            for j in self.x:
                self.box.append((self.x[i], self.y[j]))
    
    def draw(self, screen):
        """화면에 게임판의 구성요소를 그린다."""
        self.apple.draw(screen)
        self.snake.draw(screen)
    
    def put_new_apple(self):
        """게임판에 새 사과를 놓는다."""
        self.apple = Apple((random.randint(0, 19), random.randint(0, 19)))
        if len(self.snake.positions) == self.width * self.height:
            exit()
        for position in self.snake.positions:
            if self.apple.position == position:
                self.put_new_apple()
                break


    def process_turn(self):
        """게임을 한 차례 진행한다."""
        self.snake.crawl()
        
        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()
            self.put_new_apple()
            return 'faster'

        if self.snake.positions[0] in self.snake.positions[1:]:
            raise SnakeCollisionException()

        if self.snake.positions[0] not in self.box:
            raise SnakeCollisionException()
        

game_board = GameBoard()
TURN_INTERVAL = timedelta(seconds=0.3)
last_turn_time = datetime.now()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    if TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            if game_board.process_turn() == 'faster':
                TURN_INTERVAL /= 2
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()

    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()