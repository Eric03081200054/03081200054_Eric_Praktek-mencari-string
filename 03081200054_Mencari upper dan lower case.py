import os
os.system('cls')

def string_tes(z):
    y={"Upper_Case" : 0,"Lower_Case" : 0}
        
    for i in a:
        if i.isupper():
            y["Upper_Case"]+=1
        elif i.islower():
            y["Lower_Case"]+=1
        else:
            pass
    print("String yang mas cari :",a)
    print("Huruf Besar :", y["Upper_Case"])
    print("Huruf Kecil :", y["Lower_Case"])

a = str(input("Cari apa mas [string]  ?"))
string_tes(a)


