class Fact:
	def __init__(self, agent, relation, object):
		self.agent = agent
		self.relation = relation
		self.object = object

		# stuff into dictionaries, for searching
		agent.storeObject( relation, object )
		object.storeAgent( relation, agent )

		# deduce inverse relations as well
		if relation.inverse:
			object.storeObject( relation.inverse, agent )
			agent.storeAgent( relation.inverse, object )
