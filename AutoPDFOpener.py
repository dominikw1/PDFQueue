import glob
import os

#grab file names
pdfList = glob.glob("E:/.everything/books/.Currently Reading/*.pdf")


#get current index
index = 0;
with open("index.txt", "r") as f:
   indexStr = f.read()
   index = 0
   if(len(indexStr) != 0):
       index = int(indexStr)
   index +=1
   index %= len(pdfList)

#write updated index
with open("index.txt", "w") as f:
   indexStr = str(index)
   f.write(indexStr)

#open pdf
os.startfile(pdfList[index])