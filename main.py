
import os
from auth import registration
from bookings import book_room
from rooms import room_types
from data import load_data_from_file, save_data_to_file

def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

menu = """
===============================================================
                     Welcome to HOTEL LUXE                    
===============================================================

🏨 Your comfort is our priority! 🏨

Please choose an option below by typing the corresponding number:

1  Register a new account
2  Log in
3  Log out
4  Add a room to the system
5  Update room status
6  Delete a room
7  Book a room
8  Cancel a booking
9  View bookings
10 Exit

===============================================================
"""

def show_menu():
    clear_console()
    print(menu)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("You selected: Register a new account")
            # Gather input for registration
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            user_type = input("Enter your user type (admin/guest/manager): ")
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            registration(first_name, last_name, user_type, username, email, password)
            print("Registration completed successfully!")

        elif choice == "7":
            print("You selected: Book a room")
            # Example of booking logic
            user_id = int(input("Enter your user ID: "))
            room_id = int(input("Enter room ID: "))
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            book_room(user_id, room_id, check_in, check_out)
            print("Room booked successfully!")

        elif choice == "10":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

