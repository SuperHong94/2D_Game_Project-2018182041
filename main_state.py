import random
import json
import os

from pico2d import *
from enum   import Enum
import game_framework

import start_state

#import title_state

import pause_sate


name = "MainState"

boy = None
grass = None
font = None
player=None
i=0
class Player:
    def __init__(self):
        self.image=load_image('resource/player(edit).png')
        #''' self.height=self.image.h
        #self.width=self.image.w
        #self.frame=5;'''
        self.x, self.y = 400, 10
        self.frame=2  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.direction='stop'
        self.speed=1
        self.multiKey={'up':False,'down':False,'left':False,'right':False}
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
        self.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        pass

class Bullet:
    def __init__(self):
        self.image=load_image('resource/bullet.png')
        self.x,self.y=player.x,player.y+10
        self.being=False
        self.speed=1
    def draw(self):
        if self.being==True:
            self.image.clip_draw(0,0,7,7,self.x,self.y)
    def update(self):
        if self.being==True:
            if(self.y<get_canvas_height()+100):
                self.y+=self.speed
            else:
                self.x, self.y = player.x, player.y+10
                self.being=False
        else:
            self.x, self.y = player.x, player.y + 10



def enter():
   ''' global boy,grass
    grass=Grass()'''
   global player,bullets
   player=Player()
   bullets = [Bullet() for i in range(11)]



def exit():
    #global boy,grass
    #del(boy)
    #del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    global i
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            #game_framework.change_state(title_state)
            pass
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_sate)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            player.frame=0
            player.multiKey['left']=True
            player.direction='left'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_UP:
            player.frame = 2
            player.multiKey['up'] = True
            player.direction='up'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_DOWN:
            player.frame = 2
            player.multiKey['down'] = True
            player.direction='down'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_RIGHT:
            player.frame = 4
            player.multiKey['right'] = True
            player.direction='right'
        elif event.type==SDL_KEYUP and (event.key==SDLK_LEFT or event.key==SDLK_UP or event.key==SDLK_DOWN or event.key==SDLK_RIGHT):
            print(event.key)
            if event.key==SDLK_UP:
                player.multiKey['up'] = False
            elif event.key==SDLK_LEFT:
                player.multiKey['left'] = False
            elif event.key==SDLK_RIGHT:
                player.multiKey['right'] = False
            elif event.key==SDLK_DOWN:
                player.multiKey['down'] = False

            player.frame = 2
            player.direction='stop'
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            if (i == 10):
                i = 0
            bullets[i].being = True
            i += 1
            break




def update():
    player.update()
    for bullet in bullets: bullet.update()
    pass


def draw():
    clear_canvas()
    player.draw()
    for bullet in bullets: bullet.draw()
    update_canvas()

    pass
