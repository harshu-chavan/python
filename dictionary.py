dict={}
n=int(input('enter number of keys:'))
for x in range(0,n):
    key=input('enter the key:')
    if key in dict:
        print('the given key exists!')
        for key in dict.keys():
            print(key,end='')
        print('\n^use different keys from above list')
        key=input('enter the key:')
    value=input('enter the value:')
    dict[key]=value
print(dict)  
        
