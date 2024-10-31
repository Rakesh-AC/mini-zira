# Siple project called Mini Zira

This is just a project that provides the siple crud operatations

## Prerequisite

python 3.10 or greater please install the python by downloading from here [here](https://www.python.org/downloads/).

## How to run the project

1. Clone the project and open it in your IDE

   ```bash
   git clone https://github.com/Rakesh-AC/mini-zira.git
   ```

2. create a python vertual environment

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment
   ```bash
   # For Windows
   env\Scripts\activate
   # For Mac or linux
   source env/bin/activate
   ```
4. Get inside the directory where `requirements.txt` is present and run
   ```bash
   pip install -r requirements.txt
   ```
5. To create a database tables
   - step 1: create a datasbase
   ```bash
   python manage.py makemigrations
   ```
   - step 2: migrate the database
   ```bash
   python manage.py migrate
   ```
6. To run the project

   ```bash
   # To run in default 8000 port
   python manage.py runserver

   # To run in custom port `ex:8001`
   python manage.py runserver 8001
   ```

## API end points

1. **Project Dashboard**
   - **URL:** `/`
   - **Method:** GET
   - **Description:** Displays the project dashboard.
   - **Response:**
     ```json
     {
       "dashboard": "Welcome you are in dashbord"
     }
     ```
2. **Get Projects list**

   - **URL:** `/projects/`
   - **Method:** GET
   - **Description:** Displays list of projects .
   - **Response:**

     ```json
     [
       {
         "id": 1,
         "project_name": "First Project",
         "project_description": "just a project description"
       },
       {
         "id": 2,
         "project_name": "Second Project",
         "project_description": "Description of second project"
       }
     ]
     ```

3. **Get Project by id**

   - **URL:** `/projects/id/`
   - **Method:** GET
   - **Description:** Gets the project details by id.
   - **Response:**

     ```json
     {
       "id": 1,
       "project_name": "First Project",
       "project_description": "just a project description"
     }
     ```

4. **Create a new project**
   - **URL:** `/projects/create/`
   - **Method:** POST
   - **Description:** Displays list of projects.
   - **Request body example:**
     ```json
     {
       "project_name": "forth Project",
       "project_description": "just a project description"
     }
     ```
5. **Update the Project by id**

   - **URL:** `projects/id/update/`
   - **Method:** PUT
   - **Description:** updates the project details by id.
   - **Request body example:**

     ```json
     {
       "project_name": "forth Project updating",
       "project_description": "just a project description"
     }
     ```

   - **Response body:**
     ```json
     {
       "id": 4,
       "project_name": "forth Project updating",
       "project_description": "just a project description"
     }
     ```

6. **Delete the project by id**
   - **URL:** `projects/id/delete/`
   - **Method:** `DELETE`
   - **Description:** Delete the project by id.
   - **Respose body example:**
     ```json
     {
       "message": "Project deleted successfully."
     }
     ```
