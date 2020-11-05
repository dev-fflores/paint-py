import tkinter
import math
from Vector import Vector

class ColorRGB:
    r = 0
    g = 0
    b = 0
    def __init__(self,r=0,g=0,b=0):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self, other):
        return (self.r == other.r and
        self.g == other.g and
        self.b == other.b)

class Paint:
    width = 500
    heigth = 500
    clicks = []
    # list_state = []
    # index_state = 0
    color = ColorRGB(255,0,0)
    estado = 0
    press_click_rigth = False

    def __init__(self,t):        
        self.i = tkinter.PhotoImage(width = self.width,height =self.heigth)
        self.c = tkinter.Canvas(t, width=self.width+4, height=self.heigth+4)
        self.c.pack()
        self.c.create_image(2, 2, image = self.i, anchor=tkinter.NW)
        self.c.bind("<Button 1>", self.Click)
        self.c.bind("<Button 3>", self.ClickRight)
        
    def SetPixel(self, x,y,color ):
        if(x >= 0 and y >= 0 and x < self.width and y < self.heigth):
            self.i.put('#%02x%02x%02x' % tuple((color.r,color.g,color.b)),(x,y))
                        
    def GetPixel(self,x,y):
        colorpixel = [0,0,0]
        if(x >= 0 and y >= 0 and x < self.width and y < self.heigth):
            colorpixel = self.i.get(x,y)
        return ColorRGB(colorpixel[0],colorpixel[1],colorpixel[2])
    
    def Click(self, event_canvas):
        global x1, y1
        x1 = event_canvas.x
        y1 = event_canvas.y
        print((x1,y1))
        self.clicks.append(Vector(x1, y1))
        self.Draw()
        
    def ClickRight(self, event_canvas):
        self.Line(self.clicks[len(self.clicks)-1], self.clicks[0], self.color)
        self.clicks.clear()
    
    def Draw(self):
        #limpiar pantalla recorriendo todos los pixeles
# =============================================================================
#         self.i.blank()
# =============================================================================
        
        count_clicks = len(self.clicks) 
