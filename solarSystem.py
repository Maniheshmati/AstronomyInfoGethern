import requests

userInput = input("Enter yout Planer, moon etc... name: ")
apiLink = f'https://api.le-systeme-solaire.net/rest.php/bodies/{userInput}' 

r = requests.get(apiLink)

latinName = r.json()['name']
name = r.json()['englishName']
isPlanet = r.json()['isPlanet']
moons = r.json()['moons']
typeOfObject = r.json()['bodyType']
print(f"Latin Name: {latinName}\nEnglish Name: {name}\nis Planet: {isPlanet}\nmoons: {moons}\nType Of Object: {typeOfObject}")