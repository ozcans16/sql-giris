
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER
);

CREATE TABLE Courses (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    price DECIMAL,
    created_at DATE
);

CREATE TABLE Enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE,

    FOREIGN KEY(student_id) REFERENCES Students(id) ON DELETE CASCADE,
    FOREIGN KEY(course_id) REFERENCES Courses(id) ON DELETE CASCADE
);



INSERT INTO Students VALUES (1,'Ahmet','ahmet@mail.com',21);
INSERT INTO Students VALUES (2,'Mehmet','mehmet@mail.com',23);
INSERT INTO Students VALUES (3,'Ayşe','ayse@mail.com',22);
INSERT INTO Students VALUES (4,'Zeynep','zeynep@mail.com',20);
INSERT INTO Students VALUES (5,'Ali','ali@mail.com',24);
INSERT INTO Students VALUES (6,'Fatma','fatma@mail.com',19);
INSERT INTO Students VALUES (7,'Can','can@mail.com',25);
INSERT INTO Students VALUES (8,'Elif','elif@mail.com',22);
INSERT INTO Students VALUES (9,'Burak','burak@mail.com',23);
INSERT INTO Students VALUES (10,'Deniz','deniz@mail.com',21);



INSERT INTO Courses VALUES (1,'Python',1200,'2024-01-01');
INSERT INTO Courses VALUES (2,'SQL',900,'2024-02-01');
INSERT INTO Courses VALUES (3,'Data Science',2000,'2024-03-01');
INSERT INTO Courses VALUES (4,'Web Development',1500,'2024-04-01');
INSERT INTO Courses VALUES (5,'Machine Learning',2500,'2024-05-01');





INSERT INTO Enrollments VALUES (1,1,1,'2024-06-01');
INSERT INTO Enrollments VALUES (2,2,1,'2024-06-01');
INSERT INTO Enrollments VALUES (3,3,2,'2024-06-02');
INSERT INTO Enrollments VALUES (4,4,3,'2024-06-02');
INSERT INTO Enrollments VALUES (5,5,1,'2024-06-03');
INSERT INTO Enrollments VALUES (6,6,2,'2024-06-03');
INSERT INTO Enrollments VALUES (7,7,3,'2024-06-04');
INSERT INTO Enrollments VALUES (8,8,4,'2024-06-04');
INSERT INTO Enrollments VALUES (9,9,5,'2024-06-05');
INSERT INTO Enrollments VALUES (10,10,1,'2024-06-05');





SELECT * FROM Students;




SELECT * FROM Courses
ORDER BY price DESC;




SELECT * FROM Courses
ORDER BY price DESC
LIMIT 2;





SELECT Students.name, Courses.title
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.id
JOIN Courses ON Enrollments.course_id = Courses.id;




UPDATE Students
SET age = 26
WHERE id = 1;



UPDATE Courses
SET price = price + 200
WHERE id = 1;



DELETE FROM Enrollments
WHERE id = 5;




DELETE FROM Students
WHERE id = 3;




SELECT COUNT(*) FROM Students;



SELECT AVG(price) FROM Courses;



SELECT MAX(price) FROM Courses;



SELECT course_id, COUNT(student_id)
FROM Enrollments
GROUP BY course_id;




SELECT course_id, COUNT(student_id)
FROM Enrollments
GROUP BY course_id
HAVING COUNT(student_id) > 3;





import sqlite3

conn = sqlite3.connect("courses.db")
cursor = conn.cursor()



cursor.execute("SELECT * FROM Students")

rows = cursor.fetchall()

for row in rows:
    print(row)




    def add_student(name,email,age):

    cursor.execute(
        "INSERT INTO Students (name,email,age) VALUES (?,?,?)",
        (name,email,age)
    )

    conn.commit()





    def list_courses():

    cursor.execute("SELECT * FROM Courses")

    for course in cursor.fetchall():
        print(course)
        