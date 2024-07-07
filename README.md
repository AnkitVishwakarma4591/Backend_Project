# Basic Student Management System API

Basic Student Management System API using Flask(Python)

Overview
I have developed a comprehensive Basic Student Management System API utilizing Flask and SQLAlchemy ORM in Python. This project offers essential CRUD functionalities to manage student records effectively, providing a practical example of a web-based management system.
Features
1. Add Student Records: 
   - Input Fields: The system collects three primary pieces of student information: Name, Enrollment Number, and Email ID.
   - Data Validation: Ensures that no field is left empty and validates the email format.
2. Retrieve Student Information:
   - List Display: A table format is used to display all student records with columns for S.No, Student Name, Enrollment Number, and Email ID.
   - Sorting and Searching: Users can sort the list and search for specific students.
3. Update Student Records:
   - Edit Functionality: Each record has an "Update" button, redirecting the user to an update form.
   - Real-time Update: After submitting changes, the information is updated in the database and instantly reflected in the list.
4. Delete Student Records:
   - Delete Functionality: Each record includes a "Delete" button to remove the entry from the database.
   - Confirmation Prompt: Users receive a confirmation prompt before deletion to prevent accidental removal.
 Technical Details
- Flask Framework: Used to develop the backend, providing a lightweight yet powerful platform for building web applications.
- SQLAlchemy ORM: Manages database interactions, enabling seamless integration with SQLite for efficient data storage and retrieval.
- Virtual Environment: Created a virtual environment to maintain dependencies, ensuring a clean and isolated development space.
Implementation
1. Backend (`app.py`):
   - Defines routes for CRUD operations.
   - Utilizes SQLAlchemy to interact with the SQLite database.
   - Implements Flask's route handling for adding, updating, and deleting student records.
2. Frontend:
   - `home.html`: The main interface for adding new students and viewing the list of existing students.
     - Form Handling: Includes a form to input student details.
     - Display List: Uses a dynamic table to show all student records with options for update and delete.
   - `update.html`: Interface for editing existing student records.
     - Pre-filled Forms: Automatically populates the form fields with current data for editing.
     - Submission: Updates the record in the database upon submission.
Learning Outcomes
This project provided valuable insights into web development, particularly in understanding how backend processes are connected with frontend interfaces and how data flows between them. I learned:
- Flask and SQLAlchemy Integration: How to efficiently handle CRUD operations using Flask and SQLAlchemy.
- Web Forms and Data Validation: Implementing and validating web forms for user input.
- Error Handling and Debugging: Identifying and resolving errors in the development process.
- Isolation of Development Environment: Using virtual environments to manage dependencies separately from the system environment.
Project Structure
- `app.py`: The main application file handling the logic and routing.
- `templates/`:
  - `home.html`: The homepage template for adding and viewing students.
  - `update.html`: The update page template for modifying student records.
- Database: SQLite file managed through SQLAlchemy.
Conclusion
Developing the Basic Student Management System has strengthened my understanding of backend development, from setting up the server and managing databases to integrating user interfaces. This project serves as a practical demonstration of creating and managing a web application that handles essential CRUD operations.
