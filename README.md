# Discourse Hackathon Project

## Team Members
- Yenry Simon
- Joseph Bean
- Jay Lee
- Nasif Chowdhury

## Requirements Outlined

### Comparative Analysis

#### Discord
**Pros:**
- Community Engagement
- Integration Capabilities
- Flexibility in Communication
- Customization
- User Friendly Interface

**Cons:**
- Not Specifically Designed for Education
- Potential for Distraction

#### MyCourse
**Pros:**
- Educational Tools Integrations
- Structured Learning Environment
- Access Control
- Custom Education Features

**Cons:**
- Limited Real Time Interaction
- User Interface
- Flexibility

### Research About College Student
- **Perception and Engagement:** Investigates how students view these platforms and their level of engagement with them.
- **Educational Experiences:** Look at how these platforms are integrated into their academic lives.
- **Impact on Learning Outcomes:** Studies the effectiveness of these platforms in enhancing learning.
- **Student Satisfaction:** Gauges how satisfied students are with these platforms for their educational needs.
- **Academic Performance:** Assesses whether there's a noticeable impact on the students' grades or overall academic performance.

## Application Requirements

### User Roles and Permissions
- Roles for student, Teacher Assistant (TA), and Teacher with specific actions they can perform.
- Only a teacher can create new classes, assignments, channels, etc.
- A TA can view channels, assignments, quizzes, etc., but cannot create anything new.
- Students can attempt assigned tasks and view relevant channels but cannot see or create anything outside of that.

### Account and Security
- Account creation and login.
- Biometrics login rather than text-based authentication.
- Password creation requirements (length, symbols) and show/hide options.

### Communication and Collaboration
- Real-time messaging and video communication.
- Group collaboration features for studies and projects.
- Dedicated areas for different subjects or courses.

### Course Management
- Tools for tracking assignments, schedules, and resources.
- Interactive learning features like quizzes, polls, and discussion boards.

### Social Interaction
- Community building spaces.
- Event organizing tools.

### User Experience and Accessibility
- Navigation friendly for new and experienced users.
- Adaptable to various devices and screen sizes.

### Potential Additional Features
- Notifications and alerts.
- Analytics for educators.
- Feedback system for users.

## System Setup and Configuration
- Front-End Framework: React
- Backend Framework: Flask with Flask-RESTful and Flask-CORS.
- Database: PostgreSQL with Psycopg2.
- Configuration: YAML for database parameters.

## API Functionality
- **User Management:** Registration, user detail retrieval, password hashing, session management.
- **Authentication and Session Management:** Login and logout.
- **Course Management:** Course retrieval and creation.
- **Database Interaction:** SQL query execution for CRUD operations, database initialization.

