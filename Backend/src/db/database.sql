DROP TABLE IF EXISTS course_enrollment CASCADE;
DROP TABLE IF EXISTS assignments CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS chats CASCADE;
DROP TABLE IF EXISTS channels CASCADE;
DROP TABLE IF EXISTS servers CASCADE;
DROP TABLE IF EXISTS sections CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TYPE IF EXISTS user_role CASCADE;

CREATE TYPE user_role AS ENUM ('student','admin', 'course admin');

CREATE TABLE users (
    username TEXT UNIQUE NOT NULL DEFAULT '',
    password TEXT NOT NULL,
    email TEXT NOT NULL DEFAULT '',
    session_key TEXT,
    user_type user_role NOT NULL DEFAULT 'student'
);

CREATE TABLE courses (
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL
);

CREATE TABLE sections(
    id SERIAL PRIMARY KEY,
    section_code INT NOT NULL,
    course_code TEXT REFERENCES courses(course_code),
    course_admin_username TEXT REFERENCES users(username)
);

CREATE TABLE course_enrollment (
    id SERIAL PRIMARY KEY,
    student_username TEXT REFERENCES users(username),
    course_code TEXT REFERENCES courses(course_code),
    section_id INT REFERENCES sections(id),
    user_type user_role NOT NULL DEFAULT 'student'
);

CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    assignment_name TEXT NOT NULL,
    section_id INT REFERENCES sections(id),
    username TEXT REFERENCES users(username),
    due_date DATE NOT NULL DEFAULT CURRENT_DATE,
    submission_type TEXT NOT NULL DEFAULT 'pdf'
);

CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    server_name TEXT UNIQUE NOT NULL,
    section_id INT REFERENCES sections(id)
);

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    channel_name TEXT NOT NULL,
    server_name TEXT REFERENCES servers(server_name)
);

CREATE TABLE chats (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    username TEXT REFERENCES users(username),
    channel_id INT REFERENCES channels(id)
);

INSERT INTO users (username, password, email, user_type) 
VALUES ('course_admin1', 'course_admin_password', 'admin@example.com', 'course admin'),
('student1', 'student_password', 'student1@example.com', 'student');

INSERT INTO courses (course_code,course_name)
VALUES ('CSCI140', 'Introduction to computer science 1'),
('MATH140', 'Calculus 1');

INSERT INTO sections (section_code, course_code, course_admin_username)
VALUES (1, 'CSCI140', 'course_admin1'),
(2, 'CSCI140', 'course_admin1'),
(4, 'MATH140', 'course_admin1');

INSERT INTO course_enrollment(student_username,course_code, section_id, user_type)
VALUES ('student1', 'CSCI140', 1,'student'),
('student1', 'MATH140',3, 'student');

INSERT INTO assignments (assignment_name, section_id, username)
VALUES ('Assignment 1 CSCI', 1,'student1'),
('Assignment 2 CSCI', 2,'course_admin1'),
('Assignment 1 MATH', 3,'student1'),
('Assignment 2 MATH', 3,'student1');


INSERT INTO servers (server_name, section_id)
VALUES ('CSCI140', 1),
('MATH140', 3);
INSERT INTO channels (channel_name, server_name)
VALUES ('General CS', 'CSCI140'),
('General_MATH', 'MATH140'),
('General HELP', 'MATH140');
;
INSERT INTO chats (message, username, channel_id)
VALUES ('Hello ca', 'student1', 1),
('Hi??', 'course_admin1', 1),
('tf', 'student1', 2),
('cat', 'course_admin1', 2);