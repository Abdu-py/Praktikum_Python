for i in range(1, 11):
    print(i)

# ==============================

for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# ==============================

jumlah = 0
for i in range(1, 101):
    jumlah += i
print('Jumlah bilangan 1 sampai 100 adalah:', jumlah)

# ==============================

n = int(input('Masukkan bilangan: '))
hasil = 1
i = 1
while i <= n:
    hasil *= i
    i += 1
print('Faktorial dari', n, 'adalah', hasil)