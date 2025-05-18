class Rot13():
	def decode(self, ct):
		l=list(ct)
		arr=[]
		for x in l:
			o=(ord(x))
			arr.append(o)
		print(arr)
		p=[]
		for x in arr:
			o=x+13
			if(o>90):
				o=64+(o-90)
			p.append(chr(o))
		return ''.join(p)

rot13=Rot13()
ct=input("Input rot13 >> ")
pt=rot13.decode(ct)
print(f'Plaintext: {pt}')