# =============================================================================
# 
#         self.OnDraw()
#         
# =============================================================================
        
        if self.estado == 0 and count_clicks == 1:
            self.SetPixel(self.clicks[0].x, self.clicks[0].y, self.color)
            self.clicks.clear()
        elif self.estado == 1 and count_clicks == 2:
            self.Line(self.clicks[0], self.clicks[1], self.color)
            self.clicks.clear()
        elif self.estado == 2 and count_clicks >= 1:
            self.Polygon(self.clicks, self.color)
        elif self.estado == 3 and count_clicks == 2:
            self.Circle(self.clicks[0], self.clicks[1], self.color)
            self.clicks.clear()
        elif self.estado == 4 and count_clicks == 1:
            self.FloodFill(self.clicks[0])
            self.clicks.clear()
    
    def OnDraw(self):
        self.list_state.append(self.estado)
        
        for i in range(len(self.list_state)-1):
            if(self.list_state[i] == 0 and len(self.clicks) == 1):
                self.SetPixel(self.clicks[0].x, self.clicks[0].y, self.color)
                self.index_state += 1
                self.clicks.clear()
            elif(self.list_state[i] == 1 and len(self.clicks) == 2):
                self.Line(self.clicks[0], self.clicks[1], self.color)
                self.index_state += 1   
                self.clicks.clear()
            elif(self.list_state[i] == 2):
                self.Polygon(self.clicks, self.color)
                self.index_state += 1   
                self.clicks.clear()
            elif(self.list_state[i] == 3 and len(self.clicks) == 2):
                self.Circle(self.clicks[0], self.clicks[1], self.color)
                self.index_state += 1   
                self.clicks.clear()
            elif(self.list_state[i] == 4):
                self.FloodFill(self.clicks[0])
                self.index_state += 1   
                self.clicks.clear()
                
    ####-----> States <-----####
    def PointState(self):
        self.estado = 0
        self.clicks.clear()
        
    def LineState(self):
        self.estado = 1
        self.clicks.clear()
        
    def PolygonState(self):
        self.estado = 2
        self.clicks.clear()
        
    def CircleState(self):
        self.estado = 3
        self.clicks.clear()
        
    def FloodFillState(self):
        self.estado = 4
        self.clicks.clear()
    
    def Line(self, v1, v2, color):  
        
        #diferencia horizaontal y vertical entre las posiciones
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        
        #quien tiene la mayor "distancia" en un determinado eje
        if(math.fabs(dx) > math.fabs(dy)):
            distance = math.fabs(dx)
        else:
            distance = math.fabs(dy)
            
        #pendiente en x & y            
        mx = dx / distance
        my = dy / distance
        
        #punto inicial que pintara
        x0 = v1.x
        y0 = v1.y
        self.SetPixel(int(x0), int(y0), color)
        
        #recorrera cada la "distancia" pintando cada pixel sumando a su pendiente en un determinado eje
        for i in range(int(distance)-1):
            x0 += mx
            y0 += my
            self.SetPixel(int(x0), int(y0), color)
                
    def Polygon(self, list_vec, color):
        
        index_last_vec = len(list_vec)-1
        
        if(len(list_vec) == 1):
            self.SetPixel(list_vec[index_last_vec].x, list_vec[index_last_vec].y, self.color)
        else:
            self.Line(list_vec[index_last_vec-1], list_vec[index_last_vec], self.color)
        
    def Circle(self, p1, p2, color):
        center = Vector((p1.x + p2.x)/2, (p1.y + p2.y)/2)
        ratio_cuad = math.pow((p2.x - center.x), 2) + math.pow((p2.y-center.y), 2)
        ratio = math.sqrt(ratio_cuad)
        
        vec_ref = Vector(ratio, 0)
        
        self.SetPixel(
                int(vec_ref.x + center.x), int(vec_ref.y + center.y), color)
        self.SetPixel(
                int(vec_ref.y + center.x), int(vec_ref.x + center.y), color)
        self.SetPixel(
                int(-vec_ref.x + center.x), int(vec_ref.y + center.y), color)
        self.SetPixel(
                int(-vec_ref.y + center.x), int(vec_ref.x + center.y), color)
        self.SetPixel(
                int(-vec_ref.x + center.x), int(-vec_ref.y + center.y), color)
        self.SetPixel(
                int(-vec_ref.y + center.x), int(-vec_ref.x + center.y), color)
        self.SetPixel(
                int(vec_ref.x + center.x), int(-vec_ref.y + center.y), color)
        self.SetPixel(
                int(vec_ref.y + center.x), int(-vec_ref.x + center.y), color)
        
        while(vec_ref.x >= vec_ref.y):
            
            vec_a = Vector(vec_ref.x, vec_ref.y + 1)
            vec_b = Vector(vec_ref.x - 1, vec_ref.y + 1)
            
            vec_ref.x = ratio_cuad - (vec_ref.y+1)**2
            
            v_a = math.fabs(vec_a.x**2 - vec_ref.x)
            v_b = math.fabs(vec_b.x**2 - vec_ref.x)
            
            if(v_a < v_b):
                vec_ref = vec_a
            else:
                vec_ref = vec_b
            
            self.SetPixel(
                int(vec_ref.x + center.x), int(vec_ref.y + center.y), color)
            self.SetPixel(
                int(vec_ref.y + center.x), int(vec_ref.x + center.y), color)
            self.SetPixel(
                int(-vec_ref.x + center.x), int(vec_ref.y + center.y), color)
            self.SetPixel(
                int(-vec_ref.y + center.x), int(vec_ref.x + center.y), color)
            self.SetPixel(
                int(-vec_ref.x + center.x), int(-vec_ref.y + center.y), color)
            self.SetPixel(
                int(-vec_ref.y + center.x), int(-vec_ref.x + center.y), color)
            self.SetPixel(
                int(vec_ref.x + center.x), int(-vec_ref.y + center.y), color)
            self.SetPixel(
                int(vec_ref.y + center.x), int(-vec_ref.x + center.y), color)
            
    def FloodFill(self, point):
        color_point = self.GetPixel(point.x, point.y)
        new_color = ColorRGB(0,0,255)
        queue = []
        queue.append(point)
        
        while(len(queue) > 0):
            
            point_aux = queue.pop()
            
            directions = [Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0)]
            
            for i in range (len(directions)):
                
                neighbour_point = point_aux + directions[i]
                
                if(self.GetPixel(neighbour_point.x, neighbour_point.y) == color_point):
                    self.SetPixel(neighbour_point.x, neighbour_point.y, new_color)
                    queue.append(neighbour_point)
                
        
            
        
        