from Vector import Vector

class Primitive:
    list_clicks = []
    state = 0
    
    def __init__(self, list_clicks, state):
        self.list_clicks = list_clicks
        self.state = state