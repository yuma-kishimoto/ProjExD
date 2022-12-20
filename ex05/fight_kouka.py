import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    

class Sord:
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        self.blit(scr) 

class Bomb:
    bkdn_image = []
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Ban:
    def __init__(self, img_path):
        self.sfc = pg.image.load(img_path)
        self_sfc = pg.image.load("fig/ban.png")
        self_sfc = pg.transform.rotozoom(self.sfc, 0, 2.0)
        self_rct = self_sfc.get_rect()
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        self.blit(scr) 
    
    
def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def sound():                                        
    pg.mixer.init(frequency = 44100)
    pg.mixer.music.load("fig/wind.mp3")
    pg.mixer.music.play(1)

def main():
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1330,700), "fig/pg_bg.jpg")
    ken = Sord("fig/kenmini.png", 1.0, (random.randint(0, scr.rct.width),random.randint(0, scr.rct.height)))
    ken.update(scr)

    # 練習３
    kouka = Bird("fig/6mini.png", 2.0, (900,400))
    kouka.update(scr)

    kenkouka = False

    
    # 練習５
    bkdn_lst = []
    for i in range(5):
        bkdn = Bomb((255, 0, 0), 10, (+1, +1), scr)
        bkdn_lst.append(bkdn)
        
    # 練習２
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kouka.update(scr)
        ken.update(scr)
        
        font = pg.font.Font(None,80)

        delbkdn = []
        #爆弾消す処理
        for i in range(len(bkdn_lst)):
            bkdn_lst[i].update(scr)
            if kouka.rct.colliderect(bkdn_lst[i].rct):
                if kenkouka:
                    pass
                else:
                    pg.display.update()
                    pg.time.wait(1000)
                    return

            if kouka.rct.colliderect(bkdn_lst[i].rct) and kenkouka:
                delbkdn.append(i)
                bkdn.update(scr)

        for w in delbkdn:
            bkdn_lst.pop(w)
            if len(delbkdn) == 5:
                    text = font.render("Game Clear",True,"Blue")
                    scr.blit(text,(400,200))
                    pg.display.update()
                    pg.time.wait(1000)
                    return

        
        if kouka.rct.colliderect(ken.rct):
            kouka = Bird("fig/3.png", 2.0, (900,400))
            kenkouka = True
            kouka.update(scr)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    sound()
    pg.init()
    main()
    pg.quit()
    sys.exit()