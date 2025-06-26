list1 = input("1-ro‘yxat (vergul bilan): ").split(",")
list2 = input("2-ro‘yxat (vergul bilan): ").split(",")

list1 = [i.strip() for i in list1]
list2 = [i.strip() for i in list2]

for i in range(len(list1)):
    list1[i], list2[i] = list2[i], list1[i]

print("Yangi list1:", list1)
print("Yangi list2:", list2)
