import mysql.connector


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


def get_schedule():
    print("TEACHER OR STUDENT?")
    print("1. Teacher")
    print("2. Student")
    role = int(input("ENTER NUMBER: "))

    if role == 1:
        teacher_id = input("ENTER TEACHER_ID NOW (number only): ")
        print_schedule(get_teacher_schedule(teacher_id), role)
    elif role == 2:
        student_id = input("ENTER STUDENT_ID NOW (number only): ")
        print_schedule(get_student_schedule(student_id), role)


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


get_schedule()
