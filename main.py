def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No notes found.")


print("Welcome to CampusNotes!")
add_note()
view_notes()