from SemanticNetwork.Relation import Relation
from SemanticNetwork.Fact import Fact
from SemanticNetwork.Entity import Entity


from tostr import tostr
import string


IS_A = Relation("is-a",1)
EXAMPLE_OF = Relation("exampleOf", 1, IS_A)

def GetIsA(): return IS_A
def GetExampleOf(): return EXAMPLE_OF


isa = GetIsA()

example = GetExampleOf()


# Entities
thing = Entity("thing")
animal = Entity("animal")
bird = Entity("bird")
fish = Entity("fish")
minnow = Entity("minnow")
trout = Entity("trout")
ape = Entity("ape")

act = Entity("act")
swim = Entity("swim")
walk = Entity("walk")

scales = Entity("scales")
hair = Entity("hair")


# Declaring three relations
ableTo = Relation("ableTo", 0)
whatCan = Relation("whatCan", 0, ableTo)

biggerThan = Relation("bigger than", 1)
smallerThan = Relation("smaller than", 1, biggerThan)

has = Relation("has", 0)
whatHas = Relation("whatHas", 0, has)



# Connecting Entities with Relation
Fact(animal, isa, thing)
Fact(ape, isa, animal)
Fact(bird, isa, animal)
Fact(fish, isa, animal)
Fact(trout, isa, fish)
Fact(minnow, isa, fish)

Fact( minnow, smallerThan, trout )
Fact( trout, smallerThan, ape )
Fact( swim, isa, act )
Fact( walk, isa, act )
Fact( fish, ableTo, swim )
Fact( walk, whatCan, ape )

Fact( fish, has, scales )
Fact( ape, has, hair )


# Checking the subsets of a Entity
print("trout is:", tostr( trout.objects(isa)))
print("animal is:", tostr( animal.objects(isa)))
print("\n")
print("fish:", tostr( fish.objects(example) ))
print("fish:", tostr( fish.agents(isa) ))
print("animals:", tostr( animal.agents(isa)))
print("\n")

# Testing IS Relation
print("ape is a fish?", isa(ape,fish))
print("minnow is a fish?", isa(minnow,fish))
print("minnow is an animal?", isa(minnow,animal))
print("\n")
print("ape bigger than minnow?", biggerThan(ape,minnow))
print("minnow bigger than trout?", biggerThan(minnow,trout))
print("minnow is smaller than:", tostr( minnow.objects(smallerThan)))
print("ape is bigger than:", tostr( ape.objects(biggerThan)))
print("\n")

# Testing CAN Relation
print("\n")
print("fish can swim?", ableTo( fish, swim ))
print("minnow can swim?", ableTo( minnow, swim ))
print("bird can swim?", ableTo( bird, swim ))
print("what can swim?", tostr( swim.getObjects(whatCan) ))
print("what can act?", tostr( act.getObjects(whatCan) ))

# Testing HAS Relation
print("\n")
print("minnow has hair?", has( minnow, hair ))
print("minnow has scales?", has( minnow, scales ))
print("ape has hair?", has( ape, hair ))
print("ape has scales?", has( ape, scales ))
print("what has scales?", tostr( scales.getAgents(has) ))
