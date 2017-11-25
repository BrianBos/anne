# Mobile agent
# has actions and can operate in the game environment
class Agent_1:
    def __init__(self, anne, pos):
        # static attributes
        self.mutable = True
        self.anne = anne
        self.birth_tick = self.anne.ticks

        # dynamic attributes
        self.nn = None
        self.position = pos

        # energy, the driving force of agent
        self.energy = 200
        self.entropy = 10  # energy lost per tick

        self.skin = {
            "type": "circle",
            "radius": 10,
            "color": (255,255,0)
        }
        self.coll_box = [10,10]
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def add_nn(self, nn):
        self.nn = nn

    # TODO: set this to accept action index so different actions
    #       can be used from this function
    def act(self):
        assessed_action = self.nn.assess()[0]

        if (len(self.actions) == 0):
            return False
        self.actions[assessed_action].do()
        return True

    # method to decay agent and bring about it's death
    # reduce energy based on self.entropy 
    # this method should be called at every tick of the game
    def decay(self):
        self.energy -= self.entropy
        return