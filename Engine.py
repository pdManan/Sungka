#Converting a file to string
def readFile(path):
	File=open(path,'r')
	String=File.read()
	File.close()
	return String	

def appendData(playerscore,enemyscore,status):
	file=open('data.txt','a')
	data=str(playerscore)+" vs "+str(enemyscore)+" | "+status+"\n"
	file.write(data)
	file.close