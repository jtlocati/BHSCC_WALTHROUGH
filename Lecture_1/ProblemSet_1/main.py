
from utils import grade_label, get_valid_grade

# Parallel arrays (same index)
names = []
grades = []
labels = []

def add_student():
    """Collect student info and store it in the arrays."""
    name = input("Enter student name: ").strip()

    # Validate name isn't empty
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    grade = get_valid_grade()
    label = grade_label(grade)

    # Store data (arrays only)
    names.append(name)
    grades.append(grade)
    labels.append(label)

    print(f"Added: {name} (Grade {grade} - {label})")

def view_students():
    """Print all stored students."""
    print("\n=== STUDENT LIST ===")

    if len(names) == 0:
        print("No students have been added yet.")
        return

    # For loop over so we can access all 3 arrays together with the same 'i' value
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]} | Grade {grades[i]} | {labels[i]}")


def main():
    print("=== Student Tracker ===")
    print("A school-approved check-in tracker (arrays only).")

    # Menu loop
    while True:
        print("\nMenu:")
        print("1) Add a student")
        print("2) View all students")
        print("3) Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()