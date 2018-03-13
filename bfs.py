def bfs(s):
	discovered[s] = True
	L[0].append(s)
	i = 0

	print(s,end=' ')

	while len(L[i])>0:
		L.append([])		# empty L[i+1]
		for u in L[i]:
			for v in graph[u]:
				if discovered[v]==False:
					discovered[v] = True
					print(v,end=' ')
					L[i+1].append(v)
		i+=1

	print()
	L.pop()

if	__name__ == "__main__":

	n = int(input('Enter the number of vertices in graph: '))

	graph = [[] for i in range(n)]

	for i in range(n):
		v = int(input( 'Enter no. of adjacent vertices of vertex, '+str(i)+': ' ))
		for j in range(v):
			graph[i].append(int(input()))

	discovered = [False]*n
	L = [[]]
	start = 0


	print('\nBFS(0):')
	bfs(start)

	for k in range(len(L)):
		print(L[k])
	
	print()

