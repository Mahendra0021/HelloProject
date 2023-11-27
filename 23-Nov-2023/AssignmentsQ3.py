

        # List operations


l= [2, 3, 5, 3, 7, 9, 2, 5, 11, 13]
print(l)
a=l.index(11)     # index Method
print(a)
l.insert(3,32)   # insert method
print(l)
l.remove(11)      # remove method
print(l)
l.reverse()         # reverse method
print(l)
li=l.count(3)      # count Method the totel number of  element count in list
print(li)
l.append(100)      # append method (append methid list ke end poin m value append kr tha hai)
print(l)

# unique_numbers = set(l)
# print("List without Duplicates:", unique_numbers)
# for i in unique_numbers:
#      a=i*i
#      print("Squared Numbers:",a)


     # set Function
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# uset = s1.union(s2)
# intersection_set = s1.intersection(s2)
# difference_set = s1.difference(s2)
#
# print("Set 1:", s1)
# print("Set 2:", s2)
# print("Union Set:", uset)
# print("Intersection Set:", intersection_set)
# print("Difference Set :", difference_set)


# mydict={
# "fast":'in a quick manner',
# "mahendra":'A coder',# to ye update hone ke bad print A Daner kre ga
# "marks":[23,44,56,78],
# 1:2
# }
# print(mydict)
# mydict['marks']=[36,67,88,93]
# print(mydict['marks'])
# print(mydict['mahendra'])
# print(mydict.keys())
# print(list(mydict.keys()))
# print(list(mydict.values()))       #values Method
# print(type(mydict.keys()))      # keys Method

# updatedict={  #update the dictionary by adding kry-value pairs from
#     "lokesh":"friend",
#     "pawan":"bhai",
#     "sonali":"sister",
#     "mahendra":'A Dancer'   #same key ko bhi print kr the hai
# }
# mydict.update(updatedict)
# print(mydict)
#
# #Dictionary me keys pergent nahi h to get method None value
# # get method used
# print(mydict.get("mahendra1"))



#
# d={
#     "name":"python",
#     "fees":5000,
#     "course":"3 month"
# }
# print(d["fees"])
# d["course"]="2 month"
# print(d)
#
# # dictionary se kuch delete kr na hai to
# # del function ka used kre kr sk the
# # or del function and pop function m keys ka used hoga
# # kuki keys yunik hoti hai
#
# # del function ka used.
# del d['course']
# print(d)
#
# # pop function ka used.
# # pop function values ko return bhi kr tha ki vo kya delete kiya hai
# print(d.pop('fees'))
# print(d)
#
# # dict method:- dict method bhi dictionary ko create kr tha
# # lekin ise m pass kr na pdhta hai variable ke
# # sath m variable ke name ke sath use ki value
# d=dict(name='python',fees=8000)
# print(d)
#
# # insert method.
# d['job']='AWS'
# print(d)


















    # Assignment: File Handling







# reading file handing

# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt","r") as f:
#     files=f.read()
#     print("text file")
#     print(files)


# writing file handling


# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt","w") as f:
#     file=f.write('  How are you')
#     print("written text")


# append file handling


# writing file handling


# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt","a") as f:
#     file=f.write('  How are you')
#     print("written text")



    # create a new file writing method used

# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/data.txt",'w') as f:
#     f.read()


            # Read from the csv file



# import  csv
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/student.csv",'r') as f:
#     r=csv.reader(f)
#     next(r)
#     for i in r:
#         print("display csv file")
#         print(i)


        # writer from the csv file
# import csv
# d=[
#     ['name','age','city'],
#     ['parveen',23,'ajmer']
#
# ]
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/mahendra1.txt",'w',newline='') as f:
#     writer=csv.writer(f)
#     writer.writerows(d)
# print("add data")


            # Reading the json filea
# import json
#
# with open(r"C:\Users\abc\PycharmProjects\pythonProject\HelloProject\23-Nov-2023/read.json",'r')as f:
#     data=json.load(f)
#     for i in data:
#         print(i)

        # Writing the json files

# import  json
# d={
#     'name':'mahendra',
#     'age':21,
#     'city': 'jaipur'
# }
# with open('write.json', 'w') as file:
#     json.dump(d, file, indent=2)
# print("json file add and data submit.")

