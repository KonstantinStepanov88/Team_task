import random
from secrets import choice

def modul_base():
    list_name = ["Иван", "Игорь", "Петр"]
    list_surname = ["Петров", "Иванов","Орлов"]
    list_phone = ["12324", "56376", "3451", "231"]
    list_adress = ["dskf", "sjfh", "akjsgd"]
    dict = {}
    for i in range(1,10000):
        string_info = f"{choice(list_name)} {choice(list_surname)} {choice(list_phone)} {choice(list_adress)}"
        dict[i] = string_info 
    return(dict)
dict1 = modul_base()
for i in dict1:
    print(f"{i} {dict1[i]}")