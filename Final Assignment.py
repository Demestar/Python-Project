from datetime import datetime
import re
import json
ADMIN_USERNAME = "Banana"
ADMIN_PASSWORD = "B4n4n4"


try:
    with open('username_database.txt', 'r') as f:
        username_database = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "username_database.txt" could not be found!')
    exit()

try:
    with open('user_info_database.txt', 'r') as f:
        user_info_database = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "user_info_database.txt" could not be found!')
    exit()

try:
    with open('available_hall_ids.txt', 'r') as f:
        available_hall_ids = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "available_hall_ids.txt" could not be found!')
    exit()

try:
    with open('available_halls.txt', 'r') as f:
        available_halls = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "available_halls.txt" could not be found!')
    exit()

try:
    with open('booked_hall_ids.txt', 'r') as f:
        booked_hall_ids = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "booked_hall_ids.txt" could not be found!')
    exit()

try:
    with open('booked_halls.txt', 'r') as f:
        booked_halls = json.load(f)
except FileNotFoundError:
    print('Could not run the code as the file "booked_halls.txt" could not be found!')
    exit()


def valid_password(_password):
    lower, upper, number = 0, 0, 0
    for c in _password:
        if 97 <= ord(c) <= 122:
            lower += 1
        if 65 <= ord(c) <= 90:
            upper += 1
        if 48 <= ord(c) <= 57:
            number += 1
    if lower < 2 or upper < 2 or number < 2 or len(_password) < 8:
        return False
    else:
        return True


def valid_date_format(date_string, date_format="%d/%m/%Y"):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def valtime(_time):
    pattern = re.compile("^(0[1-9]|1[0-2]):[0-5][0-9] [APap][Mm]$")
    if not pattern.match(_time):
        return False


def valid_email(_email):
    format = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(format, _email))


def valid_contact(phone_number):
    pattern = re.compile(r'^[+\d-]+$')
    return bool(re.fullmatch(pattern, phone_number))


def main():
    print("==Welcome to Banana Halls! What would you like to do?==")
    print("(1) Sign up as User")
    print("(2) Login as User")
    print("(3) Login as Admin")
    print("(4) Quit")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "1234" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            sign_up()
            break
        elif option == "2":
            login()
            break
        elif option == "3":
            login_as_admin()
            break
        else:
            with open('username_database.txt', 'w') as f:
                json.dump(username_database, f)

            with open('user_info_database.txt', 'w') as f:
                json.dump(user_info_database, f)

            with open('available_hall_ids.txt', 'w') as f:
                json.dump(available_hall_ids, f)

            with open('available_halls.txt', 'w') as f:
                json.dump(available_halls, f)

            with open('booked_hall_ids.txt', 'w') as f:
                json.dump(booked_hall_ids, f)

            with open('booked_halls.txt', 'w') as f:
                json.dump(booked_halls, f)

            print("Goodbye!")
            exit()


def sign_up():
    print("==New account creation==")
    while True:
        username = input("Enter a username (Press enter to go back to main page): ")
        if len(username) < 1:
            main()
            return
        elif username in username_database:
            print("That username already is already taken! Please enter a different username")
        else:
            break

    print("Your password should contain at least 8 characters.")
    print("Your password should also include at least of 2 numbers, 2 uppercase and 2 lowercase characters.")
    password = input("Enter a password: ")
    while not valid_password(password):
        print("Your password is not strong enough! Please follow the format above.")
        password = input("Please re-enter your password: ")
        valid_password(password)

    while True:
        first_name = input("Enter your first name: ")
        if len(first_name) < 1:
            print("Please don't leave this empty!")
        else:
            break

    while True:
        last_name = input("Enter your last name: ")
        if len(last_name) < 1:
            print("Please don't leave this empty!")
        else:
            break

    while True:
        date_of_birth = input("Enter your date of birth (DD/MM/YYYY): ")
        if not valid_date_format(date_of_birth):
            print("Invalid date of birth! Please re-enter.")
        else:
            break

    while True:
        contact_number = input("Enter your contact number: ")
        if len(contact_number) < 1:
            print("Please don't leave this empty!")
        else:
            if not valid_contact(contact_number):
                print("Invalid contact number! Please re-enter.")
            else:
                break

    while True:
        email = input("Enter your email: ")
        if len(email) < 1:
            print("Please don't leave this empty!")
        else:
            if not valid_email(email):
                print("Invalid email address! Please re-enter.")
            else:
                break

    username_database.append(username)
    user_info_database.append(username)
    user_info_database.append(password)
    user_info_database.append(first_name)
    user_info_database.append(last_name)
    user_info_database.append(date_of_birth)
    user_info_database.append(contact_number)
    user_info_database.append(email)

    print("New user successfully created! Please login from the main page.")
    print("Returning to main page...")
    main()


def login():
    print("==Login to your account==")
    username = input("Please enter username (Press enter to go back to main page): ")

    if len(username) < 1:
        main()
        return
    elif username not in username_database:
        print(f"That user does not exist!")
        login()

    user_index = user_info_database.index(username)
    password = input("Please enter password: ")
    if password != user_info_database[user_index + 1]:
        print("Incorrect password!")
        login()
    else:
        user_interface(user_index)


