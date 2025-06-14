def decrypt(ct):
    arr = []
    angka_int = [int(a) for a in ct.split()]
    for i in angka_int:
        fi = i % 41
        try:
            inv = pow(fi, -1, 41)  # Modular inverse dari fi mod 41
        except ValueError:
            arr.append('?')  # Tidak ada invers
            continue

        if 1 <= inv <= 26:
            arr.append(chr(ord('A') + inv - 1))
        elif 27 <= inv <= 36:
            arr.append(str(inv - 27))
        elif inv == 37:
            arr.append('_')
        else:
            arr.append('?')  # Di luar range mapping
    return "picoCTF{" + ''.join(arr) + "}"

# Contoh pemakaian:
ct = input("input>>\n")
print(decrypt(ct))

