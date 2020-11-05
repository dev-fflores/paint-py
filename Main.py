import tkinter
from Paint import Paint
from Paint import ColorRGB
from Vector import Vector

tk = tkinter.Tk()
paint = Paint(tk)
color = ColorRGB(0,255,0)

b_point = tkinter.Button(tk, text = "Point", command = paint.PointState)
b_point.pack(side = tkinter.LEFT)

b_line = tkinter.Button(tk, text = "Line", command = paint.LineState)
b_line.pack(side = tkinter.LEFT)

b_polygon = tkinter.Button(tk, text = "Polygon", command = paint.PolygonState)
b_polygon.pack(side = tkinter.LEFT)

b_circle = tkinter.Button(tk, text = "Circle", command = paint.CircleState)
b_circle.pack(side = tkinter.LEFT)

b_circle = tkinter.Button(tk, text = "FloodFill", command = paint.FloodFillState)
b_circle.pack(side = tkinter.LEFT)

tk.mainloop()