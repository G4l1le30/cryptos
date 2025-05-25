def mirror(code, code2 = ""):
    low=code.lower()
    arr = list(low)
    newArr=[]
    for i in arr:
        num=ord(i)
        if(97<=num<=122):
            newLetter= chr(122-(num-97))
        else:
            newLetter=chr(num)
        newArr.append(newLetter)


    return("".join(newArr))



#a=mirror("hello world")
ct = mirror("abasdcas", "world")
print(ct)
