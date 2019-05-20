class KanoVertical(object):
    def __init__(self):
        '''
        The frame is an array of size 128. We can control the top left value by 
        setting 0 to the given value. We can set the botoom left value by setting
        15 to the given value.
        '''
        self.height = 16
        self.width = 8
        self.size = 128

        self.frame = ['#000000'] * self.size

    def set(self, x, y, hex):
        assert x >= 0 and x < self.width
        assert y >= 0 and y < self.height

        self.frame[x * self.height + y] = hex

    def reset(self, hex='#000000'):
        self.frame = [hex] * self.size