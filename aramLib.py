from os import system

def cmd(argv):
	system(argv)
	
def clr():
	system("clear")
	
def openData(fileName,type=list):
	with open (fileName,"r") as file:
				
		if type==str:
			return file.read()
			
		elif type==list:
			return file.read().split("\n\n\n")

def showData(fileName,data):
	with open(fileName,"w") as file:
		
		if type(data)==list:
			strData=''
			for item in data:
				strData+= str("\n\n\n" + item)
			file.write(strData)
		
		else:
			file.write(data)
			
def wordInlist(list,word):
	return [x for x in list if str(word) in x]
	
def wordInstr(para, word):
	pass
	
def chol(word):
	return wordInlist(openData("vari.txt"),word)	
	
def cholInpagam(word):
	return wordInlist(openData("pagam.txt"),word)