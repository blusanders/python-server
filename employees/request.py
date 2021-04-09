EMPLOYEES = [
    {
        "id": 1,
        "name": "Emp 1",
        "locationId": 1
    },
    {
        "name": "Test Emp",
        "locationId": 2,
        "id": 6
    },
    {
        "name": "This Guy",
        "locationId": 3,
        "id": 7
    },
    {
        "name": "New Person",
        "locationId": 3,
        "id": 8
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):

    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


