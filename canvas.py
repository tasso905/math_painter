from PIL import Image
import numpy as np

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
