import json 

animals = [
  {
    "id": 1,
    "name": "Buddy",
    "type": "dog",
    "age": 3,
    "available": True
  },
  {
    "id": 2,
    "name": "Whiskers",
    "type": "cat",
    "age": 5,
    "available": True
  },
  {
    "id": 3,
    "name": "Coco",
    "type": "rabbit",
    "age": 1,
    "available": False
  },
  {
    "id": 4,
    "name": "Max",
    "type": "dog",
    "age": 7,
    "available": True
  },
  {
    "id": 5,
    "name": "Luna",
    "type": "cat",
    "age": 2,
    "available": True
  }
]
adoption = "Luna"

def load_animals(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        animal_list = json.load(file)
        for animal in animal_list:
            return animal_list


def save_animals(file_path, animals):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(animals)


def show_animals(animals):
    for animal in animals:
        print(f"Animal name: {animal["name"]} \nType: {animal["type"]} \nAge: {animal["age"]} \nIs available: {animal["available"]}")


def get_available_animals(animals):
    available_animals = []
    for animal in animals:
        if animal["available"] == True:
            available_animals.append(animal)     
    return available_animals

animal_id = 100

def find_animal_by_id(animals, animal_id):
    for animal in animals:
        if animal["id"] == animal_id:
            print(animal)
            return animal
        else:
            print("none")
            return None

find_animal_by_id(animals, animal_id)

def update_animal_status(animals, adoption):
    for animal in animals:
        if animal["name"] == adoption:
            if animal["available"] == True:
                animal["available"] = False