from Transformer import Transformer
"""
The function to get battle result between two teams.
@param autobot: An array of Transformer whcih are autobot
@param deception: An array of Transformer which are deception
@Return: the number of battle, and a tuple of two teams (winning team, losing team)
"""
def getBattleResult(autobot, deception):
	if len(autobot) <= 0 or len(deception) <= 0:
		return 0, (autobot, deception)

	#Sort two arrays by transfomer's rank 
	autobot.sort(key=lambda t:t.spec_dict['rank'], reverse=True)
	deception.sort(key=lambda t:t.spec_dict['rank'], reverse=True)

	#Copy two arrays to savae survivors 
	autobot_survivors = list(autobot)
	deception_survivors = list(deception)
	
	autobot_eli_num, deception_eli_num, battle_count = 0, 0, 0
	for i in range(min(len(autobot), len(deception))):
		autobot[i].battle(deception[i])
		battle_count += 1
		if autobot[i].eliminated:
			autobot_survivors.pop(i - autobot_eli_num)
			autobot_eli_num += 1
		if deception[i].eliminated:
			deception_survivors.pop(i - deception_eli_num)
			deception_eli_num += 1
	
	#In teamResult the first team is winning team 
	teamResult = (deception, autobot_survivors) if autobot_eli_num > deception_eli_num else (autobot, deception_survivors)
	return battle_count, teamResult


"""
The function to generate report
@param battle_count: the number of battle
@param teamReault: the tuple to save result of two team, 
				   the first element is winning team, 
				   the second element is survivors from the losing team
"""
def generateReport(battle_count, teamResult):
	if teamResult[0][0].team == "A":
		wTeam, lTeam = 'Autobots', 'Decepticons'
	else:
		wTeam, lTeam = 'Decepticons', 'Autobots'
	w_name = ', '.join(i.name for i in teamResult[0])
	l_survivor_name = ', '.join(i.name for i in teamResult[1])
	print "{} battle".format(battle_count)
	print "Winning team ({}): {}".format(wTeam, w_name)
	print "Survivors from the losing team ({}): {}".format(lTeam, l_survivor_name)


def main():
	#Read input from file
	file_name = './input/4.txt' 
	inputs = [line.rstrip('\n') for line in open(file_name)]
	autobot, deception = [], []
	for i in inputs:
		t = Transformer(i)
		if t.team == "A":
			autobot.append(t)
		else:
			deception.append(t)
	#print autobot, deception
	battle_count, teamResult = getBattleResult(autobot, deception)
	generateReport(battle_count, teamResult)


if __name__ == '__main__':
	main()