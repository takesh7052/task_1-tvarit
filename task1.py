#check given condition
def fix_teen(num):
  if num >12 and num <20 and not num ==15 and not num ==16:
    return 0
  else:
    return num

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b)+fix_teen(c)

#check if inputs are numeric
def isNumber(s):
     if s.isdigit() != True:
            return False
     return True

# driver code
l = [x for x in input("Enter three value: ").split()]
flag =0

for i in l:
    if(isNumber(i) == False):
        print("All inputs must be numeric")
        flag =1
   
if(len(l) != 3):
    print("Exactly three numbers are required")
if(flag != 1):
    a, b, c = [l[i] for i in range(3)]   
    sum = no_teen_sum(int(a), int(b), int(c))
    print(sum) 
