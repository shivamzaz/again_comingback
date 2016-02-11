def lcs(a,b,x,y):
	l=[[0]*(y+1)]*(x+1) //x as a row and y as a column
	for i in range(0,x+1,1):
		for j in range(0,y+1,1):
			if(i==0 or j==0):
				l[i][j]= 0
			elif(a[-1]==b[-1]):
				l[i][j]= 1+l[i-1][j-1]
			else:
				l[i][j]= max(l[i-1][j],l[i][j-1])
	return l[x][y]

a="sddd"
b="d"
x=len(a)
y=len(b)
print lcs(a,b,x,y)