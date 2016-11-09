import csv


def get_name():
    return input("Please enter your username to login:  ")


def get_pass():
    return input("Enter your password to complete your login:  ")


def try_login():
    while True:
        dictionary1 = []
        keyname = get_name()
        passname = get_pass()
        with open('securedata.txt') as f:
            header = ['username', 'password', 'firstname', 'lastname', 'email']
            skimlist = csv.DictReader(f, fieldnames=header, delimiter=',')
            for row in skimlist:
                dictionary1.append(row)
        for line in dictionary1:
            if line['username'] == keyname and line['password'] == passname:
                return True


def write_in(full_list):
    data = full_list
    print(data)
    with open('securedata.txt', 'w') as f:
        header = ['username', 'password', 'firstname', 'lastname', 'email']
        newfile = csv.DictWriter(f, fieldnames=header)
        newfile = csv.writer(f)
        valuelist = []
        for row in data:
            valuelist.append(row.values())
        print(valuelist)
        newfile.writerows(valuelist)


def add_new_user():
    cat = 'green'
    temp = []
    with open('securedata.txt') as f:
        header = ['username', 'password', 'firstname', 'lastname', 'email']
        storage = csv.DictReader(f, fieldnames=header, delimiter=',')
        for line in storage:
            temp.append(line)
    while cat == 'green':
        newname = input("Please enter a new username: ")
        if newname in temp:
            print("That username is taken. Please choose a different one.")
        else:
            while True:
                passpaw = input("Please enter a password (4-8 characters): ")
                newfirst = input("Please enter your first name: ")
                newlast = input("Please enter your last name: ")
                newemail = input("Please provide an e-mail address: ")
                if ((',' not in passpaw) and (',' not in newfirst) and
                    (',' not in newlast) and (',' not in newemail) and
                    (',' not in newname)):
                    newuser = {'username': newname, 'password': passpaw, 'firstname': newfirst, 'lastname': newlast, 'email': newemail}
                    temp.append(newuser)
                    write_in(temp)
                    cat = 'blue'
                    break
                else:
                    print("Please do not include commas")


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
