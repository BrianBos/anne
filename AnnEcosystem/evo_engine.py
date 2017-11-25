import random

from . import NeuralNetworks

class EvoEngine:
	def __init__(self, anne):
		self.anne = anne
		return
	
	# method to seed an agent
	# with initial characteristics
	# based on mutable attributes
	def seed(self, agent):
		# ADD ACTIONS
		# source actions from ann.game_actions list
		actions_num = random.randint(1, len(self.anne.game_actions))
		for i in range(actions_num):
			agent.add_action(self.anne.game_actions[i](agent))
		
		# ADD NEURAL NETWORK
		# output layer must have same number of outputs
		# as actions available for agent
		agent.add_nn(NeuralNetworks.TensorFlowNN.Dense({"dna": [4, [3, 2], len(agent.actions)]}))
		return