# **IT Company Task Manager**
Task Management system for IT company made on Django Web Framework

## **Installing using GitHub**
```
git clone https://github.com/VolodymyrSeniv/TaskManager.git
cd TaskManager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## **Getting access**
- create user via `python manage.py createsuperuser`
- put your credentials on the login page

## **Features**

### User Authentication & Access Control
- Secure login for all users.
- Only authenticated users can access tasks, projects, teams, and user management.

### Home Dashboard
- Displays current date, time, and user details (name, email, position).
- Tracks number of incompleted tasks assigned to the user.
- Session tracking of user visits.

### User / Worker Management
- List, create, update, and delete workers.
- Search workers by first name.
- Pagination for easy navigation through long lists.
- Worker detail view showing full information.

### Project Management
- Create, update, delete, and view projects.
- Search projects by name.
- View associated teams for each project.
- Pagination support for project lists.

### Position Management
- CRUD operations for employee positions.
- Search positions by name.
- Pagination included.

### Team Management
- Manage teams with full CRUD functionality.
- Search by team code.
- View associated workers.
- Pagination support for team lists.

### Task Management
- Create, update, delete, and view tasks.
- Assign tasks to users and projects.
- Mark tasks as completed directly from the list view.
- Separate listing of completed and incompleted tasks.
- Search tasks by name, project, or tags.
- Pagination and efficient query optimization using `select_related` and `prefetch_related`.

### Task Types & Tags
- Manage task types and tags with CRUD operations.
- Search by name and view details.
- Pagination support.

### Search & Filtering
- Dynamic search functionality for all models.
- Supports filtering by fields such as name, project, tags, and team code.

### Performance Optimization
- Efficient database queries using `select_related` for foreign keys and `prefetch_related` for Many-to-Many relationships.

### Responsive UI & Usability
- Crispy Forms integration for clean and user-friendly forms.
- Pagination links preserve search queries and filters.

## *Database ER diagram*
<img width="781" height="741" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/f1dc2ee8-0cb6-4e24-9bd5-6eca16d1f7ef" />

## **Screenshots**
###Index
<img width="1919" height="705" alt="image" src="https://github.com/user-attachments/assets/3291af0e-0aab-4843-97b0-354edd975d2d" />

###Login
<img width="1919" height="780" alt="image" src="https://github.com/user-attachments/assets/c7a2a5fb-1e8d-48c1-9f2f-60c210d707cf" />

### 




