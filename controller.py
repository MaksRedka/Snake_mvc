class controller:
    def __init__(self):
        self.game_over = False
        self.game_close = False

    def set_gameover(self):
        self.game_over = True

    def set_gameclose(self):
        self.game_close = False

    def change_gameclose(self,param):
        if param != None:
            self.game_close = param