def user_interface(user_index):
    print(f"==Welcome, {user_info_database[user_index]}! What would you like to do?==")
    print("(1) Make a new booking")
    print("(2) View all halls")
    print("(3) View/Edit/Delete bookings")
    print("(4) View/Edit account into")
    print("(5) Delete account")
    print("(6) Logout")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "123456" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            new_booking(user_index)
        elif option == "2":
            view_all_halls(user_index)
        elif option == "3":
            view_edit_delete_bookings(user_index)
        elif option == "4":
            edit_account_info(user_index)
        elif option == "5":
            try:
                if type(user_info_database[user_index + 7]) is dict:
                    print("You cannot delete your account with halls booked! Please delete your bookings before deleting your account.")
                else:
                    delete_account(user_index)
            except IndexError:
                delete_account(user_index)
        else:
            print(f"See you again, {user_info_database[user_index]}!")
            main()


def edit_account_info(user_index):
    print("==View/Edit Account Info==")
    print("Current Info")
    print(f"Username: {user_info_database[user_index]}")
    print(f"Password: {user_info_database[user_index + 1]}")
    print(f"First name: {user_info_database[user_index + 2]}")
    print(f"Last name: {user_info_database[user_index + 3]}")
    print(f"Date of birth: {user_info_database[user_index + 4]}")
    print(f"Contact number: {user_info_database[user_index + 5]}")
    print(f"Email: {user_info_database[user_index + 6]}")

    response = input("Press enter to edit account info. Press q (or any other key) to go back: ")
    if len(response) != 0:
        user_interface(user_index)
        return
    else:
        pass

    username_database.remove(user_info_database[user_index])
    while True:
        username = input("Enter your new username (Press enter to keep current): ")
        if len(username) < 1:
            username = user_info_database[user_index]
            break
        elif username in username_database:
            print("That username already is already taken! Please enter a different username")
        else:
            break
    username_database.append(username)

    print("Your password should contain at least 8 characters.")
    print("Your password should also include at least of 2 numbers, 2 uppercase and 2 lowercase characters.")
    password = input("Enter your new password (Press enter to keep current): ")
    if len(password) < 1:
        password = user_info_database[user_index + 1]
    else:
        while not valid_password(password):
            print("Your password is not strong enough! Please follow the format above.")
            password = input("Please re-enter your password: ")
            valid_password(password)

    first_name = input("Enter your new first name (Press enter to keep current): ")
    if len(first_name) < 1:
        first_name = user_info_database[user_index + 2]

    last_name = input("Enter your new last name (Press enter to keep current): ")
    if len(last_name) < 1:
        last_name = user_info_database[user_index + 3]

    while True:
        date_of_birth = input("Enter your new date of birth (Press enter to keep current) (DD/MM/YYYY): ")
        if len(date_of_birth) < 1:
            date_of_birth = user_info_database[user_index + 4]
            break
        elif not valid_date_format(date_of_birth):
            print("Invalid date of birth! Please re-enter.")
        else:
            break

    while True:
        contact_number = input("Enter your new contact number (Press enter to keep current): ")
        if len(contact_number) < 1:
            contact_number = user_info_database[user_index + 5]
            break
        else:
            if not valid_contact(contact_number):
                print("Invalid contact number! Please re-enter.")
            else:
                break

    while True:
        email = input("Enter your new email (Press enter to keep current): ")
        if len(email) < 1:
            email = user_info_database[user_index + 6]
            break
        else:
            if not valid_email(email):
                print("Invalid email address! Please re-enter.")
            else:
                break

    user_info_database[user_index] = username
    user_info_database[user_index + 1] = password
    user_info_database[user_index + 2] = first_name
    user_info_database[user_index + 3] = last_name
    user_info_database[user_index + 4] = date_of_birth
    user_info_database[user_index + 5] = contact_number
    user_info_database[user_index + 6] = email

    print("Account successfully updated! Here's your latest account info")
    print(f"Username: {user_info_database[user_index]}")
    print(f"Password: {user_info_database[user_index + 1]}")
    print(f"First name: {user_info_database[user_index + 2]}")
    print(f"Last name: {user_info_database[user_index + 3]}")
    print(f"Date of birth: {user_info_database[user_index + 4]}")
    print(f"Contact number: {user_info_database[user_index + 5]}")
    print(f"Email: {user_info_database[user_index + 6]}")
    print("Returning to user interface...")
    user_interface(user_index)


def delete_account(user_index):
    while True:
        answer = input("Are you sure you want to delete your account? This cannot be undone! (y/n): ")
        if answer == "y":
            username_database.remove(user_info_database[user_index])
            i = 0
            while i < 7:
                user_info_database.remove(user_info_database[user_index])
                i += 1
            print("Your account has been deleted successfully. Sorry to see you go!")
            main()
            break
        elif answer == "n":
            print("Returning to user interface...")
            user_interface(user_index)
            break
        else:
            print("Please provide a valid response!")


def view_all_halls(user_index):
    print("==Viewing hall information==")
    print(f"Available halls (by ID): {available_hall_ids}")
    print(f"Booked halls (by ID): {booked_hall_ids}")

    while True:
        hall_id = input("Please enter the ID of the hall you want to view (Press enter to go back to main page): ")
        if len(hall_id) < 1:
            user_interface(user_index)
            return
        elif hall_id in available_hall_ids:
            hall_index = available_halls.index(hall_id)
            print(f"Displaying hall info of {hall_id}")
            print(f"ID: {available_halls[hall_index]}")
            print(f"Name: {available_halls[hall_index + 1]}")
            print(f"Description: {available_halls[hall_index + 2]}")
            print(f"Hall pax: {available_halls[hall_index + 3]}")
            print(f"Status: Available")
            print(f"Rate price per day: ${available_halls[hall_index + 4]}")
        elif hall_id in booked_hall_ids:
            hall_index = booked_halls.index(hall_id)
            print(f"Displaying hall info of {hall_id}")
            print(f"ID: {booked_halls[hall_index]}")
            print(f"Name: {booked_halls[hall_index + 1]}")
            print(f"Description: {booked_halls[hall_index + 2]}")
            print(f"Hall pax: {booked_halls[hall_index + 3]}")
            print(f"Status: Booked")
            print(f"Rate price per day: ${booked_halls[hall_index + 4]}")
        else:
            print(f"That hall does not exist!")


