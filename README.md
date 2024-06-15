## Task Management Application

This Task Management Application is designed to efficiently manage tasks, track progress, and collaborate within an organization. It features user roles, department management, task assignment, and task status tracking, with persistent data storage and authentication.

### Features

- **Landing Page**: Provides information about the company and includes a sign-up/log-in button.
- **User Roles**: System administrators can assign manager roles to users.
- **Manager Capabilities**:
  - Create departments and assign employees to these departments.
  - Assign tasks to employees and manage their progress.
  - Create, edit, and delete tasks.
  - Move employees between departments and remove employees from the organization.
- **Employee Capabilities**:
  - View and update task statuses.
  - Mark tasks as done or in progress.
- **Persistence**: All changes persist after page refresh.
- **Authentication**: Users remain signed in after a refresh.
- **Email Notifications**: For task due dates (extra assignment).
- **Summary Dashboard**: View task completion rates, departmental performance, and pending tasks (extra assignment).
- **Recurring Tasks**: Schedule and manage recurring tasks (extra assignment).

### Prerequisites

- Python 3.8+
- Node.js and npm (for frontend development)
- PostgreSQL (or SQLite for local development)
- Git

### Installation

#### Clone the Repository

```bash
git clone https://github.com/yourusername/task-management-app.git
cd task-management-app
```

#### Backend Setup

1. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install dependencies**:

   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the `backend` directory with the following content:

   ```plaintext
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db  # Use your PostgreSQL URI for production
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

4. **Run database migrations**:

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the Flask application**:

   ```bash
   flask run
   ```

#### Frontend Setup

1. **Navigate to the frontend directory**:

   ```bash
   cd frontend/public
   ```

2. **Serve the frontend using a static server or any web server of your choice**. For local development, you can use a simple HTTP server provided by Python:

   ```bash
   python -m http.server 8000
   ```

   This will serve the frontend at `http://localhost:8000`.

### Usage

1. **Visit the landing page**:
   Open your web browser and navigate to `http://localhost:8000`.

2. **Sign Up / Log In**:
   Use the sign-up/log-in button to create a new account or log in to an existing one.

3. **Assign Roles**:
   As a system administrator, assign manager roles to users via the `/assign_manager` endpoint.

4. **Manager Functions**:
   - **Create Departments**: Use the `/departments` endpoint to create new departments.
   - **Assign Tasks**: Use the `/tasks` endpoint to create and assign tasks.
   - **Manage Employees**: Move employees between departments and remove employees as needed.

5. **Employee Functions**:
   - **View Tasks**: Employees can view their assigned tasks.
   - **Update Task Status**: Mark tasks as done or in progress.

### API Endpoints

#### Authentication

- **Register**: `POST /register`
  - Request body: `{"username": "user", "email": "user@example.com", "password": "password"}`

- **Login**: `POST /login`
  - Request body: `{"username": "user", "password": "password"}`

#### User Management

- **Assign Manager Role**: `POST /assign_manager`
  - Request body: `{"user_id": 1}`
  - Requires JWT token in the Authorization header.

#### Department Management

- **Create Department**: `POST /departments`
  - Request body: `{"name": "Sales"}`
  - Requires JWT token in the Authorization header.

#### Task Management

- **Create Task**: `POST /tasks`
  - Request body: `{"title": "Task 1", "description": "Task description", "due_date": "2023-12-31T23:59:59", "assigned_to_id": 2, "department_id": 1}`
  - Requires JWT token in the Authorization header.

- **Update Task**: `PUT /tasks/<int:task_id>`
  - Request body: `{"title": "Updated Task", "description": "Updated description", "due_date": "2024-01-31T23:59:59", "is_completed": false}`
  - Requires JWT token in the Authorization header.

- **Delete Task**: `DELETE /tasks/<int:task_id>`
  - Requires JWT token in the Authorization header.

- **Update Task Status**: `PATCH /tasks/<int:task_id>/status`
  - Request body: `{"is_completed": true}`
  - Requires JWT token in the Authorization header.

- **Get Tasks**: `GET /tasks`
  - Requires JWT token in the Authorization header.

### Deployment

#### Deploying the Backend

1. **Set up a PostgreSQL database on your hosting platform**.
2. **Set environment variables for production**.
3. **Run migrations**.
4. **Deploy the Flask application to your hosting platform** (e.g., Heroku).

#### Deploying the Frontend

1. **Build the frontend** (if using a frontend framework):
   ```bash
   npm run build
   ```
2. **Deploy the static files to a hosting platform** (e.g., Netlify).

### Documentation

Ensure your code is well-documented with comments. Provide additional details in your README about the project structure, how to contribute, and any other relevant information.

### Contributing

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m 'Add new feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Create a new Pull Request**.

### License

This project is licensed under the MIT License.

### Contact

For support or inquiries, please contact [support@company.com](mailto:support@company.com).
