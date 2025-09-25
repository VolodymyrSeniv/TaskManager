# **IT Company Task Manager**
Task Management system for IT company made on Django Web Framework available at https://task-manager-seniv-volodymyr.onrender.com.
Credentials for using:
Username: qwerty
Password: qwerty

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

- ### Index
<img width="1919" height="705" alt="image" src="https://github.com/user-attachments/assets/3291af0e-0aab-4843-97b0-354edd975d2d" />

- ### Login
<img width="1919" height="780" alt="image" src="https://github.com/user-attachments/assets/c7a2a5fb-1e8d-48c1-9f2f-60c210d707cf" /> 

- ### Tasks List Page
<img width="1919" height="890" alt="image" src="https://github.com/user-attachments/assets/a87a150d-a083-470c-927f-283ccdba09ff" />

- ### Task Detail Page
<img width="1919" height="808" alt="image" src="https://github.com/user-attachments/assets/68cdb0c8-fcf1-4add-adab-9548ba262673" />

- ### Projects List Page
<img width="1919" height="823" alt="image" src="https://github.com/user-attachments/assets/e12a343d-7c23-498c-a9f2-c9aab7e289ec" />

- ### Project Detail Page
<img width="1919" height="850" alt="image" src="https://github.com/user-attachments/assets/b2635b13-341a-403b-9792-30b65549aaf5" />

- ### Positions List Page
<img width="1919" height="772" alt="image" src="https://github.com/user-attachments/assets/e6b2dcbd-d0dc-4c68-b244-834c200b3af9" />

- ### Position Detail Page
<img width="1919" height="780" alt="image" src="https://github.com/user-attachments/assets/7671eb28-f46f-4d5f-b635-aa0fe742a6f0" />

- ### Teams List Page
<img width="1919" height="714" alt="image" src="https://github.com/user-attachments/assets/831c41b2-2096-4dcb-be2a-d8ade9ee6866" />

- ### Teams Detail Page
<img width="1919" height="828" alt="image" src="https://github.com/user-attachments/assets/e6937856-8d68-4532-89a6-e64049b4a0f2" />

- ### Tasks Types List Page
<img width="1919" height="644" alt="image" src="https://github.com/user-attachments/assets/c510bbfc-9282-4fa8-83aa-61e7fda78b5f" />

- ### Task Type Detail Page
<img width="1919" height="595" alt="image" src="https://github.com/user-attachments/assets/6cb641d9-8d68-4d4b-bac7-57b9e6d375c2" />

- ### Workers List Page
<img width="1919" height="745" alt="image" src="https://github.com/user-attachments/assets/c3f094b1-a269-4192-a37c-a63462056c0d" />

- ### Worker Detail Page
<img width="1919" height="741" alt="image" src="https://github.com/user-attachments/assets/a89782b3-0b9e-4a4d-8b29-81c657534e99" />

- ### Tags List Page
<img width="1919" height="807" alt="image" src="https://github.com/user-attachments/assets/74b6640c-2230-4232-aa01-16a0077438cb" />

- ### Create Project Page
<img width="1919" height="737" alt="image" src="https://github.com/user-attachments/assets/bd13f17c-89e9-44df-97e1-50d4d68b23d5" />

- ### Update Project Page
<img width="1919" height="741" alt="image" src="https://github.com/user-attachments/assets/dd7bbd74-b4e8-4007-a571-0aae1205c755" />

- ### Confirm Delete Project Page
<img width="1919" height="648" alt="image" src="https://github.com/user-attachments/assets/e59c1dae-74e7-4bcc-8c20-5e1f5665b535" />

- ### Logout Page
<img width="1919" height="526" alt="image" src="https://github.com/user-attachments/assets/50f01c6d-7299-4196-a0d5-1b9632789c4c" />






















