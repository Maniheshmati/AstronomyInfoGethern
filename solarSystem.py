import requests


def appOps():
    userInput = input("Enter yout Planet, moon,dwarf planet etc... name: ")
    apiLink = f'https://api.le-systeme-solaire.net/rest.php/bodies/{userInput}' 
    r = requests.get(apiLink)
    
    if r.status_code == 200:
        latinName = r.json()['name']
        name = r.json()['englishName']
        isPlanet = r.json()['isPlanet']
        moons = r.json()['moons']
        typeOfObject = r.json()['bodyType']
        print(f"Latin Name: {latinName}\nEnglish Name: {name}\nis Planet: {isPlanet}\nmoons: {moons}\nType Of Object: {typeOfObject}")

    else:
        print(r.status_code)
        print("\n There was an error. try again later... \n")
        appOps()

appOps()
