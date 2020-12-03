'''
implementation of python itemgetter from operator package
return a function that can be used to iterate over a list

'''

class Getter:
		
	def mygetter(self, *args):
		if len(args)==1:
			def gettResults(sublist):		
				return sublist[args[0]]			
			return gettResults
		else:
			def gettResults(sublist):		
				return (sublist[args[0]], sublist[args[1]])			
			return gettResults

	

myList = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
gt = Getter()
lt = gt.mygetter(-1)
print(lt([10,20,30]))
d={'a':1,'b':2, 'c':3}
g=gt.mygetter('b')
print(g(d))
#print([lt(sublist) for sublist in myList])





