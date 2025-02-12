from shape import Square, Rectangle
from canvas import Canvas

def main():

    colors = {"white": (255,255,255), "black": (0,0,0), "red": (255,0,0), "blue": (0,0,255), "green": (0,255,0)}

    #Create user canvas with user specified dimensions & color.
    canvas_width = int(input("Enter canvas width: "))
    canvas_height = int(input("Enter canvas height: "))
    canvas_color = input("Enter canvas color (white or black): ")

    canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])
    
    while True:
        shape_type = input("What shape would you like to draw (square or rectangle: ")
        if shape_type == "rectangle":
            rect_x = int(input("Enter x of rectangle: "))
            rect_y = int(input("Enter y of rectangle: "))
            rect_width = int(input("Enter width of rectangle: "))
            rect_height = int(input("Enter height of rectangle: "))
            rect_color = input("Enter rectangle color (red, blue or green): ")

            rect = Rectangle(x=rect_x,y=rect_y, width=rect_width, height=rect_height, color=colors[rect_color])
            rect.draw(canvas)
        
        if shape_type == "square":
            sq_x = int(input("Enter x of square: "))
            sq_y = int(input("Enter y of square: "))
            sq_side = int(input("Enter side length of square: "))
            sq_color = input("Enter square color (red, blue or green): ")

            sq = Square(x=sq_x, y=sq_y,side=sq_side, color=colors[sq_color])
            sq.draw(canvas)

        if shape_type == "quit":
            break

    
    canvas.make(imagepath='thecanvas.png')


if __name__ == '__main__':
    main()