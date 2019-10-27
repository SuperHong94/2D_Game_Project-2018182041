from pico2d import *
import main_state
import random

targetX,targetY=1000,1000
Timer=0



class Enemy:
    def __init__(self):
        self.enemyType=0
        self.image=None
        self.bulletImage=load_image('resource/enemy_bullet.png')
        if self.enemyType==0:
            self.image = load_image('resource/enemy0.png')
        self.x, self.y = random.randint(100,600), 800
        self.bX,self.bY=self.x,self.y-10
        self.frame = 0  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.speed = 0.5
        self.fire=False
        pass

    def update(self):
        global targetX,targetY
        self.y-=self.speed*0.5
        print(self.y)
        if self.y==500:
            self.bX, self.bY = self.x, self.y - 10
            self.fire=True
            targetX=main_state.player.x
            targetY=main_state.player.y

        pass

    def draw(self):
        global Timer
        global targetX,targetY
        self.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        if(self.fire):
            Timer+=1
            t = Timer / 1000
            x = (1 - t) * self.bX + t * targetX
            y = (1 - t) * self.bY + t * targetY
            self.bulletImage.clip_draw(0,0,10,10,x,y)

        pass



