def new_booking(user_index):
    print("==Making a new booking==")
    print(f"Available halls (by ID): {available_hall_ids}")
    while True:
        hall_id = input("Enter a hall ID to view information about that hall (Press enter to go back): ")
        if len(hall_id) < 1:
            user_interface(user_index)
            exit()
        elif hall_id in available_hall_ids:
            break
        else:
            print("That hall ID does not exist!")

    hall_index = available_halls.index(hall_id)
    print("Hall Info")
    print(f"ID: {available_halls[hall_index]}")
    print(f"Name: {available_halls[hall_index + 1]}")
    print(f"Description: {available_halls[hall_index + 2]}")
    print(f"Hall pax: {available_halls[hall_index + 3]}")
    print(f"Status: Available")
    print(f"Rate price per day: ${available_halls[hall_index + 4]}")

    response = input("Press enter to proceed with the booking, press q (or any other key) to go back: ")
    if len(response) != 0:
        new_booking(user_index)
        return

    while True:
        event_name = input("Please enter your event name: ")
        if len(event_name) < 1:
            print("This cannot be empty!")
        else:
            break

    while True:
        event_description = input("Please enter your event description: ")
        if len(event_description) < 1:
            print("This cannot be empty!")
        else:
            break

    while True:
        number_of_pax = input("Please enter your number of pax: ")
        if number_of_pax.isdigit():
            if int(number_of_pax) > int(available_halls[hall_index + 3]):
                print(f"That amount is too big! Maximum amount of pax is {available_halls[hall_index + 3]}")
            else:
                break
        else:
            print("Please enter a valid number!")

    while True:
        date = input("Please enter your date of rental (DD/MM/YYYY): ")
        if not valid_date_format(date):
            print("Invalid date! Please re-enter.")
        else:
            break

    while True:
        time = input("Please enter your time of rental (hh:mm am/pm): ")
        if valtime(time) == False:
            print("Invalid time or incorrect format! Please re-enter")
        else:
            break

    while True:
        payment_price = input("Please enter your payment price: $")
        if payment_price.isdigit():
            if int(payment_price) < int(available_halls[hall_index + 4]):
                print(f"That is not enough! The rate price per day is ${available_halls[hall_index + 4]}!")
            else:
                break
        else:
            print("Please enter a valid number!")

    user_info_database.insert(user_index + 7, {"hall_id": available_halls[hall_index], "event_name": event_name, "event_description": event_description, "number_of_pax": number_of_pax, "date": date, "time": time, "payment_price": payment_price})
    booked_hall_ids.append(available_halls[hall_index])
    booked_halls.append(available_halls[hall_index])
    booked_halls.append(available_halls[hall_index + 1])
    booked_halls.append(available_halls[hall_index + 2])
    booked_halls.append(available_halls[hall_index + 3])
    booked_halls.append(available_halls[hall_index + 4])

    available_hall_ids.remove(available_halls[hall_index])
    i = 0
    while i < 5:
        available_halls.remove(available_halls[hall_index])
        i += 1

    print("Hall successfully booked!")
    print("Returning to user interface...")
    user_interface(user_index)


def view_edit_delete_bookings(user_index):
    print("==View/Edit/Delete Bookings==")
    print("(1) View all bookings")
    print("(2) Edit a booking")
    print("(3) Delete a booking")
    print("(4) Go back")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "1234" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            view_bookings(user_index)
        elif option == "2":
            edit_a_booking(user_index)
        elif option == "3":
            delete_a_booking(user_index)
        else:
            user_interface(user_index)


def view_bookings(user_index):
    print("==Viewing all bookings==")
    print("Here is the list of your bookings")
    print("(If nothing shows up, that means you haven't made any bookings yet)")
    x = 1
    while True:
        try:
            if type(user_info_database[user_index + 6 + x]) is dict:
                print(f"Booking {x}")
                print(f'Hall ID: {user_info_database[user_index + 6 + x]["hall_id"]}')
                print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                print(f'Event Description: {user_info_database[user_index + 6 + x]["event_description"]}')
                print(f'Number of Pax: {user_info_database[user_index + 6 + x]["number_of_pax"]}')
                print(f'Date: {user_info_database[user_index + 6 + x]["date"]}')
                print(f'Time: {user_info_database[user_index + 6 + x]["time"]}')
                print(f'Payment Price: ${user_info_database[user_index + 6 + x]["payment_price"]}')
                print("")
                x += 1
            else:
                break
        except IndexError:
            break
    view_edit_delete_bookings(user_index)


