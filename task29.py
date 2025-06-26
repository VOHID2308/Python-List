sonlar = []

for i in range(10):
    son = int(input(f"{i + 1} sonni kiriting : "))
    sonlar.append(son)

noyob_sonlar = []
for son in sonlar :
    if sonlar.count(son) == 1: 
        noyob_sonlar.append(son)

print("Takrorlanmagan sonlar ",noyob_sonlar)