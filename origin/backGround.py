from pico2d import *

class BackGround:
    def __init__(self):
        self.image=load_image('resource/backGround.png')
        self.frame=1000
        self.time =900
        self.bgm=load_music('resource/backMusic.wav')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def update(self):
        if(self.time==0):
            self.time=900
        self.time-=0.1
        pass
  

    def draw(self):
        self.image.clip_draw(0,0,600,1800,300,self.time)
