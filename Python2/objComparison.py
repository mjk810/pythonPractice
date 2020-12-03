'''
Implement class with unique hash value when a parameter is the same between instances
Python implementation has all objects being unequal
Implement equal objects if their parameters are equal

'''
class Unique(object):

	def __eq__(self, other):
		return self.x == other.x
		
	
	def __ne__(self, other):
		return not self.__eq__(other) 

	def __hash__(self):
		return hash(self.x)

class Bar(Unique):
	def __init__(self,x):
		self.x = x
		


class Foo(object):
	def __init__(self,x):
		self.x = x
	
	def __eq__(self, other):
		if isinstance(other, Foo):
			return self.x == other.x
		return False
	
	def __ne__(self, other):
		return not self.__eq__(other) 

	def __hash__(self):
		return hash(self.x)


class Driver(object):
	def __init__(self, valueArray):
		self.objs = []
		self.vals=valueArray

	def compareItems(self, obj_set):
		set_length = len(obj_set)		
		if set_length != len(self.vals):
			print([x for x in self.vals])			
			print("non-unique")
		else:
			print([x for x in self.vals])
			print("unique")

	def createObjects(self):
		counter = 0
		for item in self.vals:
			self.objs.append(Bar(self.vals[counter]))
			counter+=1
		return set(self.objs)

'''
#test using Foo class
f1=Foo(10)
f2=Foo(10)
f3=Foo(10)
s={f1, f2, f3}
print(len(s))
'''

# unique
un = [10,11,12]
driver1 = Driver(un)
obj_set = driver1.createObjects()
driver1.compareItems(obj_set)


#non_unique
non_un = [10, 10, 10]
driver = Driver(non_un)
obj_set = driver.createObjects()
driver.compareItems(obj_set)

