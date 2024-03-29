import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "StarWars"
LASER_SPEED = 10




class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__("falcon.png", 0.3)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 100

    def update(self):
        self.center_x += self.change_x

    def on_key_press(self, symbol: int, modifiers: int):
        pass


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()
        self.bg = arcade.load_texture("background.jpg")
        self.set_mouse_visible(False)

        """Sprites"""
        self.falcon = Falcon()
        # self.laser = Laser()
    #     новая тема
        self.lasers = arcade.SpriteList()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            laser=Laser()
            self.lasers.append(laser)

    def setup(self):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)

        """Sprites"""
        self.falcon.draw()
        self.lasers.draw()
        # NEW
        # self.lasers.draw()

    def update(self, delta_time):
        self.falcon.update()
        # self.laser.update()
        # NEW
        self.lasers.update()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.falcon.center_x = x


class Laser(arcade.Sprite,Game):
    def __init__(self):
        super().__init__("laser.png", 0.8)
        self.center_x = super().falcon.center_x
        # self.f=Falcon()
        # self.center_x = self.f.center_x
        # self.bottom=self.f.top
        self.bottom = super().falcon.top
        #
        self.change_y = LASER_SPEED
        self.laser_sound = arcade.load_sound("laser.wav")

    def update(self):
        self.center_y += self.change_y
#         новая тема
        if self.center_y > SCREEN_HEIGHT:

            self.kill()



print(Laser.mro())
print(dir(Game))
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

window.setup()

arcade.run()
