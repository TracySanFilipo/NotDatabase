import csv


def get_name():
    name1 = input("Please enter your username to login:  ")


def get_pass():
    pass1 = input("Enter your password to complete your login:  ")


def try_login():
    while True:
        dictionary1 = {}
        keyname = get_name()
        passname = get_pass()
        with open('securedata.txt') as f:
            skimlist = csv.DictReader(f, delimiter=",", fieldnames=['username', 'password', 'firstname', 'lastname', 'email'])
            for row in skimlist:
                dictionary1.update(row)
                print(dictionary1)
        for line in dictionary1:
    #        if line[username] == keyname and line[password] == passname:
            return True


def write_in(full_list):
    data = full_list
    with open('securedata.txt', 'w') as f:
        f.write(','.join(full_list))


def add_new_user():
    temp = []
    with open('securedata.txt', 'w') as f:
        storage = csv.DictReader(f)
        for line in storage:
            temp.append(line)
    while True:
        newname = input("Please enter a new username: ")
        if newname in temp:
            print("That username is taken. Please choose a different one.")
        else:
            while True:
                passpaw = input("Please enter a password (4-8 characters): ")
                newfirst = input("Please enter your first name: ")
                newlast = input("Please enter your last name: ")
                newemail = input("Please provide an e-mail address: ")
                if ((3 < len(passpaw) < 16) and (',' not in passpaw) and
                (1 < len(newfirst) < 19) and (',' not in newfirst)
                and (3 < len(newlast) < 31) and (',' not in newlast)
                and (3 < len(newemail) < 31) and (',' not in newemail)
                and (2 < len(newname) < 20) and (',' not in newname)):
                    newuser = [newname, passpaw, newfirst, newlast, newemail]
                    temp.append(newuser)
                    write_in(temp)
                    break
                else:
                    print("""Please keep the password between 4 and 15
                            characters, the first name between 2 and 18,
                            the last name between 2 and 30, and the e-mail
                            address between 4 and 30""")


def logged_in_options():
    while True:
        decisions = input("""Would you like to create a new login(n),
                            or logout(l)?  """)
        if decisions.lower() == 'n':
            add_new_user()
        elif decisions.lower() == 'l':
            return
        else:
            continue

def main():
    while True:
        user1 = try_login()
        if user1 == True:
            logged_in_options()


if __name__ == "__main__":
    main()
