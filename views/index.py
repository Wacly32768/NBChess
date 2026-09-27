# 这是主界面
import arcade
import math
import random

class IndexView(arcade.View):
    def __init__(self,window):
        super().__init__()
        self.mouse_t = []
        self.times = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_dx = 0
        self.mouse_dy = 0
        self.press_x = 0
        self.press_y = 0
        self.press_button = None
        self.press_modifiers = None
        self.window = window
        self.window.set_mouse_visible(True)
        self.window.set_update_rate(1/60)
        self.window.set_vsync(True)
        self.window.background_color = arcade.color.WHITE
        self._fps_history = []
        self._fps_text = arcade.Text(
            "0",
            x=0,
            y=self.window.height,
            font_size=14,
            anchor_x="left",
            anchor_y="top",
            color=arcade.color.BLACK,
        )

        word = ["富强", "民主", "文明", "和谐", "自由", "平等", "公正", "法治", "爱国", "敬业", "诚信", "友善"]
        self._particle_texts = {}
        for i in word:
            particle_text = arcade.Text(
                'temp',
                x=0,
                y=0,
                font_size=18,
                anchor_x="center",
                anchor_y="center",
                color=arcade.color.RED,
            )
            self._particle_texts[i] = particle_text

    def on_show_view(self):
        print("显示主界面")

    def on_draw(self):
        self.clear()
        arcade.draw_text("超级象棋", self.window.width / 2, self.window.height / 2, arcade.color.BLACK, font_size=50, anchor_x="center", anchor_y="center")
        arcade.draw_text("点击开始游戏", self.window.width / 2, self.window.height * 0.3, arcade.color.BLACK, font_size=30, anchor_x="center", anchor_y="center")
        
        



        self._fps_text.draw()  #要保证FPS显示在最上层，所以要放在最后绘制
        for mouse in self.mouse_t:
            # 更新文本内容（只改字符串，不重新创建）
            print(mouse)
            particle_text = self._particle_texts[mouse[4]]
            particle_text.font_size = round(mouse[3])
            particle_text.text = mouse[4]
            particle_text.x = mouse[0]
            particle_text.y = mouse[1]
            particle_text.draw()


    def on_update(self, delta_time: float):
        # dt 可能波动，用最近 60 帧做滑动平均
        if delta_time > 0:
            self._fps_history.append(1.0 / delta_time)

        if len(self._fps_history) > 30:
            self._fps_history.pop(0)

        if self._fps_history:
            avg_fps = sum(self._fps_history) / len(self._fps_history)
            self._fps_text.text = f"{round(avg_fps)}"

        for mouse in self.mouse_t:
            mouse[2] -= 2
            mouse[3] -= 0.3
            mouse[1] += 0.5
            if mouse[3] <= 1 or mouse[2] <= 10:
                self.mouse_t.remove(mouse)
        

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_x = x
        self.mouse_y = y
        self.mouse_dx = dx
        self.mouse_dy = dy


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.press_x = x
        self.press_y = y
        self.press_button = button
        self.press_modifiers = modifiers
        word = ["富强", "民主", "文明", "和谐", "自由", "平等", "公正", "法治", "爱国", "敬业", "诚信", "友善"]
        if button == arcade.MOUSE_BUTTON_LEFT:
            time = random.randint(200,350)  # 模拟时间间隔
            size = random.randint(15, 20)  # 模拟鼠标大小
            self.mouse_t.append([x, y, time, size, word[self.times]])
            self.times += 1
            if self.times > 11:
                self.times = 0
