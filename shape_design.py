import numpy as np
from PIL import Image

class Square:
    def __ini__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x+self.side, self.y:self.y+self.side] = self.color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x+self.height, self.y:self.y+self.width] = self.color

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        #create a 3D numpy array of 0's
        self.data = np.zeros((self.width,self.height,3), dtype=np.uint8)
        #change [0,0,0] with user given values for color.
        self.data[:]=self.color

    def make(self, imagepath):
        #converts the current array into an image file using PIL.
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
