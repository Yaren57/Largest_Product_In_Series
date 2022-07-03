sayi = 'problem8.txt'

i = 0
j = 1
buyuk_toplam = 0

while i < len(sayi):
    toplam = int(sayi[i])

    while j < 13 and (i + 13) <= len(sayi):
        toplam *= int(sayi[i + j])
        j += 1
    if toplam > buyuk_toplam:
        buyuk_toplam = toplam
        k = i
    i += 1

print(buyuk_toplam)
print(k)