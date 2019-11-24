import game_framework
from pico2d import *
import game_world

# Player Event
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


class FlyState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == UP_DOWN:
            player.velocityY += 1
        elif event == DOWN_DOWN:
            player.velocityY -= 1
        elif event == UP_UP:
            player.velocityY -= 1
        elif event == DOWN_DOWN:
            player.velocityY += 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        player.dir = player.velocity

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        if player.dir < 0:
            player.frame = 0
        elif player.dir > 0:
            player.frame = 4
        elif player.dir == 0:
            player.frame = 2
        player.x += player.velocity
        player.x = clamp(25, player.x, 800 - 25)

    @staticmethod
    def draw(player):
        player.image.clip_draw(30 * player.frame, 0, 30, 30, player.x, player.y)


next_state_table = {
    FlyState: {RIGHT_UP: FlyState, LEFT_UP: FlyState,
               RIGHT_DOWN: FlyState, LEFT_DOWN: FlyState,
               UP_UP:FlyState,UP_DOWN:FlyState,
               DOWN_UP:FlyState,DOWN_DOWN:FlyState
               }
}


class Player:
    image = None

    def __init__(self):
        if Player.image == None:
            Player.image = load_image('resource/player(edit).png')
        self.x, self.y = 400, 10
        self.frame = 2  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.dir = 0
        self.velocity = 1
        self.velocityY = 1
        self.event_que = []
        self.cur_state = FlyState
        self.cur_state.enter(self, None)
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self.event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
