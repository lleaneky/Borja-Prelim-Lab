class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return (f"Student ID: {self.student_id}\n"
                f"Student Name: {self.name}\n"
                f"Course: {self.course}\n"
                f"Year Level: {self.year_level}")


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.data = [None] * self.capacity
        self.size = 0

    def _resize(self):
        old_capacity = self.capacity
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        print(f">> Array capacity increased from {old_capacity} to {new_capacity}")

    def add(self, student):
        if self.size == self.capacity:
            print(">> Array is full.")
            self._resize()
        self.data[self.size] = student
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        return None

    def set(self, index, student):
        if 0 <= index < self.size:
            self.data[index] = student

    def search(self, student_id):
        for i in range(self.size):
            if self.data[i].student_id.lower() == student_id.lower():
                return i
        return -1

    def remove(self, student_id):
        index = self.search(student_id)
        if index == -1:
            return False

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1
        return True

    def is_empty(self):
        return self.size == 0

    def display(self):
        if self.is_empty():
            print("No student records found.")
            return
        for i in range(self.size):
            print("---------------------------")
            print(self.data[i])
        print("---------------------------")


def read_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Invalid input. Please enter a number.")


def print_menu():
    print("================================")
    print("      STUDENT RECORD MANAGER")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")


def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if students.search(student_id) != -1:
        print("A student with that ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    year_level = read_int("Enter Year Level: ")

    students.add(Student(student_id, name, course, year_level))
    print("Student added successfully.")


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()
    index = students.search(student_id)
    if index == -1:
        print("Student not found.")
    else:
        print(students.get(index))


def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()
    index = students.search(student_id)
    if index == -1:
        print("Student not found.")
        return

    existing = students.get(index)

    name = input(f"Enter new Student Name ({existing.name}): ").strip()
    if name:
        existing.name = name

    course = input(f"Enter new Course ({existing.course}): ").strip()
    if course:
        existing.course = course

    year_input = input(f"Enter new Year Level ({existing.year_level}), or leave blank to keep: ").strip()
    if year_input:
        existing.year_level = int(year_input)

    students.set(index, existing)
    print("Student updated successfully.")


def remove_student(students):
    student_id = input("Enter Student ID to remove: ").strip()
    removed = students.remove(student_id)
    print("Student removed successfully." if removed else "Student not found.")


def display_array_info(students):
    print(f"Current number of students: {students.size}")
    print(f"Current array capacity: {students.capacity}")


def main():
    students = DynamicArray()

    while True:
        print_menu()
        choice = read_int("Enter your choice: ")

        if choice == 1:
            add_student(students)
        elif choice == 2:
            students.display()
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            update_student(students)
        elif choice == 5:
            remove_student(students)
        elif choice == 6:
            display_array_info(students)
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

        print()


if __name__ == "__main__":
    main()
      
