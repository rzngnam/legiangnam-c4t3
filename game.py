people = ["player","enemy1"]
print(*people)

tendich = input("them quan dich ten la gi ?")
people.append(tendich)

print(*people)
print("x"*20)

action = input("shoot or spawn").lower()

if action == "shoot" or "spawn":
    if action == "shoot":
        people.append("bullet")
    elif action == "spawn":
        people.append("enemy")


print(*people)


