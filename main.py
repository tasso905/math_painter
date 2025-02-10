from shape_design import Square,Rectangle,Canvas
def main():
    canvas = Canvas(height=20, width=30, color=(255, 255, 255))
    r1 = Rectangle(x=1,y=6, width=10, height=7, color=(100,200,125))
    r1.draw(canvas)
    canvas.make(imagepath='thecanvas.png')


if __name__ == '__main__':
    main()