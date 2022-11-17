def count(elements):
	if elements[-1] == ('.' or ',' or '!', '?'):
		elements = elements[0:len(elements) - 1]

	if elements in dictionary:
		dictionary[elements] += 1

	else:
		dictionary.update({elements: 1})

file = open('lab4.txt', 'r')
line = (file.read()).lower()

dictionary = {}

list = line.split()

for elements in list:
	count(elements)

for Key in dictionary:
	print (Key, end = " ")
	print (":", end = " ")
	print (dictionary[Key], end = " ")
	print()