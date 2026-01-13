# utils.py
# Helper functions for the Student Tracker program

def grade_label(grade):
    """Convert a grade number into a label."""
    if grade == 9:
        return "Freshman"
    elif grade == 10:
        return "Sophomore"
    elif grade == 11:
        return "Junior"
    elif grade == 12:
        return "Senior"
    else:
        return "Invalid"

def get_valid_grade():
    """
    Ask the user for a grade until they enter a valid integer between 9 and 12.
    Uses a while loop for validation.
    """
    while True:
        # Input always starts as a string, so we must convert
        raw = input("Enter grade (9-12): ")

        # Check if it's a number before converting (prevents crash)
        if raw.isdigit():
            grade = int(raw)  # type conversion
            if 9 <= grade <= 12:
                return grade

        print("Invalid grade. Please enter a number from 9 to 12.")