def edit_a_booking(user_index):
    print("==Edit a booking==")
    print("Here is the list of your bookings by your event name")
    print("(If nothing shows up, that means you haven't made any bookings yet)")
    x = 1
    while True:
        try:
            if type(user_info_database[user_index + 6 + x]) is dict:
                print(f"Booking {x}")
                print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                print("")
                x += 1
            else:
                break
        except IndexError:
            break

    while True:
        option = input("Select a booking to edit by typing in the booking number (Press enter to go back): ")
        if len(option) == 0:
            view_edit_delete_bookings(user_index)
            return
        elif option.isdigit():
            try:
                if type(user_info_database[user_index + 6 + int(option)]) is dict:
                    break
                else:
                    print("Please select a valid option!")
            except IndexError:
                print("Please select a valid option!")
        else:
            print("Please select a valid option!")

    hall_id = user_info_database[user_index + 6 + int(option)]["hall_id"]
    hall_index = booked_halls.index(hall_id)

    print(f"You are now editing booking {int(option)}")
    event_name = input("Please enter your new event name (Press enter to keep current): ")
    if len(event_name) < 1:
        event_name = user_info_database[user_index + 6 + int(option)]["event_name"]

    event_description = input("Please enter your event description: ")
    if len(event_description) < 1:
        event_description = user_info_database[user_index + 6 + int(option)]["event_description"]

    while True:
        number_of_pax = input("Please enter your new number of pax (Press enter to keep current): ")
        if len(number_of_pax) < 1:
            number_of_pax = user_info_database[user_index + 6 + int(option)]["number_of_pax"]
            break
        else:
            if number_of_pax.isdigit():
                if int(number_of_pax) > int(booked_halls[hall_index + 3]):
                    print(f"That amount is too big! Maximum amount of pax is {booked_halls[hall_index + 3]}")
                else:
                    break
            else:
                print("Please enter a valid number!")

    while True:
        date = input("Please enter your new date of rental (Press enter to keep current) (DD/MM/YYYY): ")
        if len(date) < 1:
            date = user_info_database[user_index + 6 + int(option)]["date"]
            break
        elif not valid_date_format(date):
            print("Invalid date! Please re-enter.")
        else:
            break

    while True:
        time = input("Please enter your new time of rental (hh:mm am/pm): ")
        if len(time) < 1:
            time = user_info_database[user_index + 6 + int(option)]["time"]
            break
        elif valtime(time) == False:
            print("Invalid time or incorrect format! Please re-enter")
        else:
            break

    while True:
        payment_price = input("Please enter your new payment price (Press enter to keep current): $")
        if len(payment_price) < 1:
            payment_price = user_info_database[user_index + 6 + int(option)]["payment_price"]
            break
        else:
            if payment_price.isdigit():
                if int(payment_price) < int(booked_halls[hall_index + 4]):
                    print(f"That is not enough! The rate price per day is ${booked_halls[hall_index + 4]}!")
                else:
                    break
            else:
                print("Please enter a valid number!")

    user_info_database[user_index + 6 + int(option)]["event_name"] = event_name
    user_info_database[user_index + 6 + int(option)]["event_description"] = event_description
    user_info_database[user_index + 6 + int(option)]["number_of_pax"] = number_of_pax
    user_info_database[user_index + 6 + int(option)]["date"] = date
    user_info_database[user_index + 6 + int(option)]["time"] = time
    user_info_database[user_index + 6 + int(option)]["payment_price"] = payment_price

    print("Booking information successfully updated! Here's your latest booking information:")
    print(f"Booking {int(option)}")
    print(f'Hall ID: {user_info_database[user_index + 6 + int(option)]["hall_id"]}')
    print(f'Event Name: {user_info_database[user_index + 6 + int(option)]["event_name"]}')
    print(f'Event Description: {user_info_database[user_index + 6 + int(option)]["event_description"]}')
    print(f'Number of Pax: {user_info_database[user_index + 6 + int(option)]["number_of_pax"]}')
    print(f'Date: {user_info_database[user_index + 6 + int(option)]["date"]}')
    print(f'Time: {user_info_database[user_index + 6 + int(option)]["time"]}')
    print(f'Payment Price: ${user_info_database[user_index + 6 + int(option)]["payment_price"]}')

    print("Returning to view/edit/delete bookings page...")
    view_edit_delete_bookings(user_index)


def delete_a_booking(user_index):
    print("==Delete a booking==")
    print("Here is the list of your bookings by your event name")
    print("(If nothing shows up, that means you haven't made any bookings yet)")
    x = 1
    while True:
        try:
            if type(user_info_database[user_index + 6 + x]) is dict:
                print(f"Booking {x}")
                print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                print("")
                x += 1
            else:
                break
        except IndexError:
            break

    while True:
        option = input("Select a booking to delete by typing in the booking number (Press enter to go back): ")
        if len(option) == 0:
            view_edit_delete_bookings(user_index)
            return
        elif option.isdigit():
            try:
                if type(user_info_database[user_index + 6 + int(option)]) is dict:
                    hall_id = user_info_database[user_index + 6 + int(option)]["hall_id"]
                    hall_index = booked_halls.index(hall_id)

                    available_hall_ids.append(booked_halls[hall_index])
                    available_halls.append(booked_halls[hall_index])
                    available_halls.append(booked_halls[hall_index + 1])
                    available_halls.append(booked_halls[hall_index + 2])
                    available_halls.append(booked_halls[hall_index + 3])
                    available_halls.append(booked_halls[hall_index + 4])

                    user_info_database.remove(user_info_database[user_index + 6 + int(option)])

                    booked_hall_ids.remove(booked_halls[hall_index])
                    i = 0
                    while i < 5:
                        booked_halls.remove(booked_halls[hall_index])
                        i += 1

                    print("Booking successfully deleted!")
                    print("Returning to view/edit/delete bookings page...")
                    view_edit_delete_bookings(user_index)
                    break
                else:
                    print("Please select a valid option!")
            except IndexError:
                print("Please select a valid option!")
        else:
            print("Please select a valid option!")


