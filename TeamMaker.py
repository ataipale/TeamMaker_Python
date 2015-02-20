#!/usr/local/bin/Python

import csv

# create player list
playerList = [tuple]

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
	print row



#define the comparator for my list sorting
def genderSort(tuple): return tuple[3]

def ratingSort(tuple): return tuple[1]

def heightSort(tuple): return tuple[2]

 
genderList = sorted(playerList, key=lambda i: (int(i[1]), int(i[2])))
for row in genderList:
	print row




