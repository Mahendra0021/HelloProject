
            # File I/O
# python provides the open Function to open the file
# open function is a takes tow arguments
# 1 arguments is a file name and second arguments is a mode in which the file should be opened
# this mode 'r' reading 'w' writing 'a' appending



# File all Mode

# read()- read mode opens the file only reading
# write()- write mode opens the file writing only
# append()- this mode is opend the file append only





# Read Files Method

# open function  example  of how to a open a file for reading
# read(r)- mode is a default
# f=open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra.txt",'r')
# text=f.read()
# print(text)
# f.close()


# create a new txt file , mode is (w) write and filename
# but file is does not exist
#
# f=open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt",'w')
# text=f.read()
# print(text)
# f.close()


# agr binary files open karna ho to  rb mode ka used hota hai
#
# f=open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra.txt",'rb')
# text=f.read()
# print(text)
# f.close()


        # Writing File Method

#
# f=open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt",'w')
# f.write("How are you ")
# f.close()

        # append file Method

# append Method files ke andhar text ko append kr tha hai
#
# f=open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt",'a')
# f.write("How are you ")
# f.close()


            # With Statement

# With Statement to automatically colse the file

# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt", 'a') as f:
#     f.write("With statement is a best ")


        # CSV-Comma Separated Values

# CSV ke pass data table formet m hota hai
# CSV ka most used hota hai
# CSV se relete kuch bhi work hai to CSV ko import kar na hota hai


    # create a CSV file

# import csv
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/student.csv",'w')as f:
#     f.write()



        # used function


 # create a csv file and insert the data student.csv
# import csv
# def create():
#     with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/student.csv",'a') as f:
#         fobj=csv.writer(f)
#         # fobj.writerow(['Roll','Name','Marks'])
#         while True:
#             roll=int(input("Enter the Roll number:"))
#             name=input("Enter the name:")
#             marks=int(input("Enter the Marks:"))
#             r=[roll,name,marks]
#             fobj.writerow(r)
#             ch=int(input("1 Enter the \n 2 Exit \n your choice: "))
#             if ch ==2:
#                 break;
#
# create()

 # csv file data reader

#
# import csv
# def display():
#     with open(r"C:\Users\abc\Downloads\test.csv.csv", 'r') as f:
#         fobj1=csv.reader(f)
#         for i in fobj1:
#             print(i)
#
# display()

            # Search Method Used

# use data ko search kr na hai jinke marks 80 se uper ho
#
# import csv
# def search():
#     with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/student.csv", 'r') as f:
#         fbj=csv.reader(f)
#         next(fbj)
#         for i in fbj:
#             if len(i) >= 3 and int(i[2]) >= 80:
#                 print(i)
# search()
#
#



            #JSON Method

# Json data read
# load ka used string data ko python ke data type  m convert kr tha hai

# import json
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/read.json","r") as f:
#     files=f.read()
#     datajosn=json.loads(files)
#     print(datajosn)


        # Used this For Loop


# import  json
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/read.json","r") as f:
#     x=f.read()
#     DataJson=json.loads(x)
#     for i in DataJson:
#         print(i)

    # kisi ek values ko print kra na

import  json
with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/read.json","r") as f:
    x=f.read()
    DataJson=json.loads(x)
    for i in DataJson:
        print(i['title'],i['pages'])
