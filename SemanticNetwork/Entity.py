class Entity:
	def __init__(self,id):
		self.id = id
		self.mObjects = {}
		self.mAgents = {}

	def __str__(self):
		return self.id

	def objects(self,relation):
		try: ans = self.mObjects[relation]
		except: ans = []
		if relation.transitive:
			# if it's a transitive relation,
			# pursue recursively
			for i in tuple(ans):
				ans = ans + i.objects(relation)
		return ans

	def agents(self,relation):
		try: ans = self.mAgents[relation]
		except: ans = []
		if relation.inverse and relation.inverse.transitive:
			# if its inverse is a transitive relation,
			# pursue recursively
			for i in tuple(ans):
				ans = ans + i.agents(relation)
		return ans

	def storeObject(self,relation,object):
		try:
			lst = self.mObjects[relation]
			if object not in lst: lst.append(object)
		except:
			self.mObjects[relation] = [object]

	def storeAgent(self,relation,agent):
		try:
			lst = self.mAgents[relation]
			if agent not in lst: lst.append(agent)
		except:
			self.mAgents[relation] = [agent]

	def getObjects(self,relation):
		out = self.objects(relation)
		# also check type-ancestors (base classes)
		try: parents = self.mObjects[IS_A]
		except: return out
		for p in parents:
			out = out + p.getObjects(relation)
		return out

	def getAgents(self,relation):
		out = self.agents(relation)
		# also check type-ancestors (base classes)
		try: parents = self.mObjects[IS_A]
		except: return out
		for p in parents:
			out = out + p.getAgents(relation)
		return out