#!/usr/bin/python3
import sqlite3

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Create landmarks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landmarks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    # Insert sample data into landmarks table (including the additional landmarks)
    cursor.executemany('''
        INSERT INTO landmarks (name, description) VALUES (?, ?)
    ''', [
        ('Volcanoes National Park', 'Home to endangered mountain gorillas and stunning volcanic landscapes.'),
        ('Akagera National Park', 'A diverse wildlife park with savannah, lakes, and the Akagera River.'),
        ('Kigali Genocide Memorial', 'A memorial honoring the victims of the Rwandan Genocide.'),
        ('Lake Kivu', 'One of Africa\'s Great Lakes, known for its scenic beauty and resort towns.'),
        ('Nyungwe Forest National Park', 'A tropical rainforest with diverse flora, fauna, and chimpanzees.'),
        ('Inema Arts Center', 'An art space showcasing contemporary Rwandan and African art.'),
        ('Gisozi Genocide Memorial', 'A memorial site dedicated to the victims of the Rwandan Genocide, located in Kigali.'),
        ('Nyanza Royal Palace', 'A historical site featuring the former royal palace of the Rwandan monarchy, located in Nyanza.'),
        ('Murambi Genocide Memorial', 'A memorial site preserving the remains of victims of the Rwandan Genocide, located in Murambi.'),
        ('Rubavu Beach', 'A popular beach destination along the shores of Lake Kivu, offering stunning views and recreational activities.'),
        ('Musanze Caves', 'A network of caves located in Musanze district, offering opportunities for exploration and adventure.'),
        ('Karongi (Kibuye)', 'A scenic town situated on the shores of Lake Kivu, known for its picturesque landscapes and tranquil atmosphere.'),
        ('Butare National Museum', 'The largest museum in Rwanda, featuring exhibits on Rwandan history, culture, and ethnography.'),
        ('Virunga Mountains', 'A volcanic mountain range spanning Rwanda, Uganda, and the Democratic Republic of the Congo, home to endangered mountain gorillas.'),
        ('Rwesero Arts Museum', 'An art museum located in Nyanza, showcasing contemporary and traditional Rwandan art.')
    ])

    conn.commit()
    conn.close()

# Function to welcome users to the program
def welcome():
    print("Welcome to the Tourism Education Program!")
    print("Let's explore the local tourism industry.\n")

# Function to display the main menu
def display_menu():
    print("MENU:")
    print("1. Learn about local landmarks and attractions")
    print("2. Chat with the program")
    print("3. View your progress")
    print("4. Exit")

# Function to handle user input and validation
def get_user_input(prompt, options=None):
    while True:
        user_input = input(prompt).strip()

        if options and user_input not in options:
            print("Invalid input. Please try again.")
        else:
            return user_input

# Function to display information about landmarks
def display_landmarks():
    # Connect to the database
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Fetch and display landmark information
    cursor.execute("SELECT * FROM landmarks")
    landmarks = cursor.fetchall()

    if landmarks:
        print("Here is information about the local landmarks:")
        for landmark in landmarks:
            print("ID: {}, Name: {}, Description: {}".format(landmark[0], landmark[1], landmark[2]))
    else:
        print("No landmarks found in the database.")

    # Close the database connection
    conn.close()

# Function for chatting with the program
def chat_with_program():
    print("Hello! Please use this email:ank@yahoo.com ,to chat with one of our agents!!")

# Function to display progress
def display_progress():
    print("Viewing progress... You haven't visited any landmarks yet!")

# Main function to orchestrate the program
def main():
    create_database()
    welcome()

    while True:
        display_menu()
        choice = get_user_input("Enter the number of your choice (1-4): ", options=["1", "2", "3", "4"])

        if choice == "1":
            display_landmarks()
        elif choice == "2":
            chat_with_program()
        elif choice == "3":
            display_progress()
        elif choice == "4":
            print("Thank you for using the Tourism Education Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Execute the main function if the script is run
if __name__ == "__main__":
    main()

