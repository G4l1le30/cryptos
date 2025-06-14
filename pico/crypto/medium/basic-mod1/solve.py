ct=input("input>\n")

def decrypt(ct):
	arr=[]
	angka_int=[int(a) for a in ct.split()]
	for i in angka_int:
		fi=i%37
		if 0<=fi<=25:
			arr.append(chr(fi+65))
		elif 26<=fi<=35:
			arr.append(str(fi-26))
		else:
			arr.append('_')
	return "picoCTF{" + ''.join(arr)+ "}"

pt=decrypt(ct)
print(pt)
