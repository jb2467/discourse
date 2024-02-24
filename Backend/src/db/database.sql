DROP TYPE IF EXISTS user_role CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS sections CASCADE;
DROP TABLE IF EXISTS course_enrollment;

CREATE TYPE user_role AS ENUM ('student','admin', 'course admin');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL DEFAULT '',
    password TEXT NOT NULL,
    email TEXT NOT NULL DEFAULT '',
    session_key TEXT,
    user_type user_role NOT NULL DEFAULT 'student'
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL
);

CREATE TABLE sections (
    id SERIAL PRIMARY KEY,
    course_code TEXT REFERENCES courses(course_code),
    section_code TEXT UNIQUE NOT NULL,
    course_admin_username TEXT REFERENCES users(username)
);

CREATE TABLE course_enrollment (
    id SERIAL PRIMARY KEY,
    student_username TEXT REFERENCES users(username),
    course_code TEXT REFERENCES courses(course_code),
    section_code TEXT REFERENCES sections(section_code),
    user_type user_role NOT NULL DEFAULT 'student',
    UNIQUE (student_username, course_code) 
);

INSERT INTO users (username, password, email, user_type) 
VALUES ('course_admin1', 'course_admin_password', 'admin@example.com', 'course admin'),
('student1', 'student_password', 'student1@example.com', 'student');

INSERT INTO courses (course_code,course_name)
VALUES ('CSCI140', 'Introduction to computer science 1');

INSERT INTO sections (course_code,section_code,course_admin_username)
VALUES ('CSCI140', '.01', 'course_admin1');

INSERT INTO course_enrollment(student_username, course_code, section_code, user_type)
VALUES ('student1', 'CSCI140', '.01', 'student');

-- Add a new table for assignments
CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    course_code TEXT REFERENCES courses(course_code),
    section_code TEXT REFERENCES sections(section_code),
    assignment_name TEXT NOT NULL,
    pdf_file BYTEA NOT NULL
);