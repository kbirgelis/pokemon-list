
import csv
import random

pokemons = []

with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. First 10 Pokemon")
    print("7. Last 10 Pokemon")
    print("8. Print 10 Pokemon")
    print("9. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        pokefind = int(input("Enter the sequence number: "))
        print(pokemons[pokefind])
        pass
    elif choice == '2':
        pokemons.sort()
        print("Here is the pokemon list, A-Z")
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print("Here is the pokemon list, Z-A")
        print(pokemons)
        pass
    elif choice == '4':
        search_list = str(input("Enter the letters you'd like to use to find the pokemon: "))
        searching = []
        
        for x in pokemons:
            if search_list in x:
                searching.append(x)
        print(searching)
        pass
    elif choice == '5':
        length_list = []

        length_search = int(input("Input the ammount of letters in the Pokemon's name: "))
        length_list = [x for x in pokemons if len(x) == length_search]
        print(length_list)
        pass
    elif choice == '6':
        print(pokemons[:10])
        pass
    elif choice == '7':
        print(pokemons[-10:])
        pass
    elif choice == '9':
        print("Exiting")
        break
    elif choice == '8':
        start = 0
        random_pokemons = pokemons[start:start+10]
        print(random_pokemons)
        choice3 = str(input("N/Q: "))
        if choice3 == 'N':
            random_pokemons = pokemons[start:start+10]
            print(random_pokemons)
        elif choice3 == 'Q':
        
         print("Pokemon list command:")

         while True:
          print("1. Get pokemon by sequence number")
          print("2. Sort by A-Z")
          print("3. Sort by Z-A")
          print("4. Search by text in name")
          print("5. Search by length of name")
          print("6. First 10 Pokemon")
          print("7. Last 10 Pokemon")
          print("8. Print 10 Pokemon")
          print("9. Exit")

        choice = input("Enter your choice (1-9): ")

    else:
    
        print("Invalid choice, choose from 1 to 9")
        print("")

    print("==========================")
