# food1 = "egg"
# food2 = "bun dau mam tom"
# food3 = "so huyet"
# food4 = "rau sach"
# food5 = "pho"
# no = 1
# for food in menu:
#     print(no,food, sep =".")
#     no += 1

menu  = ["trung","rauxanh","pho"]
# i = int(input("enter new position"))
# new_food = input("enter new food")
# menu[i] = new_food
# print(*menu,sep = ", ")

# print(menu)
#
# menu.pop()
# print(menu)
# enumerate
for index,food in enumerate(menu):
    print(index + 1,food,sep = ". ")