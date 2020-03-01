import pyautogui as pg
import pyperclip

pg.PAUSE = 1

p_qqmusic = pg.locateCenterOnScreen('qqmusic.png', grayscale=True, region=(96,1400, 2184, 40))
if p_qqmusic is None:
    print('quit0')
    quit()

pg.click(p_qqmusic.x,p_qqmusic.y)
p0 = pg.locateCenterOnScreen('qqmusic_favorite_check.png', grayscale=True,region=(400,200, 1600, 800))
if p0 is None:
    p1 = pg.locateCenterOnScreen('qqmusic_favorite.png', grayscale=True,region=(400,200, 1600, 800))
    if p1 is None:
        print('quit')
        quit()
    else:
        pg.click(p1.x, p1.y)
else:
    pass

p2 = pg.locateCenterOnScreen('qqmusic_playall.png', grayscale=True,region=(400,200, 1600, 800))
if p2 is None:
    print('quit2')
    quit()

# pg.click(p2.x,p2.y+35)
pg.click(x=p2.x, y=p2.y+90, button='right')
pg.click(x=p2.x+90,y=p2.y+90+463, duration=0.5)
data = pyperclip.paste()
print(data)

pg.click(x=p2.x, y=p2.y+90+50, button='right')
pg.click(x=p2.x+90,y=p2.y+90+50+463, duration=0.5)
data = pyperclip.paste()
print(data)