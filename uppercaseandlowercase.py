string=input('enter a string:')
up=low=ele=0
for x in string:
    if x.isupper():
        up+=1
    elif x.islower():
        low+=1
    else:
        ele+=1
print('no.of upper case characters:',up)
print('no.of.lower case characters:',low)
print('other special symbols',ele)
print("the number of uppercase characters is:")

        
