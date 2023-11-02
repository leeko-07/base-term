import csv
import datetime

with open('base.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    ligne = ['username', 'password', 'account_number', 'registration_date']
    writer.writerow(ligne)

file = open('history.txt', 'w')
dt = datetime.datetime.now()
dt = str(dt)
file.write(dt)
file.write("\nBeginning of the history file linked to 'base.csv' where will be registrated users, passwords, users' account numbers and registration dates.\nAll activity will be related in this document (connections, registrations, password changes, account deletions... \nThanks for using SecPass !\n")
file.close

file = open('history.txt')
show = file.read()
print(show)
file.close

with open('base.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for ligne in reader:
        print(ligne)


# --------------------- END OF SETUP.PY ---------------------------------