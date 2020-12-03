'''
Implementation of head and tail to print the first and last lines of file from the command line

'''

import os
import argparse


class lineReader(object):
	def __init__(self):
		self.parser = argparse.ArgumentParser()
		self.numPrintLines = None
		self.fileName = None
		self.fileContents=None
		self.lineFlag = None

	def readFile(self):
	'''
	Function for reading the contents of the file self.filename.
	'''
		file1=open(self.fileName, 'r')
		fileContents = file1.read().splitlines()
		
		file1.close()
		self.fileContents = fileContents
	
	def parseArgs(self, flag):
	'''
	Function for parsing the command line arguments and setting the filename and number of 
	lines to print and the line flag.
	Parameters:
		flag: values of s or e; flag s (start) will run head; flag e (end) will run tail
	'''
		myargs = self.parser.parse_args()		
		self.fileName = getattr(myargs,'fn')
		self.numPrintLines = getattr(myargs, flag)
		self.lineFlag = flag

	def getPrintLines(self):
	'''
	Function to print lines from the file.
	'''
		if self.lineFlag == 'e':		
			return('\n'.join(self.fileContents[-self.numPrintLines:]))	
		else:
			return('\n'.join(self.fileContents[:self.numPrintLines]))		
		

	def createArgs(self, flag, flagType, helpStatement):
	'''
	Function to create the argument parser.
	Parameters:
		flag: values of -s or -e or -fn; flag -s (start) will run head; flag -e (end) will run tail;
			flag -fn sets the filename
		flagType: type = int if setting the number of lines; str if specifying the filename
		helpStatement: string a help statement
	'''
		self.parser.add_argument(flag, type=flagType, help=helpStatement)

	





