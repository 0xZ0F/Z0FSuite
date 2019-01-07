# This should be the first script to run.
# IMPORT THE MAIN FUNCTION *ONLY* AS THE SCRIPTS NAME/PURPOSE
# Ex: from example import main as example

from oneliners import main as oneliners


def main():

    modules = {"Quit/Exit": "Exit Z0FSuite",
               "1": "Shell Oneliners", "2": "Place Holder"}

    # Banner:
    print("<Z0FSuite>\n")

    while True:
        for module, desc in modules.items():
            print(module + " -", desc)

        option = input("What would you like to do? ").lower()
        print("")  # Makes output look nicer :P
        if(option == "exit" or option == "quit"):
            return 0
        elif(option == "1"):
            oneliners()
        elif(option == "2"):
            print("Placeholder")
        else:
            print("Invalid Type!")

    print("Quitting...")


if __name__ == "__main__":
    main()
