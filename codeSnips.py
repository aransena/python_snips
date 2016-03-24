import os

def rFilePrint(root):
		
	for fn in os.listdir(root):
		try:
			subdir = root+"/"+fn
			rFilePrint(subdir)
		except:
			print fn

def rFilesList(root, filesList):
	for fn in os.listdir(root):
		subdir = root+"/"+fn
		try:
			rFilesList(subdir, filesList)
		except:
			filesList.append(subdir)	

def contentCount(root):
	return len(os.listdir(root))


	
