import json
import time
from os import path
from ast import literal_eval
 

filename = './tweets.json'
listObj = []
 
# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename,encoding="utf8") as fp:
  listObj = json.load(fp)
  print(listObj[1])

for i in listObj:
   print(i)
   str_record=json.dumps(i)
   #print(listObj[i])
   file1 = open("./recordbyrecord.json","a+")#append mode
   file1.write(str_record+'\n')
   
   time.sleep(1)
     
   #file1.close()



    #############file 
 
 
# Verify updated list
#print(listObj)
 
