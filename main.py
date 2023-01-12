import requests
import inquirer





def mainApp():
    global answer
    questions = [ inquirer.List('userSelection',
                message="Select your choice:",
                choices=['space natural things', 'space shuttles'],
            ),
]
    answer = inquirer.prompt(questions)
    
    if answer['userSelection'] == 'space natural things':
        spaceNaturalThings()

    
def spaceNaturalThings():
    moon = []
    userInput = input("Enter yout Planet, moon,dwarf planet etc... name: ")
    apiLink = f'https://api.le-systeme-solaire.net/rest.php/bodies/{userInput}' 
    r = requests.get(apiLink)
    
    if r.status_code == 200:
        global latinName
        latinName = r.json()['name']
        name = r.json()['englishName']
        isPlanet = r.json()['isPlanet']
        moons = r.json()['moons']
        if moons != None:
             for i in moons:
                moon.append(i['moon'])
                
        typeOfObject = r.json()['bodyType']

        questions = [ inquirer.List('userSelectionPlanet',
            message="Select your choice:",
            choices=['name', 'moons', 'object type'],
            ),
        ]
        userAnswer = inquirer.prompt(questions)
        
        if userAnswer['userSelectionPlanet'] == 'name':
            print(name)
        elif userAnswer['userSelectionPlanet'] == 'moons':
            print(moon)
        elif userAnswer['userSelectionPlanet'] == 'object type':
            print(typeOfObject)
        

    else:
        print(r.status_code)
        print("\n There was an error. try again later... \n")
        spaceNaturalThings()


mainApp()