def login_as_admin():
    print("==Logging in as Admin==")
    username = input("Please enter username (Press enter to go back to main page): ")
    if len(username) < 1:
        main()
    elif username != ADMIN_USERNAME:
        print("Invalid username!")
        login_as_admin()
    else:
        password = input("Please enter password: ")
        if password != ADMIN_PASSWORD:
            print("Incorrect password!")
            login_as_admin()
        else:
            admin_interface()


def admin_interface():
    print(f"==Welcome, Admin! What would you like to do?==")
    print("(1) Manage halls")
    print("(2) Manage bookings")
    print("(3) Manage users")
    print("(4) Logout")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "1234" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            hall_management()
        elif option == "2":
            manage_bookings()
        elif option == "3":
            manage_users()
        else:
            print(f"See you again, Admin!")
            main()


def manage_users():
    print("==User management==")
    print(f"What would you like to do?==")
    print("(1) List users by username")
    print("(2) View/Edit user information")
    print("(3) Delete user")
    print("(4) Go back")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "1234" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            print("Here are the list of users by username:")
            print(username_database)
            manage_users()
        elif option == "2":
            edit_user_information()
        elif option == "3":
            delete_user()
        else:
            admin_interface()


def edit_user_information():
    while True:
        username = input("Please enter username (Press enter to go back): ")

        if len(username) < 1:
            manage_users()
            break
        elif username not in username_database:
            print(f"That user does not exist!")
        else:
            user_index = user_info_database.index(username)
            break

    print("==Viewing/Editing user info==")
    print("Current Info")
    print(f"Username: {user_info_database[user_index]}")
    print(f"Password: {user_info_database[user_index + 1]}")
    print(f"First name: {user_info_database[user_index + 2]}")
    print(f"Last name: {user_info_database[user_index + 3]}")
    print(f"Date of birth: {user_info_database[user_index + 4]}")
    print(f"Contact number: {user_info_database[user_index + 5]}")
    print(f"Email: {user_info_database[user_index + 6]}")

    response = input("Press enter to edit account info. Press q (or any other key) to go back: ")
    if len(response) != 0:
        manage_users()
        return
    else:
        pass

    username = user_info_database[user_index]
    password = user_info_database[user_index + 1]
    email = user_info_database[user_index + 6]

    first_name = input("Enter a new first name (Press enter to keep current): ")
    if len(first_name) < 1:
        first_name = user_info_database[user_index + 2]

    last_name = input("Enter a new last name (Press enter to keep current): ")
    if len(last_name) < 1:
        last_name = user_info_database[user_index + 3]

    while True:
        date_of_birth = input("Enter a new date of birth (Press enter to keep current) (DD/MM/YYYY): ")
        if len(date_of_birth) < 1:
            date_of_birth = user_info_database[user_index + 4]
            break
        elif not valid_date_format(date_of_birth):
            print("Invalid date of birth! Please re-enter.")
        else:
            break

    while True:
        contact_number = input("Enter a new contact number (Press enter to keep current): ")
        if len(contact_number) < 1:
            contact_number = user_info_database[user_index + 5]
            break
        else:
            if not valid_contact(contact_number):
                print("Invalid contact number! Please re-enter.")
            else:
                break

    user_info_database[user_index] = username
    user_info_database[user_index + 1] = password
    user_info_database[user_index + 2] = first_name
    user_info_database[user_index + 3] = last_name
    user_info_database[user_index + 4] = date_of_birth
    user_info_database[user_index + 5] = contact_number
    user_info_database[user_index + 6] = email

    print("Account successfully updated!")
    print(f"Here's the latest info for user {user_info_database[user_index]}")
    print(f"Username: {user_info_database[user_index]}")
    print(f"Password: {user_info_database[user_index + 1]}")
    print(f"First name: {user_info_database[user_index + 2]}")
    print(f"Last name: {user_info_database[user_index + 3]}")
    print(f"Date of birth: {user_info_database[user_index + 4]}")
    print(f"Contact number: {user_info_database[user_index + 5]}")
    print(f"Email: {user_info_database[user_index + 6]}")
    print("Returning to user management page...")
    manage_users()


def delete_user():
    while True:
        username = input("Please enter username (Press enter to go back): ")

        if len(username) < 1:
            manage_users()
            break
        elif username not in username_database:
            print(f"That user does not exist!")
        else:
            user_index = user_info_database.index(username)
            break

    try:
        if type(user_info_database[user_index + 7]) is dict:
            print("This user has halls booked! Please remove them before deleting their account.")
            admin_interface()
            return
    except IndexError:
        print("This user does not have any bookings. You can proceed to delete")
        pass

    while True:
        answer = input("Are you sure you want to delete this account? This cannot be undone! (y/n): ")
        if answer == "y":
            username_database.remove(user_info_database[user_index])
            i = 0
            while i < 7:
                user_info_database.remove(user_info_database[user_index])
                i += 1
            print("Account has been deleted successfully.")
            print("Returning to user management page...")
            manage_users()
            break
        elif answer == "n":
            print("Returning to user management page...")
            manage_users()
        else:
            print("Please provide a valid response!")


def hall_management():
    print(f"==Hall Management==")
    print("(1) Create new hall")
    print("(2) View halls")
    print("(3) Edit a hall")
    print("(4) Delete a hall")
    print("(5) Go back")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "12345" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            create_new_hall()
        elif option == "2":
            view_halls()
        elif option == "3":
            edit_hall()
        elif option == "4":
            delete_a_hall()
        else:
            admin_interface()


