
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Finish loading files, there are', len(data), 'files in total.')

sum_len = 0
for d in data:
	sum_len += len(d)

print ('The average length of a comment is', sum_len/len(data))

new_data = []
for d in data:
	if len(d) < 100:
		new_data.append(d)
print('There are', len(new_data), 'comments shorter than 100.')


list_good = []
for d in data:
	if 'good' in d:
		list_good.append(d)
print("There are", len(list_good),"comments mentioned the word 'good'.")
