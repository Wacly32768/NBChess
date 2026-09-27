import arcade
import math
import json
import re
from views.index import IndexView

"""
超级象棋 v0.0.0
简介:一款基于Arcade3.3.3开发的象棋游戏
变量名对照表：
- 屏幕高度 - SCREEN_HEIGHT
- 屏幕宽度 - SCREEN_WIDTH
- 窗口实例 - window
- 棋盘 - board


"""

with open("config/settings.json", "r", encoding="utf-8") as f:#读取设置文件
    settings = json.load(f)

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size() #获取屏幕分辨率

WINDOW_WIDTH = settings["width"] #窗口宽度
WINDOW_HEIGHT = settings["height"] #窗口高度

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "超级象棋 -v0.0.0") #实例化窗口
#window.set_location(math.floor(SCREEN_WIDTH*0.5 - WINDOW_WIDTH*0.5), math.floor(SCREEN_HEIGHT*0.5 - WINDOW_HEIGHT*0.5)) #设置窗口位置
window.set_update_rate(1/settings["fps"]) #设置帧率
window.set_vsync(settings["vsync"]) #设置垂直同步
R,G,B,A = settings["bg_color"]["R"], settings["bg_color"]["G"], settings["bg_color"]["B"], settings["bg_color"]["A"] #提取设置中的背景颜色
window.background_color = arcade.color.Color(r=R, g=G, b=B, a=A) #设置背景颜色























if __name__ == "__main__":
    window.show_view(IndexView(window)) #显示主界面
    arcade.run() #运行窗口