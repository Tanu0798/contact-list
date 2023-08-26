class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, idx, updated_contact):
        if 1 <= idx <= len(self.contacts):
            self.contacts[idx - 1] = updated_contact

    def delete_contact(self, idx):
        if 1 <= idx <= len(self.contacts):
            del self.contacts[idx - 1]

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contacts(query)
            print("Search Results:")
            for idx, result in enumerate(search_results, start=1):
                print(f"{idx}. {result.name} - {result.phone}")

        elif choice == "4":
            contact_manager.view_contacts()
            idx = int(input("Enter the index of the contact to update: "))
            updated_name = input("Name: ")
            updated_phone = input("Phone Number: ")
            updated_email = input("Email: ")
            updated_address = input("Address: ")
            updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
            contact_manager.update_contact(idx, updated_contact)
            print("Contact updated successfully!")

        elif choice == "5":
            contact_manager.view_contacts()
            idx = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(idx)
            print("Contact deleted successfully!")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
