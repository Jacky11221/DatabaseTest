import mysql.connector
import statistics

def connect_to_sql():
    return mysql.connector.connect(user='jackyl112',
                                   password='236714457',
                                   host='10.8.37.226',
                                   database='jackyl112_db')


def execute_statement(connection, statement):
    results = []
    cursor = connection.cursor()
    cursor.execute(statement)

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()
    return results


def get_student_schedule(student_id):
    call = (" CALL get_student_schedule(" + student_id + ");")
    return execute_statement(connect_to_sql(), call)


def get_teacher_schedule(teacher_id):
    call = (" CALL get_teacher_schedule(" + teacher_id + ");")
    return execute_statement(connect_to_sql(), call)


def get_student_grades(student_id):
    call = (" CALL get_student_grades(" + student_id + ");")
    return execute_statement(connect_to_sql(), call)


def print_schedule(schedule, role):
    print()
    if role == 1:
        for desc in schedule:
            print("Period: " + str(desc[0]))
            print("Course: " + desc[1])
            print("Room: " + desc[2] + "\n")
    elif role == 2:
        for desc in schedule:
            print("Period: " + str(desc[0]))
            print("Course: " + desc[1])
            print("Room: " + desc[2])
            print("Teacher: " + desc[3] + "\n")


def print_classes(schedule):
    print()
    count = 1
    for desc in schedule:
        print(str(count) + ". " + desc[1])
        count += 1


def calculate_class_grade(class_name, grades):
    class_grades_major = []
    class_grades_minor = []

    for desc in grades:
        if desc[1] == class_name:
            print(desc[1])
            print(str(desc[3]))

            if desc[4] == "Minor Assessment":
                class_grades_minor.append(desc[3])
            else:
                class_grades_major.append(desc[3])

    print(class_grades_minor)
    print(class_grades_major)
    grades_major_avg = statistics.mean(class_grades_major)
    grades_minor_avg = statistics.mean(class_grades_minor)

    return grades_major_avg*0.7 + grades_minor_avg*0.3


def get_student_options(role):
    student_id = input("ENTER STUDENT_ID NOW (number only): ")
    print("1. SCHEDULE | 2. GRADES")

    option = int(input("OPTIONS: "))

    if option == 1:
        print_schedule(get_student_schedule(student_id), role)

    elif option == 2:
        schedule = get_student_schedule(student_id)
        grades = get_student_grades(student_id)

        print_classes(schedule)
        class_num = int(input("CHOOSE CLASS (NUMBER): ")) - 1
        class_name = schedule[class_num][1]

        grade = calculate_class_grade(class_name, grades)
        print("Your grade in " + class_name + ": " + str(grade)[:5])


print("TEACHER OR STUDENT?")
print("1. Teacher")
print("2. Student")
designation = int(input("ENTER NUMBER: "))

if designation == 1:
    teacher_id = input("ENTER TEACHER_ID NOW (number only): ")
    print_schedule(get_teacher_schedule(teacher_id), designation)
elif designation == 2:
    get_student_options(designation)
