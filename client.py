import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
from getEventcoref import get_event_dicts
from getEventcoref import getEventDetails
from nltk.stem.wordnet import WordNetLemmatizer
import glob,os


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
os.chdir("/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned")
text_files = []
ann_files = []
for file in os.listdir("/Users/Varshini/Desktop/DirectedStudy/newswire_cleaned"):
	 if file.endswith(".txt"):
	 	text_files.append(file)	
	 if file.endswith(".ann"):
	 	ann_files.append(file)

'''QUESTION1 - What caused <after event> at <LOCATION of previous event> 	
for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)
	questions = []
	question = "What caused " #+ "<after event>" + " at " + location_word
	for event in event_after:
		question = "What caused "
		questionx = "What caused "
		#print groups
		flag = False


		for group in groups:
			
			if('R' not in group[0].split('\t')[0]):
				x = group[1].strip().split('\t')
				y = group[0].strip().split('\t')

				

				if(event == x[0]):
					event_name = y[2]
					
					#print event_name
				
		for group in groups:

				if('R' not in group[0].split('\t')[0]):
					x = group[1].strip().split('\t')
					y = group[0].strip().split('\t')
					flag = True
		
				if((flag) and event_after[event][0] == x[0]):

					question += y[2] + " at "	
					questionx += w.lemmatize(y[2], 'v')	+ "s "+ " at "			#y[2] - after event


					question1 = question
					question2 = questionx
					#print question
					#print questionx
					
					for line in data:
						try:

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
						except:
							continue
	print set(questions)

'''

'''QUESTION 2 - When did <event> happen?

for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)
	questions = []
	answers = []
	question = "When did "
	questionx = "When did "
	
	for group in groups:

		if('R' not in group[0].split('\t')[0]):
		#x = group[1].strip().split('\t')
			y = group[0].strip().split('\t')

		for line in data:
			#print line
			#print len(y)
			if(len(y) > 2):
				if y[2] in line:
					question1 = question
					question2 = questionx
					try:
						result = nlp.parse(line)
						if(len(result['sentences']) > 0):
								words = result['sentences'][0]['words']
								for word in words:
									#print word[1]['NamedEntityTag']
									#print line
									if 'date' in word[1]['NamedEntityTag'].lower():
										question += y[2] + " happen?"
										questionx += w.lemmatize(y[2], 'v')	+ " happen?"
										#print question
										questions.append(question)
										questions.append(questionx)
										#answers.append(word[0])				#NOT SURE
										question = question1
										questionx = question2
					except:
						continue
	print set(questions)

'''

'''QUESTION 3 - WHAT WAS <ORGANIZATION> <EVENT>? - WHAT DID CNN REPORT

for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)
	questions = []
	answers = []
	question = "What did "					#TRY WITH WHO ALSO
	questionx = "What did "
	for group in groups:

		if('R' not in group[0].split('\t')[0]):
			x = group[1].strip().split('\t')
			y = group[0].strip().split('\t')
		for line in data:
			#print line
			#print len(y)
			if(len(y) > 2):
				if y[2] in line:
					question1 = question
					question2 = questionx
					try:
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

										question += y[2] + " ?"	
										questionx += word[0] + " "

										questionx += y[2] + " ?"	
														#CONVERT TO PRESENT VERB
										#question += y[2] + " ?"
										#print question
										questions.append(question)
										questions.append(questionx)
										#answers.append(word[0])				
										question = question1
										questionx = question2

					except:
						continue


	print set(questions)

'''

'''QUESTION 4 - WHO WAS <ORGANIZATION> <EVENT>? -  WHO DID TALIBAN ATTACK

for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)
	questions = []
	answers = []
	question = "Who did "					#TRY WITH WHO ALSO
	questionx = "Who did "
	for group in groups:

		if('R' not in group[0].split('\t')[0]):
			x = group[1].strip().split('\t')
			y = group[0].strip().split('\t')
		for line in data:
			#print line
			#print len(y)
			if(len(y) > 2):
				if y[2] in line:
					question1 = question
					question2 = questionx
					try:
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

										question += y[2] + " ?"	
										questionx += word[0] + " "

										questionx += y[2] + " ?"	
														#CONVERT TO PRESENT VERB
										#question += y[2] + " ?"
										#print question
										questions.append(question)
										questions.append(questionx)
										#answers.append(word[0])				
										question = question1
										questionx = question2

					except:
						continue


	print set(questions)
'''

'''QUESTION 5 - Why was <person> <event>

for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)
	questions = []
	answers = []
	question = "Why was "					
	for group in groups:

		if('R' not in group[0].split('\t')[0]):
			x = group[1].strip().split('\t')
			y = group[0].strip().split('\t')
		for line in data:
			#print line
			#print len(y)
			if(len(y) > 2):
				if y[2] in line:
					question1 = question
					try:
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

					except:
						continue

	print set(questions)

'''

#TODO 
'''QUESTION 6 - Where did <coreference event> happen? Ans - location of main event 

for text,ann in zip(text_files,ann_files):
	#print text
	#fileReader = open(text)
	fileReader = open(text)
	data = fileReader.read().split('.');
	event_coref,event_after = get_event_dicts(ann)
	groups = getEventDetails(ann)

	questions = []
	 #+ "<after event>" + " at " + location_word


	for event in event_coref:
		question = "Where did "
		questionx = "Where did "
		flag = False
		for group in groups:

			question1 = question
			question2 = questionx

			if('R' not in group[0].split('\t')[0]):
				x = group[1].strip().split('\t')
				y = group[0].strip().split('\t')

			if(event == x[0]):
				event_name = y[2]
			
		for group in groups:


			if('R' not in group[0].split('\t')[0]):
				x = group[1].strip().split('\t')
				y = group[0].strip().split('\t')
				flag = True

			if((flag) and (event_coref[event][0] == x[0])):
				#question += y[2] + " at "					#y[2] - after event
				#print y[2]
				question += y[2] + " happen? "				#might want to convert verb
				questionx += w.lemmatize(y[2], 'v')	 + " happen? "
				questions.append(question)
				questions.append(questionx)
				question = question1
				questionx = question2
				#question1 = question
				
				#for answer - if needed - need to modify
				for line in data:

					try:
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
					except:
						continue
				
				#####
	print set(questions)

'''




