import os

def recursive_file_print(root):
		
	for fn in os.listdir(root):
		try:
			subdir = root+"/"+fn
			recursive_file_print(subdir)
		except:
			print fn
	
#recursive_file_print(root)
# for filename in os.listdir(root):
# 	subfolder = root+"/"+filename
# 	print subfolder
# 	try:
# 		for i in os.listdir(subfolder):
# 			print i
# 	except:
# 		print "Except: " + filename