m = 0
n = 1

for: i in range(1, 4000000)

	if i <= 1:
		j = i

	else:
		j = m+n
		m = n
		n = j
	print(j)