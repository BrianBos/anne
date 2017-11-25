import random

# class to manage the dna of agents
# dna syntax:
#   [ 
#			brain/nn[inputs, hidden[], outputs],
#			body
#		]
#		NOTE: inputs = number of agent sensors
#					outputs = number of agent actions
class Genetics:

	def __init__(self, anne):
		self.anne = anne
		self.action_pool = self.anne.ecosystem.action_pool
		return
	
	# method to seed agent with empty dna
	# [
	# 	mind
	#	  [
	#	 		input layer, depends on senses
	#	  	[[],[],[],[]],  
	#	 		hidden layers 
	#	  	[								
	#	  		[[],[],[]],
	#	  		[[],[]]
	#	  	],
	#	 		output layers, depends on actions
	#	  	[[],[],[],[]]
	#	  ],
	# 	body
	#		[]
	# ]
	# number of neurons depends on length of array
	def seed(self, agent):
		agent.dna = [[[],[],[]],[]]
		# prepare mind
		# select number of senses
		senses_num = 4
		# select number of hidden layers
		hidden_num = [3,2]
		# select number of actions
		actions_num = random.randint(1, len(self.action_pool))

		# add to dna
		for _ in range(senses_num):
			agent.dna[0][0].append([])
		for i in hidden_num:
			layer = []
			for _ in range(i):
				layer.append([])
			agent.dna[0][1].append(layer)
		for _ in range(actions_num):
			agent.dna[0][2].append([])
		return

	# method to return number of actions on agent
	# based on dna
	def actions_num(self, agent):
		return len(agent.dna[0][2])
	
	def nn_config(self, agent):
		hidden_layers = []
		for i in agent.dna[0][1]:
			hidden_layers.append({
				"units": len(i)
			})
		return {
				"input": {"units": len(agent.dna[0][0])},
				"hidden": hidden_layers,
				"output": {"units": self.actions_num(agent)}
			}