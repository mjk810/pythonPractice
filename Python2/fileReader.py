'''
Walk a file directory reading in the filename, hash of file contents, time
Dump contents to file using pickle
Rescan method looks for updated files from last time file dumped

'''

import os
import hashlib
import datetime
import pickle

class FileList(object):
	def __init__(self, search_dir, file_write_loc):
		self.search_dir=search_dir
		self.fileInfoList=[]
		self.fileWriteLocation = file_write_loc
	
	def set_initial_list(self):
	'''
	Function to set the set the fileinfolist to the fileobj returned from function scan_dir; this list is written it to a file.
	'''
		self.fileInfoList = self.scan_dir()
		pickle.dump(self.fileInfoList,open(self.fileWriteLocation, 'w'))
	
	def scan_dir(self):
	'''
	Function to scan the directory from search_dir. Function creates a list of fileobjects and creates a FileInfo
	Object for each file searched; FileInfo Object contains the filename, hash of the content, and time_stamp;
	
	'''
		fileObjList = []		
		
		for (root, dirs, files) in os.walk(self.search_dir):
			for f in files:
				p=open(f,"r")
				ha = self.getHash(p.read()_
				

				time_stamp = datetime.datetime.fromtimestamp(os.path.getmtime(f))
				fi = FileInfo(search_dir, f, m.hexdigest(), time_stamp)
				#self.fileInfoList.append(fi)
				fileObjList.append(fi)
				
				#d={'fullpath':filePath+'/'+f, 'filename':f,'hash':m.hexdigest(), 'time_stamp':time_stamp}
				#results.append(d)
		return fileObjList
			
	def getHash(self, contents):
	'''
	Function that returns the hash of the contents
	Parameters:
		contents: the contents of the current file
	'''
		m=hashlib.sha1()
		contents=p.read()
		ha=m.update(contents)
		return ha

	def getNames(self, obj):
	'''
	Function to return the filenames for all files in obj.
	Parameters:
		obj: A list of FileInfoObjects
	Returns:
		filenames
	
	'''
		names = []
		for item in obj:
			names.append(item.filename)
		return names
	
	def rescan(self):
	'''
	Function to rescan the files in the fileWriteLocation and look for new files or files that
	have been removed since the original file search
	Returns:
		A dictionary of the files added and the files removed
	'''		
		info = pickle.load(open(self.fileWriteLocation, 'rb'))
			
		added=[]
		removed = []
		changed = []		
		new_list = self.scan_dir()
		#compare new list with initial list
		orig_file_names = self.getNames(info)
		new_file_names = self.getNames(new_list)	
		for item in new_list:
			if item.filename not in orig_file_names:
				added.append(item.filename)
			
		for name in orig_file_names:
			if name not in new_file_names:
				removed.append(name)
		
		for name in new_file_names:
			p=open(f,"r")
				ha = self.getHash(p.read())
			
				
			
		print('added ', added, ' removed ', removed)
		return {'added':added, 'removed':removed}

	def print_list(self):
	'''
	Function to print filenames
	'''
		for item in self.fileInfoList:
			print(item.filename)


class FileInfo(object):
	def __init__(self, fullPath, filename, file_hash, time_stamp):
		self.fullPath=fullPath
		self.filename=filename
		self.file_hash=file_hash
		self.time_stamp=time_stamp

#Code to run
#input the full path of the directory to search
search_dir = ""
fl = FileList(search_dir, 'file_info_dump')

#set the initial list
#fl.set_initial_list()
#fl.print_list()

#rescan
fl.rescan()


					




