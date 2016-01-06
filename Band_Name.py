# Band name generator
import random


titles = ["gigantic","sour","steamy","stupid","ironic",
			"greasy","tangy","smelly","small","inventive","creative",
			"spherical","spiritual","green","blue","pot bellied","pickled",
			"prickly","bananes"]

adjs = ["tiny","fat","skinny","eclectic","fluffy","bright","corrupt","honest","aggressive",
		"passive","alarming","amazing","magical","normal","courageous","fearful","fierce",
		"colorless","colorfull","red","thoughtless","smart","delirious","fabulous",
		"fergalicious","dangerous"]
		
plural_nouns = ["apples","oranges","kiwis","clementines","wildabeasts","mammoths","rabbits",
				"sloths","bats","crashes","spices","eggs","herbs","pony tails","bears",
				"snitches","stitches","aliens","unicorns","wizards","kermits","signs",
				"indians","cowboys","cheerleaders","knights"]
				
def title():
	''' This function chooses a random title for the name '''
	return random.choice(titles)

def adj():
	''' This function chooses a random adj for the band '''
	return random.choice(adjs)
	
def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()
		
main()

