#  Шифр подстановки
orig_alpha, fin_alpha = input(), input()
for_encryption, for_decryption = input(), input()

encrypted = ''.join(fin_alpha[orig_alpha.index(c)] for c in for_encryption)
decrypted = ''.join(orig_alpha[fin_alpha.index(c)] for c in for_decryption)

print(encrypted, decrypted, sep='\n')
