import csv

with open('securedata.txt', 'r') as r:
    skimlist = csv.DictReader(r, delimiter=",", fieldnames=['username', 'password', 'firstname', 'lastname', 'email'])
    print(skimlist)
