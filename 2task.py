user_input = input("Введите список: ").strip()
count1= user_input.count("(")
count2= user_input.count(")")

if count1 == 0 or count2 == 0:
    print("0")
elif count1 == count2:
    print(count1)
elif count1 > count2:
    print(count2)
else:
    print(count1)
