import sys
sys.path.append('/home/aransena/Python_Code_Snippets')
import codeSnips as cs	

def countParticipants(root):
	return cs.contentCount(root)

def getTestNum(testPath):
	return int(testPath[len(testPath)-7:-4])

def parseFileNames(root):
	
	filesList=[]
	cs.rFilesList(root,filesList)

	returnList=[]
	xbox_man_list=[]
	xbox_click_list=[]
	xbox_fluid_list =[]
	xbox_increment_list=[]

	app_manual_list=[]
	app_auto_list=[]


	for i in filesList:
		
		if ("manual" in i or "Man" in i or "Manual" in i or "man" in i) and ("xbox" in i or "xBox" in i):
			xbox_man_list.append(i)

		elif "Click" in i or "click" in i:
			xbox_click_list.append(i)

		elif "Fluid" in i or "fluid" in i:
			xbox_fluid_list.append(i)
		
		elif "Increment" in i or "increment" in i or "incremental" in i or "Incremental" in i:
			xbox_increment_list.append(i)

		elif ("manual" in i or "Man" in i or "Manual" in i or "man" in i) and ("app" in i):
			app_manual_list.append(i)

		elif ("Auto" in i or "auto" in i) and ("main" in i or "Main" in i):
			app_auto_list.append(i)

	xbox_man_list=sorted(xbox_man_list, key=lambda x: int(x[len(x)-7:-4]))
	xbox_click_list=sorted(xbox_click_list, key=lambda x: int(x[len(x)-7:-4]))
	xbox_fluid_list=sorted(xbox_fluid_list, key=lambda x: int(x[len(x)-7:-4]))
	xbox_increment_list=sorted(xbox_increment_list, key=lambda x: int(x[len(x)-7:-4]))

	app_manual_list=sorted(app_manual_list, key=lambda x: int(x[len(x)-7:-4]))
	app_auto_list=sorted(app_auto_list, key=lambda x: int(x[len(x)-7:-4]))

	returnList.append(xbox_man_list)
	returnList.append(xbox_click_list)
	returnList.append(xbox_fluid_list)
	returnList.append(xbox_increment_list)
	returnList.append(app_manual_list)
	returnList.append(app_auto_list)

	#print app_auto_list

	return returnList
