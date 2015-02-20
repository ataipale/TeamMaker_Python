#!/usr/local/bin/Python

import csv

# create player list
playerList = []

class Player(object):
  def __init__(number, rating, height, gender):
    self.number = number
    self.rating = rating
    self.height = height
    self.gender = gender

#print my file and save it as a list of tuples
with open('sample_player_data.csv', 'rb') as csvfile:
  myfilereader = csv.reader(csvfile)
  for row in myfilereader:
  	playerList.append(tuple(row))


#define the comparator for my list sorting
def genderSort(tuple): return tuple[3]

def ratingSort(tuple): return tuple[1]

def heightSort(tuple): return tuple[2]

playerList.pop(0)
 
genderList = sorted(playerList, key=genderSort)
ratingList = sorted(genderList, key=ratingSort)

for row in genderList:
  print row
for row in ratingList:
  print row

# genderList = sorted(playerList, key=lambda i: (int(i[1]), int(i[2])))
# for row in genderList:
# 	print row




