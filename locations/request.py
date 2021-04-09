LOCATIONS = [
    {
        "id": 1,
        "name": "North Nashville",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "East Nashville",
        "address": "209 Emory Drive"
    },
    {
        "name": "Belle Meade",
        "address": "1234 Rich AF Street",
        "id": 3
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):

    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location


