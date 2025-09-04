# NUR_IZZATI
# TP079290

import json


def load_data(filename="students_data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Corrupted data file. Starting fresh.")
        return []


def save_data(data, filename="students_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # indent will add breaks and spacing in json file
    print("Data saved successfully.")


def calculate_grade(avg):
    if 80 <= avg <= 100:
        return "A+"
    elif 75 <= avg < 80:
        return "A"
    elif 70 <= avg < 75:
        return "B+"
    elif 60 <= avg < 70:
        return "B"
    elif 50 <= avg < 60:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def generate_student_id(data):
    return f"S{len(data) + 1:04d}"  # Example : S0001, S0002


def add_student(data):
    name = input("Enter student name: ")
    print("Example classes: 1 Anggun, 2 Anggerik, 3 Dahlia")
    class_name = input("Enter class name (type exactly as intended): ").strip()
    while len(class_name) < 3:
        print("Class name seems too short. Please enter a valid name like '1 Anggun'")
        class_name = input("Enter class name again: ").strip()
    student_id = generate_student_id(data)

    subjects = {}
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i + 1}: ")
        while True:
            try:
                score = float(input(f"Enter score for {subject}: "))
                if 0 <= score <= 100:
                    subjects[subject] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = sum(subjects.values()) / len(subjects)
    grade = calculate_grade(average)

    data.append({
        "id": student_id,
        "name": name,
        "class": class_name,
        "subjects": subjects,
        "average": average,
        "grade": grade
    })

    print(f"{name}'s data added successfully.")


def search_student(data):
    print("\nSearch by:")
    print("1. Name")
    print("2. Student ID")
    option = input("Choose option (1 or 2): ").strip()

    if option == "1":
        search_name = input("Enter the name to search: ").strip()
        for student in data:
            if student["name"].strip().lower() == search_name.lower():
                print("\n--- Student Found ---")
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Class: {student['class']}")
                print("Subjects and Scores:")
                for subject, score in student["subjects"].items():
                    print(f"  {subject}: {score}")
                print(f"Average: {student['average']:.2f}")
                print(f"Grade: {student['grade']}")
                return
        print("Student not found.")

    elif option == "2":
        search_id = input("Enter the Student ID to search (e.g., S0001): ").strip().upper()
        for student in data:
            if student["id"].strip().upper() == search_id:
                print("\n--- Student Found ---")
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Class: {student['class']}")
                print("Subjects and Scores:")
                for subject, score in student["subjects"].items():
                    print(f"  {subject}: {score}")
                print(f"Average: {student['average']:.2f}")
                print(f"Grade: {student['grade']}")
                return
        print("Student ID not found.")

    else:
        print("Invalid option.")


def view_summary(data):
    if not data:
        print("No student data available.")
        return

    class_name = ""

    print("\nChoose summary type:")
    print("1. School Performance Summary")
    print("2. Class Performance Summary")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        # School Performance Summary
        selected_students = data
        summary_title = "School Performance Summary"

    elif choice == "2":
        # Filter by class
        class_name: str = input("Enter class name (e.g., 5 Anggerik): ").strip()
        selected_students = [s for s in data if s.get("class", "").lower() == class_name.lower()]
        if not selected_students:
            print(f"No students found in class '{class_name}'.")
            return
        summary_title = f"Class Performance Summary - {class_name}"

    else:
        print("Invalid choice. Returning to menu.")
        return

    # Calculate summary
    averages = [student["average"] for student in selected_students]
    print(f"\n--- {summary_title} ---")
    print(f"Total Students: {len(selected_students)}")
    print(f"Highest Average: {max(averages):.2f}")
    print(f"Lowest Average: {min(averages):.2f}")
    print(f"Class Average: {sum(averages) / len(averages):.2f}")

    # Export option
    export = input("Would you like to export this summary to a .txt file? (y/n): ").lower()
    if export == 'y':
        filename = "school_summary.txt" if choice == "1" else f"{class_name.replace(' ', '_')}_summary.txt"
        with open(filename, "w") as f:
            f.write(f"--- {summary_title} ---\n")
            f.write(f"Total Students: {len(selected_students)}\n")
            f.write(f"Highest Average: {max(averages):.2f}\n")
            f.write(f"Lowest Average: {min(averages):.2f}\n")
            f.write(f"Class Average: {sum(averages) / len(averages):.2f}\n")
        print(f"Summary exported to {filename}")


