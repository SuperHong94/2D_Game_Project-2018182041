from pico2d import *

import game_world


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,SLEEP_TIMER,SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN,SDLK_SPACE):SPACE
}

class IdleState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        player.timer = 300

    @staticmethod
    def exit(player, event):
        # fill here
        if event==SPACE:
            player.fire_ball()
        pass

    @staticmethod
    def do(player):
        #player.frame = (boy.frame + 1) % 8
        # fill here
        pass


    @staticmethod
    def draw(player):
      player.image.clip_draw(30*player.frame,0,30,30,player.x,player.y)


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        player.dir = player.velocity

    @staticmethod
    def exit(player, event):
        # fill here
        if event==SPACE:
            player.fire_ball()
        pass

    @staticmethod
    def do(player):
        #player.frame = (player.frame + 1) % 8
        player.timer -= 1
        player.x += player.velocity
        player.x = clamp(25, player.x, 1600 - 25)

    @staticmethod
    def draw(player):
        player.image.clip_draw(30 * player.frame, 0, 30, 30, player.x, player.y)

next_state_table={
    IdleState:{RIGHT_UP:RunState,LEFT_UP:RunState,RIGHT_DOWN:RunState,LEFT_DOWN: RunState,
               SPACE:IdleState},
    RunState:{RIGHT_UP:IdleState,LEFT_UP:IdleState,LEFT_DOWN: IdleState,RIGHT_DOWN:IdleState,
              SPACE:RunState},
}

class Player:
    image = None
    def __init__(self):

        self.x, self.y = 400, 10
        self.frame=2  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.direction=1
        self.velocity=0
        self.timer=0
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)
        if Player.image ==None:
            Player.image=load_image('resource/player(edit).png')
        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event=self.event_que.pop()
            self.cur_state.exit(self.event)
            self.cur_state=next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)

        pass

    def add_event(self,event):
        self.event_que.insert(0,event)


    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_events(self,event):
        if(event.type,event.key) in key_event_table:
            key_event=key_event_table[(event.type,event.key)]
            self.add_event(key_event)




# class Bullet:
#     image=None
#     def __init__(self):
#         if Bullet.image==None:
#             Bullet.image=load_image('resource/bullet.png')
#         self.x,self.y=player.x,player.y+10
#         self.being=False
#         self.speed=1
#     def draw(self):
#         if self.being==True:
#             Bullet.image.clip_draw(0,0,7,7,self.x,self.y)
#     def update(self):
#         if self.being==True:
#             if(self.y<get_canvas_height()+100):
#                 self.y+=self.speed
#             else:
#                 self.x, self.y = player.x, player.y+10
#                 self.being=False
#         else:
#             self.x, self.y = player.x, player.y + 10





