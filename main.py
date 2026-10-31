def add_note():
    note = input("Enter your note: ")

    if not note.strip():
        print("Error: Note cannot be empty!")
        return

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()

            if notes:
                print("\nYour Notes:")
                print(notes)
            else:
                print("No notes available.")

    except FileNotFoundError:
        print("No notes found.")


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