def create_new_hall():
    print("==New hall creation==")
    while True:
        hall_id = input("Enter a hall ID (Press enter to go back): ")
        if len(hall_id) < 1:
            hall_management()
            return
        elif hall_id in available_hall_ids or hall_id in booked_hall_ids:
            print("That hall id already is already taken! Please enter a different one")
        else:
            break

    while True:
        hall_name = input("Enter the name of the hall: ")
        if len(hall_name) < 1:
            print("Please do not leave this empty!")
        else:
            break

    while True:
        hall_description = input("Enter the hall description: ")
        if len(hall_description) < 1:
            print("Please do not leave this empty!")
        else:
            break

    while True:
        hall_pax = input("Enter the number of pax of the hall: ")
        if hall_pax.isdigit():
            break
        else:
            print("Please enter a valid number!")

    while True:
        hall_price = input("Enter the daily price rate of the hall: $")
        if hall_price.isdigit():
            break
        else:
            print("Please enter a valid number!")


    available_hall_ids.append(hall_id)
    available_halls.append(hall_id)
    available_halls.append(hall_name)
    available_halls.append(hall_description)
    available_halls.append(hall_pax)
    available_halls.append(hall_price)

    print("New hall successfully created!")
    print("Returning to hall management page...")
    hall_management()


def view_halls():
    print("==Viewing hall information==")
    print(f"Available halls (by ID): {available_hall_ids}")
    print(f"Booked halls (by ID): {booked_hall_ids}")

    while True:
        hall_id = input("Please enter the ID of the hall you want to view (Press enter to go back to main page): ")
        if len(hall_id) < 1:
            hall_management()
            return
        elif hall_id in available_hall_ids:
            hall_index = available_halls.index(hall_id)
            print(f"Displaying hall info of {hall_id}")
            print(f"ID: {available_halls[hall_index]}")
            print(f"Name: {available_halls[hall_index + 1]}")
            print(f"Description: {available_halls[hall_index + 2]}")
            print(f"Hall pax: {available_halls[hall_index + 3]}")
            print(f"Status: Available")
            print(f"Rate price per day: ${available_halls[hall_index + 4]}")
        elif hall_id in booked_hall_ids:
            hall_index = booked_halls.index(hall_id)
            print(f"Displaying hall info of {hall_id}")
            print(f"ID: {booked_halls[hall_index]}")
            print(f"Name: {booked_halls[hall_index + 1]}")
            print(f"Description: {booked_halls[hall_index + 2]}")
            print(f"Hall pax: {booked_halls[hall_index + 3]}")
            print(f"Status: Booked")
            print(f"Rate price per day: ${booked_halls[hall_index + 4]}")
        else:
            print(f"That hall does not exist!")


def edit_hall():
    print("==Editing hall information==")
    print(f"Available halls (by ID): {available_hall_ids}")
    print(f"Booked halls (by ID): {booked_hall_ids}")

    while True:
        hall_id = input("Please enter the ID of the hall you want to view (Press enter to go back to main page): ")
        if len(hall_id) < 1:
            hall_management()
            return
        elif hall_id in available_hall_ids:
            hall_index = available_halls.index(hall_id)
            print("Current Hall Info")
            print(f"ID: {available_halls[hall_index]}")
            print(f"Name: {available_halls[hall_index + 1]}")
            print(f"Description: {available_halls[hall_index + 2]}")
            print(f"Hall pax: {available_halls[hall_index + 3]}")
            print(f"Status: Available")
            print(f"Rate price per day: ${available_halls[hall_index + 4]}")

            response = input("Press enter to edit hall info. Press q (or any other key) to go back: ")
            if len(response) != 0:
                hall_management()
                return

            hall_name = input("Enter a new hall name (Press enter to keep current): ")
            if len(hall_name) < 1:
                hall_name = available_halls[hall_index + 1]

            hall_description = input("Enter a new hall description (Press enter to keep current): ")
            if len(hall_description) < 1:
                hall_description = available_halls[hall_index + 2]

            while True:
                hall_pax = input("Enter the new number of pax of the hall: ")
                if len(hall_pax) < 1:
                    hall_pax = available_halls[hall_index + 3]
                    break
                elif hall_pax.isdigit():
                    break
                else:
                    print("Please enter a valid number!")

            while True:
                hall_price = input("Enter the new daily price rate of the hall: $")
                if len(hall_price) < 1:
                    hall_price = available_halls[hall_index + 4]
                    break
                elif hall_price.isdigit():
                    break
                else:
                    print("Please enter a valid number!")

            available_halls[hall_index + 1] = hall_name
            available_halls[hall_index + 2] = hall_description
            available_halls[hall_index + 3] = hall_pax
            available_halls[hall_index + 4] = hall_price

            print("Hall successfully updated! Here's the latest hall info")
            print(f"ID: {available_halls[hall_index]}")
            print(f"Name: {available_halls[hall_index + 1]}")
            print(f"Description: {available_halls[hall_index + 2]}")
            print(f"Hall pax: {available_halls[hall_index + 3]}")
            print(f"Status: Available")
            print(f"Rate price per day: ${available_halls[hall_index + 4]}")
            print("Returning to hall management page...")
            hall_management()
            break


        elif hall_id in booked_hall_ids:
            hall_index = booked_halls.index(hall_id)
            print("Current Hall Info")
            print(f"ID: {booked_halls[hall_index]}")
            print(f"Name: {booked_halls[hall_index + 1]}")
            print(f"Description: {booked_halls[hall_index + 2]}")
            print(f"Hall pax: {booked_halls[hall_index + 3]}")
            print(f"Status: Booked")
            print(f"Rate price per day: ${booked_halls[hall_index + 4]}")

            response = input("Press enter to edit hall info. Press q (or any other key) to go back: ")
            if len(response) != 0:
                hall_management()
                return

            hall_name = input("Enter a new hall name (Press enter to keep current): ")
            if len(hall_name) < 1:
                hall_name = booked_halls[hall_index + 1]

            hall_description = input("Enter a new hall description (Press enter to keep current): ")
            if len(hall_description) < 1:
                hall_description = booked_halls[hall_index + 2]

            while True:
                hall_pax = input("Enter the new number of pax of the hall: ")
                if len(hall_pax) < 1:
                    hall_pax = booked_halls[hall_index + 3]
                    break
                elif hall_pax.isdigit():
                    break
                else:
                    print("Please enter a valid number!")

            while True:
                hall_price = input("Enter the new daily price rate of the hall: $")
                if len(hall_price) < 1:
                    hall_price = booked_halls[hall_index + 4]
                    break
                elif hall_price.isdigit():
                    break
                else:
                    print("Please enter a valid number!")

            booked_halls[hall_index + 1] = hall_name
            booked_halls[hall_index + 2] = hall_description
            booked_halls[hall_index + 3] = hall_pax
            booked_halls[hall_index + 4] = hall_price

            print("Hall successfully updated! Here's the latest hall info")
            print(f"ID: {booked_halls[hall_index]}")
            print(f"Name: {booked_halls[hall_index + 1]}")
            print(f"Description: {booked_halls[hall_index + 2]}")
            print(f"Hall pax: {booked_halls[hall_index + 3]}")
            print(f"Status: Booked")
            print(f"Rate price per day: ${booked_halls[hall_index + 4]}")
            print("Returning to hall management page...")
            hall_management()
            break

        else:
            print(f"That hall does not exist!")


