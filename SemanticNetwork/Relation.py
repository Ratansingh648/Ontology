class Relation:
	def __init__(self, id, transitive=1, inverse=None ):
		self.id = id

		# a relation @ is transitive if
		# A @ B and B @ C implies A @ C
		self.transitive = transitive

		if inverse:
			self.inverse = inverse
			inverse.inverse = self
		else:
			self.inverse = None

	def __str__(self): return self.id

	def __call__(self, agent, object=None):
		# when used as a function, check to see whether
		# this relation applies
		obs = agent.getObjects(self)
		if not object: return obs
		if not obs or object not in obs: return 0
		else: return 1

IS_A = Relation("is-a",1)
EXAMPLE_OF = Relation("exampleOf", 1, IS_A)

# functions to allow outside access to these objects more easily:
def GetIsA(): return IS_A
def GetExampleOf(): return EXAMPLE_OF
