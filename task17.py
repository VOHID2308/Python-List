ismlar = ['Abdurahim', 'Arslon', 'Abduhalil']
necha_martta = int(input("Nechta ism kiritasiz : "))

for i in range(necha_martta):
    ism = input(f"{i+1}-ismni kiriting: ")
    ismlar.append(ism)

print("Kiritilgan ismlar ro'yxati:", ismlar)
print("oxirgi natija (uzunligi) >>", len(ismlar))
