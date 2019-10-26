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
        pass

    def update(self):
        if(self.direction=="stop"):
            pass
        elif self.direction== 'left':
            self.x-=self.speed
        elif self.direction== 'up':
            self.y+=self.speed
        elif self.direction== 'down':
            self.y-=self.speed
        elif self.direction== 'right':
            self.x+=self.speed
        pass

    def draw(self):
        self.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        pass

def enter():
   ''' global boy,grass
    grass=Grass()'''
   global player
   player=Player()



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
    global Player_direction
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            print("ahffk")
            #game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_sate)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            player.frame=0
            player.direction='left'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_UP:
            player.frame = 2
            player.direction='up'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_DOWN:
            player.frame = 2
            player.direction='down'
        elif event.type==SDL_KEYDOWN and event.key==SDLK_RIGHT:
            player.frame = 4
            player.direction='right'
        elif event.type==SDL_KEYUP and (event.key==SDLK_LEFT or event.key==SDLK_UP or event.key==SDLK_DOWN or event.key==SDLK_RIGHT):
            player.frame = 2
            player.direction='stop'




def update():
    player.update()
    pass


def draw():
    clear_canvas()
    player.draw()
    update_canvas()

    pass





