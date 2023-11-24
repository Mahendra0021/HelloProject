# l=["mahendra","Mohit","Pawan","mahendra"]
# print("This list", l)
# if(len(set(l))==len(l)):
#     print("All element unique")
# else:
#     print("All element not unique")
#
#
#
n=int(input("Enter the number:"))
i=3
for i in range(3,n):
    f=0
    for j in range(3,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i,end=' ')
    i=i+1
