import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
from getEventcoref import get_event_dicts
from getEventcoref import getEventDetails
from nltk.stem.wordnet import WordNetLemmatizer


class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

nlp = StanfordNLP()


# fileReader = open('/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned/XIN_ENG_20090915.0142.txt')
# data = fileReader.read().split('.');
# event_coref,event_after = get_event_dicts('/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned/XIN_ENG_20090915.0142.ann')
# groups = getEventDetails('/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned/XIN_ENG_20090915.0142.ann')
w = WordNetLemmatizer()

#run all files




'''
for line in data:
	line = line.strip()
	line = 'Over 300 police officers were fanning out to track down the assailants who attacked Moscow tourists in the Russian city of Nizhny Novgorod, RIA Novosti news agency reported Sunday'
	#print line
	result = nlp.parse(line)
	pprint(result)
	
	if('coref' in result):
		coref = result["coref"]
		#pprint(coref)
	#print result.keys()
	#words = result["sentences"][0]['words']
	dependencies = result["sentences"][0]['parsetree']
	#pprint(words)
	#pprint (coref)
	pprint(result)


from nltk.tree import Tree
tree = Tree.parse(result['sentences'][0]['parsetree'])
pprint(tree)
'''

'''QUESTION1 - What caused <after event> at <LOCATION of previous event>'''

questions = []
question = "What caused " #+ "<after event>" + " at " + location_word
for event in event_after:
	question = "What caused "
	questionx = "What caused "
	for group in groups:
		x = group[1].strip().split('\t')
		y = group[0].strip().split('\t')
		if(event == x[0]):
			event_name = y[2]

		if(event_after[event][0] == x[0]):
			question += y[2] + " at "	
			questionx += w.lemmatize(y[2], 'v')	+ "s "+ " at "			#y[2] - after event


			question1 = question
			question2 = questionx
			
			for line in data:
				result = nlp.parse(line)
				#pprint(result)
				if(len(result['sentences']) > 0):
					words = result['sentences'][0]['words']
					for word in words:
					#print word[1]['NamedEntityTag']
					#print line
						if 'location' in word[1]['NamedEntityTag'].lower() and event_name in line:
							#print event_name,line
							question += word[0] + " ?"
							questionx += word[0] + " ?"		
							questions.append(question)
							questions.append(questionx)
							#print question
							question = question1
							questionx = question2
							#print questionx
print set(questions)



'''QUESTION 2 - When did <event> happen?
questions = []
answers = []
question = "When did "
for group in groups:
	#x = group[1].strip().split('\t')
	y = group[0].strip().split('\t')
	for line in data:
		#print line
		#print len(y)
		if(len(y) > 2):
			if y[2] in line:
				question1 = question
				result = nlp.parse(line)
				if(len(result['sentences']) > 0):
						words = result['sentences'][0]['words']
						for word in words:
							#print word[1]['NamedEntityTag']
						#print line
							if 'date' in word[1]['NamedEntityTag'].lower():
								question += y[2] + " happen?"
								#print question
								questions.append(question)
								answers.append(word[0])				#NOT SURE
								question = question1

print set(questions)
'''

'''QUESTION 3 - WHAT WAS <ORGANIZATION> <EVENT>? - WHAT WAS CNN REPORTING

questions = []
answers = []
question = "What was "					#TRY WITH WHO ALSO
for group in groups:
	x = group[1].strip().split('\t')
	y = group[0].strip().split('\t')
	for line in data:
		#print line
		#print len(y)
		if(len(y) > 2):
			if y[2] in line:
				question1 = question
				result = nlp.parse(line)
				if(len(result['sentences']) > 0):
						words = result['sentences'][0]['words']
						for word in words:
							#print word[1]['NamedEntityTag']
							#print line
							if 'organization' in word[1]['NamedEntityTag'].lower():
								#print word[0]
								#print y[2]
								question += word[0] + " "

								question += y[2] + " ?"					#CONVERT TO PRESENT VERB
								#question += y[2] + " ?"
								#print question
								questions.append(question)
								#answers.append(word[0])				
								question = question1

print set(questions)
'''

'''QUESTION 4 - WHO WAS <ORGANIZATION> <EVENT>? -  WHO WAS TALIBAN ATTACKING

questions = []
answers = []
question = "Who was "					
for group in groups:
	x = group[1].strip().split('\t')
	y = group[0].strip().split('\t')
	for line in data:
		#print line
		#print len(y)
		if(len(y) > 2):
			if y[2] in line:
				question1 = question
				result = nlp.parse(line)
				if(len(result['sentences']) > 0):
						words = result['sentences'][0]['words']
						for word in words:
							#print word[1]['NamedEntityTag']
							#print line
							if 'organization' in word[1]['NamedEntityTag'].lower():
								#print word[0]
								#print y[2]
								question += word[0] + " "

								question += y[2] + " ?"					#CONVERT TO PRESENT VERB
								#question += y[2] + " ?"
								#print question
								questions.append(question)
								#answers.append(word[0])				
								question = question1

print set(questions)

'''


'''QUESTION 5 - Where did <coreference event> happen? Ans - location of main event

questions = []
 #+ "<after event>" + " at " + location_word
for event in event_coref:
	question = "Where did "

	for group in groups:
		x = group[1].strip().split('\t')
		y = group[0].strip().split('\t')

		if(event == x[0]):
			event_name = y[2]
		
		if(event_coref[event][0] == x[0]):
			#question += y[2] + " at "					#y[2] - after event
			#print y[2]
			question += y[2] + " happen? "				#might want to convert verb
			questions.append(question)
			#question1 = question

			#for answer - if needed - need to modify
			for line in data:
				result = nlp.parse(line)
				#pprint(result)
				if(len(result['sentences']) > 0):
					words = result['sentences'][0]['words']
					for word in words:
					#print word[1]['NamedEntityTag']
					#print line
						if 'location' in word[1]['NamedEntityTag'].lower() and event_name in line:
							#print event_name,line
							question += word[0] + " ?"		
							questions.append(question)
							#print question
							question = question1
			#####
print set(questions)
'''

'''QUESTION 6 - Why was person doing <event>

questions = []
answers = []
question = "Why was "					
for group in groups:
	x = group[1].strip().split('\t')
	y = group[0].strip().split('\t')
	for line in data:
		#print line
		#print len(y)
		if(len(y) > 2):
			if y[2] in line:
				question1 = question
				result = nlp.parse(line)
				if(len(result['sentences']) > 0):
						words = result['sentences'][0]['words']
						for word in words:
							#print word[1]['NamedEntityTag']
							#print line
							if 'person' in word[1]['NamedEntityTag'].lower():
								#print word[0]
								#print y[2]
								question += word[0] + " "

								question += y[2] + " ?"					
								#question += y[2] + " ?"
								#print question
								questions.append(question)
								#answers.append(word[0])				
								question = question1

print set(questions)

'''



