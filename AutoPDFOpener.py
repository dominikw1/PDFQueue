import glob
import os




pdfList = glob.glob("E:/.everything/books/.Currently Reading/*.pdf")
#print(pdfList);

index = 0;
with open("index.txt", "r") as f:
   # perform file operations
   
   indexStr = f.read()
   index = 0
   if(len(indexStr) != 0):
       index = int(indexStr)

   index +=1
   index %= len(pdfList)
with open("index.txt", "w") as f:
   indexstr = str(index)
   print(index)
   f.write(indexstr)


os.startfile(pdfList[index])