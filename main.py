from operator import truediv

countrydb={}
while True:
    print("choose the option you want:\n 1. Insert\n2. Display all countries\n3. display all capitals\n 4. get capitals\n 5. delete")
    choice=int(input("Enter your choice:"))
    if choice==1:
        country_name=input("type the name of your country:").upper()
        capital_name=input("enter the counties capital:").upper()
        countrydb[country_name]=capital_name
        print(countrydb)
    if choice==2:
        print(countrydb.keys())
    if choice == 3:
        print(countrydb.values())
    if choice==4:
        country_name=input("enter a country name").upper()
        print(countrydb.get(country_name))
    if choice==5:
        country_name=input("enter a country").upper()
        del countrydb[country_name]
        print("")
    if choice>=6:
        break