import random

def generate():
    '''
    https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
    '''
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())