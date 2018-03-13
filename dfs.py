def dfs(u):

	visited[u] = True
	R.append(u)

	for v in graph[u]:
		if not visited[v]:
			dfs(v)

if	__name__ == "__main__":

	n = int(input('Enter the number of vertices in graph: '))

	graph = [[] for i in range(n)]

	for i in range(n):
		v = int(input( 'Enter no. of adjacent vertices of vertex, '+str(i)+': ' ))
		for j in range(v):
			graph[i].append(int(input()))

	# graph vertices: 0 to n-1

	visited = [False]*n
	R = []
	start = 0

	dfs(start)

	print('\nDFS(0):\n')

	for i in R:
		print(i,end=' ')
	
	print()

