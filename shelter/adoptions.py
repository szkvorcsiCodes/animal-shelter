import json


def load_adoptions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_adoptions(file_path, adoptions):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(adoptions, f, indent=4, ensure_ascii=False)


def create_adoption(animal, adopter_name):
    new_adoption = {
        "animal_id": animal["id"],
        "animal_name": animal["name"],
        "adopter": adopter_name
    }
    return new_adoption


def add_adoption(adoptions, adoption):
    for existing_adoption in adoptions:
        if existing_adoption["animal_id"] == adoption["animal_id"]:
            print(f"Error: The {adoption['animal_name']} has already been adopted")
            return
    adoptions.append(adoption)


def show_adoptions(adoptions):
    if not adoptions:
        print("There is not a single adoption yet")
        return
    for adoption in adoptions:
        print(f"ID: {adoption['animal_id']} Animal: {adoption['animal_name']} Adopter: {adoption['adopter']}")
