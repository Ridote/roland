import os
import glob
import re
def removeFiles(path, pattern = None):
	path_next = os.path.join(path, '*')
	if(os.path.isdir(path)):
		files = os.listdir(path)
		if(pattern):
			removeTest = lambda file : bool(re.match(pattern, file))
		else:
			removeTest = lambda file : True
		for f in files:
			#if removeTest(f.name):
			os.remove(os.path.join(path, f))