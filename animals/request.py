ANIMALS = [
    {
        "id": 1,
        "name": "Snoopy",
        "breed": "Border Collie",
        "locationId": 2,
        "customerId": 1
    },
    {
        "id": 2,
        "name": "Spur",
        "breed": "Aussie",
        "customerId": 2,
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Bear",
        "breed": "Aussie",
        "customerId": 2,
        "locationId": 2
    },
    {
        "name": "Kit Kat",
        "breed": "Cat",
        "locationId": 1,
        "customerId": 1,
        "id": 6
    },
    {
        "name": "Pip",
        "breed": "Aussie",
        "locationId": 1,
        "customerId": 2,
        "id": 8
    }
]

def get_all_animals():
    return ANIMALS

def get_single_animal(id):

    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)