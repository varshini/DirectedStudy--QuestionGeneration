'''QUESTION1 - What caused <after event> at <LOCATION of previous event>

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
'''



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