def delete_a_hall():
    print("==Deleting a hall==")
    print("Note: You can only delete halls that haven't been booked")
    print('If you want to delete a hall that is booked, you have first to remove the booking via the "Remove a booked hall from a user" option under "Manage bookings"')
    print(f"Available halls (by ID): {available_hall_ids}")
    while True:
        hall_id = input("Please enter the ID of the hall you want to delete (Press enter to go back to main page): ")
        if len(hall_id) < 1:
            hall_management()
            return
        elif hall_id in available_hall_ids:
            hall_index = available_halls.index(hall_id)
            break
        else:
            print("Please select a valid option!")

    available_hall_ids.remove(available_halls[hall_index])
    i = 0
    while i < 5:
        available_halls.remove(available_halls[hall_index])
        i += 1

    print("Hall successfully deleted!")
    print("Returning to hall management page...")
    hall_management()


def manage_bookings():
    print("==Booking Management==")
    print("(1) View booked halls")
    print("(2) Edit booked hall information of a user")
    print("(3) Remove a booked hall from a user")
    print("(4) Go back")

    while True:
        option = input("Please pick an option by typing in the number: ")
        if option not in "12345" or len(option) != 1:
            print("Please enter a valid option!")
        elif option == "1":
            view_booked_halls()
        elif option == "2":
            edit_booked_hall_information()
        elif option == "3":
            remove_booked_hall()
        else:
            admin_interface()


def view_booked_halls():
    print("==Viewing booked halls==")
    print("Displaying user information of all booked halls now")
    print(f"List of booked halls by IDs: {booked_hall_ids}")
    print("(If nothing shows up, that means no one has made any bookings yet)")
    for item in username_database:
        user_index = user_info_database.index(item)
        x = 1
        while True:
            try:
                if type(user_info_database[user_index + 6 + x]) is dict:
                    print(f"Booking {x}")
                    print(f"Username: {item}")
                    print(f'Hall ID: {user_info_database[user_index + 6 + x]["hall_id"]}')
                    print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                    print(f'Event Description: {user_info_database[user_index + 6 + x]["event_description"]}')
                    print(f'Number of Pax: {user_info_database[user_index + 6 + x]["number_of_pax"]}')
                    print(f'Date: {user_info_database[user_index + 6 + x]["date"]}')
                    print(f'Time: {user_info_database[user_index + 6 + x]["time"]}')
                    print(f'Payment Price: ${user_info_database[user_index + 6 + x]["payment_price"]}')
                    print("")
                else:
                    break
            except IndexError:
                break

            x += 1

        manage_bookings()


