CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Welch",
        "address": "7002 Chestnut Ct",
        "email": "hannah@hannah.com"
    },
    {
        "id": 2,
        "name": "Tins Anne",
        "address": "2712 Deerfield",
        "email": "tins@tins.com"
    },
    {
        "id": 3,
        "name": "Grace Hern",
        "address": "12750 Wild Onion",
        "email": "grace@grace.com"
    },
    {
        "email": "blusanders@yahoo.com",
        "name": "Blu Sanders",
        "address": "5121 Camino de la Vista",
        "id": 4
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):

    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


