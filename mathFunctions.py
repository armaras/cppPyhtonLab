
first = lambda n: (n-3)/n**2
i = 0.0
_userinput = int(input("give n"))
_list = []
for x in range(1,_userinput+1):
    _list.append(first(x))

print(sum(_list))

def rec(n):
     global i
     if(i == n):
        print(i, " if")
        return (i/(i+2)) - 10.0
     else:
         print(i , " else ")
         i = i + 1
         return (rec(n) * ((i/(i+2.0)) - 10.0))

def rec2(n):
    if(n == 1):
       return (1/(1+2)) - 10
    else:
       return rec2(n-1) * ((n/(n+2)) - 10)



print(rec2(4))
print(rec(3))
