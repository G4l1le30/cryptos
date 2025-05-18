class Caesar():
        def decode(self, ct):
                l=list(ct.upper())
                arr=[]
                for x in l:
                        o=(ord(x))
                        arr.append(o)
                print(arr)
                p=[]
                key=0
                for i in range(1, 25):
                    for x in arr:
                            o=x+i
                            if(o>90):
                                    o=64+(o-90)
                            p.append(chr(o))
                    key+=1
                    print(f'key = {key}')
                    print(''.join(p))
                    p=[]

caesar=Caesar()
ct=input("Input caesar >> ")
pt=caesar.decode(ct)
