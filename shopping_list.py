import json
shopping_list = []


def add_to_list(item):
    shopping_list.append(item)
    print("Added! Your list has {} items".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


def remove_from_list(item):
    # shopping_list.remove(item.lower())
    for i in range(len(shopping_list)):
        if shopping_list[i].lower() == item.lower():
            del shopping_list[i]
            break
    print("Removed! Your list has {} items".format(len(shopping_list)))


def clear_list():
    shopping_list.clear()
    print("Cleared! Your list has {} items".format(len(shopping_list)))


def save_list_to_file(filename='shopping_list.json', shopping_list=shopping_list):
    with open(filename, 'w') as file:
        json.dump(shopping_list, file)
    print(f"List saved to {filename}")


def load_list_from_file(filename='shopping_list.json'):
    global shopping_list
    try:
        with open(filename, 'r') as file:
            shopping_list = json.load(file)
        print(f"List loaded from {filename}")
    except FileNotFoundError:
        print("No saved list found. Starting with an empty list.")


def  main():
    load_list_from_file()
    while True:
        print("What do you want to do?")
        print("1) Add an item")
        print("2) Show the list")
        print("3) Remove an item")
        print("4) Clear the list")
        print("5) Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item: ")
            add_to_list(item)
        elif choice == "2":
            show_list()
        elif choice == "3":
            item = input("Enter the item: ")
            remove_from_list(item)
        elif choice == "4":
            clear_list()
        elif choice == "5":
            save_list_to_file(shopping_list=shopping_list)
            break
        else:
            print("Invalid choice")
    print("Goodbye!")


main()
