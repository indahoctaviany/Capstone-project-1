# Data awal siswa dengan nama baru
students = [
    {
        'id': 1,
        'name': 'Amara',
        'math': 85,
        'english': 90,
        'science': 78
    },
    {
        'id': 2,
        'name': 'Brando',
        'math': 75,
        'english': 80,
        'science': 88
    },
    {
        'id': 3,
        'name': 'Cikita',
        'math': 90,
        'english': 85,
        'science': 92
    },
    {
        'id': 4,
        'name': 'Nabil',
        'math': 88,
        'english': 91,
        'science': 80
    },
    {
        'id': 5,
        'name': 'Zumafo',
        'math': 78,
        'english': 84,
        'science': 89
    }
]

# Fungsi untuk menampilkan semua data siswa
def display_students():
    print("\n===============================")
    print("Student Data\n")
    print(f"{'ID':<5} | {'Name':<8} | {'Math':<5} | {'English':<7} | {'Science':<7}")
    print("-" * 38)  # Garis pemisah
    for student in students:
        print(f"{student['id']:<5} | {student['name']:<8} | {student['math']:<5} | {student['english']:<7} | {student['science']:<7}")
    print("===============================\n")

# Fungsi untuk memeriksa apakah ID siswa sudah ada
def id_exists(student_id):
    return any(student['id'] == student_id for student in students)

# Fungsi untuk menambahkan data siswa
def add_student():
    while True:
        print("\n===============================")
        student_id = int(input('Enter Student ID: '))

        if id_exists(student_id):
            print("Student ID already registered.")
            return

        name = input('Enter Student Name: ')
        math = int(input('Enter Math Score: '))
        english = int(input('Enter English Score: '))
        science = int(input('Enter Science Score: '))

        students.append({
            'id': student_id,
            'name': name,
            'math': math,
            'english': english,
            'science': science
        })

        print(f"Student {name} added successfully.")
        display_students()
        print("===============================")
        return

# Fungsi untuk menghapus data siswa
def delete_student():
    while True:
        print("\n===============================")
        display_students()
        student_id = int(input('Enter Student ID to delete: '))

        if not id_exists(student_id):
            print("Student ID not found.")
            return

        global students
        students = [student for student in students if student['id'] != student_id]

        print(f"Student with ID {student_id} deleted successfully.")
        display_students()
        print("===============================")
        return

# Fungsi untuk memperbarui data siswa
def update_student():
    while True:
        print("\n===============================")
        display_students()
        student_id = int(input('Enter Student ID to update: '))

        student = next((s for s in students if s['id'] == student_id), None)
        
        if student:
            student['name'] = input(f'Enter new name (current: {student["name"]}): ') or student['name']
            student['math'] = int(input(f'Enter new Math score (current: {student["math"]}): ') or student['math'])
            student['english'] = int(input(f'Enter new English score (current: {student["english"]}): ') or student['english'])
            student['science'] = int(input(f'Enter new Science score (current: {student["science"]}): ') or student['science'])
            
            print(f"Student ID {student_id} updated successfully.")
        else:
            print("Student ID not found.")
        
        display_students()
        print("===============================")
        return

# Menu utama program
def main_menu():
    while True:
        choice = input('''\n===============================
        Student Data Management

        Menu:
        1. Display Students
        2. Add Student
        3. Delete Student
        4. Update Student
        5. Exit
        ===============================
        
        Enter your choice: ''')
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            print("\nThank you for using the Student Data Management system!")
            print("===============================")
            break
        else:
            print("Invalid choice, please try again.")

# Jalankan menu utama
if __name__ == "__main__":
    main_menu()
