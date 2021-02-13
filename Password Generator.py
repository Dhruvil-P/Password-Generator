import random

print("\nWelcome to password generator!\n")

Letters_u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
Letters_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

LU = input("Do you want uppercase letters in your password, Y/N: ")
LL = input("Do you want lowercase letters in your password, Y/N: ")
N = input("Do you want numbers in your password, Y/N: ")
S = input("Do you want symbols in your password, Y/N: ")

# YYYY
if LU == "Y" and LL == "Y" and N == "Y" and S == "Y":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    L_range = int(input("How many lower characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# YYYN
elif LU == "Y" and LL == "Y" and N == "Y" and S == "N":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    L_range = int(input("How many lower characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

#YYNY
elif LU == "Y" and LL == "Y" and N == "N" and S == "Y":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    L_range = int(input("How many lower characters do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

#YNYY
elif LU == "Y" and LL == "N" and N == "Y" and S == "Y":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NYYY
elif LU == "N" and LL == "Y" and N == "Y" and S == "Y":
    L_range = int(input("\nHow many lower characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NYYN
elif LU == "N" and LL == "Y" and N == "Y" and S == "N":
    L_range = int(input("\nHow many lower characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    Password_list = []

    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NYNY
elif LU == "N" and LL == "Y" and N == "N" and S == "Y":
    L_range = int(input("\nHow many lower characters do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NNYY
elif LU == "N" and LL == "N" and N == "Y" and S == "Y":
    N_range = int(input("\nHow many numbers do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# YNYN
elif LU == "Y" and LL == "N" and N == "Y" and S == "N":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    N_range = int(input("How many numbers do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# YNNY
elif LU == "Y" and LL == "N" and N == "N" and S == "Y":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    S_range = int(input("How many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# YYNN
elif LU == "Y" and LL == "Y" and N == "N" and S == "N":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    L_range = int(input("How many lower characters do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# YNNN
elif LU == "Y" and LL == "N" and N == "N" and S == "N":
    U_range = int(input("\nHow many upper characters do you want in your password: "))
    Password_list = []

    for lu in range(1, U_range + 1):
        Password_list += random.choice(Letters_u)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NYNN
elif LU == "N" and LL == "Y" and N == "N" and S == "N":
    L_range = int(input("\nHow many lower characters do you want in your password: "))
    Password_list = []

    for lu in range(1, L_range + 1):
        Password_list += random.choice(Letters_l)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NNYN
elif LU == "N" and LL == "N" and N == "Y" and S == "N":
    N_range = int(input("\nHow many numbers do you want in your password: "))
    Password_list = []

    for lu in range(1, N_range + 1):
        Password_list += random.choice(Numbers)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NNNY
elif LU == "N" and LL == "N" and N == "N" and S == "Y":
    S_range = int(input("\nHow many symbols do you want in your password: "))
    Password_list = []

    for lu in range(1, S_range + 1):
        Password_list += random.choice(Symbols)
    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char
    print(f"\nYour password is: {Password}")

# NNNN
elif LU == "N" and LL == "N" and N == "N" and S == "N":
    print(f"\nOk so you don't want a password. No worries!")
