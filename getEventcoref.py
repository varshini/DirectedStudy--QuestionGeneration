import sys
import re
from more_itertools import grouper

def get_event_dicts(filename):
	filereader = open(filename)
	lines = filereader.readlines()
	event_coref = {}
	event_after = {}

	for line in lines:
		words = line.split(' ')
		a = words[0].split('\t')
		if('R' in a[0].strip()):
			if('coreference' in a[1].lower()):
				#print words[1]
				#print words[2]
				l1 = words[1].split(':')
				l2 = words[2].split(':')
				if(l1[1] in event_coref.keys()):
					event_coref[l1[1]].append(l2[1].strip())
				else:
					event_coref[l1[1]] = [l2[1].strip()]
			elif('after' in a[1].lower()):
				#print words[1]
				#print words[2]
				l1 = words[1].split(':')
				l2 = words[2].split(':')
				#print l
				if(l1[1] in event_after.keys()):
					event_after[l1[1]].append(l2[1].strip())
				else:
					event_after[l1[1]] = [l2[1].strip()]

	return event_coref,event_after

def getEventDetails(filename):

	events = [[]]
	count1 = 0
	count2 = 0
	filereader = open(filename)
	lines = filereader.readlines()
	groups = [list(group) for group in grouper(3, lines)]

	return groups




#getEventDetails('/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned/XIN_ENG_20100613.0159.ann')

#print get_event_dicts('/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned/XIN_ENG_20100613.0159.ann')