def view_by_class(data):
    class_name = input("Enter class to view: ")
    class_students = []
    print(f"\n--- Students in Class {class_name} ---")
    for student in data:
        if student.get("class", "").lower() == class_name.lower():
            print(f"- {student['name']} (Average: {student['average']:.2f}, Grade: {student['grade']})")
            class_students.append(student)

    if not class_students:
        print("Try Again. No students found in that class.")
        return

    export = input("Would you like to save this class report to a file? (y/n): ").lower()
    if export == 'y':
        with open(f"{class_name.replace(' ', '_')}_report.txt", "w") as f:
            for student in class_students:
                f.write(f"{student['name']} - Avg: {student['average']:.2f}, Grade: {student['grade']}\n")
        print(f"{class_name.replace(' ', '_')}_report.txt saved.")


def edit_student(data):
    print("Edit Student Record")
    search_term = input("Enter Student ID or Name to edit: ").strip().lower()

    for student in data:
        if student["id"].lower() == search_term or student["name"].strip().lower() == search_term:
            print(f"Editing {student['name']} ({student['id']})")

            # Edit name
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            if new_name:
                student["name"] = new_name

            # Edit class
            new_class = input("Enter new class (leave blank to keep current): ").strip()
            if new_class:
                student["class"] = new_class

            # Edit existing subjects
            print("\nUpdate existing subjects:")
            for subject in student["subjects"]:
                new_score = input(f"New score for {subject} (current: {student['subjects'][subject]}) or leave blank "
                                  f"to keep: ").strip()
                if new_score:
                    try:
                        score = float(new_score)
                        if 0 <= score <= 100:
                            student["subjects"][subject] = score
                        else:
                            print("Invalid score. Keeping original.")
                    except ValueError:
                        print("Invalid input. Keeping original.")

            # Add new subjects
            print("\nAdd new subjects (optional):")
            while True:
                new_subject = input("Enter new subject name (or press Enter to stop): ").strip()
                if not new_subject:
                    break
                if new_subject in student["subjects"]:
                    print("Subject already exists. Use the update section above.")
                    continue
                try:
                    new_score = float(input(f"Enter score for {new_subject}: "))
                    if 0 <= new_score <= 100:
                        student["subjects"][new_subject] = new_score
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric score.")

            # Recalculate average and grade
            student["average"] = sum(student["subjects"].values()) / len(student["subjects"])
            student["grade"] = calculate_grade(student["average"])
            print("Student record updated.\n")
            return

    print("No matching student found by that ID or name.")


def delete_student(data):
    search_id = input("Enter Student ID to delete: ").strip().upper()
    for i, student in enumerate(data):
        if student["id"] == search_id:
            confirm = input(f"Are you sure you want to delete {student['name']} (y/n)? ").lower()
            if confirm == 'y':
                del data[i]
                print("Student record deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("Student ID not found.")


def main():
    students_data = load_data()  # Load existing data if available
    while True:
        print("\n===== ** Student Performance Analyzer ** =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. View Summary")
        print("4. View Students by Class")
        print("5. Save & Exit")
        print("6. Edit Student")
        print("7. Delete Student")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student(students_data)
        elif choice == '2':
            search_student(students_data)
        elif choice == '3':
            view_summary(students_data)
        elif choice == '4':
            view_by_class(students_data)
        elif choice == '5':
            save_data(students_data)
            print("Bye! Have a nice day ~!")
            break
        elif choice == '6':
            edit_student(students_data)
        elif choice == '7':
            delete_student(students_data)
        else:
            print("Invalid input. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
