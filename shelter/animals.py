import json 

def load_animals(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        animal_list = json.load(file)
        for animal in animal_list:
            print(animal_list)
            return animal_list


def save_animals(file_path, animals):
    with open(file_path, "r", encoding="utf-8") as file:
        animal_list = json.load(file)
        max_id = max(animal["id"] for animal in animal_list)
        for animal in animals:
            animal["id"] = max_id + 1
            animal_list.append(animal)
            max_id += 1
        print(animal_list)
    
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(animal_list, file, indent=4)


def show_animals(animals):
    for animal in animals:
        print(f"Animal name: {animal["name"]} \nType: {animal["type"]} \nAge: {animal["age"]} \nIs available: {animal["available"]}")


def get_available_animals(animals):
    available_animals = []
    for animal in animals:
        if animal["available"] == True:
            available_animals.append(animal)     
    return available_animals


def find_animal_by_id(animals, animal_id):
    for animal in animals:
        if animal["id"] == animal_id:
            return animal
        else:
            return None



def update_animal_status(animals, adoption):
    for animal in animals:
        if animal["name"] == adoption:
            if animal["available"] == True:
                animal["available"] = False