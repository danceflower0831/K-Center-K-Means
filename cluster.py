import copy
# training dataset
f = open('8gau.txt')
p = f.read().splitlines()

# distance set function
def setD(p, centroid_set):
	set_d = []
	for c in centroid_set:
		di = (float(p[0]) - float(c[0]))**2 + (float(p[1]) - float(c[1]))**2
		set_d.append(di)
	return set_d

# find initial centroid set
init_c = []			
c1 = p[0].split()	
init_c.append(c1)
p.pop(0)

while len(init_c) < 8 :
	max_dc = []
	for i in range(len(p)):
		pi = p[i].split()
		# find minimum distance
		set_dc = setD(pi, init_c)
		min_dist = min(set_dc)
		max_dc.append(min_dist)
		# find maximum minimum distance
		if len(max_dc) > 1 and max_dc[-1] < max_dc[-2]:
			max_dc.pop()
		else:
			index = i
	else:
		ci = p[index].split()
		init_c.append(ci)
		p.pop(index)

print('The initial centroid set:',init_c)
		

f.seek(0)
p = f.read().splitlines()
old_c = init_c
n = 0
while True:
	n += 1
	new_c = copy.deepcopy(old_c)
	for i in range(len(p)):
		pi = p[i].split()
		set_dc = setD(pi, new_c)
		index_c = set_dc.index(min(set_dc))
		new_c[index_c] += pi
	else:
		new_c_copy = copy.deepcopy(new_c)
		# calculate the geometric center of each part
		for i in range(len(new_c)):
			average_x = sum([float(new_c[i][x]) for x in range(2, len(new_c[i]), 2)]) / (len(new_c[i]) / 2 - 1)
			average_y = sum([float(new_c[i][y]) for y in range(3, len(new_c[i]), 2)]) / (len(new_c[i]) / 2 - 1)
			new_c[i][:] = [average_x, average_y]
	# iterations terminate when new equals old
	if new_c == old_c:
		output_file = open('output.txt', 'w+')
		for i in range(len(new_c_copy)):
			output_file.write(f'cluster {i+1}:\n')
			for c in range(2,len(new_c_copy[i]),2):
				line = [new_c_copy[i][c],new_c_copy[i][c+1]]
				output_file.write(f'{line}\n')
		break
	else:
		old_c = copy.deepcopy(new_c)

print('The minimum cost centroid set:', new_c)
print('The number of iterations:',n)

output_file.close()
f.close()





	
