
import csv
import sys
import time
import random
import datetime
import hashlib
from csv import writer
from csv import reader
from typing import OrderedDict
from getpass import getpass

"""--------------------------------------------------------
----------------SET UP MA FENETRE UN JOUR------------------
--------------------------------------------------------"""
username=str()
password=str()
accountNumber=int()
authenticated=False

def register():
    global username
    global password
    global accountNumber
    with open('base.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        line = [username, password, accountNumber, dt]
        writer.writerow(line)
    file = open('history.txt', 'a')

def hashPassword(p):
    return hashlib.md5(p.encode()).hexdigest()

def doSignIn():
    global username
    global password
    global accountNumber
    with open('base.csv', 'r') as file:
        accountNumber = 0
        for ligne in file:
            accountNumber+=1
        database=[]
    with open('base.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                database.append(row)
    q2 = input("Would you like to create an account ? ('yes' or 'no') : ")
    if q2 == 'yes':
        username = input('Username (lowercase only) : ')
        password = getpass()
        password2 = getpass()
        while password != password2 :
            print('Passwords does not match !')
            password = getpass()
            password2 = getpass()
        password = hashPassword(password)
        print('You are now successfully registered !')
        print('Your account number is ', accountNumber)
        register()
        return True

def doLogin():
    global username
    username=input('\nUsername: ')
    password = hashPassword(getpass())
    if dict[username] and dict[username]['password'] == password:
        print('You have been correctly authenticated')
        return True
    else:
        print('Unknown username or password')
        exit()
    
def dumpFile(filename):
    with open (filename, 'r') as file:
        for line in file:
            sys.stdout.write(line)


dt = datetime.datetime.now()
print(dt.strftime('%A'), dt.strftime('%B'), dt.strftime('%d'), dt.strftime('%Y'), '; ', dt.strftime('%X'), 'UTC +001')

with open('base.csv', 'r') as file:
    global x 
    x = -1
    for ligne in file:
        x+=1
    print('There are currently ', x, ' members registered.')


'''
Load user file in dictionary
'''

separator=";"
dict = {}
with open('base.csv', 'r') as file:
    headerLine = file.readline().rstrip()
    headers = headerLine.split(separator)
    for line in file:
        data = line.rstrip().split(separator)
        userDict = {}
        for i in range(len(headers)):
            userDict[headers[i]] = data[i]
        userName = userDict["username"]
        dict[userName] = userDict


q1 = input('1) Log in\n2) Sign in\n\n>>> ')

if q1 == '1':
    authenticated = doLogin()

else :
    autheticated = doSignIn()

while authenticated :
    time.sleep(1.0)
    q3=input('\nDo you want to : \n\n1) See your account informations\n2) See code (opensource file)\n3) Contact the support \n4) Exit \n\n>>> ')
    if q3 == '1' :
        print('Username : ', username,' ; \nAccount number : ', dict[username]['account_number'],' ; \nRegistration Date : ', dict[username]['registration_date'])
    elif q3 == '2' :
        print("\nHere is the main file 'login.py'\n\n")
        dumpFile('login.py')
        print("\n\nHere is the other files 'setup.py' and then 'reset.py' : \n")
        dumpFile('setup.py')
        print('\n')
        dumpFile('reset.py')
    elif q3 == '3' :
        print("You can send me an email : 'margot@habegger.fr'")
    else :
        authenticated=False


# --------------------- END OF LOGIN.PY ---------------------------------