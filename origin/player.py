from pico2d import *

#Player Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP=range(4)

key_event_table={
    (SDL_KEYDOWN,SDLK_RIGHT):RIGHT_DOWN,
    (SDL_KEYDOWN,SDLK_LEFT):LEFT_DOWN,
    (SDL_KEYUP,SDLK_RIGHT):RIGHT_UP,
    (SDL_KEYUP,SDLK_LEFT):LEFT_UP
}
class FlyState:

class Player:
    image = None
    def __init__(self):

        self.x, self.y = 400, 10
        self.frame=2  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.direction='stop'
        self.speed=1
        self.multiKey={'up':False,'down':False,'left':False,'right':False}
        if Player.image ==None:
            Player.image=load_image('resource/player(edit).png')
        pass

    def update(self):
        if(self.direction=="stop"):
            pass
        elif self.direction== 'left':
            if self.multiKey['up']==True:
                self.y+=self.speed
            elif self.multiKey['down']==True:
                self.y -= self.speed
            # elif self.multiKey['left']==True:
            #     self.x -= self.speed
            self.x-=self.speed
        elif self.direction== 'up':
            if self.multiKey['left'] == True:
                self.x -= self.speed
            elif self.multiKey['right'] == True:
                self.x += self.speed
            # elif self.multiKey['up']==True:
            #     self.y += self.speed
            self.y+=self.speed
        elif self.direction== 'down':
            if self.multiKey['left'] == True:
                self.x -= self.speed
            elif self.multiKey['right'] == True:
                self.x += self.speed
            # elif self.multiKey['down']==True:
            #     self.y -= self.speed
            self.y-=self.speed
        elif self.direction== 'right':
            if self.multiKey['up']==True:
                self.y+=self.speed
            elif self.multiKey['down']==True:
                self.y -= self.speed
            # elif self.multiKey['right'] == True:
            #     self.x += self.speed
            self.x+=self.speed
        pass

    def draw(self):
        Player.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        pass