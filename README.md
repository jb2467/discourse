# discourse
Hackathon

Discourse website 
Team Members:
 Yenry Simon
Joseph Bean 
Jay Lee
Nasif Chowdhury

REQUIREMENTS OUTLINED
Comparative Analysis
Discord
Pros
Community Engagement
Integration Capabilities
Flexibility in Communication
Customization 
User Friendly Interface
Cons
Not Specifically Designed for Education
Potential for Distraction 


MyCourse
Pros
Educational Tools Integrations
Structured Learning Environment 
Access Control 
Custom Education Features
Cons
Limited Real Time Interaction 
User Interface
Flexibility 
Research About College Student

Perception and Engagement: Investigates how students view these platforms and their level of engagement with them.

Educational Experiences: Look at how these platforms are integrated into their academic lives.

Impact on Learning Outcomes: Studies the effectiveness of these platforms in enhancing learning.

Student Satisfaction: Gauges how satisfied students are with these platforms for their educational needs.

Academic Performance: Assesses whether there's a noticeable impact on the students' grades or overall academic performance.



What are the requirements that that app needs to do
User Roles and permissions
    Roles for student, Teacher Assistant(TA), and Teacher
    Have specific things each role can do
    Only a teacher can create new classes, assignments, channels, etc
    A TA can view each channel, assignments, quizzes, etc but they cannot create anything new.
    A student can attempt each of the things assigned to them and view channels the teacher adds them to or they are a part of but cannot see or create anything outside of that.
    Students should be able to submit assignments and do quizzes in the same space as accessing channels.
Account and Security
    Create an account/Already a member?
    Biometrics login in rather than text-based authentication
    Creating a password
        Meets requirements such as length of characters and requiring symbols
        show/hide password options
Communication and Collaboration 
    Messaging and Forums: 
        Real time messaging and video communication option 
    Group Collaboration: 
        Features for group studies and project collaboration 
    Educational Channels and Servers: 
        Dedicated areas for different subjects or courses 
Course Management 
    Tools for tracking assignment, schedules and educational resources 
Interactive learning features: 
    Quizzes, Polls, and Discussion boards 
    Social Interaction
    Community Building
    Spaces for non academic interaction
    Event Organizing 
    Tools for creating and managing events or meet up 
User Experience and Accessibility
    Easy for both new and experienced users to navigate 
    Adaptable to different devices and screen sizes 
Potential Additional Features
    Notifications and alerts for educational deadlines and social updates.
    Analytics for educators.
    Feedback system for users to submit suggestions and improvements.


What features will help the users achieve their goals? 
    Notifications and Alerts: Customizable notifications for educational deadlines and social updates 
    Analytics: for educators to track engagement and participation
    Feedback System Mechanism for users to provide feedback and suggestion



System Setup and Configuration
    Flask framework for building the web application.
    Flask-RESTful for REST API development.
    Flask-CORS for handling Cross-Origin Resource Sharing (CORS), allowing the API to interact with front-end applications served from different origins.
    PostgreSQL database for storing user and course data.
    Psycopg2 for PostgreSQL database connection and operations in Python.
    YAML configuration for database connection parameters to ensure flexibility and security.
    Environment for running Python, with support for external libraries and database connections.

API Functionality
User Management
    Endpoint for user registration, allowing new users to sign up with a username, password, and email.
    Endpoint for user information retrieval, allowing fetching of all user details.
    Password hashing for secure storage of user credentials.
    Unique session key generation upon login for session management.
Authentication and Session Management
    Login endpoint accepting username and password, returning a session key upon successful authentication.
    Logout endpoint that invalidates the user's session key.
Course Management
    Endpoint to retrieve all available courses.
    Functionality to add new courses to the database.
Database Interaction
    Functions to execute SQL queries and commands related to users and courses for CRUD operations.
    Database initialization script execution as the application starts to set up the schema.

