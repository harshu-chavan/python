list1=[]
list3=[]
list2=[]
n=int(input('enter number of elements:'))
for i in range(n):
    value=int(input())
    list1.append(value)
print(list1)
n=int(input('enter a number to sort list:'))
for i in list1:
    if n>i:
        list2.append(i)
    else:
        list3.append(i)
print('less then{}value list:'.format(n),list2)
print('greater than{}value list:'.format(n),list3)       
