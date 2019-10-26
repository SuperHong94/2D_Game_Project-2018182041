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
        global pastEvent
        if(self.direction=="stop"):
            pastEvent='stop'
            pass
        if self.direction== 'left':
            pastEvent='left'
            self.x-=self.speed
        if self.direction== 'up':
            pastEvent ='up'
            self.y+=self.speed
            print(pastEvent)

        if self.direction== 'down':
            self.y-=self.speed
        if self.direction== 'right':
            self.x+=self.speed
        if self.direction=='upLeft':
            self.x-=self.speed
            self.y += self.speed
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
    global pastEvent
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            #game_framework.change_state(title_state)
            pass
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_sate)

        #방향키입력-------------------------
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_LEFT:

                if pastEvent=='up':
                    player.frame = 0
                    player.direction = 'upLeft'
                elif pastEvent=='left':
                    player.frame=0
                    player.direction='left'
                pastEvent='left'
                print(pastEvent)


            if event.key==SDLK_UP:

                if pastEvent=='up':
                    player.frame = 2
                    player.direction='up'
                if pastEvent=='left':
                    player.frame = 0
                    player.direction = 'upLeft'
                    handle_events()



            if event.key==SDLK_DOWN:
                player.frame = 2
                player.direction='down'

            if event.key==SDLK_RIGHT:
                player.frame = 4
                player.direction='right'


        elif event.type==SDL_KEYUP and (event.key==SDLK_LEFT or event.key==SDLK_UP or event.key==SDLK_DOWN or event.key==SDLK_RIGHT):
            player.frame = 2
            player.direction='stop'
        #-------------------------------




def update():
    player.update()
    pass


def draw():
    clear_canvas()
    player.draw()
    update_canvas()

    pass





