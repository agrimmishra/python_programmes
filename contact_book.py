def print_menu():
    """
    Display the menu options for the contact management system.
    """
    print("Press:")
    print("1: to Add Contact")
    print("2: to Search Contact")
    print("3: to Delete Contact")
    print("4: to Display All Contacts")
    print("5: to Update a Contact")
    print("0: to Exit Program")

def add_contact():
    """
    Add a new contact to the contact book.
    """
    no_of_contact = int(input("how many contact you want to add?: "))
    for i in range(0,no_of_contact):
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ") 
        contact_book[name] = {"phone": phone, "email": email}
        print(f"{name} added successfully.")

def search_contact():
    """
    Search for a contact by name and display their details if found.
    """
    name = input("Enter the name to search: ")
    if name in contact_book:
        print(f"Name: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}")
    else:
        print(f"No contact found with name: {name}")

def display_all_contacts():
    """
    Display details of all contacts in the contact book.
    """
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}")
    else:
        print("Contact book is empty.")

def delete_contact():
    """
    Delete a contact from the contact book by name.
    """
    if contact_book:
            name = input("Enter the name of the contact to delete: ")
            confirm = input(f"are you sure you want to delete {name} ? type y for yes or n for no :").lower()
            if confirm == "y" and name in contact_book:
                del contact_book[name]
                print(f"{name} deleted successfully.")
            else:
                print(f"No contact found with name: {name}")
    else:
        print("your contact book empty")

def update_contact():
    """
    Update phone number or email of an existing contact.
    """
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        choice = input("Enter 'P' to update phone number or 'E' to update email: ").upper()
        match choice:
            case "P":
                new_phone = input("Enter the new phone number: ")
                contact_book[name]['phone'] = new_phone
                print("Phone number updated successfully.")
            case "E":
                new_email = input("Enter the new email address: ")
                contact_book[name]['email'] = new_email
                print("Email address updated successfully.")
            case _:
                print("Invalid choice.")
    else:
        print(f"No contact found with name: {name}")

# Main program loop:
contact_book = {}

while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            add_contact()
        case 2:
            search_contact()
        case 3:
            confirm = input("are you sure? type y for yes or n for no :").lower()
            if confirm == "y":
                delete_contact()
            else:
                pass
        case 4:
            display_all_contacts()
        case 5:
            update_contact()
        case 0:
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please enter a valid option.")
