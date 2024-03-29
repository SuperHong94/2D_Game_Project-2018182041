from pico2d import *

import game_world
import main_state
import explosion
import game_framework

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN, SPACE = range(9)


framtime=0

#Player
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

playerSpeed=10
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

bullets = []


class IdleState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += playerSpeed
        elif event == LEFT_DOWN:
            player.velocity -= playerSpeed
        elif event == UP_DOWN:
            player.velocityY += playerSpeed
        elif event == DOWN_DOWN:
            player.velocityY -= playerSpeed
        elif event == UP_UP:
            player.velocityY -= playerSpeed
        elif event == DOWN_UP:
            player.velocityY += playerSpeed
        elif event == RIGHT_UP:
            player.velocity -= playerSpeed
        elif event == LEFT_UP:
            player.velocity += playerSpeed
        player.frame=2

        player.timer = 300

    @staticmethod
    def exit(player, event):
        # fill here
        if event == SPACE:
            player.fire_bullet()
        pass

    @staticmethod
    def do(player):
        # player.frame = (boy.frame + 1) % 8
        # fill here
        pass

    @staticmethod
    def draw(player):
        player.image.clip_draw(30 * player.frame, 0, 30, 30, player.x, player.y)


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += playerSpeed
            player.frame=4
        elif event == LEFT_DOWN:
            player.velocity -= playerSpeed
            player.frame=0
        elif event == UP_DOWN:
            player.velocityY += playerSpeed
        elif event == DOWN_DOWN:
            player.velocityY -= playerSpeed
        elif event == UP_UP:
            player.velocityY -= playerSpeed
        elif event == DOWN_UP:
            player.velocityY += playerSpeed
        elif event == RIGHT_UP:
            player.velocity -= playerSpeed
        elif event == LEFT_UP:
            player.velocity += playerSpeed


        player.dir = player.velocity

    @staticmethod
    def exit(player, event):
        # fill here
        if event == SPACE:
            # player.gun_sound = load_wav('resource/gun.wav')
            # player.gun_sound.set_volume(32)
            # player.gun_sound.play(1)

            player.fire_bullet()
        pass

    @staticmethod
    def do(player):
        # player.frame = (player.frame + 1) % 8
        player.timer -= 1
        player.x += player.velocity
        player.y += player.velocityY
        player.x = clamp(25, player.x, 1600 - 25)

    @staticmethod
    def draw(player):
        player.image.clip_draw(30 * player.frame, 0, 30, 30, player.x, player.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState,
                DOWN_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_UP: IdleState,
               DOWN_UP: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,
               SPACE: RunState},
}


class Player:
    y = None
    x = None
    image = None
    font = None

    def __init__(self):

        self.x, self.y = 300, 10
        self.frame = 2  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.direction = 1
        self.velocity = 0
        self.velocityY = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        # self.gun_sound=load_wav('resource/gun.wav')
        # self.gun_sound.set_volume(32)
        # self.gun_sound.play()
        if Player.image == None:
            Player.image = load_image('resource/player(edit).png')
        # if Player.font is None:
        #     Player.font = load_font('ENCR10B.TTF', 20)

    def fire_bullet(self):

        bullet = Bullet(self.x, self.y, 3)
        game_world.add_object(bullet, 1)

        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        # fill here
        return self.x - 15, self.y - 10, self.x + 10, self.y + 13

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        pass

    def draw(self):
        self.cur_state.draw(self)
        #draw_rectangle(*self.get_bb())
       # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % (get_time() - self.start_time), (0, 0, 0))
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class Bullet():
    image = None

    def __init__(self, x=400, y=300, velocity=0.5):
        if Bullet.image == None:
            Bullet.image = load_image('resource/bullet.png')
        self.x, self.y = x, y + 10
        self.speed = velocity


    def draw(self):
         #Bullet.image.clip_draw(0,0,7,7,self.x,self.y)
         self.image.draw(self.x, self.y)
         #draw_rectangle(*self.get_bb())



    def update(self):
        self.y += playerSpeed*1.5
        if self.y < 0 or self.y > 1600 - 25:
            game_world.remove_object(self)
        for enemy in main_state.Enemis:
            if main_state.collide(self, enemy):
                explosions = explosion.Explosion(self.x,self.y )
                game_world.add_object(explosions, 1)
                main_state.Enemis.remove(enemy)
                game_world.remove_object(enemy)
                game_world.remove_object(self)

    def get_bb(self):
        # fill here
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3



