inp = input("Take a Note: ")

with open("note.txt", 'w') as f:
    f.write(inp)

def read_note():
    with open("note.txt", 'r') as f:
        print("Your saved note:/n")
        print(f.read())

def save_note():
    note = input("Write your note: ")
    with open("note.txt", 'a') as f:
        f.write(note + "\n")
    print("Note saved!\n")

def read_notes():
    with open("note.txt", 'r') as f:
        print("\nYour Notes:")
        print(f.read())

while True:
    print("\n--- Aditya's Notes App ---")
    print("1. Add Note")
    print("2. Read Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        save_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
