from pico2d import *
import main_state
import random
import game_world
import main_state

class Enemy:
    image=None
    bulletImage=None
    def __init__(self):
        self.enemyType=random.randint(0,3)
        if Enemy.bulletImage==None:
            Enemy.bulletImage=load_image('resource/enemy_bullet.png')

        if self.enemyType==0:
            self.image = load_image('resource/enemy0.png')
        elif self.enemyType==1:
            self.image=load_image('resource/enemy1.png')
        elif self.enemyType==2:
            self.image=load_image('resource/enemy2.png')
        elif self.enemyType==3:
            self.image=load_image('resource/enemy3.png')
        self.x, self.y = random.randint(50,800), random.randint(800,2000)
        self.bX,self.bY=self.x,self.y-10
        self.frame = 0  # 0이left, 2==정지,위,아래 , 4==오른쪽
        self.speed = 0.5
        self.fire=False
        self.enemy3fire=True
        self.timer=0
        self.sTargetX,self.sTargetY=0,0
        self.targetX,self.targetY=500,500
        pass
    def get_bb(self):
        # fill here
        return self.x - 15, self.y - 10, self.x + 10, self.y + 13
    def get_bbBullet(self):
        return self.bX-3,self.bY-3,self.bX+3,self.bY+3

    def fire_bullet(self):
        if self.enemy3fire:
            bullet0=enemyBullet(self.x,self.y,1,0)
            game_world.add_object(bullet0,1)

            bullet1 = enemyBullet(self.x, self.y, 1, 1)
            game_world.add_object(bullet1, 1)

            bullet2 = enemyBullet(self.x, self.y, 1, 2)
            game_world.add_object(bullet2, 1)
            self.enemy3fire=False
        pass


    def update(self):
        self.y-=self.speed*0.5
        if self.y>=500 and self.y<520:
            self.bX, self.bY = self.x, self.y - 10
            self.fire=True
            self.sTargetX, self.sTargetY = self.bX,self.bY
            self.targetX,self.targetY=main_state.player.x,main_state.player.y
            if self.enemyType==3:
                self.fire_bullet()
        pass

    def draw(self):
        global Timer
        self.image.draw(self.x, self.y)
        if(self.fire):
            if self.enemyType==0:
                self.timer+=1
                t = self.timer / 500
                self.bX = (1 - t) * self.sTargetX + t * self.targetX
                self.bY = (1 - t) * self.sTargetY + t * self.targetY
                self.bulletImage.clip_draw(0, 0, 10, 10, self.bX, self.bY)
                draw_rectangle(*self.get_bbBullet())
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

                t = self.timer / 500
                self.bX = ((1 - t)**3) * self.sTargetX +3*(cX+(i*dx))*t*((1-t)**2)+3*(cX+(i*(-1)*dx1))*(t**2)*(1-t)+ (t**3) * self.targetX
                self.bY = ((1 - t)**3) * self.sTargetY + 3 * (cY * 0.25) * t * ((1 - t) ** 2) + 3 * (cY * 0.5) * (t ** 2) * (1 - t) + (t ** 3) * self.targetY
                self.bulletImage.clip_draw(0, 0, 10, 10, self.bX, self.bY)
                draw_rectangle(*self.get_bbBullet())
            elif self.enemyType==2:
                self.timer+=1
                t = self.timer / 500
                self.x = (1 - t) * self.sTargetX + t * self.targetX
                self.y = (1 - t) * self.sTargetY + t * self.targetY

        draw_rectangle(*self.get_bb())
        pass


class enemyBullet:
    image = None

    def __init__(self, x=400, y=300, velocity=0.5,type=0):
        if enemyBullet.image == None:
            enemyBullet.image = load_image('resource/enemy_bullet.png')
        self.x, self.y = x, y - 10
        self.speed = velocity
        self.type=type

    def draw(self):
        # Bullet.image.clip_draw(0,0,7,7,self.x,self.y)
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.speed
        if self.type==1:
            #self.y-=self.speed
            print("ehlsi>")
            self.x-=self.speed
        elif self.type==2:
            #self.y-=self.speed
            self.x += self.speed
        if self.y < 0 or self.y > 1600 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.player,self):
            game_world.remove_object(self)
            pass

    def get_bb(self):
        # fill here
        return self.x - 3, self.y - 3, self.x + 3, self.y + 3




















