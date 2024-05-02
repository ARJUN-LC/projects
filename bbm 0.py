
import sqlite3

def create_database():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    blood_type TEXT NOT NULL,
                    contact_number TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    blood_type TEXT PRIMARY KEY,
                    quantity INTEGER DEFAULT 0)''')

    conn.commit()
    conn.close()

def add_donor():
    name = input("Enter donor name: ")
    blood_type = input("Enter donor blood type: ")
    contact_number = input("Enter donor contact number: ")

    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()

    c.execute("INSERT INTO donors (name, blood_type, contact_number) VALUES (?, ?, ?)", (name, blood_type, contact_number))

    conn.commit()
    conn.close()

    print("Donor added successfully!")

def search_donors():
    blood_type = input("Enter blood type to search: ")

    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()

    c.execute("SELECT * FROM donors WHERE blood_type = ?", (blood_type,))
    donors = c.fetchall()

    if not donors:
        print("No donors found for the specified blood type.")
    else:
        print(f"Donors with blood type {blood_type}:")
        for donor in donors:
            print(f"Name: {donor[1]}, Contact: {donor[3]}")

    conn.close()

def update_inventory():
    blood_type = input("Enter blood type to update: ")
    quantity = int(input("Enter quantity to add: "))

    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()

    c.execute("INSERT INTO inventory (blood_type, quantity) VALUES (?, ?) ON CONFLICT (blood_type) DO UPDATE SET quantity = quantity + ?", (blood_type, quantity, quantity))

    conn.commit()
    conn.close()

    print("Blood inventory updated successfully!")

def view_inventory():
    conn = sqlite3.connect('blood_bank.db')
    c = conn.cursor()

    c.execute("SELECT * FROM inventory")
    inventory = c.fetchall()

    print("Blood Inventory:")
    for item in inventory:
        print(f"Blood Type: {item[0]}, Quantity: {item[1]}")

    conn.close()

def main():
    create_database()

    while True:
        print("\nBlood Bank Management")
        print("1. Add Donor")
        print("2. Search Donors by Blood Type")
        print("3. Update Blood Inventory")
        print("4. View Blood Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_donor()
        elif choice == '2':
            search_donors()
        elif choice == '3':
            update_inventory()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()