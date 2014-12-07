# encoding:utf-8
from chessboard import Chessboard
from neural import Neural
BLACK_PLAYER = 1
WHITE_PLAYER = 2
class GameFlow(object):
    """description of class"""
    def __init__(self, black_stone_img, white_stone_img):
        self.chessboard = Chessboard()
        self.neural = Neural(19, 19)
        self.player = BLACK_PLAYER
        self.black_stone_img = black_stone_img
        self.white_stone_img = white_stone_img
        return super(GameFlow, self).__init__(*args, **kwargs)
    def _change_player(self):
        if self.player == BLACK_PLAYER:
            self.player = WHITE_PLAYER
        elif self.player == WHITE_PLAYER:
            self.player = BLACK_PLAYER
        else:
            assert(false)
            self.player = BLACK_PLAYER

    def update(self, pos):
        px, py = pos
        ix, iy = self.chessboard.get_index(px, py)
        if ix is None or iy is None:
            return
        if self.neural.set_value(ix, iy, self.player):
            self._change_player()

    def _get_player_img(self):
        if self.player == BLACK_PLAYER:
            return self.black_stone_img
        elif self.player == WHITE_PLAYER:
            return self.white_stone_img
        else:
            assert(False)
            return None
        
    def get_mouse_cursor(self):
        return self._get_player_img()

    def draw(self, screen):
        for w in range(self.neural.width):
            for h in range(self.neural.height):
                value = self.neural.get_value(w,h)
                if value != 0:
