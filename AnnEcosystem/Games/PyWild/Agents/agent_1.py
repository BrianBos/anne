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

        # energy, the driving force of an agent
        self.energy = 42
        self.entropy = 0.1  # energy lost per tick

        # regulate thoughts agents can have
        # used in act()
        self.assessed_action = None
        self.ticks_per_thought = 5

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

    def act(self):
        # return false if there are no actions to perform
        if (len(self.actions) == 0):
            return False

        # update assessed_action based on ticks_per_thought
        if self.age() % self.ticks_per_thought == 0:
            self.assessed_action = self.nn.assess()[0]

        self.actions[self.assessed_action].do()
        return True

    def age(self):
        return self.anne.ticks - self.birth_tick

    # method to decay agent and bring about it's death
    # reduce energy based on self.entropy 
    # this method should be called at every tick of the game
    def decay(self):
        self.energy -= self.entropy

        if self.energy < 0:
            self.anne.agents.remove(self)
        return