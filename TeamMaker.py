#!/usr/local/bin/Python

import csv

# create player list
playerList = []

#print my file and save it as a list of tuples
with open('sample_player_data.csv', 'rb') as csvfile:
  myfilereader = csv.reader(csvfile)
  for row in myfilereader:
  	playerList.append(tuple(row))

#get rid of headers row of CSV file
playerList.pop(0)

#Sort my list by gender, then rating, then height; print results
sortedList = sorted(playerList, key= lambda x: (x[3], x[1], x[2]))

for row in sortedList:
	print row

numberOfPlayers = len(sortedList)
print numberOfPlayers

#calculate number of teams needed, assuming five people per team
numberOfTeams = numberOfPlayers / 5

countPlayers = 0
countRounds = 0

#forms list of lists to hold teams
teamList = [[] for i in range(numberOfTeams)]

while countPlayers < numberOfPlayers:
	countTeams = 0
	for team in teamList:
		if countPlayers < numberOfPlayers:	
			if countRounds%2 == 0:
				teamList[countTeams].append(sortedList.pop(0)) 
				countTeams = countTeams + 1
			else:
				countTeams = countTeams - 1
				teamList[countTeams].append(sortedList.pop(0))
			countPlayers = countPlayers + 1
	countRounds = countRounds + 1

for team in teamList:
	size = 0
	teamRatingSum = 0
	teamHeightSum = 0
	teamGenderSum = 0
	for player in team:
		size = size + 1
		teamRatingSum = teamRatingSum + float(player[1])
		teamHeightSum = teamHeightSum + float(player[2])
		if player[3] == 'F':
			teamGenderSum = teamGenderSum + 1.0
	print "Team Average Stats: %f %f %f" % (teamRatingSum/size, teamHeightSum/size, teamGenderSum/size)
	print team








