import game_framework
#import title_state
import main_state

from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global  image
    image=load_image('resource/logo.png')

    pass


def exit():
    global image
    del(image)
    pass


def update():
    global  logo_time

    # if(logo_time>1.0):
    #     logo_time=0
    #     #game_framework.quit()
    #     game_framework.change_state
    delay(0.01)
    logo_time+=0.01
    pass


def draw():
    global image
    clear_canvas()
    image.draw_to_origin(0,0,get_canvas_width(),get_canvas_height())
    update_canvas()
    pass




def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)

    pass


def pause(): pass


def resume(): pass




