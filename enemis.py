from pico2d import *
import main_state
import random




class Enemy:
    image=None
    bulletImage=None
    def __init__(self):
        self.enemyType=0
        if Enemy.bulletImage==None:
            Enemy.bulletImage=load_image('resource/enemy_bullet.png')
        if self.enemyType==0:
            Enemy.image = load_image('resource/enemy0.png')
        self.x, self.y = random.randint(50,800), random.randint(800,1000)
        self.bX,self.bY=self.x,self.y-10
        self.frame = 0  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.speed = 0.5
        self.fire=False
        self.timer=0
        self.targetX,self.targetY=500,500
        pass

    def update(self):

        self.y-=self.speed*0.5
        if self.y>=500 and self.y<520:
            self.bX, self.bY = self.x, self.y - 10
            self.fire=True
            self.targetX,self.targetY=main_state.player.x,main_state.player.y

        pass

    def draw(self):
        global Timer

        self.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        if(self.fire):
            self.timer+=1
            t = self.timer / 500
            x = (1 - t) * self.bX + t * self.targetX
            y = (1 - t) * self.bY + t * self.targetY
            self.bulletImage.clip_draw(0,0,10,10,x,y)

        pass



















