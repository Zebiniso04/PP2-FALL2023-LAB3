import math
import time
#1
List = [int (i) for i in input().split()]
prod = math.prod(List)
print(prod)
 
#2
s = str(input())
countUp = 0
countlow = 0

for i in s:
    if(i.isupper()):
        countUp=countUp+1
    else:
        countlow=countlow+1
print(countUp, countlow) 

#3
s = str(input())
r = reversed(s)
rev = ''
for i in r:
    rev=rev+i
    
if(s == rev):
    print("isPalindrome")
else:
    print("isNoPalindrome")
     
#4
num = int(input("number:"))
milsec = int(input("outputAfetTime:"))
res = float(math.sqrt(num))
time.sleep(milsec/1000)
print("Square root of ", num, " after ", milsec, " miliseconds is ", res )
         
#5
my_tuple = {True,True,True,False}
res = all(my_tuple)
if(res):
    print("All elements is True")
else:
    print("Not all elements is True")