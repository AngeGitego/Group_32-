import sqlite3

# Function to welcome users
def welcome():
    print("Welcome to the Tourism Education Program for Local Schools!")
    print("This program aims to provide basic knowledge and appreciation of the local tourism industry.")
    print("Let's get started!\n")

# Function to display basic information about local landmarks and attractions
def display_information():
    # Connect to the SQLite database
    conn = sqlite3.connect('tourism.db')
    c = conn.cursor()

    # Fetch and display information from the database
    c.execute("SELECT * FROM landmarks")
    landmarks = c.fetchall()
    for landmark in landmarks:
        print(f"{landmark[0]}: {landmark[1]}")
    
    conn.close()

# Function to implement a simple text-based chat interface
def communication_interface():
    print("Welcome to the Communication Interface.")
    print("Feel free to ask any questions or start a discussion.")

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Exiting Communication Interface.")
            break
        else:
            # You can add logic here to handle responses from educators or other students
            print("Educator/Peer: That's an interesting question! Let's discuss.")

# Function to implement basic technical support
def help_function():
    print("Basic Technical Support:")
    print("If you encounter any issues or have questions, please reach out to your teacher or administrator for assistance.")

# Function to display the main menu
def display_menu():
    print("\nMenu:")
    print("1. Information Level")
    print("2. Communication Level")
    print("3. Help")
    print("4. Exit")

# Main function to orchestrate the execution of the program
def main():
    welcome()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_information()
        elif choice == '2':
            communication_interface()
        elif choice == '3':
            help_function()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

