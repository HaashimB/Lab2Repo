m = 1
n = 2
x = 0
y = 2
while(n, 4000000)

	x = m + n
  m = n
  n = x

  if(x%2==0)
    y = y + x
print(y)