from lineReader import lineReader

class Tail(lineReader):
	def __init__(self):
		pass

	def printLines(self, tailLines):
		print(tailLines)		

	

lr = lineReader()
lr.createArgs('-s',int,'Add the number of lines from the start')
lr.createArgs('-fn', str, 'Add the filename')
lr.parseArgs('s')
lr.readFile()

tl = Tail()
tailLines = lr.getPrintLines()
tl.printLines(tailLines)
