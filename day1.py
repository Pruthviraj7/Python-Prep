# """ 
#  #Q.1 Can you reverse the below string?
# (without using reversed modules)

# s = "Data Analytics"
# """
s="Data Analytics"
num=len(s)-1
reversed_string=''

while num>=0:
    # print(s[num])
    reversed_string+=s[num]
    num-=1

print(reversed_string)
# print(len(s)) # counts space as well


""" 
Task
Q.2
Remove duplicates elements from below list
(while maintaining the order, also return as list)


"""

my_list = [3, 1, 1, 2, 4, 4]

my_dict=list(dict.fromkeys(my_list))
print(my_dict)