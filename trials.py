# import random
# INF = 99999
# edge_weight = [1,2,3,4,5,6,7,8,9,10,11,12,INF]
# V = 12
# graph = a = [[0] * V for i in range(V)]

# for i in range(V):
# 	for j in range(V):
# 		if i!=j:
# 			# r = random.randint(0,12)
# 			# if r == 13:
# 			# 	print "hit"
# 			# print graph	
# 			graph[i][j] = random.choice(edge_weight) 
# 			# print random.choice(edge_weight)

# # print graph
# V = 12

# # Define infinity 
# INF = 99999
# edge_weight = [1,2,3,4,5,6,7,8,9,10,INF,INF,INF,INF,INF]

# import networkx as nx
# import matplotlib.pyplot as plt
# import random
# import time

# ims = []
# for i in range(10):
# 	graph = a = [[0] * V for i in range(V)]
# 	for i in range(V):
# 		for j in range(V):
# 			if i!=j:	
# 				graph[i][j] = random.choice(edge_weight) 
# 	# new part 

# 	G=nx.Graph()
# 	G.add_nodes_from(range(0,V))
# 	print G.nodes()
# 	G.add_edge(*[1,2])

# 	for i in range(V):
# 		for j in range(V):
# 			if i!=j & graph[i][j]!=INF:	
# 				G.add_edge(*[i,j])
# 	ims.append(nx.draw(G))
# 	# plt.show()
# 	# time.sleep(1)
# 	# plt.close()

# plt.show()
# print ims

################## VERSION 2 #############################

# print graph
V = 12

# Define infinity 
INF = 99999
edge_weight = [1,2,3,4,5,6,7,8,9,10,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF]

import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import pylab

pylab.ioff()
pylab.show()



def get_graph(graph):

	# generating graph
	G=nx.Graph()
	G.add_nodes_from(range(0,V))
	for i in range(V):
		for j in range(V):
			if i!=j:
				if graph[i][j]!=INF:	
					G.add_edge(*[i,j])


	# displaying graph
	return G



fig = pylab.figure()

# return fig	
for i in range(100):
	graph = a = [[0] * V for i in range(V)]
	for i in range(V):
		for j in range(V):
			if i!=j:	
				graph[i][j] = random.choice(edge_weight) 

	G = get_graph(graph)
	nx.draw(G,pos=nx.circular_layout(G))
	fig.canvas.draw()
	# pylab.draw()
	plt.pause(1)
	fig.clf()

