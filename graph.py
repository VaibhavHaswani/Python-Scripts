class Graph:
		def __init__(self):
			self.graph=dict() #graph dictionary
			
		def addNodes(self):
			nodes=input("Enter nodes (seperated by comma):").split(",")
			print("enter nodes attached to the entered nodes.....")
			for node in nodes:
					a_nodes=input(f"Enter nodes attached with {node} (seperated by comma):").split(",")
					self.graph[node]=a_nodes
			self.order=len(self.graph)
		   
		def genEdges(self):
			par=int(input("enter 1 if any parllel edge 0 otherwise"))
			if  bool(par):
					pairs=input("Enter pairs that are parallel (seperate elements by space and pairs by comma)").split(",")
					pairs=list(map(lambda x:tuple(x.split(" ")),pairs))
			self.edges=[]
			for node,a_nodes in self.graph.items():
					for n in a_nodes:
						if (node,n) and (n,node) not in self.edges:
							self.edges.append((node,n))
			if par:
					for i,j in pairs:
						if (i,j) in self.edges:
							self.edges.append((j,i))
						elif (j,i) in self.edges:
							self.edges.append((i,j))
						else:
							self.edges.append((i,j))
			self.size=len(self.edges)

		def genDegrees(self):
			for k,v in self.graph.items():
				print(f"{k}  , degree ={len(v)}")
''' 	def genPaths(self,node):
			reachable=self.graph[node]
			for item in reachable:
				  print(f"{node}--->{item}")
			notReached=list(set(self.graph.keys())-set(reachable))
			notReached.remove(node)
			if bool(notReached):
				  for i in notReached:
						if  self.graph[i]:
							  path=self._backtrack(reachable,i,[node])
							  print(f"{path[0]}",end="")
							  for item in path[1:]:
									print(f"--->{item}",end="")
							  print()
						else:
							  print(f"{i} is not reachble")
							  
	 def _backtrack(self,nodes,item,visited):
			if visited==self.graph.items():
				  return -1
			else:
				  for node in nodes:
						if node not in visited:
							  visited.append(node)
						if item in self.graph[node]:
							  visited.append(item)
							  return visited
						else:
							  return self._backtrack(self.graph[node],item,visited)'''
						
			
			
			
				  

g=Graph()
g.addNodes()


print("Generating Degrees...")
g.genDegrees()
print("Generating edges....")
g.genEdges()
print("Edges:\n",g.edges)



