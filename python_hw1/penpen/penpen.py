import tkinter
import random

# 輸入按鍵
key = ""
koff = False
def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    # global koff # Mac
    # koff = True # Mac
    global key # Win
    key = ""   # Win


DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]

idx = 0
tmr = 0
health=5
score = 0
candy = 0
count=0
delay=0

pen_x = 0
pen_y = 0
pen_d = 0
pen_a = 0

red_x = 0
red_y = 0
red_d = 0
red_a = 0

boss_x = 0
boss_y = 0
boss_d = 0
boss_a = 0

boss_create=0

map_data = []

def set_stage(): # 設定關卡資料
    global map_data, candy
    map_data = [
    [0,1,1,1,1,0,0,1,1,1,1,0],
    [0,2,3,3,2,1,1,2,3,3,2,0],
    [0,3,0,0,3,3,3,3,0,0,3,0],
    [0,3,1,1,3,0,0,3,1,1,3,0],
    [0,3,2,2,3,0,0,3,2,2,3,0],
    [0,3,0,0,3,1,1,3,0,0,3,0],
    [0,3,1,1,3,3,3,3,1,1,3,0],
    [0,2,3,3,2,0,0,2,3,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    candy = 32


def set_chara_pos(): # 角色的起始位置
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    global boss_x, boss_y, boss_d, boss_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = 630
    red_y = 450
    red_d = DIR_DOWN
    red_a = 3
    boss_x = 90
    boss_y = 450
    boss_d = DIR_DOWN
    boss_a = 3


def draw_txt(txt, x, y, siz, col): # 陰影文字
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
    canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")


def draw_screen(): # 繪製遊戲畫面
    global boss_create,health
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30, y*60+30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN")
    boss_create=canvas.create_image(boss_x, boss_y, image=img_red[red_a], tag="SCREEN")
    if(health>=5):
        draw_txt("HEALTH "+str(health), 500, 30, 30, "white")
    elif(health==3 or health==4):
        draw_txt("HEALTH "+str(health), 500, 30, 30, "pink")
    elif(health<=1):
        draw_txt("HEALTH "+str(health), 500, 30, 30, "red")
    draw_txt("SCORE "+str(score), 200, 30, 30, "white")


def check_wall(cx, cy, di, dot): # 確認每個方向是否有牆壁
    chk = False
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    return chk

def move_penpen(): # 移動penpen
    global score, candy,count, pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 10) == False:
            pen_y = pen_y - 10
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 10) == False:
            pen_y = pen_y + 10
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 10) == False:
            pen_x = pen_x - 10
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 10) == False:
            pen_x = pen_x + 10
    pen_a = pen_d*3 + ANIMATION[tmr%4]
    mx = int(pen_x/60)
    my = int(pen_y/60)
    if map_data[my][mx] == 3: # 取得糖果了嗎？
        score = score + 100
        map_data[my][mx] = 2
        count+=1
        candy = candy - 1


def move_enemy(): # 移動red
    global idx, tmr, red_x, red_y, red_d, red_a
    speed = 10
    if red_x%60 == 30 and red_y%60 == 30:
        red_d = random.randint(0, 6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d*3 + ANIMATION[tmr%4]
    if abs(red_x-pen_x) <= 10 and abs(red_y-pen_y) <= 10:
        idx = 2
        tmr = 0

def move_boss(): # 移動boss
    global idx, tmr, boss_x, boss_y, boss_d, boss_a
    speed = 20
    if boss_x%60 == 30 and boss_y%60 == 30:
        boss_d = random.randint(0, 6)
        if boss_d >= 4:
            if pen_y < boss_y:
                boss_d = DIR_UP
            if pen_y > boss_y:
                boss_d = DIR_DOWN
            if pen_x < boss_x:
                boss_d = DIR_LEFT
            if pen_x > boss_x:
                boss_d = DIR_RIGHT
    if boss_d == DIR_UP:
        if check_wall(boss_x, boss_y, boss_d, speed) == False:
            boss_y = boss_y - speed
    if boss_d == DIR_DOWN:
        if check_wall(boss_x, boss_y, boss_d, speed) == False:
            boss_y = boss_y + speed
    if boss_d == DIR_LEFT:
        if check_wall(boss_x, boss_y, boss_d, speed) == False:
            boss_x = boss_x - speed
    if boss_d == DIR_RIGHT:
        if check_wall(boss_x, boss_y, boss_d, speed) == False:
            boss_x = boss_x + speed
    boss_a = boss_d*3 + ANIMATION[tmr%4]
    if abs(boss_x-pen_x) <= 10 and abs(boss_y-pen_y) <= 10:
        idx = 3
        tmr = 0
    
def main(): # 主要迴圈
    global key, koff, idx, tmr, score ,health,count,boss_create,delay
    tmr = tmr + 1
    draw_screen()

    if idx == 0: # 標題畫面
        health=5
        canvas.create_image(360, 200, image=img_title, tag="SCREEN")
        if tmr%10 < 5:
            draw_txt("Press SPACE !", 360, 380, 30, "yellow")
        if key == "space":
            score = 0
            set_stage()
            set_chara_pos()
            idx = 1

    if idx == 1: # 玩遊戲
        if(count==10):
            health+=1
            count=0
        if(candy>12):
            move_penpen()
            move_enemy()
            move_boss()
        else:
            move_penpen()
            move_enemy()
            canvas.delete(boss_create)
        if candy == 0:
            idx = 4
            tmr = 0
        if(health<=0):
            draw_txt("GAME OVER", 360, 270, 40, "red")
            if tmr == 50:
                idx = 0
    if idx == 2: # 被敵人攻擊
        if(health<=0):
            draw_txt("GAME OVER", 360, 270, 40, "red")
            if tmr == 50:
                idx = 0
        else:
            health-=1
            idx=1

    if idx == 3: # 被boss攻擊
        if(health<=0):
            draw_txt("GAME OVER", 360, 270, 40, "red")
            if tmr == 50:
                idx = 0
        else:
            health-=2
            idx=1

    if idx == 4: # 過關
        draw_txt("STAGE CLEAR", 360, 270, 40, "pink")
        if tmr == 50:
            idx = 0


    if koff == True:
        key = ""
        koff = False

    root.after(100, main)


root = tkinter.Tk()

img_bg = [
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\chip00.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\chip01.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\chip02.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\chip03.png")
]
img_pen = [
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen00.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen01.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen02.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen03.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen04.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen05.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen06.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen07.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen08.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen09.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen10.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\pen11.png")
]
img_red = [
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red00.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red01.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red02.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red03.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red04.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red05.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red06.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red07.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red08.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red09.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red10.png"),
    tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\red11.png")
]
img_title = tkinter.PhotoImage(file="D:\python_hw1\penpen\image_penpen\\title.png")

root.title("提心吊膽企鵝迷宮")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()
set_stage()
set_chara_pos()
main()
root.mainloop()
