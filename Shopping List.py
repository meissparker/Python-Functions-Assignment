shopping_list = []

def add():
    global shopping_list
    item = input("Enter the item you would like to add to the list: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove():
    global shopping_list
    sub = input("Enter the item you would like to remove from the shopping list. ")
    shopping_list.remove(sub)
    print(f"{sub} has been removed from the shopping list.")

def view():
    global shopping_list
    print(f" Current Shopping List: {shopping_list}")

while True:
    choice = input("Choose an action for the shopping list: \n([A]dd item, [R]emove item, [V]iew list), [Q]uit: ").upper()
    if choice == "A":
        add()
    elif choice == "R":
        remove()
    elif choice == "V":
        view()
    elif choice == "Q":
        break
    else: 
        print("Invalid Response")


