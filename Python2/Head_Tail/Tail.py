
from lineReader import lineReader

class Tail(lineReader):
	def __init__(self):
		pass

	def printLines(self, tailLines):
		print(tailLines)		

	

lr = lineReader()
lr.createArgs('-e',int,'Add the number of lines from the end')
lr.createArgs('-fn', str, 'Add the filename')
lr.parseArgs('e')
lr.readFile()

tl = Tail()
tailLines = lr.getPrintLines()
tl.printLines(tailLines)

