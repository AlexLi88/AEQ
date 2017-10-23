#The global variable to save the order of specification and spec's name 
SPEC_ORDER = ['strength', 'intelligence', 'speed', 'endurance', 'rank', 'courage', 'firepower', 'skill']
SPECIAL_NAME = ['Optimus Prime', 'Predaking']
class Transformer(object):
	"""An OO Class of Transformer  

	Attributes:
		name: The name of Transfomer
		team: The team of Transfomer, only accept A or D 
		spec_dict: The dictionary to save Spec of Transformer
		overall_rating: The overall rating of Transformer
		eliminated: The boolean value to save if Transformer is eliminated in a battle.  
	"""

	def __init__(self, input):
		input_arr = input.split(',')
		self.name = input_arr[0].strip()
		if input_arr[1].strip() == 'A' or input_arr[1].strip() == 'D': 
			self.team = input_arr[1].strip()
		else: 
			raise Exception('Except team name be A or D')
		self.spec_dict = dict(zip(SPEC_ORDER, map(int, input_arr[2:])))
		self.overall_rating = self.spec_dict['strength'] + self.spec_dict['intelligence'] + self.spec_dict['speed'] \
							+ self.spec_dict['endurance'] + self.spec_dict['firepower']
		self.eliminated = False

	"""
		The function used for debug 
	"""
	def __repr__(self):
		return "name: {}\n team: {}\nspec: {}\neliminated: {}\n".format(self.name, self.team, self.spec_dict, self.eliminated)


	"""
		The battle function to check who is eliminated in the battle. 
		@param opponent: The opponent transformer  
	"""
	def battle(self, opponent):
		if opponent.name in SPECIAL_NAME and self.name not in SPECIAL_NAME:
			self.eliminated = True
			return

		if self.name in SPECIAL_NAME and opponent.name in SPECIAL_NAME:
			self.eliminated = True
			opponent.eliminated = True
			return

		if opponent.spec_dict['courage'] - self.spec_dict['courage'] >= 4 \
		or opponent.spec_dict['strength'] - self.spec_dict['strength'] >= 3 \
		or opponent.spec_dict['skill'] - self.spec_dict['skill'] >= 3:
			self.eliminated = True
		
		elif self.spec_dict['courage'] - opponent.spec_dict['courage'] >= 4 \
		or self.spec_dict['strength'] - opponent.spec_dict['strength'] >= 3 \
		or self.spec_dict['skill'] - opponent.spec_dict['skill'] >= 3:
			opponent.eliminated = True
		
		else:
			if opponent.overall_rating > self.overall_rating:
				self.eliminated = True
			elif opponent.overall_rating == self.overall_rating:
				self.eliminated = True
				opponent.eliminated = True
			else:
				opponent.eliminated = True

