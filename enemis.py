from pico2d import *
import main_state
import random



class Enemy:
    image=None
    bulletImage=None
    def __init__(self):
        self.enemyType=random.randint(0,1)
        if Enemy.bulletImage==None:
            Enemy.bulletImage=load_image('resource/enemy_bullet.png')

        if self.enemyType==0:
            self.image = load_image('resource/enemy0.png')
        elif self.enemyType==1:
            self.image=load_image('resource/enemy1.png')
        self.x, self.y = random.randint(50,800), random.randint(800,1000)
        self.bX,self.bY=self.x,self.y-10
        self.frame = 0  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.speed = 0.5
        self.fire=False
        self.timer=0
        self.sTargetX,self.sTargetY=0,0
        self.targetX,self.targetY=500,500
        pass


    def update(self):
        self.y-=self.speed*0.5
        if self.y>=500 and self.y<520:
            self.bX, self.bY = self.x, self.y - 10
            self.fire=True
            self.sTargetX, self.sTargetY = self.bX,self.bY
            self.targetX,self.targetY=main_state.player.x,main_state.player.y
        pass

    def draw(self):
        global Timer
        self.image.clip_draw(30*self.frame,0,30,30,self.x,self.y)
        if(self.fire):
            if self.enemyType==0:
                self.timer+=1
                t = self.timer / 500
                self.bX = (1 - t) * self.sTargetX + t * self.targetX
                self.bY = (1 - t) * self.sTargetY + t * self.targetY

                self.bulletImage.clip_draw(0, 0, 10, 10, self.bX, self.bY)

            elif self.enemyType==1:
                self.timer += 1
                #cX=((self.targetX-self.sTargetX)**2)**0.5
                cX=self.sTargetX
                cY=((self.targetY-self.sTargetY)**2)**0.5
                dx=500
                dx1=500
                i=0
                if self.sTargetX>400:
                    i=1
                else:
                    i=-1

                print(i*dx)

                t = self.timer / 500
                self.bX = ((1 - t)**3) * self.sTargetX +3*(cX+(i*dx))*t*((1-t)**2)+3*(cX+(i*(-1)*dx1))*(t**2)*(1-t)+ (t**3) * self.targetX
                self.bY = ((1 - t)**3) * self.sTargetY + 3 * (cY * 0.25) * t * ((1 - t) ** 2) + 3 * (cY * 0.5) * (t ** 2) * (1 - t) + (t ** 3) * self.targetY

                self.bulletImage.clip_draw(0,0,10,10,self.bX,self.bY)

        pass



















