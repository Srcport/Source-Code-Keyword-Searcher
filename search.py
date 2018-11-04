import os,sys

folder = "/Users/Phil/Desktop/vlc-0.9.4"
search = ["input stream", "get_chunk_header", "stream_Peek"]
searchCode = [] #"strcpy", "gets", "sprintf"
comment = ["//", "///", "////" "#", "*"]
fileType = []

searchCount = 0
count = 0

def searchLine(sStr, line):
	global searchCount
	if sStr.replace(" ", "").upper() in line.replace(" ", "").upper():
		print ("[File]: " + file)
		#print ("[Line]: " + line)
		print ("[search]: " + sStr + " on Line " + str(count) + "\n")
		searchCount = searchCount + 1

def openFile(file):
	global count
	with open(file) as f:
		count = 0
		for line in f:
			count = count + 1
			for sStr in search:
				searchLine(sStr, line)
			for cmt in comment:
				if line.replace(" ", "").startswith(cmt):
					break
				else:
					for sStr in searchCode:
						searchLine(sStr, line)
						

for path, subdirs, files in os.walk(folder):
    for name in files:
        file = os.path.join(path, name)
        if len(fileType) == 0:
        	openFile(file)
        else:
        	if os.path.splitext(file)[1] in fileType:
        		openFile(file)
    					
    					
print ("Found " + str(searchCount) + " matching strings.")
       	 		