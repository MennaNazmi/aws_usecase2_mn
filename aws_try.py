# This program prints Hello, world!

#print('Hello, world!')
#D:\amazon AWS\proj_vs
#from ast import literal_eval
#import json
#import time
# Opening JSON file
#f = open('D:\\amazon AWS\\proj_vs\\tryfile.json')
# returns JSON object as
# a dictionary
#data = json.load(f)
 
# Iterating through the json
# list
#json_object = json.dumps(data, indent = 3)
#print(json_object)
#for i in data['users']:
  #  time.sleep(1)
   # print(i)
    #json_object = json.dumps(i)
    #data.append(json_object)
    #print(json_object)
  #  z = json.loads(json_object)
    #print(z)
    #z.update(eval(json_object))
    #print(json.dumps(z))
    #data.update(i)
    #f2.seek(0)
    #json_string = json.dumps(i)
    #print(json_string)
 #   with open('output_from_tryfile.json', 'w') as outfile:
 #     outfile.write(json_object)
 #output_from_tryfile
# Closing file

  
#f.close()
###############################
import json
import time
from os import path
from ast import literal_eval
 
filename = 'D:\\amazon AWS\\proj_vs\\tweets.json'
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
   file1 = open("D:\\amazon AWS\\proj_vs\\myfile.txt","a+")#append mode
   file1.write(str_record+'\n')
   
   time.sleep(1)
   print("###############")
   
   #file1.close()



    #############file 
 
 
# Verify updated list
#print(listObj)
 
