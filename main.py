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


if __name__ == "__main__":
    main()
