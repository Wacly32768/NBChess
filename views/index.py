# 这是主界面
import arcade
import math

class IndexView(arcade.View):
    def __init__(self,window):
        super().__init__()
        self.window = window
        self.window.set_mouse_visible(True)
        self.window.set_update_rate(1/60)
        self.window.set_vsync(True)
        self.window.background_color = arcade.color.WHITE
        self._fps_history = []
        self._fps_text = arcade.Text(
            "0",
            x=10,
            y=self.window.height - 20,
            font_size=14,
            color=arcade.color.LIME,
        )

    def on_show_view(self):
        print("显示主界面")

    def on_draw(self):
        self.clear()
        arcade.draw_text("超级象棋", self.window.width / 2, self.window.height / 2, arcade.color.BLACK, font_size=50, anchor_x="center", anchor_y="center")
        arcade.draw_text("点击开始游戏", self.window.width / 2, self.window.height * 0.3, arcade.color.BLACK, font_size=30, anchor_x="center", anchor_y="center")



        arcade.draw_text(f"FPS: {self._fps_text.text}", 0, self.window.height - 14, arcade.color.BLACK, font_size=14, anchor_x="left", anchor_y="top") #要保证FPS显示在最上层，所以要放在最后绘制

    def on_update(self, delta_time: float):
        # dt 可能波动，用最近 60 帧做滑动平均
        if delta_time > 0:
            self._fps_history.append(1.0 / delta_time)

        if len(self._fps_history) > 30:
            self._fps_history.pop(0)

        if self._fps_history:
            avg_fps = sum(self._fps_history) / len(self._fps_history)
            self._fps_text.text = f"{round(avg_fps)}"