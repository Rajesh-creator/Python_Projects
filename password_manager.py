master_pwd = input("What is the master password? >> ")


def view():
    with open("D:\Python\Projects\Mini Projects\passwords.txt", "r") as f:
        for line in f.readlines():
            print(line)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("D:\Python\Projects\Mini Projects\passwords.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? >> ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid Mode.")
        continue