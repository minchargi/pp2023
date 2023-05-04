def input_student_info(): #input student information
    student = {}
    student['id'] = input("Enter student ID: ") #input id of the student
    student['name'] = input("Enter student name: ") #input name of the student 
    student['DoB'] = input("Enter student DoB: ") #input student's date of birth
    student['courses'] = []
    return student

def input_course_info(): #input course information
    course = {}
    course['id'] = input("Enter course ID: ") #enter course id 
    course['name'] = input("Enter course name: ") #enter course name
    return course

def select_course(student, courses): 
    print("Available courses: ")
    for course in courses: 
        print(course['id'], course['name'])
    selected_course_id = input("Enter course ID to select: ")
    for course in courses: 
        if course['id'] == selected_course_id: 
            student['courses'].append(course)
            break

def input_course_marks(student, course): 
    marks = int(input(f"Enter marks for {student['name']} in {course['name']}: "))
    course['marks'] = marks

def list_courses(courses): 
    print("Courses:")
    for course in courses: 
        print(course['id'], course['name'])

def list_students(students): 
    print("Students:")
    for student in students: 
        print(student['id'], student['name'])

def show_student_marks(student, course_id): 
    for course in student['courses']: 
        if course['id'] == course_id: 
            print(f"{student['name']}'s mark in {course['name']}: {course['marks']}")
            break

students = []
courses = []

while True: 
    print("1. Add student\n2. Add course\n3. Select course\n4. Input marks\n5. List courses\n6. List students\n7. Show marks\n8. Exit")
    option = int(input("Choose an option: "))

    if option == 1: 
        students.append(input_student_info())
    elif option == 2: 
        courses.append(input_course_info())
    elif option == 3: 
        student_id = input("Enter student ID: ")
        student = None
        for s in students: 
            if s['id'] == student_id: 
                student = s
                break
        if student: 
            select_course(student, courses)
        else: 
            print("Who is this?")
    elif option == 4: 
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = None
        course = None
        for s in students: 
            if s['id'] == student_id: 
                student = s
                break
        for c in courses: 
            if c['id'] == course_id: 
                course = c
                break
        if student and course: 
            input_course_marks(student, course)
        else:
            print("Err they are not found here.")
    elif option == 5: 
        list_courses(courses)
    elif option == 6: 
        list_students(students)
    elif option == 7: 
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = None
        for s in students: 
            if s['id'] == student_id: 
                student = s
                break
        if student: 
            show_student_marks(student, course_id)
        else: 
            print("Again, who is this?")
    elif option == 8: 
        break