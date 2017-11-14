# TODO: Look into other planes for movement alon them
# Action that alters an agent's position along [x,y]
# Config options:
# [
#   displacement(2D Vector) eg [0,0]
# ]
class Step2D:
    def __init__(self, agent):
        self.agent = agent
        self.options = [[5,0]]

    def do(self):
        self.agent.position[0] += self.options[0][0]
        self.agent.position[1] += self.options[0][1]

