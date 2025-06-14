ct= input("input>>\n")

def decrypt(ct):
	arr=[]
	angka_int=[int(a) for a in ct.split()]
	for i in angka_int:
		fi = i%41
		try:
			inv=pow(fi, -1 ,41)
		except ValueError:
			arr.append('?')
			continue
		if 1<=inv<=26:
			arr.append(chr(ord('A')+inv-1))
		elif 27<=inv<=36:
			arr.append(str(inv-27))
		else: 
			arr.append('_')
	return "picoCTF{" + ''.join(arr) + "}"
pt=decrypt(ct)
print(pt)
