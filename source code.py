import pandas as pd
import sys

filename = input("insert excel file name: ")
filename = filename + ".xlsx"
tablename = input("please insert the name of the table containing the data: ")

try:
    df = pd.read_excel(filename, sheet_name=0) # can also index sheet by name or fetch all sheets
    list1 = df[tablename].tolist()
except:
    print("something went wrong, either the file doesn't exist or the tablename is incorrect")
    print("please check possible capital letters too")
    input("press enter to exit")
    sys.exit()



filename2 = input("insert the name of the second excel file: ")
filename2 = filename2 + ".xlsx" 
tablename2 = input("insert the name of the table containing the data: ")

try:
    df = pd.read_excel(filename2, sheet_name=0)
    darklist = df[tablename2].tolist()
except:
    print("something went wrong, either the file doesn't exist or the tablename is incorrect")
    print("please check possible capital letters too")
    input("press enter to exit")
    exit()

newlist = (set(list1) & set(darklist))

print("")
print("")
print("")
print("")
print("These are all the ships in common on both excel sheets:")
print("")

for i in newlist:
    print(i)
    
input("Press enter to quit")
sys.exit()
