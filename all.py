# Question 1 Task 1: Formatting Flight Itineraries 
def format_itineraries(itineraries):
    formatted_string = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        formatted_string += f"Itinerary {i}: {traveler_name} - from {origin} to {destination}"
        return formatted_string.strip()

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(itineraries))

# Question 2 Task 1: Library System Enhancement
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] 
def add_book(library, new_book):
    ''' add a new book to the library if it is not duplicate.
    Parameters:
    library (list): The list of book in the library. 
    new_book (tuple): The new book to be added, represented as a tuple (title, author).
    
    returns:
    list: updated library list.
    '''
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")

        return library

new_book_1 = ("To kill mockingbird","Harper Lee")
new_book_2 = ("1984", "George Orwell")

library = add_book(library, new_book_1)
library = add_book(library, new_book_2)
print("Updated Library:", library)


# Question 3 Task 1:  Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
def process_orders(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f" Customer:{customer_name}, Product:{product}, Quantity: {quantity}")
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

process_orders(orders)

