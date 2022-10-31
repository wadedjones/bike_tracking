# creating software to track total miles on bike
# practice using databases with Postgres

from sql_functions import insert_data, show_all, show_most_recent, total_miles

def main():
    greeting()
    user_input = menu()
    if user_input == 1:
        show_all()
    elif user_input == 2:
        show_most_recent()
    elif user_input == 3:
        total_miles()
    elif user_input == 4:
        user_date, user_miles = enter_stats()
        insert_data(user_date, user_miles)
        print("Ride Entered!")
        show_most_recent()


def greeting():
    print("Welcome to Bike Tracker")

def menu():
    print("Would you like to: ")
    print("\t(1). Show all rides.\n\t(2). Show recent rides.\n\t(3). Show total miles.\n\t(4). Enter a new ride.")
    user_input = None
    while user_input not in [1, 2, 3, 4]:
        user_input = int(input("\tEnter a number (1, 2, 3, 4)\n"))
    return user_input

def check_stats():
    pass

def enter_stats():
    user_date = input("Enter the date of the ride: (YYYY-MM-DD) ")
    user_miles = int(input("Enter the total miles: "))
    return user_date, user_miles

if __name__ == '__main__':
    main()
