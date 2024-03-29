import random
import json
import os

from pico2d import *
import game_framework
import game_world

import start_state
from backGround import BackGround
import enemis
import pause_sate
from player import Player
import explosion

name = "MainState"
# main tmain state
player = None
Enemis = []
bullet = None
backGround = None
gameEnd=False

def collideBullet(a, b):  # 충돌함수
    left_a, bottom_a, right_a, top_a = a.get_bbBullet()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def collide(a, b):  # 충돌함수
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global player, Enemis, backGround,gameEnd
    backGround = BackGround()
    gameEnd=False

    # Enemis = [enemis.Enemy() for i in range(10)]
    # game_world.add_objects(Enemis, 1)
    game_world.add_object(backGround, 0)
    player = Player()
    game_world.add_object(player, 1)





def exit():
    # del(bullets)
    clear_canvas()
    game_world.clear()

    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global gameEnd
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(start_state)
        else:
            player.handle_event(event)
        # Enemis.handle_event(event)
    if gameEnd:
        game_framework.change_state(start_state)




enemyNum=0
worldTime=1
def update():
    global player,worldTime,Enemis,enemyNum,gameEnd
    for game_object in game_world.all_objects():
        game_object.update()
    # for Enemy0 in Enemis:Enemy0.update()
    if 200%worldTime==200:
        enemys  =[enemis.Enemy() for i in range(3+enemyNum)]
        game_world.add_objects(enemys, 1)
        Enemis.extend(enemys)
        worldTime=1
        enemyNum +=1



    for enemy in Enemis:
        if collide(player, enemy):
            explosions = explosion.Explosion(player.x, player.y)
            game_world.add_object(explosions, 1) 
            Enemis.remove(enemy)
            game_world.remove_object(enemy)
            gameEnd=True

    worldTime+=1

    print(worldTime)

    pass


def draw():
    global font
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # for Enemy0 in Enemis: Enemy0.draw()

    update_canvas()


    pass
