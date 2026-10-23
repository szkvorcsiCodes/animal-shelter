from shelter.animals import load_animals, save_animals, show_animals, get_available_animals, find_animal_by_id, update_animal_status
from shelter.adoptions import load_adoptions, save_adoptions, show_adoptions, create_adoption, add_adoption
import json


def main():
    animals = load_animals("data/animals.json")
    adoptions = load_adoptions("data/adoptions.json")
    while True:
        print("=== MENU ===")
        print("1. Show available animals")
        print("2. Adopt animal")
        print("3. Show adoptions")
        print("4. Exit")


        choice = input("Press a number")
        if choice == "1":
            show_animals(animals)
        elif choice == "2":
            adopter_name = input("Give me your name: ")
            animal_id_input = int(input("Give me the animal id: "))
            animal = find_animal_by_id(animals, animal_id_input)
            print(animal)
            new_adoption = create_adoption(find_animal_by_id(animals, animal_id_input), adopter_name)
            add_adoption(adoptions, new_adoption)
            save_adoptions("data/adoptions.json", adoptions)
        elif choice == "3":
            show_adoptions(adoptions)
        elif choice == "4":
            break




if __name__ == "__main__":
    main()
