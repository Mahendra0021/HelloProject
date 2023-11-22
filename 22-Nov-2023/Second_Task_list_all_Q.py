# Q5 Sort a list of strings in ascending order
# s= ["mahendra", "nihit", "gagan", "pawan"]
# x= sorted(s)
# print("Sorted list in ascending order:", x)


# Q6 Remove duplicates from a list while preserving the order of elements.
# s={1,2,4,1,2,5}
# print(s)

# Q7 Perform basic arithmetic operations (addition, subtraction, multiplication, division) using user input.
# a=int(input("Enter the a number: "))
# b=int(input("Enter the b number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Q8 Check if a given number is even or odd.

# a=int(input("Enter the number: "))
# if a%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")



# Q9. Check whether a given year is a leap year or not.
def leap_Year(year):
    if year%400==0 or year%100!=0 and year % 4 == 0:
        print("Year is Leap year")
    else:
        print("Year is not a Leap year ")
year=int(input("Enter Number:"))
leap_Year(year)


# Q10 Use logical operators (AND, OR, NOT) to check conditions and return True or False.

# def fun(n):
#     if n>0 and n%2==0:
#         return  True
#     else:
#         return False
# operator_check=int(input("Enter Number"))
# r=fun(operator_check)
# print(f"Tha NUmber {operator_check} is Even {r} ")


# Q11. Find the maximum and minimum values in a list of numbers.
# l=[34,563,643,65,32]
# print(l)
# a=min(l)
# print(a)
# b=max(l)
# print(b)


# Q12 Check if a string is a pangram (contains all letters of the alphabet)
# def fun(i):
#     a= set("abcdefghijklmnopqrstuvwxyz")
#     b = set(i.lower())
#     return a.issubset(b)
#
# # Example usage
# Name = "mahendra sain "
# if fun(Name):
#     print("The sentence is a pangram.")
# else:
#     print("The sentence is not a pangram.")



# Q13. Split a string into words and count the frequency of each word.
#
# def frequency(n):
#     word=n.split()
#     w_frequency = {}
#     for i in word:
#         if i in w_frequency:
#             w_frequency[i]+=1
#         else:
#             w_frequency[i]=1
#     return w_frequency
# text = "This is a sample text. This is "
#
# result=frequency(text)
# for i,count in result.items():
#     print(f"word: '{i}', Frequency: {count} ")


#Q14. Find the intersection of two lists (common elements).

# l1=[1,2,3,4,5]
# l2=[3,4,5,6,7]
# a=list(set(l1).intersection(l2))
# print("Intersection of the two lists:",a)
#

# Q15. Create a dictionary from two lists (keys and values).

# key_list=["name","age","city"]
# values_list=["mahendra",21,"jaipur"]
# result_dict=dict(zip(key_list,values_list))
# print(result_dict)

#Q16. Check if all elements in a list are unique.
#
# l=[1,3,6,12,32]
# print("The original list is : " + str(l))
# f=0
# f=len(set(l))==len(l)
# if f:
#     print("all unique elements")
# else:
#     print("not all unique elements")



# Q17. Merge two sorted lists into a single sorted list.
#
# l1=[1, 3, 5, 7, 9]
# l2=[2, 4, 6, 8, 10]
# a=l1+l2
# print(a)
# print(sorted(a))

# Q18. Rotate elements in a list by a specified number of positions.

# def rotate(x,y):
#     y=y%len(x)
#     x.extend(x[:y])
#     del x[:y]
#     return x
# x=[1,2,3,4,5,6]
# print("Orignal List:",x)
# y=3
# print("Update List:",rotate(x,y))

# Q19. Determine the factorial of a given number

# a=int(input("Enter the factorial number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# Q20. Find the second largest element in a list of numbers.


# l= [20, 30, 40, 25, 10]
# l.sort()
# print("The second largest element:", l[-2])
