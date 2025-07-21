import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="student_results",
    user="zeel",
    password=2121
)
cursor = conn.cursor()
