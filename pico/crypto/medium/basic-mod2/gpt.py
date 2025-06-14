ct = input("input>>\n")

def decrypt(ct):
    arr = []
    angka_int = [int(a) for a in ct.split()]
    for i in angka_int:
        fi = i % 41
        if 1 <= fi <= 26:
            arr.append(chr(ord('A') + fi - 1))  # Perbaikan di sini
        elif 27 <= fi <= 36:
            arr.append(str(fi - 27))
        else:
            arr.append('_')
    return "picoCTF{" + ''.join(arr) + "}"

pt = decrypt(ct)
print(pt)
