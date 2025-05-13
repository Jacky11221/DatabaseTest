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


student_id = input("ENTER STUDENT_ID NOW (number only): ")
student_schedule = get_student_schedule(student_id)

for desc in student_schedule:
    print("Period: " + str(desc[0]))
    print("Course: " + desc[1])
    print("Room: " + desc[2])
    print("Teacher: " + desc[3] + "\n")