def decrypt(ct):
	arr=[]
	for i in ct:
		if 'a'<=i<='z':
			arr.append(chr(((ord(i)+13-97)%26)+97))
		elif 'A'<=i<='Z':
			arr.append(chr(((ord(i)+13-65)%26)+65))
		else: 
			arr.append(i)
	return ''.join(arr)
ct=input("input >>\n")
pt = decrypt(ct)
print(pt)
