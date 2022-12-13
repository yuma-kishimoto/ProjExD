import pygame as pg
import sys
import random

px,py = random.randint(-10,10),random.randint(-10,10)

def check_bound(obj_rct, scr_rct):
    yoko,tate = +1, +1
    #範囲内なら+1、範囲外なら-1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko,tate

def main():
    clock = pg.time.Clock()

    #ここにゲームの処理かく　Ctrl+F5
    pg.display.set_caption("逃げろこうかとん")
    scrn_sfc = pg.display.set_mode((1350,650))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/8.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    m1,m2 = 20,20
    bomb_sfc = pg.image.load("fig/Dai.png")
    bomb_sfc = pg.transform.scale(bomb_sfc, (m1, m2))
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centerx = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    
    v1, v2= 50, 50
    bomb1_sfc = pg.image.load("fig/bom.png")
    bomb1_sfc = pg.transform.scale(bomb1_sfc, (v1, v2))
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx = random.randint(0, scrn_rct.width)
    bomb1_rct.centerx = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb1_sfc, bomb_rct)

    vx, vy, = +1, +1

    ban_sfc = pg.image.load("fig/ban.png")
    ban_sfc = pg.transform.rotozoom(ban_sfc, 0, 2.0)
    ban_rct = ban_sfc.get_rect()
    ban_rct.center = tori_rct.centerx, tori_rct.centery
    scrn_sfc.blit(ban_sfc, ban_rct)

    nx,ny = -1.2,-1.2

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_dct[pg.K_1]:
            tori_rct.centery -= 2
        if key_dct[pg.K_2]:
            tori_rct.centery += 2
        if key_dct[pg.K_3]:
            tori_rct.centerx -= 2
        if key_dct[pg.K_4]:
            tori_rct.centerx += 2

        if check_bound(tori_rct,scrn_rct) != (+1,+1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
            if key_dct[pg.K_1]:
                tori_rct.centery += 2
            if key_dct[pg.K_2]:
                tori_rct.centery -= 2
            if key_dct[pg.K_3]:
                tori_rct.centerx += 2
            if key_dct[pg.K_4]:
                tori_rct.centerx -= 2

        scrn_sfc.blit(tori_sfc, tori_rct)


        
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        yoko, tate =  check_bound (bomb_rct, scrn_rct)
        vx *= yoko 
        vy *= tate 

        
        bomb1_rct.move_ip(nx,ny)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct)
        yoko, tate =  check_bound (bomb1_rct, scrn_rct)
        nx *= yoko 
        ny *= tate 

        if yoko == -1:
            m2 += 15
            v2 += 10
            bomb_sfc = pg.transform.scale(bomb_sfc, (m1, m2))
            bomb1_sfc = pg.transform.scale(bomb1_sfc, (v1, v2))
            pg.display.update()

        if tate == -1:
            m1 += 15
            v1 += 10
            bomb_sfc = pg.transform.scale(bomb_sfc, (m1, m2))
            bomb1_sfc = pg.transform.scale(bomb1_sfc, (v1, v2))
            pg.display.update()
        
    
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb1_rct):
            scrn_sfc.blit(ban_sfc, ban_rct)
            pg.display.update()
            pg.time.wait(1000)
            return


        scrn_sfc.blit(bomb_sfc, bomb_rct)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()