import pyautogui
import time
import keyboard

def rgb_to_hex(rgb):
    r, g, b = rgb
    # 转两位十六进制，大写/小写可选
    return f"#{r:02x}{g:02x}{b:02x}"

def click(a,b):
    pyautogui.moveTo(a, b)
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(0.08)
    pyautogui.mouseUp()

def get_x(pos):
    temp_list = pos.split()
    return int(temp_list[0]) * 110 + 484

def get_y(pos):
    temp_list = pos.split()
    return int(temp_list[1]) * 110 + 90


land_list = []
num = int(input("受保护地块数量："))
color = input("请输入你的地块颜色：")
army = input("每次进攻兵力：")
for i in range(num):
    land_list.append(input("输入地块，坐标之间空格分隔："))
print("按P键来控制开始/停止")
print("请确保您的休闲成神处于全屏状态，并且处于帮会战争页面")

while True:
    time.sleep(0.05) 
    if keyboard.is_pressed('p'):
        time.sleep(0.2) 
        stop = False
        while stop == False:
            time.sleep(0.05)
            # 主要代码
            for i in range(num):
                now_color = rgb_to_hex(pyautogui.pixel(get_x(land_list[i]),get_y(land_list[i])))
                if color != now_color:
                    while color != now_color:
                        click(get_x(land_list[i]),get_y(land_list[i]))
                        click(1300,1200)
                        pyautogui.typewrite(army)
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        now_color = rgb_to_hex(pyautogui.pixel(get_x(land_list[i]),get_y(land_list[i])))

            if keyboard.is_pressed('p'):
                time.sleep(0.2)
                stop = True
