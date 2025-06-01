from rsa_user import create_user, select_user, send_message, read_message, menu

import sys

def main():
    while True:
        menu()
        option = input("Choose an option: ").strip()
        if option == '1':
            create_user()
        elif option == '2':
            send_message()
        elif option == '3':
            read_message()
        elif option == '4':
            print("Exiting the RSA Messaging System")
            input("Press Enter to exit...")
            sys.exit()
        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()
