fullname = input("Enter your full name separated by a space: ")
surname, name, patronymic = fullname.split()
nickname = surname + name[0] + patronymic[0]
with open("out3.txt", "a") as f:
    f.write(f"{fullname} - {nickname}\n")