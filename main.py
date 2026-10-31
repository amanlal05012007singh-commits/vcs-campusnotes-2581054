def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")


def read_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def add_note():
    note = input("Enter your note: ")

    if not note.strip():
        print("Error: Note cannot be empty!")
        return

    save_note(note)
    print("Note saved successfully!")


def view_notes():
    notes = read_notes()

    if notes:
        print("\nYour Notes:")
        print(notes)
    else:
        print("No notes available.")


def main():
    while True:
        print("\n--- CampusNotes ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()