'''
Walk through a directory and get filenames, hash of contents, and time stamp
Return results as a dictionary

'''

import os
import hashlib
import datetime

def get_file_info(filePath):
	results = []
	m=hashlib.sha1()
	for (root, dirs, files) in os.walk(filePath):
		for f in files:
			p=open(f,"r")
			contents=p.read()
			ha=m.update(contents)

			time_stamp = datetime.datetime.fromtimestamp(os.path.getmtime(f))
			d={'fullpath':filePath+'/'+f, 'filename':f,'hash':m.hexdigest(), 'time_stamp':time_stamp}
			results.append(d)
	return results
					

#input filepath to search
filePath = ""
results = get_file_info(filePath)
print(results)
