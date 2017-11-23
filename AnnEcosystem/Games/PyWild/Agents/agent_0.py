# Base agent
# contains the basic functions needed to operate in the ecosystem
class Agent_0:
    def __init__(self, anne, pos):
        self.anne = anne
        self.eco = 200
        self.position = pos

        self.skin = {
            "type": "circle",
            "radius": 5,
            "color": (0,255,0)
        }
        self.coll_box = [10,10]
    
    def act(self):
        return
