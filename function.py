def max_num(a,b,c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

print(max_num(8,5,2))


def multi_list(mylist):
    result = 1
    for x in mylist: 
        result = result * x
    return result

list=[4,5,6]
print(multi_list(list))

def reverse(s):
    if len(s) ==0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "HarshitDesai"
print(reverse(s))