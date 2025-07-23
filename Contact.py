contacts = []

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("✅ Contact added successfully.")

# View all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📋 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search by name or phone
def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep old value):")
            phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New email ({contact['email']}): ") or contact['email']
            address = input(f"New address ({contact['address']}): ") or contact['address']
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            print("✅ Contact updated.")
            return
    print("❌ Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("🗑️ Contact deleted.")
            return
    print("❌ Contact not found.")

# Main menu loop
def main():
    while True:
        print("\n===== 📱 Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

# Run the program
main()
