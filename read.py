data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Finish loading files, there are', len(data), 'files in total.')

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
	
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
	word = input('Enter the word you want to look up:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'appeared: ', wc[word], 'times.')
	else:
		print('The word does not exist!')
print('Thank you for using this')	
	

	
	








#sum_len = 0
#for d in data:
#	sum_len += len(d)

#print ('The average length of a comment is', sum_len/len(data))

#new_data = []
#for d in data:
#	if len(d) < 100:
##print('There are', len(new_data), 'comments shorter than 100.')


#for d in data:
#	if 'good' in d:
#		list_good.append(d)
#print("There are", len(list_good),"comments mentioned the word 'good'.")