def edit_booked_hall_information():
    print("==Editing booked hall information of a user==")
    username = input("Please enter username (Press enter to go back): ")

    if len(username) < 1:
        manage_bookings()
        return
    elif username not in username_database:
        print(f"That user does not exist!")
        edit_booked_hall_information()

    user_index = user_info_database.index(username)
    try:
        if type(user_info_database[user_index + 7]) is dict:
            pass
    except IndexError:
        print("That user does not have any bookings!")
        edit_booked_hall_information()

    print(f"Here is the list of bookings by {username}")
    x = 1
    while True:
        try:
            if type(user_info_database[user_index + 6 + x]) is dict:
                print(f"Booking {x}")
                print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                print("")
                x += 1
            else:
                break
        except IndexError:
            break

    while True:
        option = input("Select a booking to edit by typing in the booking number (Press enter to go back): ")
        if len(option) == 0:
            edit_booked_hall_information()
            break
        elif option.isdigit():
            try:
                if type(user_info_database[user_index + 6 + int(option)]) is dict:
                    break
                else:
                    print("Please select a valid option!")
            except IndexError:
                print("Please select a valid option!")
        else:
            print("Please select a valid option!")

    print(f"You are now editing booking {int(option)}")
    event_name = input("Please enter a new event name (Press enter to keep current): ")
    if len(event_name) < 1:
        event_name = user_info_database[user_index + 6 + int(option)]["event_name"]

    event_description = input("Please enter a event description: ")
    if len(event_description) < 1:
        event_description = user_info_database[user_index + 6 + int(option)]["event_description"]

    while True:
        number_of_pax = input("Please enter a new number of pax (Press enter to keep current): ")
        if len(number_of_pax) < 1:
            number_of_pax = user_info_database[user_index + 6 + int(option)]["number_of_pax"]
            break
        if number_of_pax.isdigit():
            break
        else:
            print("Please enter a valid number!")

    while True:
        date = input("Please enter a new date of rental (Press enter to keep current) (DD/MM/YYYY): ")
        if len(date) < 1:
            date = user_info_database[user_index + 6 + int(option)]["date"]
            break
        elif not valid_date_format(date):
            print("Invalid date! Please re-enter.")
        else:
            break

    while True:
        time = input("Please enter a new time of rental (Press enter to keep current) (hh:mm am/pm): ")
        if len(time) < 1:
            time = user_info_database[user_index + 6 + int(option)]["time"]
            break
        elif valtime(time) == False:
            print("Invalid time or incorrect format! Please re-enter")
        else:
            break

    while True:
        payment_price = input("Please enter a new payment price (Press enter to keep current): $")
        if len(payment_price) < 1:
            payment_price = user_info_database[user_index + 6 + int(option)]["payment_price"]
            break
        else:
            if payment_price.isdigit():
                break
            else:
                print("Please enter a valid number!")

    user_info_database[user_index + 6 + int(option)]["event_name"] = event_name
    user_info_database[user_index + 6 + int(option)]["event_description"] = event_description
    user_info_database[user_index + 6 + int(option)]["number_of_pax"] = number_of_pax
    user_info_database[user_index + 6 + int(option)]["date"] = date
    user_info_database[user_index + 6 + int(option)]["time"] = time
    user_info_database[user_index + 6 + int(option)]["payment_price"] = payment_price

    print(f"Booking information successfully updated! Here's the latest booking information for {username}:")
    print(f"Booking {int(option)}")
    print(f'Hall ID: {user_info_database[user_index + 6 + int(option)]["hall_id"]}')
    print(f'Event Name: {user_info_database[user_index + 6 + int(option)]["event_name"]}')
    print(f'Event Description: {user_info_database[user_index + 6 + int(option)]["event_description"]}')
    print(f'Number of Pax: {user_info_database[user_index + 6 + int(option)]["number_of_pax"]}')
    print(f'Date: {user_info_database[user_index + 6 + int(option)]["date"]}')
    print(f'Time: {user_info_database[user_index + 6 + int(option)]["time"]}')
    print(f'Payment Price: ${user_info_database[user_index + 6 + int(option)]["payment_price"]}')

    print("Returning to booking management page...")
    manage_bookings()


def remove_booked_hall():
    print("==Removing a booked hall from a user==")
    username = input("Please enter username (Press enter to go back): ")

    if len(username) < 1:
        manage_bookings()
        return
    elif username not in username_database:
        print(f"That user does not exist!")
        remove_booked_hall()

    user_index = user_info_database.index(username)
    try:
        if type(user_info_database[user_index + 7]) is dict:
            pass
    except IndexError:
        print("That user does not have any bookings!")
        remove_booked_hall()

    print(f"Here is the list of bookings by {username}")
    x = 1
    while True:
        try:
            if type(user_info_database[user_index + 6 + x]) is dict:
                print(f"Booking {x}")
                print(f'Event Name: {user_info_database[user_index + 6 + x]["event_name"]}')
                print("")
                x += 1
            else:
                break
        except IndexError:
            break

    while True:
        option = input("Select a booking to remove by typing in the booking number (Press enter to go back): ")
        if len(option) == 0:
            remove_booked_hall()
            break
        elif option.isdigit():
            try:
                if type(user_info_database[user_index + 6 + int(option)]) is dict:
                    hall_id = user_info_database[user_index + 6 + int(option)]["hall_id"]
                    hall_index = booked_halls.index(hall_id)

                    available_hall_ids.append(booked_halls[hall_index])
                    available_halls.append(booked_halls[hall_index])
                    available_halls.append(booked_halls[hall_index + 1])
                    available_halls.append(booked_halls[hall_index + 2])
                    available_halls.append(booked_halls[hall_index + 3])
                    available_halls.append(booked_halls[hall_index + 4])

                    user_info_database.remove(user_info_database[user_index + 6 + int(option)])

                    booked_hall_ids.remove(booked_halls[hall_index])
                    i = 0
                    while i < 5:
                        booked_halls.remove(booked_halls[hall_index])
                        i += 1

                    print("Booking successfully removed!")
                    print("Returning to booking management page...")
                    manage_bookings()
                    break
                else:
                    print("Please select a valid option!")
            except IndexError:
                print("Please select a valid option!")
        else:
            print("Please select a valid option!")


main()
