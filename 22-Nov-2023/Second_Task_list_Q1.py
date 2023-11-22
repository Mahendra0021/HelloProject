
# """palindrome is a sequence of characters and when reversed,
#   would result in the exact same sequence of characters"""

i=int(input("Enter the Number: "))
reverse=0
x=i
while (i>0):
    reverse=(reverse*10)+i%10
    i=i//10
if x==reverse:
    print("Palindrome Number")
else:
    print(" Not Palindrome Number")