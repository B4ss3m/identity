#! /usr/bin/python3.5

import csv
import random
import time
import datetime

start = time.time()

#Handling CSV files

nameFile = "./baby-names.csv"
surnameFile = "./surnames.csv"
statescitiesFile = "./citiesStates.csv"


nameFile, surnameFile, statescitiesFile = open(nameFile), open(surnameFile), open(statescitiesFile)
nameFile, surnameFile, statescitiesFile = csv.reader(nameFile), csv.reader(surnameFile), csv.reader(statescitiesFile)
nameFile, surnameFile, statescitiesFile = list(nameFile), list(surnameFile), list(statescitiesFile)

    
#Generating identity #Create a function for that

def falseID_NameSurnameGender():
    random_Name_Gender = random.randint(1, 258001)
    random_Surname = random.randint(1, 151672)

    fake_Name = nameFile[random_Name_Gender][1]
    fake_Surname = surnameFile[random_Surname][0]
    fake_Gender = nameFile[random_Name_Gender][3].upper()

    fake_NSG = list()
    fake_NSG.extend([fake_Name, fake_Surname, fake_Gender])

    return fake_NSG

def falseID_AgeBirthday():
    age = random.randint(18, 65)
    jour = random.randint(1, 28)
    month = random.randint(1, 12)

    dt = datetime.datetime.now()
    year = dt.year

    year_Born = year - age

    fake_Date = list()
    fake_Date.extend([age, jour, month, year_Born])
    return fake_Date

def falseID_CityStateCounty():
    random_City = random.randint(1, 63212)

    fake_City = statescitiesFile[random_City][0]
    fake_CityAlias = statescitiesFile[random_City][4]
    
    fake_State = statescitiesFile[random_City][2]
    fake_StateShort = statescitiesFile[random_City][1]
    
    fake_County = statescitiesFile[random_City][3]

    fake_Location = list()
    fake_Location.extend([fake_City, fake_CityAlias, fake_State, fake_StateShort, fake_County])
    return fake_Location

def generating_password_12():
    Speciaux = "[&é\"\'(-è_çà)=ù*^]!?%µ+¹~#{|`@}§:/.;,\\"
    Character = "abcdefghijklmnopqrstuvwxyz"
    Nombre = []
    password = []
    for i in range(1, 13):
        for i in range(0, 10):
            Nombre.append(str(i))
        aléatoire = random.randint(1, 3)
        if aléatoire == 1:
            password.append(Speciaux[random.randint(0, 36)])
        elif aléatoire == 2:
            password.append(Nombre[random.randint(0, 9)])
        elif aléatoire == 3:
            chance = random.randint(1, 2)
            if chance == 1:
                lettre = Character[random.randint(0, 25)].upper()
                password.append(lettre)
            elif chance == 2:
                lettre = Character[random.randint(0, 25)]
                password.append(lettre)
    Ppassword = str()
    for i in password:
        Ppassword += i
    return Ppassword

def generating_email(nameParameter, surnameParameter, stateshortParameter):
    three_first = nameParameter[0:3]
    three_middle = surnameParameter[0:3]
    two_last = stateshortParameter
    domain = ["@protonmail.com", "@gmx.com", "@yandex.com", "@outlook.com", "@yahoo.com"]
    randomize = random.randint(0, len(domain))
    email = three_first + "_" + three_middle + two_last + domain[randomize - 1]
    email = email.lower()
    return email


def presentation(i, NSG, AD, City, Password, Email):
    print("\n -------- Identity #%s -------- \n" % (i + 1))
    print("Name:     %s %s" % (NSG[0], NSG[1]))
    print("Gender:   %s" % (NSG[2]))
    print("Age:      %s   Birthday: %s/%s/%s" % (AD[0], AD[1], AD[2], AD[3]))
    if City[0] == City[1]:
        print("City:     %s   (alias: None)" % (City[0]))
    else:
        print("City:     %s   (alias: %s)" % (City[0], City[1]))
    print("State:    %s (%s)" % (City[2], City[3]))
    print("County:   %s" % (City[4]))
    print("\n")
    print("Email:   ", Email)
    print("Password:", Password)
    print("\n\n")
    
    
def falseID(loop):
    for i in range(loop):
        nameSurnameGender = falseID_NameSurnameGender()
        ageBirthday       = falseID_AgeBirthday()
        cityStateCounty   = falseID_CityStateCounty()
        password          = generating_password_12()
        email             = generating_email(nameSurnameGender[0], nameSurnameGender[1], cityStateCounty[3])
        presentation(i, nameSurnameGender, ageBirthday, cityStateCounty, password, email)
        

number = int(input("How much ID ? "))

falseID(number)

end = time.time()
 
execution = round(end - start, 2)

print("Execution time:", execution, "secondes")
