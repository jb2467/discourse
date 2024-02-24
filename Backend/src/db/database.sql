DROP TYPE IF EXISTS user_role CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS course_enrollment;
CREATE TYPE user_role AS ENUM ('student','admin', 'course admin');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL DEFAULT '',
    password TEXT NOT NULL,
    email TEXT NOT NULL DEFAULT '',
    session_key TEXT,
    user_type user_role NOT NULL DEFAULT 'student'
);


INSERT INTO users (username, password, email, user_type) 
VALUES ('course_admin1', 'course_admin_password', 'admin@example.com', 'course admin'),
('student1', 'student_password', 'student1@example.com', 'student');

